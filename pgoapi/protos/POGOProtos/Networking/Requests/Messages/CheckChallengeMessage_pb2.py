# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: POGOProtos/Networking/Requests/Messages/CheckChallenge.proto

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
  name='POGOProtos/Networking/Requests/Messages/CheckChallenge.proto',
  package='POGOProtos.Networking.Requests.Messages',
  syntax='proto3',
  serialized_pb=_b('\n<POGOProtos/Networking/Requests/Messages/CheckChallenge.proto\x12\'POGOProtos.Networking.Requests.Messages\".\n\x15\x43heckChallengeMessage\x12\x15\n\rdebug_request\x18\x01 \x01(\x08\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CHECKCHALLENGEMESSAGE = _descriptor.Descriptor(
  name='CheckChallengeMessage',
  full_name='POGOProtos.Networking.Requests.Messages.CheckChallengeMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='debug_request', full_name='POGOProtos.Networking.Requests.Messages.CheckChallengeMessage.debug_request', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=105,
  serialized_end=151,
)

DESCRIPTOR.message_types_by_name['CheckChallengeMessage'] = _CHECKCHALLENGEMESSAGE

CheckChallengeMessage = _reflection.GeneratedProtocolMessageType('CheckChallengeMessage', (_message.Message,), dict(
  DESCRIPTOR = _CHECKCHALLENGEMESSAGE,
  __module__ = 'POGOProtos.Networking.Requests.Messages.CheckChallenge_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Networking.Requests.Messages.CheckChallengeMessage)
  ))
_sym_db.RegisterMessage(CheckChallengeMessage)


# @@protoc_insertion_point(module_scope)
