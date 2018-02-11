// Generated by gencpp from file randomwalker/GetScoreRequest.msg
// DO NOT EDIT!


#ifndef RANDOMWALKER_MESSAGE_GETSCOREREQUEST_H
#define RANDOMWALKER_MESSAGE_GETSCOREREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace randomwalker
{
template <class ContainerAllocator>
struct GetScoreRequest_
{
  typedef GetScoreRequest_<ContainerAllocator> Type;

  GetScoreRequest_()
    : row(0)
    , col(0)  {
    }
  GetScoreRequest_(const ContainerAllocator& _alloc)
    : row(0)
    , col(0)  {
  (void)_alloc;
    }



   typedef int32_t _row_type;
  _row_type row;

   typedef int32_t _col_type;
  _col_type col;




  typedef boost::shared_ptr< ::randomwalker::GetScoreRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::randomwalker::GetScoreRequest_<ContainerAllocator> const> ConstPtr;

}; // struct GetScoreRequest_

typedef ::randomwalker::GetScoreRequest_<std::allocator<void> > GetScoreRequest;

typedef boost::shared_ptr< ::randomwalker::GetScoreRequest > GetScoreRequestPtr;
typedef boost::shared_ptr< ::randomwalker::GetScoreRequest const> GetScoreRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::randomwalker::GetScoreRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::randomwalker::GetScoreRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace randomwalker

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::randomwalker::GetScoreRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::randomwalker::GetScoreRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::randomwalker::GetScoreRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::randomwalker::GetScoreRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::randomwalker::GetScoreRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::randomwalker::GetScoreRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::randomwalker::GetScoreRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "0d84ae8c1de5e21d4e0f4c459d2e02dd";
  }

  static const char* value(const ::randomwalker::GetScoreRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x0d84ae8c1de5e21dULL;
  static const uint64_t static_value2 = 0x4e0f4c459d2e02ddULL;
};

template<class ContainerAllocator>
struct DataType< ::randomwalker::GetScoreRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "randomwalker/GetScoreRequest";
  }

  static const char* value(const ::randomwalker::GetScoreRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::randomwalker::GetScoreRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "\n\
int32 row\n\
int32 col\n\
";
  }

  static const char* value(const ::randomwalker::GetScoreRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::randomwalker::GetScoreRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.row);
      stream.next(m.col);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct GetScoreRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::randomwalker::GetScoreRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::randomwalker::GetScoreRequest_<ContainerAllocator>& v)
  {
    s << indent << "row: ";
    Printer<int32_t>::stream(s, indent + "  ", v.row);
    s << indent << "col: ";
    Printer<int32_t>::stream(s, indent + "  ", v.col);
  }
};

} // namespace message_operations
} // namespace ros

#endif // RANDOMWALKER_MESSAGE_GETSCOREREQUEST_H