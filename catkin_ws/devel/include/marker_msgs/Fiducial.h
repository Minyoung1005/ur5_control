// Generated by gencpp from file marker_msgs/Fiducial.msg
// DO NOT EDIT!


#ifndef MARKER_MSGS_MESSAGE_FIDUCIAL_H
#define MARKER_MSGS_MESSAGE_FIDUCIAL_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <geometry_msgs/Point.h>
#include <geometry_msgs/Point.h>

namespace marker_msgs
{
template <class ContainerAllocator>
struct Fiducial_
{
  typedef Fiducial_<ContainerAllocator> Type;

  Fiducial_()
    : ids()
    , ids_confidence()
    , object_points()
    , image_points()  {
    }
  Fiducial_(const ContainerAllocator& _alloc)
    : ids(_alloc)
    , ids_confidence(_alloc)
    , object_points(_alloc)
    , image_points(_alloc)  {
  (void)_alloc;
    }



   typedef std::vector<int32_t, typename ContainerAllocator::template rebind<int32_t>::other >  _ids_type;
  _ids_type ids;

   typedef std::vector<double, typename ContainerAllocator::template rebind<double>::other >  _ids_confidence_type;
  _ids_confidence_type ids_confidence;

   typedef std::vector< ::geometry_msgs::Point_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::geometry_msgs::Point_<ContainerAllocator> >::other >  _object_points_type;
  _object_points_type object_points;

   typedef std::vector< ::geometry_msgs::Point_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::geometry_msgs::Point_<ContainerAllocator> >::other >  _image_points_type;
  _image_points_type image_points;





  typedef boost::shared_ptr< ::marker_msgs::Fiducial_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::marker_msgs::Fiducial_<ContainerAllocator> const> ConstPtr;

}; // struct Fiducial_

typedef ::marker_msgs::Fiducial_<std::allocator<void> > Fiducial;

typedef boost::shared_ptr< ::marker_msgs::Fiducial > FiducialPtr;
typedef boost::shared_ptr< ::marker_msgs::Fiducial const> FiducialConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::marker_msgs::Fiducial_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::marker_msgs::Fiducial_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace marker_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'marker_msgs': ['/home/dof6/catkin_ws/src/marker_msgs-master/msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::marker_msgs::Fiducial_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::marker_msgs::Fiducial_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::marker_msgs::Fiducial_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::marker_msgs::Fiducial_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::marker_msgs::Fiducial_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::marker_msgs::Fiducial_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::marker_msgs::Fiducial_<ContainerAllocator> >
{
  static const char* value()
  {
    return "0771474f385b4ef416eeda4ba2143ce2";
  }

  static const char* value(const ::marker_msgs::Fiducial_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x0771474f385b4ef4ULL;
  static const uint64_t static_value2 = 0x16eeda4ba2143ce2ULL;
};

template<class ContainerAllocator>
struct DataType< ::marker_msgs::Fiducial_<ContainerAllocator> >
{
  static const char* value()
  {
    return "marker_msgs/Fiducial";
  }

  static const char* value(const ::marker_msgs::Fiducial_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::marker_msgs::Fiducial_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# This expresses a known detected fiducial in image space\n\
int32[] ids                         # possible ids of the detected fiducial (empty if no id could be identified)\n\
float64[] ids_confidence            # confidence of the possible ids in [0, 1]\n\
geometry_msgs/Point[] object_points # Array of object points in the object coordinate space.\n\
geometry_msgs/Point[] image_points  # Array of corresponding image points. Point.z is not used.\n\
================================================================================\n\
MSG: geometry_msgs/Point\n\
# This contains the position of a point in free space\n\
float64 x\n\
float64 y\n\
float64 z\n\
";
  }

  static const char* value(const ::marker_msgs::Fiducial_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::marker_msgs::Fiducial_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.ids);
      stream.next(m.ids_confidence);
      stream.next(m.object_points);
      stream.next(m.image_points);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct Fiducial_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::marker_msgs::Fiducial_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::marker_msgs::Fiducial_<ContainerAllocator>& v)
  {
    s << indent << "ids[]" << std::endl;
    for (size_t i = 0; i < v.ids.size(); ++i)
    {
      s << indent << "  ids[" << i << "]: ";
      Printer<int32_t>::stream(s, indent + "  ", v.ids[i]);
    }
    s << indent << "ids_confidence[]" << std::endl;
    for (size_t i = 0; i < v.ids_confidence.size(); ++i)
    {
      s << indent << "  ids_confidence[" << i << "]: ";
      Printer<double>::stream(s, indent + "  ", v.ids_confidence[i]);
    }
    s << indent << "object_points[]" << std::endl;
    for (size_t i = 0; i < v.object_points.size(); ++i)
    {
      s << indent << "  object_points[" << i << "]: ";
      s << std::endl;
      s << indent;
      Printer< ::geometry_msgs::Point_<ContainerAllocator> >::stream(s, indent + "    ", v.object_points[i]);
    }
    s << indent << "image_points[]" << std::endl;
    for (size_t i = 0; i < v.image_points.size(); ++i)
    {
      s << indent << "  image_points[" << i << "]: ";
      s << std::endl;
      s << indent;
      Printer< ::geometry_msgs::Point_<ContainerAllocator> >::stream(s, indent + "    ", v.image_points[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // MARKER_MSGS_MESSAGE_FIDUCIAL_H
