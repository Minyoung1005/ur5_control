// Generated by gencpp from file marker_msgs/MarkerWithCovarianceStamped.msg
// DO NOT EDIT!


#ifndef MARKER_MSGS_MESSAGE_MARKERWITHCOVARIANCESTAMPED_H
#define MARKER_MSGS_MESSAGE_MARKERWITHCOVARIANCESTAMPED_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>
#include <marker_msgs/MarkerWithCovariance.h>

namespace marker_msgs
{
template <class ContainerAllocator>
struct MarkerWithCovarianceStamped_
{
  typedef MarkerWithCovarianceStamped_<ContainerAllocator> Type;

  MarkerWithCovarianceStamped_()
    : header()
    , marker()  {
    }
  MarkerWithCovarianceStamped_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , marker(_alloc)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef  ::marker_msgs::MarkerWithCovariance_<ContainerAllocator>  _marker_type;
  _marker_type marker;





  typedef boost::shared_ptr< ::marker_msgs::MarkerWithCovarianceStamped_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::marker_msgs::MarkerWithCovarianceStamped_<ContainerAllocator> const> ConstPtr;

}; // struct MarkerWithCovarianceStamped_

typedef ::marker_msgs::MarkerWithCovarianceStamped_<std::allocator<void> > MarkerWithCovarianceStamped;

typedef boost::shared_ptr< ::marker_msgs::MarkerWithCovarianceStamped > MarkerWithCovarianceStampedPtr;
typedef boost::shared_ptr< ::marker_msgs::MarkerWithCovarianceStamped const> MarkerWithCovarianceStampedConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::marker_msgs::MarkerWithCovarianceStamped_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::marker_msgs::MarkerWithCovarianceStamped_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace marker_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': True}
// {'marker_msgs': ['/home/dof6/catkin_ws/src/marker_msgs-master/msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::marker_msgs::MarkerWithCovarianceStamped_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::marker_msgs::MarkerWithCovarianceStamped_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::marker_msgs::MarkerWithCovarianceStamped_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::marker_msgs::MarkerWithCovarianceStamped_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::marker_msgs::MarkerWithCovarianceStamped_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::marker_msgs::MarkerWithCovarianceStamped_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::marker_msgs::MarkerWithCovarianceStamped_<ContainerAllocator> >
{
  static const char* value()
  {
    return "1c6b4e4db4f1f1f63303a467ab44aef6";
  }

  static const char* value(const ::marker_msgs::MarkerWithCovarianceStamped_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x1c6b4e4db4f1f1f6ULL;
  static const uint64_t static_value2 = 0x3303a467ab44aef6ULL;
};

template<class ContainerAllocator>
struct DataType< ::marker_msgs::MarkerWithCovarianceStamped_<ContainerAllocator> >
{
  static const char* value()
  {
    return "marker_msgs/MarkerWithCovarianceStamped";
  }

  static const char* value(const ::marker_msgs::MarkerWithCovarianceStamped_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::marker_msgs::MarkerWithCovarianceStamped_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# This represents a marker with reference coordinate frame and timestamp and covariance matrix\n\
Header header\n\
MarkerWithCovariance marker\n\
================================================================================\n\
MSG: std_msgs/Header\n\
# Standard metadata for higher-level stamped data types.\n\
# This is generally used to communicate timestamped data \n\
# in a particular coordinate frame.\n\
# \n\
# sequence ID: consecutively increasing ID \n\
uint32 seq\n\
#Two-integer timestamp that is expressed as:\n\
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n\
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n\
# time-handling sugar is provided by the client library\n\
time stamp\n\
#Frame this data is associated with\n\
# 0: no frame\n\
# 1: global frame\n\
string frame_id\n\
\n\
================================================================================\n\
MSG: marker_msgs/MarkerWithCovariance\n\
# This expresses a marker in free space with uncertainty.\n\
\n\
Marker marker\n\
\n\
# Row-major representation of the 6x6 covariance matrix\n\
# The orientation parameters use a fixed-axis representation.\n\
# In order, the parameters are:\n\
# (x, y, z, rotation about X axis, rotation about Y axis, rotation about Z axis)\n\
float64[36] covariance\n\
\n\
================================================================================\n\
MSG: marker_msgs/Marker\n\
# This expresses a marker/fiducial in a 3D space\n\
int32[] ids                  # possible ids of the detected fiducial (empty if no id could be identified)\n\
float64[] ids_confidence     # confidence of the possible ids in [0, 1]\n\
geometry_msgs/Pose pose      # pose of the detected marker/fiducial\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Pose\n\
# A representation of pose in free space, composed of position and orientation. \n\
Point position\n\
Quaternion orientation\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Point\n\
# This contains the position of a point in free space\n\
float64 x\n\
float64 y\n\
float64 z\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Quaternion\n\
# This represents an orientation in free space in quaternion form.\n\
\n\
float64 x\n\
float64 y\n\
float64 z\n\
float64 w\n\
";
  }

  static const char* value(const ::marker_msgs::MarkerWithCovarianceStamped_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::marker_msgs::MarkerWithCovarianceStamped_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.marker);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct MarkerWithCovarianceStamped_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::marker_msgs::MarkerWithCovarianceStamped_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::marker_msgs::MarkerWithCovarianceStamped_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "marker: ";
    s << std::endl;
    Printer< ::marker_msgs::MarkerWithCovariance_<ContainerAllocator> >::stream(s, indent + "  ", v.marker);
  }
};

} // namespace message_operations
} // namespace ros

#endif // MARKER_MSGS_MESSAGE_MARKERWITHCOVARIANCESTAMPED_H
