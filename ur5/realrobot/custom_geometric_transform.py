import numpy as np
import cv2

def get_Rp_from_T(T):
    R = T[0:3, 0:3]
    p = T[0:3, 3:4]
    return (R, p)

def form_T(R, p):
    T = np.identity(4)
    T[0:3, 0:3] = R
    T[0:3, 3:4] = np.array(p).reshape((3, 1))
    return T

def rot3x3_to_4x4(R):
    T = np.identity(4)
    T[0:3, 0:3] = R
    return T

def rot(axis, angle, matrix_len=3):
    R_vec = np.array(axis).astype(float)*angle
    R, _ = cv2.Rodrigues(R_vec)
    if matrix_len == 4:
        R = rot3x3_to_4x4(R)
    return R

def rotx(angle, matrix_len=3):
    return rot([1,0,0], angle, matrix_len)

def roty(angle, matrix_len=3):
    return rot([0,1,0], angle, matrix_len)

def rotz(angle, matrix_len=3):
    return rot([0,0,1], angle, matrix_len)

def euler2matrix(x, y, z, order='rzxz'):
    if order=='rxyz':
        return rotx(x).dot(roty(y)).dot(rotz(z))
    elif order=='rzxz':
        th1, th2, th3 = x, y, z
        x1 = np.cos(th1)*np.cos(th3) - np.cos(th2)*np.sin(th1)*np.sin(th3)
        x2 = -np.cos(th1)*np.sin(th3) - np.cos(th2)*np.cos(th3)*np.sin(th1)
        x3 = np.sin(th1)*np.sin(th2)
        y1 = np.cos(th3)*np.sin(th1) + np.cos(th1)*np.cos(th2)*np.sin(th3)
        y2 = np.cos(th1)*np.cos(th2)*np.cos(th3) - np.sin(th1)*np.sin(th3)
        y3 = -np.cos(th1)*np.sin(th2)
        z1 = np.sin(th2)*np.sin(th3)
        z2 = np.cos(th3)*np.sin(th2)
        z3 = np.cos(th2)
        return np.array([[x1,x2,x3],
                     [y1,y2,y3],
                     [z1,z2,z3]])
