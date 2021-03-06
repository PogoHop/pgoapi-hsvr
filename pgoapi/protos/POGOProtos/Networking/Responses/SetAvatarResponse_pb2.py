# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: POGOProtos/Networking/Responses/SetAvatarResponse.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from POGOProtos.Data import PlayerData_pb2 as POGOProtos_dot_Data_dot_PlayerData__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='POGOProtos/Networking/Responses/SetAvatarResponse.proto',
  package='POGOProtos.Networking.Responses',
  syntax='proto3',
  serialized_pb=_b('\n7POGOProtos/Networking/Responses/SetAvatarResponse.proto\x12\x1fPOGOProtos.Networking.Responses\x1a POGOProtos/Data/PlayerData.proto\"\xd7\x01\n\x11SetAvatarResponse\x12I\n\x06status\x18\x01 \x01(\x0e\x32\x39.POGOProtos.Networking.Responses.SetAvatarResponse.Status\x12\x30\n\x0bplayer_data\x18\x02 \x01(\x0b\x32\x1b.POGOProtos.Data.PlayerData\"E\n\x06Status\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x16\n\x12\x41VATAR_ALREADY_SET\x10\x02\x12\x0b\n\x07\x46\x41ILURE\x10\x03\x62\x06proto3')
  ,
  dependencies=[POGOProtos_dot_Data_dot_PlayerData__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_SETAVATARRESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='POGOProtos.Networking.Responses.SetAvatarResponse.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AVATAR_ALREADY_SET', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILURE', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=273,
  serialized_end=342,
)
_sym_db.RegisterEnumDescriptor(_SETAVATARRESPONSE_STATUS)


_SETAVATARRESPONSE = _descriptor.Descriptor(
  name='SetAvatarResponse',
  full_name='POGOProtos.Networking.Responses.SetAvatarResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='POGOProtos.Networking.Responses.SetAvatarResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player_data', full_name='POGOProtos.Networking.Responses.SetAvatarResponse.player_data', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SETAVATARRESPONSE_STATUS,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=127,
  serialized_end=342,
)

_SETAVATARRESPONSE.fields_by_name['status'].enum_type = _SETAVATARRESPONSE_STATUS
_SETAVATARRESPONSE.fields_by_name['player_data'].message_type = POGOProtos_dot_Data_dot_PlayerData__pb2._PLAYERDATA
_SETAVATARRESPONSE_STATUS.containing_type = _SETAVATARRESPONSE
DESCRIPTOR.message_types_by_name['SetAvatarResponse'] = _SETAVATARRESPONSE

SetAvatarResponse = _reflection.GeneratedProtocolMessageType('SetAvatarResponse', (_message.Message,), dict(
  DESCRIPTOR = _SETAVATARRESPONSE,
  __module__ = 'POGOProtos.Networking.Responses.SetAvatarResponse_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Networking.Responses.SetAvatarResponse)
  ))
_sym_db.RegisterMessage(SetAvatarResponse)


# @@protoc_insertion_point(module_scope)
