## *********************************************************
##
## File autogenerated for the tuw_aruco package
## by the dynamic_reconfigure package.
## Please do not edit.
##
## ********************************************************/

from dynamic_reconfigure.encoding import extract_params

inf = float('inf')

config_description = {'upper': 'DEFAULT', 'lower': 'groups', 'srcline': 245, 'name': 'Default', 'parent': 0, 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'cstate': 'true', 'parentname': 'Default', 'class': 'DEFAULT', 'field': 'default', 'state': True, 'parentclass': '', 'groups': [], 'parameters': [{'srcline': 290, 'description': 'Show camera debug image', 'max': True, 'cconsttype': 'const bool', 'ctype': 'bool', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'show_debug_image', 'edit_method': '', 'default': True, 'level': 0, 'min': False, 'type': 'bool'}, {'srcline': 290, 'description': 'Marker dictonary type', 'max': '', 'cconsttype': 'const char * const', 'ctype': 'std::string', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'marker_dictonary', 'edit_method': "{'enum_description': 'Marker dictonary type', 'enum': [{'srcline': 11, 'description': 'ArUco orginal', 'srcfile': '/home/dof6/catkin_ws/src/tuw_marker_detection-kinetic-devel/tuw_aruco/cfg/ArUco.cfg', 'cconsttype': 'const char * const', 'value': 'ARUCO', 'ctype': 'std::string', 'type': 'str', 'name': 'ARUCO'}, {'srcline': 12, 'description': '', 'srcfile': '/home/dof6/catkin_ws/src/tuw_marker_detection-kinetic-devel/tuw_aruco/cfg/ArUco.cfg', 'cconsttype': 'const char * const', 'value': 'ARUCO_MIP_25h7', 'ctype': 'std::string', 'type': 'str', 'name': 'ARUCO_MIP_25h7'}, {'srcline': 13, 'description': '', 'srcfile': '/home/dof6/catkin_ws/src/tuw_marker_detection-kinetic-devel/tuw_aruco/cfg/ArUco.cfg', 'cconsttype': 'const char * const', 'value': 'ARUCO_MIP_16h3', 'ctype': 'std::string', 'type': 'str', 'name': 'ARUCO_MIP_16h3'}, {'srcline': 14, 'description': 'recommended', 'srcfile': '/home/dof6/catkin_ws/src/tuw_marker_detection-kinetic-devel/tuw_aruco/cfg/ArUco.cfg', 'cconsttype': 'const char * const', 'value': 'ARUCO_MIP_36h12', 'ctype': 'std::string', 'type': 'str', 'name': 'ARUCO_MIP_36h12'}, {'srcline': 15, 'description': '', 'srcfile': '/home/dof6/catkin_ws/src/tuw_marker_detection-kinetic-devel/tuw_aruco/cfg/ArUco.cfg', 'cconsttype': 'const char * const', 'value': 'ARTAG', 'ctype': 'std::string', 'type': 'str', 'name': 'ARTAG'}, {'srcline': 16, 'description': '', 'srcfile': '/home/dof6/catkin_ws/src/tuw_marker_detection-kinetic-devel/tuw_aruco/cfg/ArUco.cfg', 'cconsttype': 'const char * const', 'value': 'ARTOOLKITPLUS', 'ctype': 'std::string', 'type': 'str', 'name': 'ARTOOLKITPLUS'}, {'srcline': 17, 'description': 'default', 'srcfile': '/home/dof6/catkin_ws/src/tuw_marker_detection-kinetic-devel/tuw_aruco/cfg/ArUco.cfg', 'cconsttype': 'const char * const', 'value': 'ARTOOLKITPLUSBCH', 'ctype': 'std::string', 'type': 'str', 'name': 'ARTOOLKITPLUSBCH'}, {'srcline': 19, 'description': '', 'srcfile': '/home/dof6/catkin_ws/src/tuw_marker_detection-kinetic-devel/tuw_aruco/cfg/ArUco.cfg', 'cconsttype': 'const char * const', 'value': 'TAG16h5', 'ctype': 'std::string', 'type': 'str', 'name': 'TAG16h5'}, {'srcline': 20, 'description': '', 'srcfile': '/home/dof6/catkin_ws/src/tuw_marker_detection-kinetic-devel/tuw_aruco/cfg/ArUco.cfg', 'cconsttype': 'const char * const', 'value': 'TAG25h7', 'ctype': 'std::string', 'type': 'str', 'name': 'TAG25h7'}, {'srcline': 21, 'description': '', 'srcfile': '/home/dof6/catkin_ws/src/tuw_marker_detection-kinetic-devel/tuw_aruco/cfg/ArUco.cfg', 'cconsttype': 'const char * const', 'value': 'TAG25h9', 'ctype': 'std::string', 'type': 'str', 'name': 'TAG25h9'}, {'srcline': 22, 'description': '', 'srcfile': '/home/dof6/catkin_ws/src/tuw_marker_detection-kinetic-devel/tuw_aruco/cfg/ArUco.cfg', 'cconsttype': 'const char * const', 'value': 'TAG36h11', 'ctype': 'std::string', 'type': 'str', 'name': 'TAG36h11'}, {'srcline': 23, 'description': '', 'srcfile': '/home/dof6/catkin_ws/src/tuw_marker_detection-kinetic-devel/tuw_aruco/cfg/ArUco.cfg', 'cconsttype': 'const char * const', 'value': 'TAG36h10', 'ctype': 'std::string', 'type': 'str', 'name': 'TAG36h10'}]}", 'default': 'ARTOOLKITPLUSBCH', 'level': 0, 'min': '', 'type': 'str'}, {'srcline': 290, 'description': 'Marker size in meters', 'max': inf, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'marker_size', 'edit_method': '', 'default': 0.06, 'level': 0, 'min': -inf, 'type': 'double'}, {'srcline': 290, 'description': '', 'max': True, 'cconsttype': 'const bool', 'ctype': 'bool', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'publish_tf', 'edit_method': '', 'default': True, 'level': 0, 'min': False, 'type': 'bool'}, {'srcline': 290, 'description': '', 'max': True, 'cconsttype': 'const bool', 'ctype': 'bool', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'publish_markers', 'edit_method': '', 'default': True, 'level': 0, 'min': False, 'type': 'bool'}, {'srcline': 290, 'description': 'Publish fiducials to allow 3th party pose estimation.', 'max': True, 'cconsttype': 'const bool', 'ctype': 'bool', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'publish_fiducials', 'edit_method': '', 'default': False, 'level': 0, 'min': False, 'type': 'bool'}, {'srcline': 290, 'description': 'ArUco pose estimation is enabled.', 'max': True, 'cconsttype': 'const bool', 'ctype': 'bool', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'pose_estimation_enabled', 'edit_method': '', 'default': True, 'level': 0, 'min': False, 'type': 'bool'}], 'type': '', 'id': 0}

