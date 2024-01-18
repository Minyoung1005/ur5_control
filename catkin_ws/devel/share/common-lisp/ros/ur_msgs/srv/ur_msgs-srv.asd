
(cl:in-package :asdf)

(defsystem "ur_msgs-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
               :trajectory_msgs-msg
)
  :components ((:file "_package")
    (:file "EndPose" :depends-on ("_package_EndPose"))
    (:file "_package_EndPose" :depends-on ("_package"))
    (:file "JointStates" :depends-on ("_package_JointStates"))
    (:file "_package_JointStates" :depends-on ("_package"))
    (:file "JointTrajectory" :depends-on ("_package_JointTrajectory"))
    (:file "_package_JointTrajectory" :depends-on ("_package"))
    (:file "SetIO" :depends-on ("_package_SetIO"))
    (:file "_package_SetIO" :depends-on ("_package"))
    (:file "SetPayload" :depends-on ("_package_SetPayload"))
    (:file "_package_SetPayload" :depends-on ("_package"))
    (:file "SetSpeedSliderFraction" :depends-on ("_package_SetSpeedSliderFraction"))
    (:file "_package_SetSpeedSliderFraction" :depends-on ("_package"))
  ))