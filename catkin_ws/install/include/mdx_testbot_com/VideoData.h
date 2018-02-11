// Generated by gencpp from file mdx_testbot_com/VideoData.msg
// DO NOT EDIT!


#ifndef MDX_TESTBOT_COM_MESSAGE_VIDEODATA_H
#define MDX_TESTBOT_COM_MESSAGE_VIDEODATA_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace mdx_testbot_com
{
template <class ContainerAllocator>
struct VideoData_
{
  typedef VideoData_<ContainerAllocator> Type;

  VideoData_()
    : left_data()
    , right_data()  {
    }
  VideoData_(const ContainerAllocator& _alloc)
    : left_data(_alloc)
    , right_data(_alloc)  {
  (void)_alloc;
    }



   typedef std::vector<int32_t, typename ContainerAllocator::template rebind<int32_t>::other >  _left_data_type;
  _left_data_type left_data;

   typedef std::vector<int32_t, typename ContainerAllocator::template rebind<int32_t>::other >  _right_data_type;
  _right_data_type right_data;




  typedef boost::shared_ptr< ::mdx_testbot_com::VideoData_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::mdx_testbot_com::VideoData_<ContainerAllocator> const> ConstPtr;

}; // struct VideoData_

typedef ::mdx_testbot_com::VideoData_<std::allocator<void> > VideoData;

typedef boost::shared_ptr< ::mdx_testbot_com::VideoData > VideoDataPtr;
typedef boost::shared_ptr< ::mdx_testbot_com::VideoData const> VideoDataConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::mdx_testbot_com::VideoData_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::mdx_testbot_com::VideoData_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace mdx_testbot_com

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'mdx_testbot_com': ['/home/chibike/catkin_ws/src/mdx_testbot_com/msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::mdx_testbot_com::VideoData_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::mdx_testbot_com::VideoData_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::mdx_testbot_com::VideoData_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::mdx_testbot_com::VideoData_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::mdx_testbot_com::VideoData_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::mdx_testbot_com::VideoData_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::mdx_testbot_com::VideoData_<ContainerAllocator> >
{
  static const char* value()
  {
    return "a486237169ce6e905ee06bbd36d2b929";
  }

  static const char* value(const ::mdx_testbot_com::VideoData_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xa486237169ce6e90ULL;
  static const uint64_t static_value2 = 0x5ee06bbd36d2b929ULL;
};

template<class ContainerAllocator>
struct DataType< ::mdx_testbot_com::VideoData_<ContainerAllocator> >
{
  static const char* value()
  {
    return "mdx_testbot_com/VideoData";
  }

  static const char* value(const ::mdx_testbot_com::VideoData_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::mdx_testbot_com::VideoData_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int32[] left_data\n\
int32[] right_data\n\
";
  }

  static const char* value(const ::mdx_testbot_com::VideoData_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::mdx_testbot_com::VideoData_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.left_data);
      stream.next(m.right_data);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct VideoData_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::mdx_testbot_com::VideoData_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::mdx_testbot_com::VideoData_<ContainerAllocator>& v)
  {
    s << indent << "left_data[]" << std::endl;
    for (size_t i = 0; i < v.left_data.size(); ++i)
    {
      s << indent << "  left_data[" << i << "]: ";
      Printer<int32_t>::stream(s, indent + "  ", v.left_data[i]);
    }
    s << indent << "right_data[]" << std::endl;
    for (size_t i = 0; i < v.right_data.size(); ++i)
    {
      s << indent << "  right_data[" << i << "]: ";
      Printer<int32_t>::stream(s, indent + "  ", v.right_data[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // MDX_TESTBOT_COM_MESSAGE_VIDEODATA_H
