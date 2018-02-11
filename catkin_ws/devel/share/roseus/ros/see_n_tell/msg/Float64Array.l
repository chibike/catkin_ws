;; Auto-generated. Do not edit!


(when (boundp 'see_n_tell::Float64Array)
  (if (not (find-package "SEE_N_TELL"))
    (make-package "SEE_N_TELL"))
  (shadow 'Float64Array (find-package "SEE_N_TELL")))
(unless (find-package "SEE_N_TELL::FLOAT64ARRAY")
  (make-package "SEE_N_TELL::FLOAT64ARRAY"))

(in-package "ROS")
;;//! \htmlinclude Float64Array.msg.html


(defclass see_n_tell::Float64Array
  :super ros::object
  :slots (_data ))

(defmethod see_n_tell::Float64Array
  (:init
   (&key
    ((:data __data) (make-array 0 :initial-element 0.0 :element-type :float))
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
    ;; float64[] _data
    (* 8    (length _data)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64[] _data
     (write-long (length _data) s)
     (dotimes (i (length _data))
       (sys::poke (elt _data i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64[] _data
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _data (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _data i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;;
   self)
  )

(setf (get see_n_tell::Float64Array :md5sum-) "788898178a3da2c3718461eecda8f714")
(setf (get see_n_tell::Float64Array :datatype-) "see_n_tell/Float64Array")
(setf (get see_n_tell::Float64Array :definition-)
      "float64[] data

")



(provide :see_n_tell/Float64Array "788898178a3da2c3718461eecda8f714")


