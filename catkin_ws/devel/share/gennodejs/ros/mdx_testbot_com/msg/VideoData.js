// Auto-generated. Do not edit!

// (in-package mdx_testbot_com.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class VideoData {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.left_data = null;
      this.right_data = null;
    }
    else {
      if (initObj.hasOwnProperty('left_data')) {
        this.left_data = initObj.left_data
      }
      else {
        this.left_data = [];
      }
      if (initObj.hasOwnProperty('right_data')) {
        this.right_data = initObj.right_data
      }
      else {
        this.right_data = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type VideoData
    // Serialize message field [left_data]
    bufferOffset = _arraySerializer.int32(obj.left_data, buffer, bufferOffset, null);
    // Serialize message field [right_data]
    bufferOffset = _arraySerializer.int32(obj.right_data, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type VideoData
    let len;
    let data = new VideoData(null);
    // Deserialize message field [left_data]
    data.left_data = _arrayDeserializer.int32(buffer, bufferOffset, null)
    // Deserialize message field [right_data]
    data.right_data = _arrayDeserializer.int32(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += 4 * object.left_data.length;
    length += 4 * object.right_data.length;
    return length + 8;
  }

  static datatype() {
    // Returns string type for a message object
    return 'mdx_testbot_com/VideoData';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'a486237169ce6e905ee06bbd36d2b929';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int32[] left_data
    int32[] right_data
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new VideoData(null);
    if (msg.left_data !== undefined) {
      resolved.left_data = msg.left_data;
    }
    else {
      resolved.left_data = []
    }

    if (msg.right_data !== undefined) {
      resolved.right_data = msg.right_data;
    }
    else {
      resolved.right_data = []
    }

    return resolved;
    }
};

module.exports = VideoData;
