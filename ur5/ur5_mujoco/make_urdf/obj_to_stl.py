from mesh import Mesh3D
import os
import trimesh
import matplotlib.pyplot as plt
from lxml import etree

filepath = "/home/cyh/meshes/3dnet/1a4daa4904bb4a0949684e7f0bb99f9c.obj"
maxhulls = 20
mesh = Mesh3D(filepath)
mesh.clean_mesh()
# for other mesh files 
# mesh.clean_mesh(rescale_mesh=True, scale=0.04, rescaling_type='min') 
org_trimesh = trimesh.Trimesh(vertices=mesh.vertices, faces=mesh.triangles)
convex_list = org_trimesh.convex_decomposition(maxhulls=maxhulls)

'''ASCII stl file
def save_stl(savename, triangles, vertices, normals):
    f = open(savename, 'w')
    f.write("solid\n")
    for i in range(0, triangles.shape[0]):
        x, y, z = normals[i]
        line = "  facet normal " + str(x) + " " + str(y) + " " + str(z) + "\n"
        f.write(line)
        f.write("    outer loop\n")
        x, y, z = triangles[i][0]
        line = "      vertex " + str(x) + " " + str(y) + " " + str(z) + "\n"
        f.write(line)
        x, y, z = triangles[i][1]
        line = "      vertex " + str(x) + " " + str(y) + " " + str(z) + "\n"
        f.write(line)
        x, y, z = triangles[i][2]
        line = "      vertex " + str(x) + " " + str(y) + " " + str(z) + "\n"
        f.write(line)
        f.write("    endloop\n")
        f.write("  endfacet\n")
    f.write("endsolid\n")
    f.close()
'''

for i in range(0, len(convex_list)):
    savename = "/home/cyh/meshes/meshes/obj1_" + str(i) + ".stl"
    part_trimesh = convex_list[i]
    trimesh.exchange.export.export_mesh(part_trimesh, savename, file_type="stl")
    #save_stl(savename, triangles, vertices, normals)

obj_name= 'obj1'

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
    asset.append( etree.Element('mesh', file='meshes/'+obj_name+'/'+obj_name+'_'+str(i)+'.stl', name=obj_name+'_'+str(i)) )
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
s = etree.tostring(mujoco, pretty_print=True)
file = open(obj_name+'.xml', 'w')
file.write(s)
file.close()
