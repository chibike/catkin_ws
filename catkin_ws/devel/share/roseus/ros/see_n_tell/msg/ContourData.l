;; Auto-generated. Do not edit!


(when (boundp 'see_n_tell::ContourData)
  (if (not (find-package "SEE_N_TELL"))
    (make-package "SEE_N_TELL"))
  (shadow 'ContourData (find-package "SEE_N_TELL")))
(unless (find-package "SEE_N_TELL::CONTOURDATA")
  (make-package "SEE_N_TELL::CONTOURDATA"))

(in-package "ROS")
;;//! \htmlinclude ContourData.msg.html


(defclass see_n_tell::ContourData
  :super ros::object
  :slots (_data_lengths _data ))

(defmethod see_n_tell::ContourData
  (:init
   (&key
    ((:data_lengths __data_lengths) (make-array 0 :initial-element 0 :element-type :integer))
    ((:data __data) (make-array 0 :initial-element 0 :element-type :integer))
    )
   (send-super :init)
   (setq _data_lengths __data_lengths)
   (setq _data __data)
   self)
  (:data_lengths
   (&optional __data_lengths)
   (if __data_lengths (setq _data_lengths __data_lengths)) _data_lengths)
  (:data
   (&optional __data)
   (if __data (setq _data __data)) _data)
  (:serialization-length
   ()
   (+
    ;; uint64[] _data_lengths
    (* 8    (length _data_lengths)) 4
    ;; uint64[] _data
    (* 8    (length _data)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint64[] _data_lengths
     (write-long (length _data_lengths) s)
     (dotimes (i (length _data_lengths))
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke (elt _data_lengths i) (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class (elt _data_lengths i)) (= (length ((elt _data_lengths i) . bv)) 2)) ;; bignum
              (write-long (ash (elt ((elt _data_lengths i) . bv) 0) 0) s)
              (write-long (ash (elt ((elt _data_lengths i) . bv) 1) -1) s))
             ((and (class (elt _data_lengths i)) (= (length ((elt _data_lengths i) . bv)) 1)) ;; big1
              (write-long (elt ((elt _data_lengths i) . bv) 0) s)
              (write-long (if (>= (elt _data_lengths i) 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long (elt _data_lengths i) s)(write-long (if (>= (elt _data_lengths i) 0) 0 #xffffffff) s)))
       )
     ;; uint64[] _data
     (write-long (length _data) s)
     (dotimes (i (length _data))
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke (elt _data i) (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class (elt _data i)) (= (length ((elt _data i) . bv)) 2)) ;; bignum
              (write-long (ash (elt ((elt _data i) . bv) 0) 0) s)
              (write-long (ash (elt ((elt _data i) . bv) 1) -1) s))
             ((and (class (elt _data i)) (= (length ((elt _data i) . bv)) 1)) ;; big1
              (write-long (elt ((elt _data i) . bv) 0) s)
              (write-long (if (>= (elt _data i) 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long (elt _data i) s)(write-long (if (>= (elt _data i) 0) 0 #xffffffff) s)))
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint64[] _data_lengths
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _data_lengths (instantiate integer-vector n))
     (dotimes (i n)
     
#+(or :alpha :irix6 :x86_64)
      (setf (elt _data_lengths i) (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf (elt _data_lengths i) (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
     ))
   ;; uint64[] _data
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _data (instantiate integer-vector n))
     (dotimes (i n)
     
#+(or :alpha :irix6 :x86_64)
      (setf (elt _data i) (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf (elt _data i) (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
     ))
   ;;
   self)
  )

(setf (get see_n_tell::ContourData :md5sum-) "ebaaef9a06efaba93f1f22be3f7556c2")
(setf (get see_n_tell::ContourData :datatype-) "see_n_tell/ContourData")
(setf (get see_n_tell::ContourData :definition-)
      "uint64[]          data_lengths
uint64[]          data

")



(provide :see_n_tell/ContourData "ebaaef9a06efaba93f1f22be3f7556c2")


