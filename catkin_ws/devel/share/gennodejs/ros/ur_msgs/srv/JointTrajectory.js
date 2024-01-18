// Auto-generated. Do not edit!

// (in-package ur_msgs.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

let trajectory_msgs = _finder('trajectory_msgs');

//-----------------------------------------------------------

class JointTrajectoryRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.arm_joint_name = null;
      this.arm_qpos = null;
      this.eef_pose = null;
      this.eef_quat = null;
      this.grasp = null;
    }
    else {
      if (initObj.hasOwnProperty('arm_joint_name')) {
        this.arm_joint_name = initObj.arm_joint_name
      }
      else {
        this.arm_joint_name = [];
      }
      if (initObj.hasOwnProperty('arm_qpos')) {
        this.arm_qpos = initObj.arm_qpos
      }
      else {
        this.arm_qpos = [];
      }
      if (initObj.hasOwnProperty('eef_pose')) {
        this.eef_pose = initObj.eef_pose
      }
      else {
        this.eef_pose = [];
      }
      if (initObj.hasOwnProperty('eef_quat')) {
        this.eef_quat = initObj.eef_quat
      }
      else {
        this.eef_quat = [];
      }
      if (initObj.hasOwnProperty('grasp')) {
        this.grasp = initObj.grasp
      }
      else {
        this.grasp = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type JointTrajectoryRequest
    // Serialize message field [arm_joint_name]
    bufferOffset = _arraySerializer.string(obj.arm_joint_name, buffer, bufferOffset, null);
    // Serialize message field [arm_qpos]
    bufferOffset = _arraySerializer.float64(obj.arm_qpos, buffer, bufferOffset, null);
    // Serialize message field [eef_pose]
    bufferOffset = _arraySerializer.float64(obj.eef_pose, buffer, bufferOffset, null);
    // Serialize message field [eef_quat]
    bufferOffset = _arraySerializer.float64(obj.eef_quat, buffer, bufferOffset, null);
    // Serialize message field [grasp]
    bufferOffset = _serializer.float64(obj.grasp, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type JointTrajectoryRequest
    let len;
    let data = new JointTrajectoryRequest(null);
    // Deserialize message field [arm_joint_name]
    data.arm_joint_name = _arrayDeserializer.string(buffer, bufferOffset, null)
    // Deserialize message field [arm_qpos]
    data.arm_qpos = _arrayDeserializer.float64(buffer, bufferOffset, null)
    // Deserialize message field [eef_pose]
    data.eef_pose = _arrayDeserializer.float64(buffer, bufferOffset, null)
    // Deserialize message field [eef_quat]
    data.eef_quat = _arrayDeserializer.float64(buffer, bufferOffset, null)
    // Deserialize message field [grasp]
    data.grasp = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    object.arm_joint_name.forEach((val) => {
      length += 4 + val.length;
    });
    length += 8 * object.arm_qpos.length;
    length += 8 * object.eef_pose.length;
    length += 8 * object.eef_quat.length;
    return length + 24;
  }

  static datatype() {
    // Returns string type for a service object
    return 'ur_msgs/JointTrajectoryRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '11a12f53ad6d8c438206098e03d31517';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    
    string[] arm_joint_name
    float64[] arm_qpos
    float64[] eef_pose
    float64[] eef_quat
    float64 grasp
    
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

    if (msg.arm_qpos !== undefined) {
      resolved.arm_qpos = msg.arm_qpos;
    }
    else {
      resolved.arm_qpos = []
    }

    if (msg.eef_pose !== undefined) {
      resolved.eef_pose = msg.eef_pose;
    }
    else {
      resolved.eef_pose = []
    }

    if (msg.eef_quat !== undefined) {
      resolved.eef_quat = msg.eef_quat;
    }
    else {
      resolved.eef_quat = []
    }

    if (msg.grasp !== undefined) {
      resolved.grasp = msg.grasp;
    }
    else {
      resolved.grasp = 0.0
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
  md5sum() { return '1373137967a4be74f31370fe945d1aee'; },
  datatype() { return 'ur_msgs/JointTrajectory'; }
};
