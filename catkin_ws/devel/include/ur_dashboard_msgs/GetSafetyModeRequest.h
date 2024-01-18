// Generated by gencpp from file ur_dashboard_msgs/GetSafetyModeRequest.msg
// DO NOT EDIT!


#ifndef UR_DASHBOARD_MSGS_MESSAGE_GETSAFETYMODEREQUEST_H
#define UR_DASHBOARD_MSGS_MESSAGE_GETSAFETYMODEREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace ur_dashboard_msgs
{
template <class ContainerAllocator>
struct GetSafetyModeRequest_
{
  typedef GetSafetyModeRequest_<ContainerAllocator> Type;

  GetSafetyModeRequest_()
    {
    }
  GetSafetyModeRequest_(const ContainerAllocator& _alloc)
    {
  (void)_alloc;
    }







  typedef boost::shared_ptr< ::ur_dashboard_msgs::GetSafetyModeRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::ur_dashboard_msgs::GetSafetyModeRequest_<ContainerAllocator> const> ConstPtr;

}; // struct GetSafetyModeRequest_

typedef ::ur_dashboard_msgs::GetSafetyModeRequest_<std::allocator<void> > GetSafetyModeRequest;

typedef boost::shared_ptr< ::ur_dashboard_msgs::GetSafetyModeRequest > GetSafetyModeRequestPtr;
typedef boost::shared_ptr< ::ur_dashboard_msgs::GetSafetyModeRequest const> GetSafetyModeRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::ur_dashboard_msgs::GetSafetyModeRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::ur_dashboard_msgs::GetSafetyModeRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace ur_dashboard_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'actionlib_msgs': ['/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg'], 'ur_dashboard_msgs': ['/home/dof6/catkin_ws/src/Universal_Robots_ROS_Driver/ur_dashboard_msgs/msg', '/home/dof6/catkin_ws/devel/share/ur_dashboard_msgs/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::ur_dashboard_msgs::GetSafetyModeRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::ur_dashboard_msgs::GetSafetyModeRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ur_dashboard_msgs::GetSafetyModeRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ur_dashboard_msgs::GetSafetyModeRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ur_dashboard_msgs::GetSafetyModeRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ur_dashboard_msgs::GetSafetyModeRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::ur_dashboard_msgs::GetSafetyModeRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "d41d8cd98f00b204e9800998ecf8427e";
  }

  static const char* value(const ::ur_dashboard_msgs::GetSafetyModeRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xd41d8cd98f00b204ULL;
  static const uint64_t static_value2 = 0xe9800998ecf8427eULL;
};

template<class ContainerAllocator>
struct DataType< ::ur_dashboard_msgs::GetSafetyModeRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ur_dashboard_msgs/GetSafetyModeRequest";
  }

  static const char* value(const ::ur_dashboard_msgs::GetSafetyModeRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::ur_dashboard_msgs::GetSafetyModeRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "\n\
";
  }

  static const char* value(const ::ur_dashboard_msgs::GetSafetyModeRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::ur_dashboard_msgs::GetSafetyModeRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream&, T)
    {}

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct GetSafetyModeRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::ur_dashboard_msgs::GetSafetyModeRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream&, const std::string&, const ::ur_dashboard_msgs::GetSafetyModeRequest_<ContainerAllocator>&)
  {}
};

} // namespace message_operations
} // namespace ros

#endif // UR_DASHBOARD_MSGS_MESSAGE_GETSAFETYMODEREQUEST_H
