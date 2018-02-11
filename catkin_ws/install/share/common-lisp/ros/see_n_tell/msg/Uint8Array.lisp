; Auto-generated. Do not edit!


(cl:in-package see_n_tell-msg)


;//! \htmlinclude Uint8Array.msg.html

(cl:defclass <Uint8Array> (roslisp-msg-protocol:ros-message)
  ((data
    :reader data
    :initarg :data
    :type (cl:vector cl:fixnum)
   :initform (cl:make-array 0 :element-type 'cl:fixnum :initial-element 0)))
)

(cl:defclass Uint8Array (<Uint8Array>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Uint8Array>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Uint8Array)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name see_n_tell-msg:<Uint8Array> is deprecated: use see_n_tell-msg:Uint8Array instead.")))

(cl:ensure-generic-function 'data-val :lambda-list '(m))
(cl:defmethod data-val ((m <Uint8Array>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader see_n_tell-msg:data-val is deprecated.  Use see_n_tell-msg:data instead.")
  (data m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Uint8Array>) ostream)
  "Serializes a message object of type '<Uint8Array>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'data))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:write-byte (cl:ldb (cl:byte 8 0) ele) ostream))
   (cl:slot-value msg 'data))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Uint8Array>) istream)
  "Deserializes a message object of type '<Uint8Array>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'data) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'data)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:aref vals i)) (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Uint8Array>)))
  "Returns string type for a message object of type '<Uint8Array>"
  "see_n_tell/Uint8Array")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Uint8Array)))
  "Returns string type for a message object of type 'Uint8Array"
  "see_n_tell/Uint8Array")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Uint8Array>)))
  "Returns md5sum for a message object of type '<Uint8Array>"
  "f43a8e1b362b75baa741461b46adc7e0")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Uint8Array)))
  "Returns md5sum for a message object of type 'Uint8Array"
  "f43a8e1b362b75baa741461b46adc7e0")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Uint8Array>)))
  "Returns full string definition for message of type '<Uint8Array>"
  (cl:format cl:nil "uint8[] data~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Uint8Array)))
  "Returns full string definition for message of type 'Uint8Array"
  (cl:format cl:nil "uint8[] data~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Uint8Array>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'data) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 1)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Uint8Array>))
  "Converts a ROS message object to a list"
  (cl:list 'Uint8Array
    (cl:cons ':data (data msg))
))
