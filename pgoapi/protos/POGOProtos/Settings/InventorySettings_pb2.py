# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: POGOProtos/Settings/InventorySettings.proto

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
  name='POGOProtos/Settings/InventorySettings.proto',
  package='POGOProtos.Settings',
  syntax='proto3',
  serialized_pb=_b('\n+POGOProtos/Settings/InventorySettings.proto\x12\x13POGOProtos.Settings\"\x80\x01\n\x11InventorySettings\x12\x13\n\x0bmax_pokemon\x18\x01 \x01(\x05\x12\x15\n\rmax_bag_items\x18\x02 \x01(\x05\x12\x14\n\x0c\x62\x61se_pokemon\x18\x03 \x01(\x05\x12\x16\n\x0e\x62\x61se_bag_items\x18\x04 \x01(\x05\x12\x11\n\tbase_eggs\x18\x05 \x01(\x05\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_INVENTORYSETTINGS = _descriptor.Descriptor(
  name='InventorySettings',
  full_name='POGOProtos.Settings.InventorySettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='max_pokemon', full_name='POGOProtos.Settings.InventorySettings.max_pokemon', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_bag_items', full_name='POGOProtos.Settings.InventorySettings.max_bag_items', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='base_pokemon', full_name='POGOProtos.Settings.InventorySettings.base_pokemon', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='base_bag_items', full_name='POGOProtos.Settings.InventorySettings.base_bag_items', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='base_eggs', full_name='POGOProtos.Settings.InventorySettings.base_eggs', index=4,
      number=5, type=5, cpp_type=1, label=1,
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
  serialized_start=69,
  serialized_end=197,
)

DESCRIPTOR.message_types_by_name['InventorySettings'] = _INVENTORYSETTINGS

InventorySettings = _reflection.GeneratedProtocolMessageType('InventorySettings', (_message.Message,), dict(
  DESCRIPTOR = _INVENTORYSETTINGS,
  __module__ = 'POGOProtos.Settings.InventorySettings_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Settings.InventorySettings)
  ))
_sym_db.RegisterMessage(InventorySettings)


# @@protoc_insertion_point(module_scope)
