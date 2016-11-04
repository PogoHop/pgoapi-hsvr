# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: POGOProtos/Inventory/InventoryUpgrade.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from POGOProtos.Inventory import InventoryUpgradeType_pb2 as POGOProtos_dot_Inventory_dot_InventoryUpgradeType__pb2
from POGOProtos.Inventory.Item import ItemId_pb2 as POGOProtos_dot_Inventory_dot_Item_dot_ItemId__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='POGOProtos/Inventory/InventoryUpgrade.proto',
  package='POGOProtos.Inventory',
  syntax='proto3',
  serialized_pb=_b('\n+POGOProtos/Inventory/InventoryUpgrade.proto\x12\x14POGOProtos.Inventory\x1a/POGOProtos/Inventory/InventoryUpgradeType.proto\x1a&POGOProtos/Inventory/Item/ItemId.proto\"\xa4\x01\n\x10InventoryUpgrade\x12\x32\n\x07item_id\x18\x01 \x01(\x0e\x32!.POGOProtos.Inventory.Item.ItemId\x12@\n\x0cupgrade_type\x18\x02 \x01(\x0e\x32*.POGOProtos.Inventory.InventoryUpgradeType\x12\x1a\n\x12\x61\x64\x64itional_storage\x18\x03 \x01(\x05\x62\x06proto3')
  ,
  dependencies=[POGOProtos_dot_Inventory_dot_InventoryUpgradeType__pb2.DESCRIPTOR,POGOProtos_dot_Inventory_dot_Item_dot_ItemId__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_INVENTORYUPGRADE = _descriptor.Descriptor(
  name='InventoryUpgrade',
  full_name='POGOProtos.Inventory.InventoryUpgrade',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item_id', full_name='POGOProtos.Inventory.InventoryUpgrade.item_id', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='upgrade_type', full_name='POGOProtos.Inventory.InventoryUpgrade.upgrade_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='additional_storage', full_name='POGOProtos.Inventory.InventoryUpgrade.additional_storage', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=159,
  serialized_end=323,
)

_INVENTORYUPGRADE.fields_by_name['item_id'].enum_type = POGOProtos_dot_Inventory_dot_Item_dot_ItemId__pb2._ITEMID
_INVENTORYUPGRADE.fields_by_name['upgrade_type'].enum_type = POGOProtos_dot_Inventory_dot_InventoryUpgradeType__pb2._INVENTORYUPGRADETYPE
DESCRIPTOR.message_types_by_name['InventoryUpgrade'] = _INVENTORYUPGRADE

InventoryUpgrade = _reflection.GeneratedProtocolMessageType('InventoryUpgrade', (_message.Message,), dict(
  DESCRIPTOR = _INVENTORYUPGRADE,
  __module__ = 'POGOProtos.Inventory.InventoryUpgrade_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Inventory.InventoryUpgrade)
  ))
_sym_db.RegisterMessage(InventoryUpgrade)


# @@protoc_insertion_point(module_scope)
