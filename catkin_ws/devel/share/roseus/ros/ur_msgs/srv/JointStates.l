;; Auto-generated. Do not edit!


(when (boundp 'ur_msgs::JointStates)
  (if (not (find-package "UR_MSGS"))
    (make-package "UR_MSGS"))
  (shadow 'JointStates (find-package "UR_MSGS")))
(unless (find-package "UR_MSGS::JOINTSTATES")
  (make-package "UR_MSGS::JOINTSTATES"))
(unless (find-package "UR_MSGS::JOINTSTATESREQUEST")
  (make-package "UR_MSGS::JOINTSTATESREQUEST"))
(unless (find-package "UR_MSGS::JOINTSTATESRESPONSE")
  (make-package "UR_MSGS::JOINTSTATESRESPONSE"))

(in-package "ROS")





(defclass ur_msgs::JointStatesRequest
  :super ros::object
  :slots ())

(defmethod ur_msgs::JointStatesRequest
  (:init
   (&key
    )
   (send-super :init)
   self)
  (:serialization-length
   ()
   (+
    0
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;;
   self)
  )

(defclass ur_msgs::JointStatesResponse
  :super ros::object
  :slots (_joint_states ))

(defmethod ur_msgs::JointStatesResponse
  (:init
   (&key
    ((:joint_states __joint_states) "")
    )
   (send-super :init)
   (setq _joint_states (string __joint_states))
   self)
  (:joint_states
   (&optional __joint_states)
   (if __joint_states (setq _joint_states __joint_states)) _joint_states)
  (:serialization-length
   ()
   (+
    ;; string _joint_states
    4 (length _joint_states)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _joint_states
       (write-long (length _joint_states) s) (princ _joint_states s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _joint_states
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _joint_states (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass ur_msgs::JointStates
  :super ros::object
  :slots ())

(setf (get ur_msgs::JointStates :md5sum-) "5581a04fddc1f7d62a2958142211f72d")
(setf (get ur_msgs::JointStates :datatype-) "ur_msgs/JointStates")
(setf (get ur_msgs::JointStates :request) ur_msgs::JointStatesRequest)
(setf (get ur_msgs::JointStates :response) ur_msgs::JointStatesResponse)

(defmethod ur_msgs::JointStatesRequest
  (:response () (instance ur_msgs::JointStatesResponse :init)))

(setf (get ur_msgs::JointStatesRequest :md5sum-) "5581a04fddc1f7d62a2958142211f72d")
(setf (get ur_msgs::JointStatesRequest :datatype-) "ur_msgs/JointStatesRequest")
(setf (get ur_msgs::JointStatesRequest :definition-)
      "
---
string joint_states

")

(setf (get ur_msgs::JointStatesResponse :md5sum-) "5581a04fddc1f7d62a2958142211f72d")
(setf (get ur_msgs::JointStatesResponse :datatype-) "ur_msgs/JointStatesResponse")
(setf (get ur_msgs::JointStatesResponse :definition-)
      "
---
string joint_states

")



(provide :ur_msgs/JointStates "5581a04fddc1f7d62a2958142211f72d")


