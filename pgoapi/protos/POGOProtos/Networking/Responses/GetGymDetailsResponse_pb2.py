# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: POGOProtos/Networking/Responses/GetGymDetailsResponse.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from POGOProtos.Data.Gym import GymState_pb2 as POGOProtos_dot_Data_dot_Gym_dot_GymState__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='POGOProtos/Networking/Responses/GetGymDetailsResponse.proto',
  package='POGOProtos.Networking.Responses',
  syntax='proto3',
  serialized_pb=_b('\n;POGOProtos/Networking/Responses/GetGymDetailsResponse.proto\x12\x1fPOGOProtos.Networking.Responses\x1a\"POGOProtos/Data/Gym/GymState.proto\"\x83\x02\n\x15GetGymDetailsResponse\x12\x30\n\tgym_state\x18\x01 \x01(\x0b\x32\x1d.POGOProtos.Data.Gym.GymState\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04urls\x18\x03 \x03(\t\x12M\n\x06result\x18\x04 \x01(\x0e\x32=.POGOProtos.Networking.Responses.GetGymDetailsResponse.Result\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\"8\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x16\n\x12\x45RROR_NOT_IN_RANGE\x10\x02\x62\x06proto3')
  ,
  dependencies=[POGOProtos_dot_Data_dot_Gym_dot_GymState__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_GETGYMDETAILSRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='POGOProtos.Networking.Responses.GetGymDetailsResponse.Result',
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
      name='ERROR_NOT_IN_RANGE', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=336,
  serialized_end=392,
)
_sym_db.RegisterEnumDescriptor(_GETGYMDETAILSRESPONSE_RESULT)


_GETGYMDETAILSRESPONSE = _descriptor.Descriptor(
  name='GetGymDetailsResponse',
  full_name='POGOProtos.Networking.Responses.GetGymDetailsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gym_state', full_name='POGOProtos.Networking.Responses.GetGymDetailsResponse.gym_state', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='POGOProtos.Networking.Responses.GetGymDetailsResponse.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='urls', full_name='POGOProtos.Networking.Responses.GetGymDetailsResponse.urls', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='result', full_name='POGOProtos.Networking.Responses.GetGymDetailsResponse.result', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='POGOProtos.Networking.Responses.GetGymDetailsResponse.description', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GETGYMDETAILSRESPONSE_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=133,
  serialized_end=392,
)

_GETGYMDETAILSRESPONSE.fields_by_name['gym_state'].message_type = POGOProtos_dot_Data_dot_Gym_dot_GymState__pb2._GYMSTATE
_GETGYMDETAILSRESPONSE.fields_by_name['result'].enum_type = _GETGYMDETAILSRESPONSE_RESULT
_GETGYMDETAILSRESPONSE_RESULT.containing_type = _GETGYMDETAILSRESPONSE
DESCRIPTOR.message_types_by_name['GetGymDetailsResponse'] = _GETGYMDETAILSRESPONSE

GetGymDetailsResponse = _reflection.GeneratedProtocolMessageType('GetGymDetailsResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETGYMDETAILSRESPONSE,
  __module__ = 'POGOProtos.Networking.Responses.GetGymDetailsResponse_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Networking.Responses.GetGymDetailsResponse)
  ))
_sym_db.RegisterMessage(GetGymDetailsResponse)


# @@protoc_insertion_point(module_scope)
