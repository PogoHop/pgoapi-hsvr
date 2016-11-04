# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: POGOProtos/Data/PokemonData.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from POGOProtos.Enums import PokemonId_pb2 as POGOProtos_dot_Enums_dot_PokemonId__pb2
from POGOProtos.Enums import PokemonMove_pb2 as POGOProtos_dot_Enums_dot_PokemonMove__pb2
from POGOProtos.Inventory.Item import ItemId_pb2 as POGOProtos_dot_Inventory_dot_Item_dot_ItemId__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='POGOProtos/Data/PokemonData.proto',
  package='POGOProtos.Data',
  syntax='proto3',
  serialized_pb=_b('\n!POGOProtos/Data/PokemonData.proto\x12\x0fPOGOProtos.Data\x1a POGOProtos/Enums/PokemonId.proto\x1a\"POGOProtos/Enums/PokemonMove.proto\x1a&POGOProtos/Inventory/Item/ItemId.proto\"\xb5\x06\n\x0bPokemonData\x12\n\n\x02id\x18\x01 \x01(\x06\x12/\n\npokemon_id\x18\x02 \x01(\x0e\x32\x1b.POGOProtos.Enums.PokemonId\x12\n\n\x02\x63p\x18\x03 \x01(\x05\x12\x0f\n\x07stamina\x18\x04 \x01(\x05\x12\x13\n\x0bstamina_max\x18\x05 \x01(\x05\x12-\n\x06move_1\x18\x06 \x01(\x0e\x32\x1d.POGOProtos.Enums.PokemonMove\x12-\n\x06move_2\x18\x07 \x01(\x0e\x32\x1d.POGOProtos.Enums.PokemonMove\x12\x18\n\x10\x64\x65ployed_fort_id\x18\x08 \x01(\t\x12\x12\n\nowner_name\x18\t \x01(\t\x12\x0e\n\x06is_egg\x18\n \x01(\x08\x12\x1c\n\x14\x65gg_km_walked_target\x18\x0b \x01(\x01\x12\x1b\n\x13\x65gg_km_walked_start\x18\x0c \x01(\x01\x12\x0e\n\x06origin\x18\x0e \x01(\x05\x12\x10\n\x08height_m\x18\x0f \x01(\x02\x12\x11\n\tweight_kg\x18\x10 \x01(\x02\x12\x19\n\x11individual_attack\x18\x11 \x01(\x05\x12\x1a\n\x12individual_defense\x18\x12 \x01(\x05\x12\x1a\n\x12individual_stamina\x18\x13 \x01(\x05\x12\x15\n\rcp_multiplier\x18\x14 \x01(\x02\x12\x33\n\x08pokeball\x18\x15 \x01(\x0e\x32!.POGOProtos.Inventory.Item.ItemId\x12\x18\n\x10\x63\x61ptured_cell_id\x18\x16 \x01(\x04\x12\x18\n\x10\x62\x61ttles_attacked\x18\x17 \x01(\x05\x12\x18\n\x10\x62\x61ttles_defended\x18\x18 \x01(\x05\x12\x18\n\x10\x65gg_incubator_id\x18\x19 \x01(\t\x12\x18\n\x10\x63reation_time_ms\x18\x1a \x01(\x04\x12\x14\n\x0cnum_upgrades\x18\x1b \x01(\x05\x12 \n\x18\x61\x64\x64itional_cp_multiplier\x18\x1c \x01(\x02\x12\x10\n\x08\x66\x61vorite\x18\x1d \x01(\x05\x12\x10\n\x08nickname\x18\x1e \x01(\t\x12\x11\n\tfrom_fort\x18\x1f \x01(\x05\x12\x1b\n\x13\x62uddy_candy_awarded\x18  \x01(\x05\x62\x06proto3')
  ,
  dependencies=[POGOProtos_dot_Enums_dot_PokemonId__pb2.DESCRIPTOR,POGOProtos_dot_Enums_dot_PokemonMove__pb2.DESCRIPTOR,POGOProtos_dot_Inventory_dot_Item_dot_ItemId__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_POKEMONDATA = _descriptor.Descriptor(
  name='PokemonData',
  full_name='POGOProtos.Data.PokemonData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='POGOProtos.Data.PokemonData.id', index=0,
      number=1, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokemon_id', full_name='POGOProtos.Data.PokemonData.pokemon_id', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cp', full_name='POGOProtos.Data.PokemonData.cp', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stamina', full_name='POGOProtos.Data.PokemonData.stamina', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stamina_max', full_name='POGOProtos.Data.PokemonData.stamina_max', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='move_1', full_name='POGOProtos.Data.PokemonData.move_1', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='move_2', full_name='POGOProtos.Data.PokemonData.move_2', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='deployed_fort_id', full_name='POGOProtos.Data.PokemonData.deployed_fort_id', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='owner_name', full_name='POGOProtos.Data.PokemonData.owner_name', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_egg', full_name='POGOProtos.Data.PokemonData.is_egg', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='egg_km_walked_target', full_name='POGOProtos.Data.PokemonData.egg_km_walked_target', index=10,
      number=11, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='egg_km_walked_start', full_name='POGOProtos.Data.PokemonData.egg_km_walked_start', index=11,
      number=12, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='origin', full_name='POGOProtos.Data.PokemonData.origin', index=12,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='height_m', full_name='POGOProtos.Data.PokemonData.height_m', index=13,
      number=15, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='weight_kg', full_name='POGOProtos.Data.PokemonData.weight_kg', index=14,
      number=16, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='individual_attack', full_name='POGOProtos.Data.PokemonData.individual_attack', index=15,
      number=17, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='individual_defense', full_name='POGOProtos.Data.PokemonData.individual_defense', index=16,
      number=18, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='individual_stamina', full_name='POGOProtos.Data.PokemonData.individual_stamina', index=17,
      number=19, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cp_multiplier', full_name='POGOProtos.Data.PokemonData.cp_multiplier', index=18,
      number=20, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokeball', full_name='POGOProtos.Data.PokemonData.pokeball', index=19,
      number=21, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='captured_cell_id', full_name='POGOProtos.Data.PokemonData.captured_cell_id', index=20,
      number=22, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battles_attacked', full_name='POGOProtos.Data.PokemonData.battles_attacked', index=21,
      number=23, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battles_defended', full_name='POGOProtos.Data.PokemonData.battles_defended', index=22,
      number=24, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='egg_incubator_id', full_name='POGOProtos.Data.PokemonData.egg_incubator_id', index=23,
      number=25, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='creation_time_ms', full_name='POGOProtos.Data.PokemonData.creation_time_ms', index=24,
      number=26, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_upgrades', full_name='POGOProtos.Data.PokemonData.num_upgrades', index=25,
      number=27, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='additional_cp_multiplier', full_name='POGOProtos.Data.PokemonData.additional_cp_multiplier', index=26,
      number=28, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='favorite', full_name='POGOProtos.Data.PokemonData.favorite', index=27,
      number=29, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nickname', full_name='POGOProtos.Data.PokemonData.nickname', index=28,
      number=30, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='from_fort', full_name='POGOProtos.Data.PokemonData.from_fort', index=29,
      number=31, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='buddy_candy_awarded', full_name='POGOProtos.Data.PokemonData.buddy_candy_awarded', index=30,
      number=32, type=5, cpp_type=1, label=1,
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
  serialized_start=165,
  serialized_end=986,
)

_POKEMONDATA.fields_by_name['pokemon_id'].enum_type = POGOProtos_dot_Enums_dot_PokemonId__pb2._POKEMONID
_POKEMONDATA.fields_by_name['move_1'].enum_type = POGOProtos_dot_Enums_dot_PokemonMove__pb2._POKEMONMOVE
_POKEMONDATA.fields_by_name['move_2'].enum_type = POGOProtos_dot_Enums_dot_PokemonMove__pb2._POKEMONMOVE
_POKEMONDATA.fields_by_name['pokeball'].enum_type = POGOProtos_dot_Inventory_dot_Item_dot_ItemId__pb2._ITEMID
DESCRIPTOR.message_types_by_name['PokemonData'] = _POKEMONDATA

PokemonData = _reflection.GeneratedProtocolMessageType('PokemonData', (_message.Message,), dict(
  DESCRIPTOR = _POKEMONDATA,
  __module__ = 'POGOProtos.Data.PokemonData_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Data.PokemonData)
  ))
_sym_db.RegisterMessage(PokemonData)


# @@protoc_insertion_point(module_scope)
