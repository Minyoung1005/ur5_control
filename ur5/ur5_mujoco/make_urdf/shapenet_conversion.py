from mesh import Mesh3D
import os
import trimesh
import matplotlib.pyplot as plt
from lxml import etree


def decompose_mesh(obj_path):
    maxhulls = 20
    mesh = Mesh3D(obj_path)
    mesh.clean_mesh()
    # for other mesh files 
    # mesh.clean_mesh(rescale_mesh=True, scale=0.04, rescaling_type='min') 
    org_trimesh = trimesh.Trimesh(vertices=mesh.vertices, faces=mesh.triangles)
    convex_list = org_trimesh.convex_decomposition(maxhulls=maxhulls)
    return convex_list

def export_stl(obj_name, convex_list):
    print(len(convex_list), 'meshes.')
    for i in range(0, len(convex_list)):
        if not os.path.isdir("meshes/{}".format(obj_name)):
            os.mkdir("meshes/{}".format(obj_name))
        savename = "meshes/{}/{}_{}.stl".format(obj_name, obj_name, i)
        part_trimesh = convex_list[i]
        trimesh.exchange.export.export_mesh(part_trimesh, savename, file_type="stl")
        #save_stl(savename, triangles, vertices, normals)

def export_xml(obj_name, convex_list):
    mujoco = etree.Element('mujoco', model=obj_name)
    asset = etree.Element('asset')
    worldbody = etree.Element('worldbody')
    body = etree.Element('body')
    body_col = etree.Element('body', name='collision')
    body_vis = etree.Element('body', name='visual')
    site1 = etree.Element('site', rgba='0 0 0 0', size='0.005', pos='0 0 -0.06', name='bottom_site')
    site2 = etree.Element('site', rgba='0 0 0 0', size='0.005', pos='0 0 0.04', name='top_site')
    site3 = etree.Element('site', rgba='0 0 0 0', size='0.005', pos='0.025 0.025 0', name='horizontal_radius_site')

    for i in range(0, len(convex_list)):
        asset.append( etree.Element('mesh', file='meshes/'+obj_name+'/'+obj_name+'_'+str(i)+'.stl', name=obj_name+'_'+str(i), scale="0.1 0.1 0.1") )
        body_col.append( etree.Element('geom', pos='0 0 0', mesh=obj_name+'_'+str(i), type='mesh', solimp='0.998 0.998 0.001',
            solref='0.001 1', density='100', friction='0.95 0.3 0.1', rgba='0 1 0 1', group='1', condim='4') )
        body_vis.append( etree.Element('geom', pos='0 0 0', mesh=obj_name+'_'+str(i), type='mesh', rgba='0 1 0 1',
            conaffinity='0', contype='0', group='0', mass='0.0001') )

    mujoco.append(asset)
    mujoco.append(worldbody)
    body.append(body_col)
    body.append(body_vis)
    body.append(site1)
    body.append(site2)
    body.append(site3)
    worldbody.append(body)    
    s = etree.tostring(mujoco, pretty_print=True).decode('utf-8')
    file = open("xml_objects/{}.xml".format(obj_name), 'w')
    file.write(s)
    file.close()


if __name__=='__main__':
    indices1 = [d for d in os.listdir() if os.path.isdir(d) and len(d)==8]
    for n1, dir1 in enumerate(indices1):
        indices2 = [d2 for d2 in os.listdir(dir1)]
        for n2, dir2 in enumerate(indices2):
            if n2==5: break
            model_path = os.path.join(dir1, dir2, 'models', 'model_normalized.obj')
            obj_name= 'shapenet{}-{}'.format(n1, n2)
            print(obj_name)

            convex_list = decompose_mesh(model_path)
            if type(convex_list)==trimesh.base.Trimesh:
                convex_list = [convex_list]
            export_stl(obj_name, convex_list)
            export_xml(obj_name, convex_list)
