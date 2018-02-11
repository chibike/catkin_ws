// Generated by gencpp from file see_n_tell/Uint16Array.msg
// DO NOT EDIT!


#ifndef SEE_N_TELL_MESSAGE_UINT16ARRAY_H
#define SEE_N_TELL_MESSAGE_UINT16ARRAY_H


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
struct Uint16Array_
{
  typedef Uint16Array_<ContainerAllocator> Type;

  Uint16Array_()
    : data()  {
    }
  Uint16Array_(const ContainerAllocator& _alloc)
    : data(_alloc)  {
  (void)_alloc;
    }



   typedef std::vector<uint16_t, typename ContainerAllocator::template rebind<uint16_t>::other >  _data_type;
  _data_type data;




  typedef boost::shared_ptr< ::see_n_tell::Uint16Array_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::see_n_tell::Uint16Array_<ContainerAllocator> const> ConstPtr;

}; // struct Uint16Array_

typedef ::see_n_tell::Uint16Array_<std::allocator<void> > Uint16Array;

typedef boost::shared_ptr< ::see_n_tell::Uint16Array > Uint16ArrayPtr;
typedef boost::shared_ptr< ::see_n_tell::Uint16Array const> Uint16ArrayConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::see_n_tell::Uint16Array_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::see_n_tell::Uint16Array_<ContainerAllocator> >::stream(s, "", v);
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
struct IsFixedSize< ::see_n_tell::Uint16Array_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::see_n_tell::Uint16Array_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::see_n_tell::Uint16Array_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::see_n_tell::Uint16Array_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::see_n_tell::Uint16Array_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::see_n_tell::Uint16Array_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::see_n_tell::Uint16Array_<ContainerAllocator> >
{
  static const char* value()
  {
    return "e066daa5966378a57445687eb65bfa3b";
  }

  static const char* value(const ::see_n_tell::Uint16Array_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xe066daa5966378a5ULL;
  static const uint64_t static_value2 = 0x7445687eb65bfa3bULL;
};

template<class ContainerAllocator>
struct DataType< ::see_n_tell::Uint16Array_<ContainerAllocator> >
{
  static const char* value()
  {
    return "see_n_tell/Uint16Array";
  }

  static const char* value(const ::see_n_tell::Uint16Array_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::see_n_tell::Uint16Array_<ContainerAllocator> >
{
  static const char* value()
  {
    return "uint16[] data\n\
";
  }

  static const char* value(const ::see_n_tell::Uint16Array_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::see_n_tell::Uint16Array_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.data);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct Uint16Array_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::see_n_tell::Uint16Array_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::see_n_tell::Uint16Array_<ContainerAllocator>& v)
  {
    s << indent << "data[]" << std::endl;
    for (size_t i = 0; i < v.data.size(); ++i)
    {
      s << indent << "  data[" << i << "]: ";
      Printer<uint16_t>::stream(s, indent + "  ", v.data[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // SEE_N_TELL_MESSAGE_UINT16ARRAY_H
