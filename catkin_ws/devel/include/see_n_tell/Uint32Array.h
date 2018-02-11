// Generated by gencpp from file see_n_tell/Uint32Array.msg
// DO NOT EDIT!


#ifndef SEE_N_TELL_MESSAGE_UINT32ARRAY_H
#define SEE_N_TELL_MESSAGE_UINT32ARRAY_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace see_n_tell
{
template <class ContainerAllocator>
struct Uint32Array_
{
  typedef Uint32Array_<ContainerAllocator> Type;

  Uint32Array_()
    : data()  {
    }
  Uint32Array_(const ContainerAllocator& _alloc)
    : data(_alloc)  {
  (void)_alloc;
    }



   typedef std::vector<uint32_t, typename ContainerAllocator::template rebind<uint32_t>::other >  _data_type;
  _data_type data;




  typedef boost::shared_ptr< ::see_n_tell::Uint32Array_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::see_n_tell::Uint32Array_<ContainerAllocator> const> ConstPtr;

}; // struct Uint32Array_

typedef ::see_n_tell::Uint32Array_<std::allocator<void> > Uint32Array;

typedef boost::shared_ptr< ::see_n_tell::Uint32Array > Uint32ArrayPtr;
typedef boost::shared_ptr< ::see_n_tell::Uint32Array const> Uint32ArrayConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::see_n_tell::Uint32Array_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::see_n_tell::Uint32Array_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace see_n_tell

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'see_n_tell': ['/home/chibike/catkin_ws/src/see_n_tell/msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::see_n_tell::Uint32Array_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::see_n_tell::Uint32Array_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::see_n_tell::Uint32Array_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::see_n_tell::Uint32Array_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::see_n_tell::Uint32Array_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::see_n_tell::Uint32Array_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::see_n_tell::Uint32Array_<ContainerAllocator> >
{
  static const char* value()
  {
    return "a1376ac15481ebcd67c3fe86a75a7d55";
  }

  static const char* value(const ::see_n_tell::Uint32Array_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xa1376ac15481ebcdULL;
  static const uint64_t static_value2 = 0x67c3fe86a75a7d55ULL;
};

template<class ContainerAllocator>
struct DataType< ::see_n_tell::Uint32Array_<ContainerAllocator> >
{
  static const char* value()
  {
    return "see_n_tell/Uint32Array";
  }

  static const char* value(const ::see_n_tell::Uint32Array_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::see_n_tell::Uint32Array_<ContainerAllocator> >
{
  static const char* value()
  {
    return "uint32[] data\n\
";
  }

  static const char* value(const ::see_n_tell::Uint32Array_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::see_n_tell::Uint32Array_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.data);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct Uint32Array_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::see_n_tell::Uint32Array_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::see_n_tell::Uint32Array_<ContainerAllocator>& v)
  {
    s << indent << "data[]" << std::endl;
    for (size_t i = 0; i < v.data.size(); ++i)
    {
      s << indent << "  data[" << i << "]: ";
      Printer<uint32_t>::stream(s, indent + "  ", v.data[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // SEE_N_TELL_MESSAGE_UINT32ARRAY_H
