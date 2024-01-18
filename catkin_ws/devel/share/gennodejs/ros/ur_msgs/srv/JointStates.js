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


//-----------------------------------------------------------

class JointStatesRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
    }
    else {
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type JointStatesRequest
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type JointStatesRequest
    let len;
    let data = new JointStatesRequest(null);
    return data;
  }

  static getMessageSize(object) {
    return 0;
  }

  static datatype() {
    // Returns string type for a service object
    return 'ur_msgs/JointStatesRequest';
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
    const resolved = new JointStatesRequest(null);
    return resolved;
    }
};

class JointStatesResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.joint_states = null;
    }
    else {
      if (initObj.hasOwnProperty('joint_states')) {
        this.joint_states = initObj.joint_states
      }
      else {
        this.joint_states = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type JointStatesResponse
    // Serialize message field [joint_states]
    bufferOffset = _serializer.string(obj.joint_states, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type JointStatesResponse
    let len;
    let data = new JointStatesResponse(null);
    // Deserialize message field [joint_states]
    data.joint_states = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.joint_states.length;
    return length + 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'ur_msgs/JointStatesResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '5581a04fddc1f7d62a2958142211f72d';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string joint_states
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new JointStatesResponse(null);
    if (msg.joint_states !== undefined) {
      resolved.joint_states = msg.joint_states;
    }
    else {
      resolved.joint_states = ''
    }

    return resolved;
    }
};

module.exports = {
  Request: JointStatesRequest,
  Response: JointStatesResponse,
  md5sum() { return '5581a04fddc1f7d62a2958142211f72d'; },
  datatype() { return 'ur_msgs/JointStates'; }
};
