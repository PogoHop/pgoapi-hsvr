# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: POGOProtos/Settings/DownloadSettingsAction.proto

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
  name='POGOProtos/Settings/DownloadSettingsAction.proto',
  package='POGOProtos.Settings',
  syntax='proto3',
  serialized_pb=_b('\n0POGOProtos/Settings/DownloadSettingsAction.proto\x12\x13POGOProtos.Settings\"&\n\x16\x44ownloadSettingsAction\x12\x0c\n\x04hash\x18\x01 \x01(\tb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_DOWNLOADSETTINGSACTION = _descriptor.Descriptor(
  name='DownloadSettingsAction',
  full_name='POGOProtos.Settings.DownloadSettingsAction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hash', full_name='POGOProtos.Settings.DownloadSettingsAction.hash', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=73,
  serialized_end=111,
)

DESCRIPTOR.message_types_by_name['DownloadSettingsAction'] = _DOWNLOADSETTINGSACTION

DownloadSettingsAction = _reflection.GeneratedProtocolMessageType('DownloadSettingsAction', (_message.Message,), dict(
  DESCRIPTOR = _DOWNLOADSETTINGSACTION,
  __module__ = 'POGOProtos.Settings.DownloadSettingsAction_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Settings.DownloadSettingsAction)
  ))
_sym_db.RegisterMessage(DownloadSettingsAction)


# @@protoc_insertion_point(module_scope)
