;; Auto-generated. Do not edit!


(when (boundp 'see_n_tell::Uint16Array)
  (if (not (find-package "SEE_N_TELL"))
    (make-package "SEE_N_TELL"))
  (shadow 'Uint16Array (find-package "SEE_N_TELL")))
(unless (find-package "SEE_N_TELL::UINT16ARRAY")
  (make-package "SEE_N_TELL::UINT16ARRAY"))

(in-package "ROS")
;;//! \htmlinclude Uint16Array.msg.html


(defclass see_n_tell::Uint16Array
  :super ros::object
  :slots (_data ))

(defmethod see_n_tell::Uint16Array
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
    ;; uint16[] _data
    (* 2    (length _data)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint16[] _data
     (write-long (length _data) s)
     (dotimes (i (length _data))
       (write-word (elt _data i) s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint16[] _data
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _data (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _data i) (sys::peek buf ptr- :short)) (incf ptr- 2)
     ))
   ;;
   self)
  )

(setf (get see_n_tell::Uint16Array :md5sum-) "e066daa5966378a57445687eb65bfa3b")
(setf (get see_n_tell::Uint16Array :datatype-) "see_n_tell/Uint16Array")
(setf (get see_n_tell::Uint16Array :definition-)
      "uint16[] data

")



(provide :see_n_tell/Uint16Array "e066daa5966378a57445687eb65bfa3b")


