;; Auto-generated. Do not edit!


(when (boundp 'ur_msgs::JointTrajectory)
  (if (not (find-package "UR_MSGS"))
    (make-package "UR_MSGS"))
  (shadow 'JointTrajectory (find-package "UR_MSGS")))
(unless (find-package "UR_MSGS::JOINTTRAJECTORY")
  (make-package "UR_MSGS::JOINTTRAJECTORY"))
(unless (find-package "UR_MSGS::JOINTTRAJECTORYREQUEST")
  (make-package "UR_MSGS::JOINTTRAJECTORYREQUEST"))
(unless (find-package "UR_MSGS::JOINTTRAJECTORYRESPONSE")
  (make-package "UR_MSGS::JOINTTRAJECTORYRESPONSE"))

(in-package "ROS")



(if (not (find-package "TRAJECTORY_MSGS"))
  (ros::roseus-add-msgs "trajectory_msgs"))


(defclass ur_msgs::JointTrajectoryRequest
  :super ros::object
  :slots (_arm_joint_name _arm_qpos _eef_pose _eef_quat _grasp ))

(defmethod ur_msgs::JointTrajectoryRequest
  (:init
   (&key
    ((:arm_joint_name __arm_joint_name) (let (r) (dotimes (i 0) (push "" r)) r))
    ((:arm_qpos __arm_qpos) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:eef_pose __eef_pose) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:eef_quat __eef_quat) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:grasp __grasp) 0.0)
    )
   (send-super :init)
   (setq _arm_joint_name __arm_joint_name)
   (setq _arm_qpos __arm_qpos)
   (setq _eef_pose __eef_pose)
   (setq _eef_quat __eef_quat)
   (setq _grasp (float __grasp))
   self)
  (:arm_joint_name
   (&optional __arm_joint_name)
   (if __arm_joint_name (setq _arm_joint_name __arm_joint_name)) _arm_joint_name)
  (:arm_qpos
   (&optional __arm_qpos)
   (if __arm_qpos (setq _arm_qpos __arm_qpos)) _arm_qpos)
  (:eef_pose
   (&optional __eef_pose)
   (if __eef_pose (setq _eef_pose __eef_pose)) _eef_pose)
  (:eef_quat
   (&optional __eef_quat)
   (if __eef_quat (setq _eef_quat __eef_quat)) _eef_quat)
  (:grasp
   (&optional __grasp)
   (if __grasp (setq _grasp __grasp)) _grasp)
  (:serialization-length
   ()
   (+
    ;; string[] _arm_joint_name
    (apply #'+ (mapcar #'(lambda (x) (+ 4 (length x))) _arm_joint_name)) 4
    ;; float64[] _arm_qpos
    (* 8    (length _arm_qpos)) 4
    ;; float64[] _eef_pose
    (* 8    (length _eef_pose)) 4
    ;; float64[] _eef_quat
    (* 8    (length _eef_quat)) 4
    ;; float64 _grasp
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string[] _arm_joint_name
     (write-long (length _arm_joint_name) s)
     (dolist (elem _arm_joint_name)
       (write-long (length elem) s) (princ elem s)
       )
     ;; float64[] _arm_qpos
     (write-long (length _arm_qpos) s)
     (dotimes (i (length _arm_qpos))
       (sys::poke (elt _arm_qpos i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64[] _eef_pose
     (write-long (length _eef_pose) s)
     (dotimes (i (length _eef_pose))
       (sys::poke (elt _eef_pose i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64[] _eef_quat
     (write-long (length _eef_quat) s)
     (dotimes (i (length _eef_quat))
       (sys::poke (elt _eef_quat i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64 _grasp
       (sys::poke _grasp (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string[] _arm_joint_name
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _arm_joint_name (make-list n))
     (dotimes (i n)
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setf (elt _arm_joint_name i) (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
     ))
   ;; float64[] _arm_qpos
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _arm_qpos (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _arm_qpos i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; float64[] _eef_pose
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _eef_pose (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _eef_pose i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; float64[] _eef_quat
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _eef_quat (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _eef_quat i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; float64 _grasp
     (setq _grasp (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(defclass ur_msgs::JointTrajectoryResponse
  :super ros::object
  :slots (_plan ))

(defmethod ur_msgs::JointTrajectoryResponse
  (:init
   (&key
    ((:plan __plan) (instance trajectory_msgs::JointTrajectory :init))
    )
   (send-super :init)
   (setq _plan __plan)
   self)
  (:plan
   (&rest __plan)
   (if (keywordp (car __plan))
       (send* _plan __plan)
     (progn
       (if __plan (setq _plan (car __plan)))
       _plan)))
  (:serialization-length
   ()
   (+
    ;; trajectory_msgs/JointTrajectory _plan
    (send _plan :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; trajectory_msgs/JointTrajectory _plan
       (send _plan :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; trajectory_msgs/JointTrajectory _plan
     (send _plan :deserialize buf ptr-) (incf ptr- (send _plan :serialization-length))
   ;;
   self)
  )

(defclass ur_msgs::JointTrajectory
  :super ros::object
  :slots ())

(setf (get ur_msgs::JointTrajectory :md5sum-) "1373137967a4be74f31370fe945d1aee")
(setf (get ur_msgs::JointTrajectory :datatype-) "ur_msgs/JointTrajectory")
(setf (get ur_msgs::JointTrajectory :request) ur_msgs::JointTrajectoryRequest)
(setf (get ur_msgs::JointTrajectory :response) ur_msgs::JointTrajectoryResponse)

(defmethod ur_msgs::JointTrajectoryRequest
  (:response () (instance ur_msgs::JointTrajectoryResponse :init)))

(setf (get ur_msgs::JointTrajectoryRequest :md5sum-) "1373137967a4be74f31370fe945d1aee")
(setf (get ur_msgs::JointTrajectoryRequest :datatype-) "ur_msgs/JointTrajectoryRequest")
(setf (get ur_msgs::JointTrajectoryRequest :definition-)
      "
string[] arm_joint_name
float64[] arm_qpos
float64[] eef_pose
float64[] eef_quat
float64 grasp
---
trajectory_msgs/JointTrajectory plan


================================================================================
MSG: trajectory_msgs/JointTrajectory
Header header
string[] joint_names
JointTrajectoryPoint[] points
================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: trajectory_msgs/JointTrajectoryPoint
# Each trajectory point specifies either positions[, velocities[, accelerations]]
# or positions[, effort] for the trajectory to be executed.
# All specified values are in the same order as the joint names in JointTrajectory.msg

float64[] positions
float64[] velocities
float64[] accelerations
float64[] effort
duration time_from_start
")

(setf (get ur_msgs::JointTrajectoryResponse :md5sum-) "1373137967a4be74f31370fe945d1aee")
(setf (get ur_msgs::JointTrajectoryResponse :datatype-) "ur_msgs/JointTrajectoryResponse")
(setf (get ur_msgs::JointTrajectoryResponse :definition-)
      "
string[] arm_joint_name
float64[] arm_qpos
float64[] eef_pose
float64[] eef_quat
float64 grasp
---
trajectory_msgs/JointTrajectory plan


================================================================================
MSG: trajectory_msgs/JointTrajectory
Header header
string[] joint_names
JointTrajectoryPoint[] points
================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: trajectory_msgs/JointTrajectoryPoint
# Each trajectory point specifies either positions[, velocities[, accelerations]]
# or positions[, effort] for the trajectory to be executed.
# All specified values are in the same order as the joint names in JointTrajectory.msg

float64[] positions
float64[] velocities
float64[] accelerations
float64[] effort
duration time_from_start
")



(provide :ur_msgs/JointTrajectory "1373137967a4be74f31370fe945d1aee")


