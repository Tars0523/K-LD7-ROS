// Auto-generated. Do not edit!

// (in-package radar.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class radar_message {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.start_time = null;
      this.num = null;
      this.data = null;
    }
    else {
      if (initObj.hasOwnProperty('start_time')) {
        this.start_time = initObj.start_time
      }
      else {
        this.start_time = {secs: 0, nsecs: 0};
      }
      if (initObj.hasOwnProperty('num')) {
        this.num = initObj.num
      }
      else {
        this.num = 0.0;
      }
      if (initObj.hasOwnProperty('data')) {
        this.data = initObj.data
      }
      else {
        this.data = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type radar_message
    // Serialize message field [start_time]
    bufferOffset = _serializer.time(obj.start_time, buffer, bufferOffset);
    // Serialize message field [num]
    bufferOffset = _serializer.float32(obj.num, buffer, bufferOffset);
    // Serialize message field [data]
    bufferOffset = _arraySerializer.float64(obj.data, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type radar_message
    let len;
    let data = new radar_message(null);
    // Deserialize message field [start_time]
    data.start_time = _deserializer.time(buffer, bufferOffset);
    // Deserialize message field [num]
    data.num = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [data]
    data.data = _arrayDeserializer.float64(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += 8 * object.data.length;
    return length + 16;
  }

  static datatype() {
    // Returns string type for a message object
    return 'radar/radar_message';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '9d156b01ce488aed0a9757f924f4b8e0';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    time start_time
    float32 num
    float64[] data
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new radar_message(null);
    if (msg.start_time !== undefined) {
      resolved.start_time = msg.start_time;
    }
    else {
      resolved.start_time = {secs: 0, nsecs: 0}
    }

    if (msg.num !== undefined) {
      resolved.num = msg.num;
    }
    else {
      resolved.num = 0.0
    }

    if (msg.data !== undefined) {
      resolved.data = msg.data;
    }
    else {
      resolved.data = []
    }

    return resolved;
    }
};

module.exports = radar_message;
