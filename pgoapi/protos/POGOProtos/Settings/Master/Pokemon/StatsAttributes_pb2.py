# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: POGOProtos/Settings/Master/Pokemon/StatsAttributes.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='POGOProtos/Settings/Master/Pokemon/StatsAttributes.proto',
  package='POGOProtos.Settings.Master.Pokemon',
  syntax='proto3',
  serialized_pb=_b('\n8POGOProtos/Settings/Master/Pokemon/StatsAttributes.proto\x12\"POGOProtos.Settings.Master.Pokemon\"n\n\x0fStatsAttributes\x12\x14\n\x0c\x62\x61se_stamina\x18\x01 \x01(\x05\x12\x13\n\x0b\x62\x61se_attack\x18\x02 \x01(\x05\x12\x14\n\x0c\x62\x61se_defense\x18\x03 \x01(\x05\x12\x1a\n\x12\x64odge_energy_delta\x18\x08 \x01(\x05\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_STATSATTRIBUTES = _descriptor.Descriptor(
  name='StatsAttributes',
  full_name='POGOProtos.Settings.Master.Pokemon.StatsAttributes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='base_stamina', full_name='POGOProtos.Settings.Master.Pokemon.StatsAttributes.base_stamina', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='base_attack', full_name='POGOProtos.Settings.Master.Pokemon.StatsAttributes.base_attack', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='base_defense', full_name='POGOProtos.Settings.Master.Pokemon.StatsAttributes.base_defense', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dodge_energy_delta', full_name='POGOProtos.Settings.Master.Pokemon.StatsAttributes.dodge_energy_delta', index=3,
      number=8, type=5, cpp_type=1, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=96,
  serialized_end=206,
)

DESCRIPTOR.message_types_by_name['StatsAttributes'] = _STATSATTRIBUTES

StatsAttributes = _reflection.GeneratedProtocolMessageType('StatsAttributes', (_message.Message,), dict(
  DESCRIPTOR = _STATSATTRIBUTES,
  __module__ = 'POGOProtos.Settings.Master.Pokemon.StatsAttributes_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Settings.Master.Pokemon.StatsAttributes)
  ))
_sym_db.RegisterMessage(StatsAttributes)


# @@protoc_insertion_point(module_scope)
