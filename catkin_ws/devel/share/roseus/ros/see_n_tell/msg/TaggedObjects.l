;; Auto-generated. Do not edit!


(when (boundp 'see_n_tell::TaggedObjects)
  (if (not (find-package "SEE_N_TELL"))
    (make-package "SEE_N_TELL"))
  (shadow 'TaggedObjects (find-package "SEE_N_TELL")))
(unless (find-package "SEE_N_TELL::TAGGEDOBJECTS")
  (make-package "SEE_N_TELL::TAGGEDOBJECTS"))

(in-package "ROS")
;;//! \htmlinclude TaggedObjects.msg.html


(defclass see_n_tell::TaggedObjects
  :super ros::object
  :slots (_row _column _depth _width _height _tag ))

(defmethod see_n_tell::TaggedObjects
  (:init
   (&key
    ((:row __row) (make-array 0 :initial-element 0 :element-type :integer))
    ((:column __column) (make-array 0 :initial-element 0 :element-type :integer))
    ((:depth __depth) (make-array 0 :initial-element 0 :element-type :integer))
    ((:width __width) (make-array 0 :initial-element 0 :element-type :integer))
    ((:height __height) (make-array 0 :initial-element 0 :element-type :integer))
    ((:tag __tag) (let (r) (dotimes (i 0) (push "" r)) r))
    )
   (send-super :init)
   (setq _row __row)
   (setq _column __column)
   (setq _depth __depth)
   (setq _width __width)
   (setq _height __height)
   (setq _tag __tag)
   self)
  (:row
   (&optional __row)
   (if __row (setq _row __row)) _row)
  (:column
   (&optional __column)
   (if __column (setq _column __column)) _column)
  (:depth
   (&optional __depth)
   (if __depth (setq _depth __depth)) _depth)
  (:width
   (&optional __width)
   (if __width (setq _width __width)) _width)
  (:height
   (&optional __height)
   (if __height (setq _height __height)) _height)
  (:tag
   (&optional __tag)
   (if __tag (setq _tag __tag)) _tag)
  (:serialization-length
   ()
   (+
    ;; int32[] _row
    (* 4    (length _row)) 4
    ;; int32[] _column
    (* 4    (length _column)) 4
    ;; int32[] _depth
    (* 4    (length _depth)) 4
    ;; int32[] _width
    (* 4    (length _width)) 4
    ;; int32[] _height
    (* 4    (length _height)) 4
    ;; string[] _tag
    (apply #'+ (mapcar #'(lambda (x) (+ 4 (length x))) _tag)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32[] _row
     (write-long (length _row) s)
     (dotimes (i (length _row))
       (write-long (elt _row i) s)
       )
     ;; int32[] _column
     (write-long (length _column) s)
     (dotimes (i (length _column))
       (write-long (elt _column i) s)
       )
     ;; int32[] _depth
     (write-long (length _depth) s)
     (dotimes (i (length _depth))
       (write-long (elt _depth i) s)
       )
     ;; int32[] _width
     (write-long (length _width) s)
     (dotimes (i (length _width))
       (write-long (elt _width i) s)
       )
     ;; int32[] _height
     (write-long (length _height) s)
     (dotimes (i (length _height))
       (write-long (elt _height i) s)
       )
     ;; string[] _tag
     (write-long (length _tag) s)
     (dolist (elem _tag)
       (write-long (length elem) s) (princ elem s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32[] _row
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _row (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _row i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;; int32[] _column
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _column (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _column i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;; int32[] _depth
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _depth (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _depth i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;; int32[] _width
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _width (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _width i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;; int32[] _height
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _height (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _height i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;; string[] _tag
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _tag (make-list n))
     (dotimes (i n)
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setf (elt _tag i) (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
     ))
   ;;
   self)
  )

(setf (get see_n_tell::TaggedObjects :md5sum-) "54bcb59402f83d7fc9ccfd758dee382b")
(setf (get see_n_tell::TaggedObjects :datatype-) "see_n_tell/TaggedObjects")
(setf (get see_n_tell::TaggedObjects :definition-)
      "int32[]          row
int32[]          column
int32[]          depth
int32[]          width
int32[]          height
string[]         tag

")



(provide :see_n_tell/TaggedObjects "54bcb59402f83d7fc9ccfd758dee382b")


