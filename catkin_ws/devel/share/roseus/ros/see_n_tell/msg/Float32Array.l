;; Auto-generated. Do not edit!


(when (boundp 'see_n_tell::Float32Array)
  (if (not (find-package "SEE_N_TELL"))
    (make-package "SEE_N_TELL"))
  (shadow 'Float32Array (find-package "SEE_N_TELL")))
(unless (find-package "SEE_N_TELL::FLOAT32ARRAY")
  (make-package "SEE_N_TELL::FLOAT32ARRAY"))

(in-package "ROS")
;;//! \htmlinclude Float32Array.msg.html


(defclass see_n_tell::Float32Array
  :super ros::object
  :slots (_data ))

(defmethod see_n_tell::Float32Array
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
    ;; float32[] _data
    (* 4    (length _data)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32[] _data
     (write-long (length _data) s)
     (dotimes (i (length _data))
       (sys::poke (elt _data i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32[] _data
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _data (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _data i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     ))
   ;;
   self)
  )

(setf (get see_n_tell::Float32Array :md5sum-) "420cd38b6b071cd49f2970c3e2cee511")
(setf (get see_n_tell::Float32Array :datatype-) "see_n_tell/Float32Array")
(setf (get see_n_tell::Float32Array :definition-)
      "float32[] data

")



(provide :see_n_tell/Float32Array "420cd38b6b071cd49f2970c3e2cee511")


