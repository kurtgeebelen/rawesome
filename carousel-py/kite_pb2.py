# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='kite.proto',
  package='kite',
  serialized_pb='\n\nkite.proto\x12\x04kite\"&\n\x03Xyz\x12\t\n\x01x\x18\x01 \x02(\x01\x12\t\n\x01y\x18\x02 \x02(\x01\x12\t\n\x01z\x18\x03 \x02(\x01\"z\n\x03\x44\x63m\x12\x0b\n\x03r11\x18\x01 \x02(\x01\x12\x0b\n\x03r12\x18\x02 \x02(\x01\x12\x0b\n\x03r13\x18\x03 \x02(\x01\x12\x0b\n\x03r21\x18\x04 \x02(\x01\x12\x0b\n\x03r22\x18\x05 \x02(\x01\x12\x0b\n\x03r23\x18\x06 \x02(\x01\x12\x0b\n\x03r31\x18\x07 \x02(\x01\x12\x0b\n\x03r32\x18\x08 \x02(\x01\x12\x0b\n\x03r33\x18\t \x02(\x01\"\x9a\x01\n\rCarouselState\x12\x1a\n\x07kiteXyz\x18\x01 \x02(\x0b\x32\t.kite.Xyz\x12\x1a\n\x07kiteDcm\x18\x02 \x02(\x0b\x32\t.kite.Dcm\x12\r\n\x05\x64\x65lta\x18\x03 \x02(\x01\x12\x0e\n\x06\x64\x64\x65lta\x18\x04 \x02(\x01\x12\n\n\x02u1\x18\x05 \x02(\x01\x12\n\n\x02u2\x18\x06 \x02(\x01\x12\n\n\x02tc\x18\x07 \x02(\x01\x12\x0e\n\x06wind_x\x18\x08 \x02(\x01')




_XYZ = descriptor.Descriptor(
  name='Xyz',
  full_name='kite.Xyz',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='x', full_name='kite.Xyz.x', index=0,
      number=1, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='y', full_name='kite.Xyz.y', index=1,
      number=2, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='z', full_name='kite.Xyz.z', index=2,
      number=3, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=20,
  serialized_end=58,
)


_DCM = descriptor.Descriptor(
  name='Dcm',
  full_name='kite.Dcm',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='r11', full_name='kite.Dcm.r11', index=0,
      number=1, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='r12', full_name='kite.Dcm.r12', index=1,
      number=2, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='r13', full_name='kite.Dcm.r13', index=2,
      number=3, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='r21', full_name='kite.Dcm.r21', index=3,
      number=4, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='r22', full_name='kite.Dcm.r22', index=4,
      number=5, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='r23', full_name='kite.Dcm.r23', index=5,
      number=6, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='r31', full_name='kite.Dcm.r31', index=6,
      number=7, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='r32', full_name='kite.Dcm.r32', index=7,
      number=8, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='r33', full_name='kite.Dcm.r33', index=8,
      number=9, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=60,
  serialized_end=182,
)


_CAROUSELSTATE = descriptor.Descriptor(
  name='CarouselState',
  full_name='kite.CarouselState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='kiteXyz', full_name='kite.CarouselState.kiteXyz', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='kiteDcm', full_name='kite.CarouselState.kiteDcm', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='delta', full_name='kite.CarouselState.delta', index=2,
      number=3, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='ddelta', full_name='kite.CarouselState.ddelta', index=3,
      number=4, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='u1', full_name='kite.CarouselState.u1', index=4,
      number=5, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='u2', full_name='kite.CarouselState.u2', index=5,
      number=6, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='tc', full_name='kite.CarouselState.tc', index=6,
      number=7, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='wind_x', full_name='kite.CarouselState.wind_x', index=7,
      number=8, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=185,
  serialized_end=339,
)

_CAROUSELSTATE.fields_by_name['kiteXyz'].message_type = _XYZ
_CAROUSELSTATE.fields_by_name['kiteDcm'].message_type = _DCM
DESCRIPTOR.message_types_by_name['Xyz'] = _XYZ
DESCRIPTOR.message_types_by_name['Dcm'] = _DCM
DESCRIPTOR.message_types_by_name['CarouselState'] = _CAROUSELSTATE

class Xyz(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _XYZ
  
  # @@protoc_insertion_point(class_scope:kite.Xyz)

class Dcm(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DCM
  
  # @@protoc_insertion_point(class_scope:kite.Dcm)

class CarouselState(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CAROUSELSTATE
  
  # @@protoc_insertion_point(class_scope:kite.CarouselState)

# @@protoc_insertion_point(module_scope)
