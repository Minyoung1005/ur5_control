; Auto-generated. Do not edit!


(cl:in-package ur_msgs-srv)


;//! \htmlinclude JointTrajectory-request.msg.html

(cl:defclass <JointTrajectory-request> (roslisp-msg-protocol:ros-message)
  ((arm_joint_name
    :reader arm_joint_name
    :initarg :arm_joint_name
    :type (cl:vector cl:string)
   :initform (cl:make-array 0 :element-type 'cl:string :initial-element ""))
   (arm_pose
    :reader arm_pose
    :initarg :arm_pose
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0))
   (endeffector_pose
    :reader endeffector_pose
    :initarg :endeffector_pose
    :type geometry_msgs-msg:Pose
    :initform (cl:make-instance 'geometry_msgs-msg:Pose)))
)

(cl:defclass JointTrajectory-request (<JointTrajectory-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <JointTrajectory-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'JointTrajectory-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ur_msgs-srv:<JointTrajectory-request> is deprecated: use ur_msgs-srv:JointTrajectory-request instead.")))

(cl:ensure-generic-function 'arm_joint_name-val :lambda-list '(m))
(cl:defmethod arm_joint_name-val ((m <JointTrajectory-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ur_msgs-srv:arm_joint_name-val is deprecated.  Use ur_msgs-srv:arm_joint_name instead.")
  (arm_joint_name m))

(cl:ensure-generic-function 'arm_pose-val :lambda-list '(m))
(cl:defmethod arm_pose-val ((m <JointTrajectory-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ur_msgs-srv:arm_pose-val is deprecated.  Use ur_msgs-srv:arm_pose instead.")
  (arm_pose m))

(cl:ensure-generic-function 'endeffector_pose-val :lambda-list '(m))
(cl:defmethod endeffector_pose-val ((m <JointTrajectory-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ur_msgs-srv:endeffector_pose-val is deprecated.  Use ur_msgs-srv:endeffector_pose instead.")
  (endeffector_pose m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <JointTrajectory-request>) ostream)
  "Serializes a message object of type '<JointTrajectory-request>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'arm_joint_name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((__ros_str_len (cl:length ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) ele))
   (cl:slot-value msg 'arm_joint_name))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'arm_pose))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-double-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream)))
   (cl:slot-value msg 'arm_pose))
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'endeffector_pose) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <JointTrajectory-request>) istream)
  "Deserializes a message object of type '<JointTrajectory-request>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'arm_joint_name) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'arm_joint_name)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:aref vals i) __ros_str_idx) (cl:code-char (cl:read-byte istream))))))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'arm_pose) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'arm_pose)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-double-float-bits bits))))))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'endeffector_pose) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<JointTrajectory-request>)))
  "Returns string type for a service object of type '<JointTrajectory-request>"
  "ur_msgs/JointTrajectoryRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'JointTrajectory-request)))
  "Returns string type for a service object of type 'JointTrajectory-request"
  "ur_msgs/JointTrajectoryRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<JointTrajectory-request>)))
  "Returns md5sum for a message object of type '<JointTrajectory-request>"
  "12a44cb8e62d7a40f63a508f9572c425")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'JointTrajectory-request)))
  "Returns md5sum for a message object of type 'JointTrajectory-request"
  "12a44cb8e62d7a40f63a508f9572c425")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<JointTrajectory-request>)))
  "Returns full string definition for message of type '<JointTrajectory-request>"
  (cl:format cl:nil "~%string[] arm_joint_name~%float64[] arm_pose~%geometry_msgs/Pose endeffector_pose~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'JointTrajectory-request)))
  "Returns full string definition for message of type 'JointTrajectory-request"
  (cl:format cl:nil "~%string[] arm_joint_name~%float64[] arm_pose~%geometry_msgs/Pose endeffector_pose~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <JointTrajectory-request>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'arm_joint_name) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4 (cl:length ele))))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'arm_pose) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 8)))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'endeffector_pose))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <JointTrajectory-request>))
  "Converts a ROS message object to a list"
  (cl:list 'JointTrajectory-request
    (cl:cons ':arm_joint_name (arm_joint_name msg))
    (cl:cons ':arm_pose (arm_pose msg))
    (cl:cons ':endeffector_pose (endeffector_pose msg))
))
;//! \htmlinclude JointTrajectory-response.msg.html

(cl:defclass <JointTrajectory-response> (roslisp-msg-protocol:ros-message)
  ((plan
    :reader plan
    :initarg :plan
    :type trajectory_msgs-msg:JointTrajectory
    :initform (cl:make-instance 'trajectory_msgs-msg:JointTrajectory)))
)

(cl:defclass JointTrajectory-response (<JointTrajectory-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <JointTrajectory-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'JointTrajectory-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ur_msgs-srv:<JointTrajectory-response> is deprecated: use ur_msgs-srv:JointTrajectory-response instead.")))

(cl:ensure-generic-function 'plan-val :lambda-list '(m))
(cl:defmethod plan-val ((m <JointTrajectory-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ur_msgs-srv:plan-val is deprecated.  Use ur_msgs-srv:plan instead.")
  (plan m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <JointTrajectory-response>) ostream)
  "Serializes a message object of type '<JointTrajectory-response>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'plan) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <JointTrajectory-response>) istream)
  "Deserializes a message object of type '<JointTrajectory-response>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'plan) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<JointTrajectory-response>)))
  "Returns string type for a service object of type '<JointTrajectory-response>"
  "ur_msgs/JointTrajectoryResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'JointTrajectory-response)))
  "Returns string type for a service object of type 'JointTrajectory-response"
  "ur_msgs/JointTrajectoryResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<JointTrajectory-response>)))
  "Returns md5sum for a message object of type '<JointTrajectory-response>"
  "12a44cb8e62d7a40f63a508f9572c425")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'JointTrajectory-response)))
  "Returns md5sum for a message object of type 'JointTrajectory-response"
  "12a44cb8e62d7a40f63a508f9572c425")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<JointTrajectory-response>)))
  "Returns full string definition for message of type '<JointTrajectory-response>"
  (cl:format cl:nil "trajectory_msgs/JointTrajectory plan~%~%~%================================================================================~%MSG: trajectory_msgs/JointTrajectory~%Header header~%string[] joint_names~%JointTrajectoryPoint[] points~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: trajectory_msgs/JointTrajectoryPoint~%# Each trajectory point specifies either positions[, velocities[, accelerations]]~%# or positions[, effort] for the trajectory to be executed.~%# All specified values are in the same order as the joint names in JointTrajectory.msg~%~%float64[] positions~%float64[] velocities~%float64[] accelerations~%float64[] effort~%duration time_from_start~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'JointTrajectory-response)))
  "Returns full string definition for message of type 'JointTrajectory-response"
  (cl:format cl:nil "trajectory_msgs/JointTrajectory plan~%~%~%================================================================================~%MSG: trajectory_msgs/JointTrajectory~%Header header~%string[] joint_names~%JointTrajectoryPoint[] points~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: trajectory_msgs/JointTrajectoryPoint~%# Each trajectory point specifies either positions[, velocities[, accelerations]]~%# or positions[, effort] for the trajectory to be executed.~%# All specified values are in the same order as the joint names in JointTrajectory.msg~%~%float64[] positions~%float64[] velocities~%float64[] accelerations~%float64[] effort~%duration time_from_start~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <JointTrajectory-response>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'plan))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <JointTrajectory-response>))
  "Converts a ROS message object to a list"
  (cl:list 'JointTrajectory-response
    (cl:cons ':plan (plan msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'JointTrajectory)))
  'JointTrajectory-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'JointTrajectory)))
  'JointTrajectory-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'JointTrajectory)))
  "Returns string type for a service object of type '<JointTrajectory>"
  "ur_msgs/JointTrajectory")