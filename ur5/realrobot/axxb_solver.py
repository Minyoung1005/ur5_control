import numpy as np
from scipy.spatial.transform import Rotation
from scipy.linalg import expm, logm


def RandomRGen():
    """
    Creates random rotation matrix, SO(3)
    """
    RandR = Rotation.random().as_matrix()
    return RandR

def RandomTGen():
    """
    Creates random transformation matrix, SE(3)
    """
    RandT = np.zeros((4, 4))
    RandR = RandomRGen()
    t = np.random.rand(3)
    RandT[:3, :3] = RandR
    RandT[:3, 3] = t
    RandT[3, 3] = 1
    return RandT

def RandAXXBGen(n=2, noisy=False):
    """
    Creates list of matrices As and Bs to solve AX=XB
    """
    X = RandomTGen()
    A_set = []
    B_set = []
    for i in range(n):
        A = RandomTGen()
        B = np.linalg.inv(X) @ A @ X
        if noisy:
            B += np.random.normal(0, 0.1, size=(4, 4))
        A_set.append(A)
        B_set.append(B)
    return X, A_set, B_set

def CalcAXXB(A1, B1, A2, B2, verbose=False):
    """
    Calculate unique (analytical) solution for AX=XB. Assumes no noise.
    Frank C. Park and Bryan J. Martin, "Robot Sensor Calibration: Solving AX=XB on the Euclidean Group", IEEE 1994
    * A. Finding a Unique Solution on SO(3)
    * B. Solution on SE(3)
    """
    # Get rotation matrices and translation vectors
    RotA1 = A1[:3, :3]
    RotB1 = B1[:3, :3]
    RotA2 = A2[:3, :3]
    RotB2 = B2[:3, :3]
    tA1 = A1[:3, 3]
    tB1 = B1[:3, 3]
    tA2 = A2[:3, 3]
    tB2 = B2[:3, 3]
    # Matrix Logarithm mapping
    a1 = np.take(logm(RotA1).reshape(-1), indices=[7, 2, 3])
    b1 = np.take(logm(RotB1).reshape(-1), indices=[7, 2, 3])
    a2 = np.take(logm(RotA2).reshape(-1), indices=[7, 2, 3])
    b2 = np.take(logm(RotB2).reshape(-1), indices=[7, 2, 3])
    # Cross product
    a1xa2 = np.cross(a1, a2)
    b1xb2 = np.cross(b1, b2)
    # Unique solution on SO(3)
    A_ = np.zeros((3, 3))
    B_ = np.zeros((3, 3))
    A_[:, 0] = a1
    A_[:, 1] = a2
    A_[:, 2] = a1xa2
    B_[:, 0] = b1
    B_[:, 1] = b2
    B_[:, 2] = b1xb2
    RotX = A_ @ np.linalg.inv(B_)
    if verbose:
        print("RotX:", RotX)
    # Unique solution on SE(3)
    Left = np.concatenate([RotA1 - np.eye(3), 
                           RotA2 - np.eye(3)], axis=0)
    Right = np.concatenate([RotX @ tB1 - tA1, 
                            RotX @ tB2 - tA2], axis=0)
    tX = np.linalg.pinv(Left) @ Right
    if verbose:
        print("tX:", tX)
    X = np.zeros((4, 4))
    X[:3, :3] = RotX
    X[:3, 3] = tX
    X[3, 3] = 1
    return X

def NormalizeR(R):
    """
    Normalizes rotation matrix for noisy matrices which do not satisfy properties of SO(3)
    *** Need to find a better way to normalize... Sometimes produces error as matrix logarithm gives complex numbers
    """
    assert R.shape == (3, 3)
    for i in range(3):
        v = R[:, i]
        norm = np.linalg.norm(v)
        R[:, i] = v / norm
    return R

