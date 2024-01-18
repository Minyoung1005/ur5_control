// Auto-generated. Do not edit!

// (in-package ur_msgs.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let geometry_msgs = _finder('geometry_msgs');

//-----------------------------------------------------------

let trajectory_msgs = _finder('trajectory_msgs');

//-----------------------------------------------------------

class JointTrajectoryRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.arm_joint_name = null;
      this.arm_pose = null;
      this.endeffector_pose = null;
    }
    else {
      if (initObj.hasOwnProperty('arm_joint_name')) {
        this.arm_joint_name = initObj.arm_joint_name
      }
      else {
        this.arm_joint_name = [];
      }
      if (initObj.hasOwnProperty('arm_pose')) {
        this.arm_pose = initObj.arm_pose
      }
      else {
        this.arm_pose = [];
      }
      if (initObj.hasOwnProperty('endeffector_pose')) {
        this.endeffector_pose = initObj.endeffector_pose
      }
      else {
        this.endeffector_pose = new geometry_msgs.msg.Pose();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type JointTrajectoryRequest
    // Serialize message field [arm_joint_name]
    bufferOffset = _arraySerializer.string(obj.arm_joint_name, buffer, bufferOffset, null);
    // Serialize message field [arm_pose]
    bufferOffset = _arraySerializer.float64(obj.arm_pose, buffer, bufferOffset, null);
    // Serialize message field [endeffector_pose]
    bufferOffset = geometry_msgs.msg.Pose.serialize(obj.endeffector_pose, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type JointTrajectoryRequest
    let len;
    let data = new JointTrajectoryRequest(null);
    // Deserialize message field [arm_joint_name]
    data.arm_joint_name = _arrayDeserializer.string(buffer, bufferOffset, null)
    // Deserialize message field [arm_pose]
    data.arm_pose = _arrayDeserializer.float64(buffer, bufferOffset, null)
    // Deserialize message field [endeffector_pose]
    data.endeffector_pose = geometry_msgs.msg.Pose.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    object.arm_joint_name.forEach((val) => {
      length += 4 + val.length;
    });
    length += 8 * object.arm_pose.length;
    return length + 64;
  }

  static datatype() {
    // Returns string type for a service object
    return 'ur_msgs/JointTrajectoryRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '5ecfb8f10c4da4c8be5720ef8e891dea';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    
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
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new JointTrajectoryRequest(null);
    if (msg.arm_joint_name !== undefined) {
      resolved.arm_joint_name = msg.arm_joint_name;
    }
    else {
      resolved.arm_joint_name = []
    }

    if (msg.arm_pose !== undefined) {
      resolved.arm_pose = msg.arm_pose;
    }
    else {
      resolved.arm_pose = []
    }

    if (msg.endeffector_pose !== undefined) {
      resolved.endeffector_pose = geometry_msgs.msg.Pose.Resolve(msg.endeffector_pose)
    }
    else {
      resolved.endeffector_pose = new geometry_msgs.msg.Pose()
    }

    return resolved;
    }
};

class JointTrajectoryResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.plan = null;
    }
    else {
      if (initObj.hasOwnProperty('plan')) {
        this.plan = initObj.plan
      }
      else {
        this.plan = new trajectory_msgs.msg.JointTrajectory();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type JointTrajectoryResponse
    // Serialize message field [plan]
    bufferOffset = trajectory_msgs.msg.JointTrajectory.serialize(obj.plan, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type JointTrajectoryResponse
    let len;
    let data = new JointTrajectoryResponse(null);
    // Deserialize message field [plan]
    data.plan = trajectory_msgs.msg.JointTrajectory.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += trajectory_msgs.msg.JointTrajectory.getMessageSize(object.plan);
    return length;
  }

  static datatype() {
    // Returns string type for a service object
    return 'ur_msgs/JointTrajectoryResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '1406506fbfd269e79e1a93b4e8386da6';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
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
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new JointTrajectoryResponse(null);
    if (msg.plan !== undefined) {
      resolved.plan = trajectory_msgs.msg.JointTrajectory.Resolve(msg.plan)
    }
    else {
      resolved.plan = new trajectory_msgs.msg.JointTrajectory()
    }

    return resolved;
    }
};

module.exports = {
  Request: JointTrajectoryRequest,
  Response: JointTrajectoryResponse,
  md5sum() { return '12a44cb8e62d7a40f63a508f9572c425'; },
  datatype() { return 'ur_msgs/JointTrajectory'; }
};
