# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: POGOProtos/Networking/Responses/EchoResponse.proto

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
  name='POGOProtos/Networking/Responses/EchoResponse.proto',
  package='POGOProtos.Networking.Responses',
  syntax='proto3',
  serialized_pb=_b('\n2POGOProtos/Networking/Responses/EchoResponse.proto\x12\x1fPOGOProtos.Networking.Responses\"\x1f\n\x0c\x45\x63hoResponse\x12\x0f\n\x07\x63ontext\x18\x01 \x01(\tb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ECHORESPONSE = _descriptor.Descriptor(
  name='EchoResponse',
  full_name='POGOProtos.Networking.Responses.EchoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='context', full_name='POGOProtos.Networking.Responses.EchoResponse.context', index=0,
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
  serialized_start=87,
  serialized_end=118,
)

DESCRIPTOR.message_types_by_name['EchoResponse'] = _ECHORESPONSE

EchoResponse = _reflection.GeneratedProtocolMessageType('EchoResponse', (_message.Message,), dict(
  DESCRIPTOR = _ECHORESPONSE,
  __module__ = 'POGOProtos.Networking.Responses.EchoResponse_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Networking.Responses.EchoResponse)
  ))
_sym_db.RegisterMessage(EchoResponse)


# @@protoc_insertion_point(module_scope)
