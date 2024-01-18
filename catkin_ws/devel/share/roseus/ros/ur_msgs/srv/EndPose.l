;; Auto-generated. Do not edit!


(when (boundp 'ur_msgs::EndPose)
  (if (not (find-package "UR_MSGS"))
    (make-package "UR_MSGS"))
  (shadow 'EndPose (find-package "UR_MSGS")))
(unless (find-package "UR_MSGS::ENDPOSE")
  (make-package "UR_MSGS::ENDPOSE"))
(unless (find-package "UR_MSGS::ENDPOSEREQUEST")
  (make-package "UR_MSGS::ENDPOSEREQUEST"))
(unless (find-package "UR_MSGS::ENDPOSERESPONSE")
  (make-package "UR_MSGS::ENDPOSERESPONSE"))

(in-package "ROS")



(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))


(defclass ur_msgs::EndPoseRequest
  :super ros::object
  :slots ())

(defmethod ur_msgs::EndPoseRequest
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

(defclass ur_msgs::EndPoseResponse
  :super ros::object
  :slots (_eef_pose ))

(defmethod ur_msgs::EndPoseResponse
  (:init
   (&key
    ((:eef_pose __eef_pose) (instance geometry_msgs::Pose :init))
    )
   (send-super :init)
   (setq _eef_pose __eef_pose)
   self)
  (:eef_pose
   (&rest __eef_pose)
   (if (keywordp (car __eef_pose))
       (send* _eef_pose __eef_pose)
     (progn
       (if __eef_pose (setq _eef_pose (car __eef_pose)))
       _eef_pose)))
  (:serialization-length
   ()
   (+
    ;; geometry_msgs/Pose _eef_pose
    (send _eef_pose :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; geometry_msgs/Pose _eef_pose
       (send _eef_pose :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; geometry_msgs/Pose _eef_pose
     (send _eef_pose :deserialize buf ptr-) (incf ptr- (send _eef_pose :serialization-length))
   ;;
   self)
  )

(defclass ur_msgs::EndPose
  :super ros::object
  :slots ())

(setf (get ur_msgs::EndPose :md5sum-) "1e78f5a947f0283d2ebd6c70bccbefe0")
(setf (get ur_msgs::EndPose :datatype-) "ur_msgs/EndPose")
(setf (get ur_msgs::EndPose :request) ur_msgs::EndPoseRequest)
(setf (get ur_msgs::EndPose :response) ur_msgs::EndPoseResponse)

(defmethod ur_msgs::EndPoseRequest
  (:response () (instance ur_msgs::EndPoseResponse :init)))

(setf (get ur_msgs::EndPoseRequest :md5sum-) "1e78f5a947f0283d2ebd6c70bccbefe0")
(setf (get ur_msgs::EndPoseRequest :datatype-) "ur_msgs/EndPoseRequest")
(setf (get ur_msgs::EndPoseRequest :definition-)
      "
---
geometry_msgs/Pose eef_pose


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
")

(setf (get ur_msgs::EndPoseResponse :md5sum-) "1e78f5a947f0283d2ebd6c70bccbefe0")
(setf (get ur_msgs::EndPoseResponse :datatype-) "ur_msgs/EndPoseResponse")
(setf (get ur_msgs::EndPoseResponse :definition-)
      "
---
geometry_msgs/Pose eef_pose


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
")



(provide :ur_msgs/EndPose "1e78f5a947f0283d2ebd6c70bccbefe0")


