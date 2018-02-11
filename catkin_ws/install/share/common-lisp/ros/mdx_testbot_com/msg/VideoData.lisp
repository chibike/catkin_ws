; Auto-generated. Do not edit!


(cl:in-package mdx_testbot_com-msg)


;//! \htmlinclude VideoData.msg.html

(cl:defclass <VideoData> (roslisp-msg-protocol:ros-message)
  ((left_data
    :reader left_data
    :initarg :left_data
    :type (cl:vector cl:integer)
   :initform (cl:make-array 0 :element-type 'cl:integer :initial-element 0))
   (right_data
    :reader right_data
    :initarg :right_data
    :type (cl:vector cl:integer)
   :initform (cl:make-array 0 :element-type 'cl:integer :initial-element 0)))
)

(cl:defclass VideoData (<VideoData>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <VideoData>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'VideoData)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name mdx_testbot_com-msg:<VideoData> is deprecated: use mdx_testbot_com-msg:VideoData instead.")))

(cl:ensure-generic-function 'left_data-val :lambda-list '(m))
(cl:defmethod left_data-val ((m <VideoData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mdx_testbot_com-msg:left_data-val is deprecated.  Use mdx_testbot_com-msg:left_data instead.")
  (left_data m))

(cl:ensure-generic-function 'right_data-val :lambda-list '(m))
(cl:defmethod right_data-val ((m <VideoData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mdx_testbot_com-msg:right_data-val is deprecated.  Use mdx_testbot_com-msg:right_data instead.")
  (right_data m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <VideoData>) ostream)
  "Serializes a message object of type '<VideoData>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'left_data))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let* ((signed ele) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    ))
   (cl:slot-value msg 'left_data))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'right_data))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let* ((signed ele) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    ))
   (cl:slot-value msg 'right_data))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <VideoData>) istream)
  "Deserializes a message object of type '<VideoData>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'left_data) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'left_data)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296)))))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'right_data) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'right_data)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296)))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<VideoData>)))
  "Returns string type for a message object of type '<VideoData>"
  "mdx_testbot_com/VideoData")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'VideoData)))
  "Returns string type for a message object of type 'VideoData"
  "mdx_testbot_com/VideoData")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<VideoData>)))
  "Returns md5sum for a message object of type '<VideoData>"
  "a486237169ce6e905ee06bbd36d2b929")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'VideoData)))
  "Returns md5sum for a message object of type 'VideoData"
  "a486237169ce6e905ee06bbd36d2b929")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<VideoData>)))
  "Returns full string definition for message of type '<VideoData>"
  (cl:format cl:nil "int32[] left_data~%int32[] right_data~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'VideoData)))
  "Returns full string definition for message of type 'VideoData"
  (cl:format cl:nil "int32[] left_data~%int32[] right_data~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <VideoData>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'left_data) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'right_data) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <VideoData>))
  "Converts a ROS message object to a list"
  (cl:list 'VideoData
    (cl:cons ':left_data (left_data msg))
    (cl:cons ':right_data (right_data msg))
))