min = {}
max = {}
defaults = {}
level = {}
type = {}
all_level = 0

#def extract_params(config):
#    params = []
#    params.extend(config['parameters'])
#    for group in config['groups']:
#        params.extend(extract_params(group))
#    return params

for param in extract_params(config_description):
    min[param['name']] = param['min']
    max[param['name']] = param['max']
    defaults[param['name']] = param['default']
    level[param['name']] = param['level']
    type[param['name']] = param['type']
    all_level = all_level | param['level']

ArUco_ARUCO = 'ARUCO'
ArUco_ARUCO_MIP_25h7 = 'ARUCO_MIP_25h7'
ArUco_ARUCO_MIP_16h3 = 'ARUCO_MIP_16h3'
ArUco_ARUCO_MIP_36h12 = 'ARUCO_MIP_36h12'
ArUco_ARTAG = 'ARTAG'
ArUco_ARTOOLKITPLUS = 'ARTOOLKITPLUS'
ArUco_ARTOOLKITPLUSBCH = 'ARTOOLKITPLUSBCH'
ArUco_TAG16h5 = 'TAG16h5'
ArUco_TAG25h7 = 'TAG25h7'
ArUco_TAG25h9 = 'TAG25h9'
ArUco_TAG36h11 = 'TAG36h11'
ArUco_TAG36h10 = 'TAG36h10'
