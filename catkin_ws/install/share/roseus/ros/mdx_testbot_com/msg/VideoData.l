;; Auto-generated. Do not edit!


(when (boundp 'mdx_testbot_com::VideoData)
  (if (not (find-package "MDX_TESTBOT_COM"))
    (make-package "MDX_TESTBOT_COM"))
  (shadow 'VideoData (find-package "MDX_TESTBOT_COM")))
(unless (find-package "MDX_TESTBOT_COM::VIDEODATA")
  (make-package "MDX_TESTBOT_COM::VIDEODATA"))

(in-package "ROS")
;;//! \htmlinclude VideoData.msg.html


(defclass mdx_testbot_com::VideoData
  :super ros::object
  :slots (_left_data _right_data ))

(defmethod mdx_testbot_com::VideoData
  (:init
   (&key
    ((:left_data __left_data) (make-array 0 :initial-element 0 :element-type :integer))
    ((:right_data __right_data) (make-array 0 :initial-element 0 :element-type :integer))
    )
   (send-super :init)
   (setq _left_data __left_data)
   (setq _right_data __right_data)
   self)
  (:left_data
   (&optional __left_data)
   (if __left_data (setq _left_data __left_data)) _left_data)
  (:right_data
   (&optional __right_data)
   (if __right_data (setq _right_data __right_data)) _right_data)
  (:serialization-length
   ()
   (+
    ;; int32[] _left_data
    (* 4    (length _left_data)) 4
    ;; int32[] _right_data
    (* 4    (length _right_data)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32[] _left_data
     (write-long (length _left_data) s)
     (dotimes (i (length _left_data))
       (write-long (elt _left_data i) s)
       )
     ;; int32[] _right_data
     (write-long (length _right_data) s)
     (dotimes (i (length _right_data))
       (write-long (elt _right_data i) s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32[] _left_data
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _left_data (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _left_data i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;; int32[] _right_data
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _right_data (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _right_data i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;;
   self)
  )

(setf (get mdx_testbot_com::VideoData :md5sum-) "a486237169ce6e905ee06bbd36d2b929")
(setf (get mdx_testbot_com::VideoData :datatype-) "mdx_testbot_com/VideoData")
(setf (get mdx_testbot_com::VideoData :definition-)
      "int32[] left_data
int32[] right_data

")



(provide :mdx_testbot_com/VideoData "a486237169ce6e905ee06bbd36d2b929")


