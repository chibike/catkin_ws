;; Auto-generated. Do not edit!


(when (boundp 'see_n_tell::Uint8Array)
  (if (not (find-package "SEE_N_TELL"))
    (make-package "SEE_N_TELL"))
  (shadow 'Uint8Array (find-package "SEE_N_TELL")))
(unless (find-package "SEE_N_TELL::UINT8ARRAY")
  (make-package "SEE_N_TELL::UINT8ARRAY"))

(in-package "ROS")
;;//! \htmlinclude Uint8Array.msg.html


(defclass see_n_tell::Uint8Array
  :super ros::object
  :slots (_data ))

(defmethod see_n_tell::Uint8Array
  (:init
   (&key
    ((:data __data) (make-array 0 :initial-element 0 :element-type :char))
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
    ;; uint8[] _data
    (* 1    (length _data)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint8[] _data
     (write-long (length _data) s)
     (princ _data s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint8[] _data
   (let ((n (sys::peek buf ptr- :integer))) (incf ptr- 4)
     (setq _data (make-array n :element-type :char))
     (replace _data buf :start2 ptr-) (incf ptr- n))
   ;;
   self)
  )

(setf (get see_n_tell::Uint8Array :md5sum-) "f43a8e1b362b75baa741461b46adc7e0")
(setf (get see_n_tell::Uint8Array :datatype-) "see_n_tell/Uint8Array")
(setf (get see_n_tell::Uint8Array :definition-)
      "uint8[] data

")



(provide :see_n_tell/Uint8Array "f43a8e1b362b75baa741461b46adc7e0")


