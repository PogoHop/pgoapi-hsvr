# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: POGOProtos/Networking/Platform/Responses/BuyItemPokeCoinsResponse.proto

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
  name='POGOProtos/Networking/Platform/Responses/BuyItemPokeCoinsResponse.proto',
  package='POGOProtos.Networking.Platform.Responses',
  syntax='proto3',
  serialized_pb=_b('\nGPOGOProtos/Networking/Platform/Responses/BuyItemPokeCoinsResponse.proto\x12(POGOProtos.Networking.Platform.Responses\"\xb3\x01\n\x18\x42uyItemPokeCoinsResponse\x12Y\n\x06result\x18\x01 \x01(\x0e\x32I.POGOProtos.Networking.Platform.Responses.BuyItemPokeCoinsResponse.Status\"<\n\x06Status\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x18\n\x14NOT_ENOUGH_POKECOINS\x10\x03\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_BUYITEMPOKECOINSRESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='POGOProtos.Networking.Platform.Responses.BuyItemPokeCoinsResponse.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_ENOUGH_POKECOINS', index=2, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=237,
  serialized_end=297,
)
_sym_db.RegisterEnumDescriptor(_BUYITEMPOKECOINSRESPONSE_STATUS)


_BUYITEMPOKECOINSRESPONSE = _descriptor.Descriptor(
  name='BuyItemPokeCoinsResponse',
  full_name='POGOProtos.Networking.Platform.Responses.BuyItemPokeCoinsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='POGOProtos.Networking.Platform.Responses.BuyItemPokeCoinsResponse.result', index=0,
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
    _BUYITEMPOKECOINSRESPONSE_STATUS,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=118,
  serialized_end=297,
)

_BUYITEMPOKECOINSRESPONSE.fields_by_name['result'].enum_type = _BUYITEMPOKECOINSRESPONSE_STATUS
_BUYITEMPOKECOINSRESPONSE_STATUS.containing_type = _BUYITEMPOKECOINSRESPONSE
DESCRIPTOR.message_types_by_name['BuyItemPokeCoinsResponse'] = _BUYITEMPOKECOINSRESPONSE

BuyItemPokeCoinsResponse = _reflection.GeneratedProtocolMessageType('BuyItemPokeCoinsResponse', (_message.Message,), dict(
  DESCRIPTOR = _BUYITEMPOKECOINSRESPONSE,
  __module__ = 'POGOProtos.Networking.Platform.Responses.BuyItemPokeCoinsResponse_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Networking.Platform.Responses.BuyItemPokeCoinsResponse)
  ))
_sym_db.RegisterMessage(BuyItemPokeCoinsResponse)


# @@protoc_insertion_point(module_scope)
