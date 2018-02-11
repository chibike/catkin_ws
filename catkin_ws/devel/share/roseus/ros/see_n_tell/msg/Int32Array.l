;; Auto-generated. Do not edit!


(when (boundp 'see_n_tell::Int32Array)
  (if (not (find-package "SEE_N_TELL"))
    (make-package "SEE_N_TELL"))
  (shadow 'Int32Array (find-package "SEE_N_TELL")))
(unless (find-package "SEE_N_TELL::INT32ARRAY")
  (make-package "SEE_N_TELL::INT32ARRAY"))

(in-package "ROS")
;;//! \htmlinclude Int32Array.msg.html


(defclass see_n_tell::Int32Array
  :super ros::object
  :slots (_data ))

(defmethod see_n_tell::Int32Array
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

(setf (get see_n_tell::Int32Array :md5sum-) "563b27884d008b0d2adff54dc1f9e4f5")
(setf (get see_n_tell::Int32Array :datatype-) "see_n_tell/Int32Array")
(setf (get see_n_tell::Int32Array :definition-)
      "int32[] data

")



(provide :see_n_tell/Int32Array "563b27884d008b0d2adff54dc1f9e4f5")


