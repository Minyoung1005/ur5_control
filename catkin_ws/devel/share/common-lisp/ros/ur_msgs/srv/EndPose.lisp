; Auto-generated. Do not edit!


(cl:in-package ur_msgs-srv)


;//! \htmlinclude EndPose-request.msg.html

(cl:defclass <EndPose-request> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass EndPose-request (<EndPose-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <EndPose-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'EndPose-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ur_msgs-srv:<EndPose-request> is deprecated: use ur_msgs-srv:EndPose-request instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <EndPose-request>) ostream)
  "Serializes a message object of type '<EndPose-request>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <EndPose-request>) istream)
  "Deserializes a message object of type '<EndPose-request>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<EndPose-request>)))
  "Returns string type for a service object of type '<EndPose-request>"
  "ur_msgs/EndPoseRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'EndPose-request)))
  "Returns string type for a service object of type 'EndPose-request"
  "ur_msgs/EndPoseRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<EndPose-request>)))
  "Returns md5sum for a message object of type '<EndPose-request>"
  "1e78f5a947f0283d2ebd6c70bccbefe0")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'EndPose-request)))
  "Returns md5sum for a message object of type 'EndPose-request"
  "1e78f5a947f0283d2ebd6c70bccbefe0")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<EndPose-request>)))
  "Returns full string definition for message of type '<EndPose-request>"
  (cl:format cl:nil "~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'EndPose-request)))
  "Returns full string definition for message of type 'EndPose-request"
  (cl:format cl:nil "~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <EndPose-request>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <EndPose-request>))
  "Converts a ROS message object to a list"
  (cl:list 'EndPose-request
))
;//! \htmlinclude EndPose-response.msg.html

(cl:defclass <EndPose-response> (roslisp-msg-protocol:ros-message)
  ((eef_pose
    :reader eef_pose
    :initarg :eef_pose
    :type geometry_msgs-msg:Pose
    :initform (cl:make-instance 'geometry_msgs-msg:Pose)))
)

(cl:defclass EndPose-response (<EndPose-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <EndPose-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'EndPose-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ur_msgs-srv:<EndPose-response> is deprecated: use ur_msgs-srv:EndPose-response instead.")))

(cl:ensure-generic-function 'eef_pose-val :lambda-list '(m))
(cl:defmethod eef_pose-val ((m <EndPose-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ur_msgs-srv:eef_pose-val is deprecated.  Use ur_msgs-srv:eef_pose instead.")
  (eef_pose m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <EndPose-response>) ostream)
  "Serializes a message object of type '<EndPose-response>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'eef_pose) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <EndPose-response>) istream)
  "Deserializes a message object of type '<EndPose-response>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'eef_pose) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<EndPose-response>)))
  "Returns string type for a service object of type '<EndPose-response>"
  "ur_msgs/EndPoseResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'EndPose-response)))
  "Returns string type for a service object of type 'EndPose-response"
  "ur_msgs/EndPoseResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<EndPose-response>)))
  "Returns md5sum for a message object of type '<EndPose-response>"
  "1e78f5a947f0283d2ebd6c70bccbefe0")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'EndPose-response)))
  "Returns md5sum for a message object of type 'EndPose-response"
  "1e78f5a947f0283d2ebd6c70bccbefe0")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<EndPose-response>)))
  "Returns full string definition for message of type '<EndPose-response>"
  (cl:format cl:nil "geometry_msgs/Pose eef_pose~%~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'EndPose-response)))
  "Returns full string definition for message of type 'EndPose-response"
  (cl:format cl:nil "geometry_msgs/Pose eef_pose~%~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <EndPose-response>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'eef_pose))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <EndPose-response>))
  "Converts a ROS message object to a list"
  (cl:list 'EndPose-response
    (cl:cons ':eef_pose (eef_pose msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'EndPose)))
  'EndPose-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'EndPose)))
  'EndPose-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'EndPose)))
  "Returns string type for a service object of type '<EndPose>"
  "ur_msgs/EndPose")