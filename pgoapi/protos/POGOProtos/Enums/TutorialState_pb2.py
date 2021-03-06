# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: POGOProtos/Enums/TutorialState.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='POGOProtos/Enums/TutorialState.proto',
  package='POGOProtos.Enums',
  syntax='proto3',
  serialized_pb=_b('\n$POGOProtos/Enums/TutorialState.proto\x12\x10POGOProtos.Enums*\xe4\x01\n\rTutorialState\x12\x10\n\x0cLEGAL_SCREEN\x10\x00\x12\x14\n\x10\x41VATAR_SELECTION\x10\x01\x12\x14\n\x10\x41\x43\x43OUNT_CREATION\x10\x02\x12\x13\n\x0fPOKEMON_CAPTURE\x10\x03\x12\x12\n\x0eNAME_SELECTION\x10\x04\x12\x11\n\rPOKEMON_BERRY\x10\x05\x12\x0c\n\x08USE_ITEM\x10\x06\x12\"\n\x1e\x46IRST_TIME_EXPERIENCE_COMPLETE\x10\x07\x12\x15\n\x11POKESTOP_TUTORIAL\x10\x08\x12\x10\n\x0cGYM_TUTORIAL\x10\tb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_TUTORIALSTATE = _descriptor.EnumDescriptor(
  name='TutorialState',
  full_name='POGOProtos.Enums.TutorialState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='LEGAL_SCREEN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AVATAR_SELECTION', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACCOUNT_CREATION', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POKEMON_CAPTURE', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NAME_SELECTION', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POKEMON_BERRY', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USE_ITEM', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FIRST_TIME_EXPERIENCE_COMPLETE', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POKESTOP_TUTORIAL', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GYM_TUTORIAL', index=9, number=9,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=59,
  serialized_end=287,
)
_sym_db.RegisterEnumDescriptor(_TUTORIALSTATE)

TutorialState = enum_type_wrapper.EnumTypeWrapper(_TUTORIALSTATE)
LEGAL_SCREEN = 0
AVATAR_SELECTION = 1
ACCOUNT_CREATION = 2
POKEMON_CAPTURE = 3
NAME_SELECTION = 4
POKEMON_BERRY = 5
USE_ITEM = 6
FIRST_TIME_EXPERIENCE_COMPLETE = 7
POKESTOP_TUTORIAL = 8
GYM_TUTORIAL = 9


DESCRIPTOR.enum_types_by_name['TutorialState'] = _TUTORIALSTATE


# @@protoc_insertion_point(module_scope)
