// Generated by gencpp from file easy_handeye_msgs/SetAlgorithm.msg
// DO NOT EDIT!


#ifndef EASY_HANDEYE_MSGS_MESSAGE_SETALGORITHM_H
#define EASY_HANDEYE_MSGS_MESSAGE_SETALGORITHM_H

#include <ros/service_traits.h>


#include <easy_handeye_msgs/SetAlgorithmRequest.h>
#include <easy_handeye_msgs/SetAlgorithmResponse.h>


namespace easy_handeye_msgs
{

struct SetAlgorithm
{

typedef SetAlgorithmRequest Request;
typedef SetAlgorithmResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct SetAlgorithm
} // namespace easy_handeye_msgs


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::easy_handeye_msgs::SetAlgorithm > {
  static const char* value()
  {
    return "e997a30f8fd361b5c93f82bb8a67d408";
  }

  static const char* value(const ::easy_handeye_msgs::SetAlgorithm&) { return value(); }
};

template<>
struct DataType< ::easy_handeye_msgs::SetAlgorithm > {
  static const char* value()
  {
    return "easy_handeye_msgs/SetAlgorithm";
  }

  static const char* value(const ::easy_handeye_msgs::SetAlgorithm&) { return value(); }
};


// service_traits::MD5Sum< ::easy_handeye_msgs::SetAlgorithmRequest> should match 
// service_traits::MD5Sum< ::easy_handeye_msgs::SetAlgorithm > 
template<>
struct MD5Sum< ::easy_handeye_msgs::SetAlgorithmRequest>
{
  static const char* value()
  {
    return MD5Sum< ::easy_handeye_msgs::SetAlgorithm >::value();
  }
  static const char* value(const ::easy_handeye_msgs::SetAlgorithmRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::easy_handeye_msgs::SetAlgorithmRequest> should match 
// service_traits::DataType< ::easy_handeye_msgs::SetAlgorithm > 
template<>
struct DataType< ::easy_handeye_msgs::SetAlgorithmRequest>
{
  static const char* value()
  {
    return DataType< ::easy_handeye_msgs::SetAlgorithm >::value();
  }
  static const char* value(const ::easy_handeye_msgs::SetAlgorithmRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::easy_handeye_msgs::SetAlgorithmResponse> should match 
// service_traits::MD5Sum< ::easy_handeye_msgs::SetAlgorithm > 
template<>
struct MD5Sum< ::easy_handeye_msgs::SetAlgorithmResponse>
{
  static const char* value()
  {
    return MD5Sum< ::easy_handeye_msgs::SetAlgorithm >::value();
  }
  static const char* value(const ::easy_handeye_msgs::SetAlgorithmResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::easy_handeye_msgs::SetAlgorithmResponse> should match 
// service_traits::DataType< ::easy_handeye_msgs::SetAlgorithm > 
template<>
struct DataType< ::easy_handeye_msgs::SetAlgorithmResponse>
{
  static const char* value()
  {
    return DataType< ::easy_handeye_msgs::SetAlgorithm >::value();
  }
  static const char* value(const ::easy_handeye_msgs::SetAlgorithmResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // EASY_HANDEYE_MSGS_MESSAGE_SETALGORITHM_H
