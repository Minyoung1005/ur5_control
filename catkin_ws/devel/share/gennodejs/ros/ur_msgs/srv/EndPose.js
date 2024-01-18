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

let geometry_msgs = _finder('geometry_msgs');

//-----------------------------------------------------------

class EndPoseRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
    }
    else {
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type EndPoseRequest
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type EndPoseRequest
    let len;
    let data = new EndPoseRequest(null);
    return data;
  }

  static getMessageSize(object) {
    return 0;
  }

  static datatype() {
    // Returns string type for a service object
    return 'ur_msgs/EndPoseRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'd41d8cd98f00b204e9800998ecf8427e';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new EndPoseRequest(null);
    return resolved;
    }
};

class EndPoseResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.eef_pose = null;
    }
    else {
      if (initObj.hasOwnProperty('eef_pose')) {
        this.eef_pose = initObj.eef_pose
      }
      else {
        this.eef_pose = new geometry_msgs.msg.Pose();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type EndPoseResponse
    // Serialize message field [eef_pose]
    bufferOffset = geometry_msgs.msg.Pose.serialize(obj.eef_pose, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type EndPoseResponse
    let len;
    let data = new EndPoseResponse(null);
    // Deserialize message field [eef_pose]
    data.eef_pose = geometry_msgs.msg.Pose.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 56;
  }

  static datatype() {
    // Returns string type for a service object
    return 'ur_msgs/EndPoseResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '1e78f5a947f0283d2ebd6c70bccbefe0';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
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
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new EndPoseResponse(null);
    if (msg.eef_pose !== undefined) {
      resolved.eef_pose = geometry_msgs.msg.Pose.Resolve(msg.eef_pose)
    }
    else {
      resolved.eef_pose = new geometry_msgs.msg.Pose()
    }

    return resolved;
    }
};

module.exports = {
  Request: EndPoseRequest,
  Response: EndPoseResponse,
  md5sum() { return '1e78f5a947f0283d2ebd6c70bccbefe0'; },
  datatype() { return 'ur_msgs/EndPose'; }
};
