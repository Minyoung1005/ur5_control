# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from marker_msgs/MarkerWithCovariance.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import marker_msgs.msg

class MarkerWithCovariance(genpy.Message):
  _md5sum = "ace241bc4ec8f4b399c13e05763be31a"
  _type = "marker_msgs/MarkerWithCovariance"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# This expresses a marker in free space with uncertainty.

Marker marker

# Row-major representation of the 6x6 covariance matrix
# The orientation parameters use a fixed-axis representation.
# In order, the parameters are:
# (x, y, z, rotation about X axis, rotation about Y axis, rotation about Z axis)
float64[36] covariance

================================================================================
MSG: marker_msgs/Marker
# This expresses a marker/fiducial in a 3D space
int32[] ids                  # possible ids of the detected fiducial (empty if no id could be identified)
float64[] ids_confidence     # confidence of the possible ids in [0, 1]
geometry_msgs/Pose pose      # pose of the detected marker/fiducial

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w
"""
  __slots__ = ['marker','covariance']
  _slot_types = ['marker_msgs/Marker','float64[36]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       marker,covariance

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(MarkerWithCovariance, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.marker is None:
        self.marker = marker_msgs.msg.Marker()
      if self.covariance is None:
        self.covariance = [0.] * 36
    else:
      self.marker = marker_msgs.msg.Marker()
      self.covariance = [0.] * 36

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      length = len(self.marker.ids)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(struct.Struct(pattern).pack(*self.marker.ids))
      length = len(self.marker.ids_confidence)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.marker.ids_confidence))
      _x = self
      buff.write(_get_struct_7d().pack(_x.marker.pose.position.x, _x.marker.pose.position.y, _x.marker.pose.position.z, _x.marker.pose.orientation.x, _x.marker.pose.orientation.y, _x.marker.pose.orientation.z, _x.marker.pose.orientation.w))
      buff.write(_get_struct_36d().pack(*self.covariance))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.marker is None:
        self.marker = marker_msgs.msg.Marker()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.marker.ids = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.marker.ids_confidence = s.unpack(str[start:end])
      _x = self
      start = end
      end += 56
      (_x.marker.pose.position.x, _x.marker.pose.position.y, _x.marker.pose.position.z, _x.marker.pose.orientation.x, _x.marker.pose.orientation.y, _x.marker.pose.orientation.z, _x.marker.pose.orientation.w,) = _get_struct_7d().unpack(str[start:end])
      start = end
      end += 288
      self.covariance = _get_struct_36d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      length = len(self.marker.ids)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(self.marker.ids.tostring())
      length = len(self.marker.ids_confidence)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.marker.ids_confidence.tostring())
      _x = self
      buff.write(_get_struct_7d().pack(_x.marker.pose.position.x, _x.marker.pose.position.y, _x.marker.pose.position.z, _x.marker.pose.orientation.x, _x.marker.pose.orientation.y, _x.marker.pose.orientation.z, _x.marker.pose.orientation.w))
      buff.write(self.covariance.tostring())
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.marker is None:
        self.marker = marker_msgs.msg.Marker()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.marker.ids = numpy.frombuffer(str[start:end], dtype=numpy.int32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.marker.ids_confidence = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      _x = self
      start = end
      end += 56
      (_x.marker.pose.position.x, _x.marker.pose.position.y, _x.marker.pose.position.z, _x.marker.pose.orientation.x, _x.marker.pose.orientation.y, _x.marker.pose.orientation.z, _x.marker.pose.orientation.w,) = _get_struct_7d().unpack(str[start:end])
      start = end
      end += 288
      self.covariance = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=36)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_36d = None
def _get_struct_36d():
    global _struct_36d
    if _struct_36d is None:
        _struct_36d = struct.Struct("<36d")
    return _struct_36d
_struct_7d = None
def _get_struct_7d():
    global _struct_7d
    if _struct_7d is None:
        _struct_7d = struct.Struct("<7d")
    return _struct_7d