def find_closest_orthogonal_matrix(A):
    '''
    Find closest orthogonal matrix to *A* using iterative method.
    
    Bases on the code from REMOVE_SOURCE_LEAKAGE function from OSL Matlab package.
    Args:
        A (numpy.array): array shaped k, n, where k is number of channels, n - data points
    
    Returns:
        L (numpy.array): orthogonalized matrix with amplitudes preserved
    Reading:
        Colclough GL et al., A symmetric multivariate leakage correction for MEG connectomes.,
                    Neuroimage. 2015 Aug 15;117:439-48. doi: 10.1016/j.neuroimage.2015.03.071
    
    '''
    MAX_ITER  = 2000

    TOLERANCE = np.max((1, np.max(A.shape) * np.linalg.svd(A.T, False, False)[0])) * np.finfo(A.dtype).eps# TODO
    reldiff     = lambda a,b: 2*abs(a-b) / (abs(a)+abs(b))
    convergence = lambda rho, prev_rho: reldiff(rho, prev_rho) <= TOLERANCE

    A_b  = A.conj()
    d = np.sqrt(np.sum(A*A_b,axis=1))

    rhos = np.zeros(MAX_ITER)

    for i in range(MAX_ITER):
        scA = A.T * d

        u, s, vh = np.linalg.svd(scA, False)

        V = np.dot(u, vh)

        # TODO check is rank is full
        d = np.sum(A_b*V.T, axis=1)

        L = (V * d).T
        E = A-L
        rhos[i] = np.sqrt(np.sum(E*E.conj()))
        if i > 0 and convergence(rhos[i], rhos[i - 1]):
            break
    return L

def LeastSquaresAXXB(A_set, B_set, verbose=False):
    """
    Calculate least-squares solution for AX=XB with noise.
    Frank C. Park and Bryan J. Martin, "Robot Sensor Calibration: Solving AX=XB on the Euclidean Group", IEEE 1994
    * IV. A Least-Squares Solution
    """
    assert len(A_set) == len(B_set)
    n = len(A_set)
    M = np.zeros((3, 3))
    tA_set = []
    tB_set = []
    RotA_set = []
    for i in range(n):
        Ai = A_set[i]
        Bi = B_set[i]
        # Get rotation matrices and translation vectors
        RotAi = find_closest_orthogonal_matrix(Ai[:3, :3])
        RotBi = find_closest_orthogonal_matrix(Bi[:3, :3])
        tAi = Ai[:3, 3]
        tBi = Bi[:3, 3]
        # Matrix Logarithm mapping
        ai = np.take(logm(RotAi).reshape(-1), indices=[7, 2, 3])
        bi = np.take(logm(RotBi).reshape(-1), indices=[7, 2, 3])
        # Add onto matrix M
        M += bi.reshape(3, 1) @ ai.reshape(1, 3)
        # Append
        tA_set.append(tAi)
        tB_set.append(tBi)
        RotA_set.append(RotAi)
    # Solution on SO(3)
    MTM = M.T @ M
    w, v = np.linalg.eig(MTM)
    w_ = np.power(w, -0.5)
    Diag = np.diag(w_)
    RotX = v @ Diag @ np.linalg.inv(v) @ M.T
    RotX = NormalizeR(RotX)
    if verbose:
        print("RotX:", RotX)
    # Solution on SE(3)
    C_set = []
    d_set = []
    for i in range(n):
        Ci = np.eye(3) - RotA_set[i]
        di = tA_set[i].reshape(3, 1) - RotX @ tB_set[i].reshape(3, 1)
        C_set.append(Ci)
        d_set.append(di)
    C = np.concatenate(C_set, axis=0)
    d = np.concatenate(d_set, axis=0)
    tX = (np.linalg.pinv(C) @ d).reshape(-1)
    if verbose:
        print("tX:", tX)
    X = np.zeros((4, 4))
    X[:3, :3] = RotX
    X[:3, 3] = tX
    X[3, 3] = 1
    return X

if __name__=='__main__':
    X, A_set, B_set = RandAXXBGen(n=10, noisy=True)
    print("True RotX:", X[:3, :3])
    print("True tX:", X[:3, 3])
    X_pred = LeastSquaresAXXB(A_set, B_set, verbose=True)
    print(X_pred - X) # goal: all zeros (***noisy)
