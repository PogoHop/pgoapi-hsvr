# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: POGOProtos/Networking/Responses/EncounterResponse.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from POGOProtos.Data.Capture import CaptureProbability_pb2 as POGOProtos_dot_Data_dot_Capture_dot_CaptureProbability__pb2
from POGOProtos.Map.Pokemon import WildPokemon_pb2 as POGOProtos_dot_Map_dot_Pokemon_dot_WildPokemon__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='POGOProtos/Networking/Responses/EncounterResponse.proto',
  package='POGOProtos.Networking.Responses',
  syntax='proto3',
  serialized_pb=_b('\n7POGOProtos/Networking/Responses/EncounterResponse.proto\x12\x1fPOGOProtos.Networking.Responses\x1a\x30POGOProtos/Data/Capture/CaptureProbability.proto\x1a(POGOProtos/Map/Pokemon/WildPokemon.proto\"\xb4\x04\n\x11\x45ncounterResponse\x12\x39\n\x0cwild_pokemon\x18\x01 \x01(\x0b\x32#.POGOProtos.Map.Pokemon.WildPokemon\x12Q\n\nbackground\x18\x02 \x01(\x0e\x32=.POGOProtos.Networking.Responses.EncounterResponse.Background\x12I\n\x06status\x18\x03 \x01(\x0e\x32\x39.POGOProtos.Networking.Responses.EncounterResponse.Status\x12H\n\x13\x63\x61pture_probability\x18\x04 \x01(\x0b\x32+.POGOProtos.Data.Capture.CaptureProbability\"\"\n\nBackground\x12\x08\n\x04PARK\x10\x00\x12\n\n\x06\x44\x45SERT\x10\x01\"\xd7\x01\n\x06Status\x12\x13\n\x0f\x45NCOUNTER_ERROR\x10\x00\x12\x15\n\x11\x45NCOUNTER_SUCCESS\x10\x01\x12\x17\n\x13\x45NCOUNTER_NOT_FOUND\x10\x02\x12\x14\n\x10\x45NCOUNTER_CLOSED\x10\x03\x12\x1a\n\x16\x45NCOUNTER_POKEMON_FLED\x10\x04\x12\x1a\n\x16\x45NCOUNTER_NOT_IN_RANGE\x10\x05\x12\x1e\n\x1a\x45NCOUNTER_ALREADY_HAPPENED\x10\x06\x12\x1a\n\x16POKEMON_INVENTORY_FULL\x10\x07\x62\x06proto3')
  ,
  dependencies=[POGOProtos_dot_Data_dot_Capture_dot_CaptureProbability__pb2.DESCRIPTOR,POGOProtos_dot_Map_dot_Pokemon_dot_WildPokemon__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_ENCOUNTERRESPONSE_BACKGROUND = _descriptor.EnumDescriptor(
  name='Background',
  full_name='POGOProtos.Networking.Responses.EncounterResponse.Background',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PARK', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DESERT', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=497,
  serialized_end=531,
)
_sym_db.RegisterEnumDescriptor(_ENCOUNTERRESPONSE_BACKGROUND)

_ENCOUNTERRESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='POGOProtos.Networking.Responses.EncounterResponse.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ENCOUNTER_ERROR', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENCOUNTER_SUCCESS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENCOUNTER_NOT_FOUND', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENCOUNTER_CLOSED', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENCOUNTER_POKEMON_FLED', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENCOUNTER_NOT_IN_RANGE', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENCOUNTER_ALREADY_HAPPENED', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POKEMON_INVENTORY_FULL', index=7, number=7,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=534,
  serialized_end=749,
)
_sym_db.RegisterEnumDescriptor(_ENCOUNTERRESPONSE_STATUS)


_ENCOUNTERRESPONSE = _descriptor.Descriptor(
  name='EncounterResponse',
  full_name='POGOProtos.Networking.Responses.EncounterResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='wild_pokemon', full_name='POGOProtos.Networking.Responses.EncounterResponse.wild_pokemon', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='background', full_name='POGOProtos.Networking.Responses.EncounterResponse.background', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='POGOProtos.Networking.Responses.EncounterResponse.status', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='capture_probability', full_name='POGOProtos.Networking.Responses.EncounterResponse.capture_probability', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ENCOUNTERRESPONSE_BACKGROUND,
    _ENCOUNTERRESPONSE_STATUS,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=185,
  serialized_end=749,
)

_ENCOUNTERRESPONSE.fields_by_name['wild_pokemon'].message_type = POGOProtos_dot_Map_dot_Pokemon_dot_WildPokemon__pb2._WILDPOKEMON
_ENCOUNTERRESPONSE.fields_by_name['background'].enum_type = _ENCOUNTERRESPONSE_BACKGROUND
_ENCOUNTERRESPONSE.fields_by_name['status'].enum_type = _ENCOUNTERRESPONSE_STATUS
_ENCOUNTERRESPONSE.fields_by_name['capture_probability'].message_type = POGOProtos_dot_Data_dot_Capture_dot_CaptureProbability__pb2._CAPTUREPROBABILITY
_ENCOUNTERRESPONSE_BACKGROUND.containing_type = _ENCOUNTERRESPONSE
_ENCOUNTERRESPONSE_STATUS.containing_type = _ENCOUNTERRESPONSE
DESCRIPTOR.message_types_by_name['EncounterResponse'] = _ENCOUNTERRESPONSE

EncounterResponse = _reflection.GeneratedProtocolMessageType('EncounterResponse', (_message.Message,), dict(
  DESCRIPTOR = _ENCOUNTERRESPONSE,
  __module__ = 'POGOProtos.Networking.Responses.EncounterResponse_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Networking.Responses.EncounterResponse)
  ))
_sym_db.RegisterMessage(EncounterResponse)


# @@protoc_insertion_point(module_scope)
