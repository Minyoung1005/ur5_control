; Auto-generated. Do not edit!


(cl:in-package ur_msgs-srv)


;//! \htmlinclude JointStates-request.msg.html

(cl:defclass <JointStates-request> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass JointStates-request (<JointStates-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <JointStates-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'JointStates-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ur_msgs-srv:<JointStates-request> is deprecated: use ur_msgs-srv:JointStates-request instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <JointStates-request>) ostream)
  "Serializes a message object of type '<JointStates-request>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <JointStates-request>) istream)
  "Deserializes a message object of type '<JointStates-request>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<JointStates-request>)))
  "Returns string type for a service object of type '<JointStates-request>"
  "ur_msgs/JointStatesRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'JointStates-request)))
  "Returns string type for a service object of type 'JointStates-request"
  "ur_msgs/JointStatesRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<JointStates-request>)))
  "Returns md5sum for a message object of type '<JointStates-request>"
  "5581a04fddc1f7d62a2958142211f72d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'JointStates-request)))
  "Returns md5sum for a message object of type 'JointStates-request"
  "5581a04fddc1f7d62a2958142211f72d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<JointStates-request>)))
  "Returns full string definition for message of type '<JointStates-request>"
  (cl:format cl:nil "~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'JointStates-request)))
  "Returns full string definition for message of type 'JointStates-request"
  (cl:format cl:nil "~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <JointStates-request>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <JointStates-request>))
  "Converts a ROS message object to a list"
  (cl:list 'JointStates-request
))
;//! \htmlinclude JointStates-response.msg.html

(cl:defclass <JointStates-response> (roslisp-msg-protocol:ros-message)
  ((joint_states
    :reader joint_states
    :initarg :joint_states
    :type cl:string
    :initform ""))
)

(cl:defclass JointStates-response (<JointStates-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <JointStates-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'JointStates-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ur_msgs-srv:<JointStates-response> is deprecated: use ur_msgs-srv:JointStates-response instead.")))

(cl:ensure-generic-function 'joint_states-val :lambda-list '(m))
(cl:defmethod joint_states-val ((m <JointStates-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ur_msgs-srv:joint_states-val is deprecated.  Use ur_msgs-srv:joint_states instead.")
  (joint_states m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <JointStates-response>) ostream)
  "Serializes a message object of type '<JointStates-response>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'joint_states))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'joint_states))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <JointStates-response>) istream)
  "Deserializes a message object of type '<JointStates-response>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'joint_states) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'joint_states) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<JointStates-response>)))
  "Returns string type for a service object of type '<JointStates-response>"
  "ur_msgs/JointStatesResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'JointStates-response)))
  "Returns string type for a service object of type 'JointStates-response"
  "ur_msgs/JointStatesResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<JointStates-response>)))
  "Returns md5sum for a message object of type '<JointStates-response>"
  "5581a04fddc1f7d62a2958142211f72d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'JointStates-response)))
  "Returns md5sum for a message object of type 'JointStates-response"
  "5581a04fddc1f7d62a2958142211f72d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<JointStates-response>)))
  "Returns full string definition for message of type '<JointStates-response>"
  (cl:format cl:nil "string joint_states~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'JointStates-response)))
  "Returns full string definition for message of type 'JointStates-response"
  (cl:format cl:nil "string joint_states~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <JointStates-response>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'joint_states))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <JointStates-response>))
  "Converts a ROS message object to a list"
  (cl:list 'JointStates-response
    (cl:cons ':joint_states (joint_states msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'JointStates)))
  'JointStates-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'JointStates)))
  'JointStates-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'JointStates)))
  "Returns string type for a service object of type '<JointStates>"
  "ur_msgs/JointStates")