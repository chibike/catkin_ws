;; Auto-generated. Do not edit!


(when (boundp 'mdx_testbot_com::Int32Array)
  (if (not (find-package "MDX_TESTBOT_COM"))
    (make-package "MDX_TESTBOT_COM"))
  (shadow 'Int32Array (find-package "MDX_TESTBOT_COM")))
(unless (find-package "MDX_TESTBOT_COM::INT32ARRAY")
  (make-package "MDX_TESTBOT_COM::INT32ARRAY"))

(in-package "ROS")
;;//! \htmlinclude Int32Array.msg.html


(defclass mdx_testbot_com::Int32Array
  :super ros::object
  :slots (_data ))

(defmethod mdx_testbot_com::Int32Array
  (:init
   (&key
    ((:data __data) (make-array 0 :initial-element 0 :element-type :integer))
    )
   (send-super :init)
   (setq _data __data)
   self)
  (:data
   (&optional __data)
   (if __data (setq _data __data)) _data)
  (:serialization-length
   ()
   (+
    ;; int32[] _data
    (* 4    (length _data)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32[] _data
     (write-long (length _data) s)
     (dotimes (i (length _data))
       (write-long (elt _data i) s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32[] _data
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _data (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _data i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;;
   self)
  )

(setf (get mdx_testbot_com::Int32Array :md5sum-) "563b27884d008b0d2adff54dc1f9e4f5")
(setf (get mdx_testbot_com::Int32Array :datatype-) "mdx_testbot_com/Int32Array")
(setf (get mdx_testbot_com::Int32Array :definition-)
      "int32[] data

")



(provide :mdx_testbot_com/Int32Array "563b27884d008b0d2adff54dc1f9e4f5")


