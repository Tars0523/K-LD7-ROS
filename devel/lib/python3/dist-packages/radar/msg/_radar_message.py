# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from radar/radar_message.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import genpy

class radar_message(genpy.Message):
  _md5sum = "9d156b01ce488aed0a9757f924f4b8e0"
  _type = "radar/radar_message"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """time start_time
float32 num
float64[] data

"""
  __slots__ = ['start_time','num','data']
  _slot_types = ['time','float32','float64[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       start_time,num,data

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(radar_message, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.start_time is None:
        self.start_time = genpy.Time()
      if self.num is None:
        self.num = 0.
      if self.data is None:
        self.data = []
    else:
      self.start_time = genpy.Time()
      self.num = 0.
      self.data = []

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_2If().pack(_x.start_time.secs, _x.start_time.nsecs, _x.num))
      length = len(self.data)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.data))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.start_time is None:
        self.start_time = genpy.Time()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.start_time.secs, _x.start_time.nsecs, _x.num,) = _get_struct_2If().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.data = s.unpack(str[start:end])
      self.start_time.canon()
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_2If().pack(_x.start_time.secs, _x.start_time.nsecs, _x.num))
      length = len(self.data)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.data.tostring())
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.start_time is None:
        self.start_time = genpy.Time()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.start_time.secs, _x.start_time.nsecs, _x.num,) = _get_struct_2If().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.data = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      self.start_time.canon()
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2If = None
def _get_struct_2If():
    global _struct_2If
    if _struct_2If is None:
        _struct_2If = struct.Struct("<2If")
    return _struct_2If