# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: POGOProtos/Networking/Requests/Messages/EquipBadgeMessage.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from POGOProtos.Enums import BadgeType_pb2 as POGOProtos_dot_Enums_dot_BadgeType__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='POGOProtos/Networking/Requests/Messages/EquipBadgeMessage.proto',
  package='POGOProtos.Networking.Requests.Messages',
  syntax='proto3',
  serialized_pb=_b('\n?POGOProtos/Networking/Requests/Messages/EquipBadgeMessage.proto\x12\'POGOProtos.Networking.Requests.Messages\x1a POGOProtos/Enums/BadgeType.proto\"D\n\x11\x45quipBadgeMessage\x12/\n\nbadge_type\x18\x01 \x01(\x0e\x32\x1b.POGOProtos.Enums.BadgeTypeb\x06proto3')
  ,
  dependencies=[POGOProtos_dot_Enums_dot_BadgeType__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_EQUIPBADGEMESSAGE = _descriptor.Descriptor(
  name='EquipBadgeMessage',
  full_name='POGOProtos.Networking.Requests.Messages.EquipBadgeMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='badge_type', full_name='POGOProtos.Networking.Requests.Messages.EquipBadgeMessage.badge_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
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
  serialized_start=142,
  serialized_end=210,
)

_EQUIPBADGEMESSAGE.fields_by_name['badge_type'].enum_type = POGOProtos_dot_Enums_dot_BadgeType__pb2._BADGETYPE
DESCRIPTOR.message_types_by_name['EquipBadgeMessage'] = _EQUIPBADGEMESSAGE

EquipBadgeMessage = _reflection.GeneratedProtocolMessageType('EquipBadgeMessage', (_message.Message,), dict(
  DESCRIPTOR = _EQUIPBADGEMESSAGE,
  __module__ = 'POGOProtos.Networking.Requests.Messages.EquipBadgeMessage_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Networking.Requests.Messages.EquipBadgeMessage)
  ))
_sym_db.RegisterMessage(EquipBadgeMessage)


# @@protoc_insertion_point(module_scope)
