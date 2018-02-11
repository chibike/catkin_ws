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

class TaggedObjects {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.row = null;
      this.column = null;
      this.depth = null;
      this.width = null;
      this.height = null;
      this.tag = null;
    }
    else {
      if (initObj.hasOwnProperty('row')) {
        this.row = initObj.row
      }
      else {
        this.row = [];
      }
      if (initObj.hasOwnProperty('column')) {
        this.column = initObj.column
      }
      else {
        this.column = [];
      }
      if (initObj.hasOwnProperty('depth')) {
        this.depth = initObj.depth
      }
      else {
        this.depth = [];
      }
      if (initObj.hasOwnProperty('width')) {
        this.width = initObj.width
      }
      else {
        this.width = [];
      }
      if (initObj.hasOwnProperty('height')) {
        this.height = initObj.height
      }
      else {
        this.height = [];
      }
      if (initObj.hasOwnProperty('tag')) {
        this.tag = initObj.tag
      }
      else {
        this.tag = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type TaggedObjects
    // Serialize message field [row]
    bufferOffset = _arraySerializer.int32(obj.row, buffer, bufferOffset, null);
    // Serialize message field [column]
    bufferOffset = _arraySerializer.int32(obj.column, buffer, bufferOffset, null);
    // Serialize message field [depth]
    bufferOffset = _arraySerializer.int32(obj.depth, buffer, bufferOffset, null);
    // Serialize message field [width]
    bufferOffset = _arraySerializer.int32(obj.width, buffer, bufferOffset, null);
    // Serialize message field [height]
    bufferOffset = _arraySerializer.int32(obj.height, buffer, bufferOffset, null);
    // Serialize message field [tag]
    bufferOffset = _arraySerializer.string(obj.tag, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type TaggedObjects
    let len;
    let data = new TaggedObjects(null);
    // Deserialize message field [row]
    data.row = _arrayDeserializer.int32(buffer, bufferOffset, null)
    // Deserialize message field [column]
    data.column = _arrayDeserializer.int32(buffer, bufferOffset, null)
    // Deserialize message field [depth]
    data.depth = _arrayDeserializer.int32(buffer, bufferOffset, null)
    // Deserialize message field [width]
    data.width = _arrayDeserializer.int32(buffer, bufferOffset, null)
    // Deserialize message field [height]
    data.height = _arrayDeserializer.int32(buffer, bufferOffset, null)
    // Deserialize message field [tag]
    data.tag = _arrayDeserializer.string(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += 4 * object.row.length;
    length += 4 * object.column.length;
    length += 4 * object.depth.length;
    length += 4 * object.width.length;
    length += 4 * object.height.length;
    object.tag.forEach((val) => {
      length += 4 + val.length;
    });
    return length + 24;
  }

  static datatype() {
    // Returns string type for a message object
    return 'see_n_tell/TaggedObjects';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '54bcb59402f83d7fc9ccfd758dee382b';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int32[]          row
    int32[]          column
    int32[]          depth
    int32[]          width
    int32[]          height
    string[]         tag
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new TaggedObjects(null);
    if (msg.row !== undefined) {
      resolved.row = msg.row;
    }
    else {
      resolved.row = []
    }

    if (msg.column !== undefined) {
      resolved.column = msg.column;
    }
    else {
      resolved.column = []
    }

    if (msg.depth !== undefined) {
      resolved.depth = msg.depth;
    }
    else {
      resolved.depth = []
    }

    if (msg.width !== undefined) {
      resolved.width = msg.width;
    }
    else {
      resolved.width = []
    }

    if (msg.height !== undefined) {
      resolved.height = msg.height;
    }
    else {
      resolved.height = []
    }

    if (msg.tag !== undefined) {
      resolved.tag = msg.tag;
    }
    else {
      resolved.tag = []
    }

    return resolved;
    }
};

module.exports = TaggedObjects;
