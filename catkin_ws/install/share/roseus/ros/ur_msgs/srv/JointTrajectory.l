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

(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))


(if (not (find-package "TRAJECTORY_MSGS"))
  (ros::roseus-add-msgs "trajectory_msgs"))


(defclass ur_msgs::JointTrajectoryRequest
  :super ros::object
  :slots (_arm_joint_name _arm_pose _endeffector_pose ))

(defmethod ur_msgs::JointTrajectoryRequest
  (:init
   (&key
    ((:arm_joint_name __arm_joint_name) (let (r) (dotimes (i 0) (push "" r)) r))
    ((:arm_pose __arm_pose) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:endeffector_pose __endeffector_pose) (instance geometry_msgs::Pose :init))
    )
   (send-super :init)
   (setq _arm_joint_name __arm_joint_name)
   (setq _arm_pose __arm_pose)
   (setq _endeffector_pose __endeffector_pose)
   self)
  (:arm_joint_name
   (&optional __arm_joint_name)
   (if __arm_joint_name (setq _arm_joint_name __arm_joint_name)) _arm_joint_name)
  (:arm_pose
   (&optional __arm_pose)
   (if __arm_pose (setq _arm_pose __arm_pose)) _arm_pose)
  (:endeffector_pose
   (&rest __endeffector_pose)
   (if (keywordp (car __endeffector_pose))
       (send* _endeffector_pose __endeffector_pose)
     (progn
       (if __endeffector_pose (setq _endeffector_pose (car __endeffector_pose)))
       _endeffector_pose)))
  (:serialization-length
   ()
   (+
    ;; string[] _arm_joint_name
    (apply #'+ (mapcar #'(lambda (x) (+ 4 (length x))) _arm_joint_name)) 4
    ;; float64[] _arm_pose
    (* 8    (length _arm_pose)) 4
    ;; geometry_msgs/Pose _endeffector_pose
    (send _endeffector_pose :serialization-length)
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
     ;; float64[] _arm_pose
     (write-long (length _arm_pose) s)
     (dotimes (i (length _arm_pose))
       (sys::poke (elt _arm_pose i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; geometry_msgs/Pose _endeffector_pose
       (send _endeffector_pose :serialize s)
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
   ;; float64[] _arm_pose
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _arm_pose (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _arm_pose i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; geometry_msgs/Pose _endeffector_pose
     (send _endeffector_pose :deserialize buf ptr-) (incf ptr- (send _endeffector_pose :serialization-length))
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

(setf (get ur_msgs::JointTrajectory :md5sum-) "12a44cb8e62d7a40f63a508f9572c425")
(setf (get ur_msgs::JointTrajectory :datatype-) "ur_msgs/JointTrajectory")
(setf (get ur_msgs::JointTrajectory :request) ur_msgs::JointTrajectoryRequest)
(setf (get ur_msgs::JointTrajectory :response) ur_msgs::JointTrajectoryResponse)

(defmethod ur_msgs::JointTrajectoryRequest
  (:response () (instance ur_msgs::JointTrajectoryResponse :init)))

(setf (get ur_msgs::JointTrajectoryRequest :md5sum-) "12a44cb8e62d7a40f63a508f9572c425")
(setf (get ur_msgs::JointTrajectoryRequest :datatype-) "ur_msgs/JointTrajectoryRequest")
(setf (get ur_msgs::JointTrajectoryRequest :definition-)
      "
string[] arm_joint_name
float64[] arm_pose
geometry_msgs/Pose endeffector_pose

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w
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

(setf (get ur_msgs::JointTrajectoryResponse :md5sum-) "12a44cb8e62d7a40f63a508f9572c425")
(setf (get ur_msgs::JointTrajectoryResponse :datatype-) "ur_msgs/JointTrajectoryResponse")
(setf (get ur_msgs::JointTrajectoryResponse :definition-)
      "
string[] arm_joint_name
float64[] arm_pose
geometry_msgs/Pose endeffector_pose

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w
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



(provide :ur_msgs/JointTrajectory "12a44cb8e62d7a40f63a508f9572c425")


