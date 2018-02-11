// Auto-generated. Do not edit!

// (in-package see_n_tell.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class ContourData {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.data_lengths = null;
      this.data = null;
    }
    else {
      if (initObj.hasOwnProperty('data_lengths')) {
        this.data_lengths = initObj.data_lengths
      }
      else {
        this.data_lengths = [];
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
    // Serializes a message object of type ContourData
    // Serialize message field [data_lengths]
    bufferOffset = _arraySerializer.uint64(obj.data_lengths, buffer, bufferOffset, null);
    // Serialize message field [data]
    bufferOffset = _arraySerializer.uint64(obj.data, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ContourData
    let len;
    let data = new ContourData(null);
    // Deserialize message field [data_lengths]
    data.data_lengths = _arrayDeserializer.uint64(buffer, bufferOffset, null)
    // Deserialize message field [data]
    data.data = _arrayDeserializer.uint64(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += 8 * object.data_lengths.length;
    length += 8 * object.data.length;
    return length + 8;
  }

  static datatype() {
    // Returns string type for a message object
    return 'see_n_tell/ContourData';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'ebaaef9a06efaba93f1f22be3f7556c2';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    uint64[]          data_lengths
    uint64[]          data
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new ContourData(null);
    if (msg.data_lengths !== undefined) {
      resolved.data_lengths = msg.data_lengths;
    }
    else {
      resolved.data_lengths = []
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

module.exports = ContourData;
