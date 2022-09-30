;; Auto-generated. Do not edit!


(when (boundp 'radar::radar_message)
  (if (not (find-package "RADAR"))
    (make-package "RADAR"))
  (shadow 'radar_message (find-package "RADAR")))
(unless (find-package "RADAR::RADAR_MESSAGE")
  (make-package "RADAR::RADAR_MESSAGE"))

(in-package "ROS")
;;//! \htmlinclude radar_message.msg.html


(defclass radar::radar_message
  :super ros::object
  :slots (_start_time _num _data ))

(defmethod radar::radar_message
  (:init
   (&key
    ((:start_time __start_time) (instance ros::time :init))
    ((:num __num) 0.0)
    ((:data __data) (make-array 0 :initial-element 0.0 :element-type :float))
    )
   (send-super :init)
   (setq _start_time __start_time)
   (setq _num (float __num))
   (setq _data __data)
   self)
  (:start_time
   (&optional __start_time)
   (if __start_time (setq _start_time __start_time)) _start_time)
  (:num
   (&optional __num)
   (if __num (setq _num __num)) _num)
  (:data
   (&optional __data)
   (if __data (setq _data __data)) _data)
  (:serialization-length
   ()
   (+
    ;; time _start_time
    8
    ;; float32 _num
    4
    ;; float64[] _data
    (* 8    (length _data)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; time _start_time
       (write-long (send _start_time :sec) s) (write-long (send _start_time :nsec) s)
     ;; float32 _num
       (sys::poke _num (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float64[] _data
     (write-long (length _data) s)
     (dotimes (i (length _data))
       (sys::poke (elt _data i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; time _start_time
     (send _start_time :sec (sys::peek buf ptr- :integer)) (incf ptr- 4)  (send _start_time :nsec (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; float32 _num
     (setq _num (sys::peek buf ptr- :float)) (incf ptr- 4)
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

(setf (get radar::radar_message :md5sum-) "9d156b01ce488aed0a9757f924f4b8e0")
(setf (get radar::radar_message :datatype-) "radar/radar_message")
(setf (get radar::radar_message :definition-)
      "time start_time
float32 num
float64[] data


")



(provide :radar/radar_message "9d156b01ce488aed0a9757f924f4b8e0")


