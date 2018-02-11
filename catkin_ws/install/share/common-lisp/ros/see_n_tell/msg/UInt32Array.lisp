; Auto-generated. Do not edit!


(cl:in-package see_n_tell-msg)


;//! \htmlinclude UInt32Array.msg.html

(cl:defclass <UInt32Array> (roslisp-msg-protocol:ros-message)
  ((data
    :reader data
    :initarg :data
    :type (cl:vector cl:integer)
   :initform (cl:make-array 0 :element-type 'cl:integer :initial-element 0)))
)

(cl:defclass UInt32Array (<UInt32Array>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <UInt32Array>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'UInt32Array)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name see_n_tell-msg:<UInt32Array> is deprecated: use see_n_tell-msg:UInt32Array instead.")))

(cl:ensure-generic-function 'data-val :lambda-list '(m))
(cl:defmethod data-val ((m <UInt32Array>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader see_n_tell-msg:data-val is deprecated.  Use see_n_tell-msg:data instead.")
  (data m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <UInt32Array>) ostream)
  "Serializes a message object of type '<UInt32Array>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'data))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:write-byte (cl:ldb (cl:byte 8 0) ele) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) ele) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) ele) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) ele) ostream))
   (cl:slot-value msg 'data))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <UInt32Array>) istream)
  "Deserializes a message object of type '<UInt32Array>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'data) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'data)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:aref vals i)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:aref vals i)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:aref vals i)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:aref vals i)) (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<UInt32Array>)))
  "Returns string type for a message object of type '<UInt32Array>"
  "see_n_tell/UInt32Array")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'UInt32Array)))
  "Returns string type for a message object of type 'UInt32Array"
  "see_n_tell/UInt32Array")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<UInt32Array>)))
  "Returns md5sum for a message object of type '<UInt32Array>"
  "a1376ac15481ebcd67c3fe86a75a7d55")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'UInt32Array)))
  "Returns md5sum for a message object of type 'UInt32Array"
  "a1376ac15481ebcd67c3fe86a75a7d55")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<UInt32Array>)))
  "Returns full string definition for message of type '<UInt32Array>"
  (cl:format cl:nil "uint32[] data~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'UInt32Array)))
  "Returns full string definition for message of type 'UInt32Array"
  (cl:format cl:nil "uint32[] data~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <UInt32Array>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'data) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <UInt32Array>))
  "Converts a ROS message object to a list"
  (cl:list 'UInt32Array
    (cl:cons ':data (data msg))
))
