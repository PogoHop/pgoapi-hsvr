# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: POGOProtos/Settings/Master/GymBattleSettings.proto

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
  name='POGOProtos/Settings/Master/GymBattleSettings.proto',
  package='POGOProtos.Settings.Master',
  syntax='proto3',
  serialized_pb=_b('\n2POGOProtos/Settings/Master/GymBattleSettings.proto\x12\x1aPOGOProtos.Settings.Master\"\xee\x03\n\x11GymBattleSettings\x12\x16\n\x0e\x65nergy_per_sec\x18\x01 \x01(\x02\x12\x19\n\x11\x64odge_energy_cost\x18\x02 \x01(\x02\x12\x18\n\x10retarget_seconds\x18\x03 \x01(\x02\x12\x1d\n\x15\x65nemy_attack_interval\x18\x04 \x01(\x02\x12\x1e\n\x16\x61ttack_server_interval\x18\x05 \x01(\x02\x12\x1e\n\x16round_duration_seconds\x18\x06 \x01(\x02\x12#\n\x1b\x62onus_time_per_ally_seconds\x18\x07 \x01(\x02\x12$\n\x1cmaximum_attackers_per_battle\x18\x08 \x01(\x05\x12)\n!same_type_attack_bonus_multiplier\x18\t \x01(\x02\x12\x16\n\x0emaximum_energy\x18\n \x01(\x05\x12$\n\x1c\x65nergy_delta_per_health_lost\x18\x0b \x01(\x02\x12\x19\n\x11\x64odge_duration_ms\x18\x0c \x01(\x05\x12\x1c\n\x14minimum_player_level\x18\r \x01(\x05\x12\x18\n\x10swap_duration_ms\x18\x0e \x01(\x05\x12&\n\x1e\x64odge_damage_reduction_percent\x18\x0f \x01(\x02\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_GYMBATTLESETTINGS = _descriptor.Descriptor(
  name='GymBattleSettings',
  full_name='POGOProtos.Settings.Master.GymBattleSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='energy_per_sec', full_name='POGOProtos.Settings.Master.GymBattleSettings.energy_per_sec', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dodge_energy_cost', full_name='POGOProtos.Settings.Master.GymBattleSettings.dodge_energy_cost', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='retarget_seconds', full_name='POGOProtos.Settings.Master.GymBattleSettings.retarget_seconds', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='enemy_attack_interval', full_name='POGOProtos.Settings.Master.GymBattleSettings.enemy_attack_interval', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attack_server_interval', full_name='POGOProtos.Settings.Master.GymBattleSettings.attack_server_interval', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='round_duration_seconds', full_name='POGOProtos.Settings.Master.GymBattleSettings.round_duration_seconds', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bonus_time_per_ally_seconds', full_name='POGOProtos.Settings.Master.GymBattleSettings.bonus_time_per_ally_seconds', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='maximum_attackers_per_battle', full_name='POGOProtos.Settings.Master.GymBattleSettings.maximum_attackers_per_battle', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='same_type_attack_bonus_multiplier', full_name='POGOProtos.Settings.Master.GymBattleSettings.same_type_attack_bonus_multiplier', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='maximum_energy', full_name='POGOProtos.Settings.Master.GymBattleSettings.maximum_energy', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='energy_delta_per_health_lost', full_name='POGOProtos.Settings.Master.GymBattleSettings.energy_delta_per_health_lost', index=10,
      number=11, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dodge_duration_ms', full_name='POGOProtos.Settings.Master.GymBattleSettings.dodge_duration_ms', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='minimum_player_level', full_name='POGOProtos.Settings.Master.GymBattleSettings.minimum_player_level', index=12,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='swap_duration_ms', full_name='POGOProtos.Settings.Master.GymBattleSettings.swap_duration_ms', index=13,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dodge_damage_reduction_percent', full_name='POGOProtos.Settings.Master.GymBattleSettings.dodge_damage_reduction_percent', index=14,
      number=15, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=83,
  serialized_end=577,
)

DESCRIPTOR.message_types_by_name['GymBattleSettings'] = _GYMBATTLESETTINGS

GymBattleSettings = _reflection.GeneratedProtocolMessageType('GymBattleSettings', (_message.Message,), dict(
  DESCRIPTOR = _GYMBATTLESETTINGS,
  __module__ = 'POGOProtos.Settings.Master.GymBattleSettings_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Settings.Master.GymBattleSettings)
  ))
_sym_db.RegisterMessage(GymBattleSettings)


# @@protoc_insertion_point(module_scope)
