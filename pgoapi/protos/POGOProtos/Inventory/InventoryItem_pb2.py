# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: POGOProtos/Inventory/InventoryItem.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from POGOProtos.Inventory import InventoryItemData_pb2 as POGOProtos_dot_Inventory_dot_InventoryItemData__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='POGOProtos/Inventory/InventoryItem.proto',
  package='POGOProtos.Inventory',
  syntax='proto3',
  serialized_pb=_b('\n(POGOProtos/Inventory/InventoryItem.proto\x12\x14POGOProtos.Inventory\x1a,POGOProtos/Inventory/InventoryItemData.proto\"\xde\x01\n\rInventoryItem\x12\x1d\n\x15modified_timestamp_ms\x18\x01 \x01(\x03\x12\x45\n\x0c\x64\x65leted_item\x18\x02 \x01(\x0b\x32/.POGOProtos.Inventory.InventoryItem.DeletedItem\x12\x44\n\x13inventory_item_data\x18\x03 \x01(\x0b\x32\'.POGOProtos.Inventory.InventoryItemData\x1a!\n\x0b\x44\x65letedItem\x12\x12\n\npokemon_id\x18\x01 \x01(\x06\x62\x06proto3')
  ,
  dependencies=[POGOProtos_dot_Inventory_dot_InventoryItemData__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_INVENTORYITEM_DELETEDITEM = _descriptor.Descriptor(
  name='DeletedItem',
  full_name='POGOProtos.Inventory.InventoryItem.DeletedItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pokemon_id', full_name='POGOProtos.Inventory.InventoryItem.DeletedItem.pokemon_id', index=0,
      number=1, type=6, cpp_type=4, label=1,
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
  serialized_start=302,
  serialized_end=335,
)

_INVENTORYITEM = _descriptor.Descriptor(
  name='InventoryItem',
  full_name='POGOProtos.Inventory.InventoryItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='modified_timestamp_ms', full_name='POGOProtos.Inventory.InventoryItem.modified_timestamp_ms', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='deleted_item', full_name='POGOProtos.Inventory.InventoryItem.deleted_item', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inventory_item_data', full_name='POGOProtos.Inventory.InventoryItem.inventory_item_data', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_INVENTORYITEM_DELETEDITEM, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=113,
  serialized_end=335,
)

_INVENTORYITEM_DELETEDITEM.containing_type = _INVENTORYITEM
_INVENTORYITEM.fields_by_name['deleted_item'].message_type = _INVENTORYITEM_DELETEDITEM
_INVENTORYITEM.fields_by_name['inventory_item_data'].message_type = POGOProtos_dot_Inventory_dot_InventoryItemData__pb2._INVENTORYITEMDATA
DESCRIPTOR.message_types_by_name['InventoryItem'] = _INVENTORYITEM

InventoryItem = _reflection.GeneratedProtocolMessageType('InventoryItem', (_message.Message,), dict(

  DeletedItem = _reflection.GeneratedProtocolMessageType('DeletedItem', (_message.Message,), dict(
    DESCRIPTOR = _INVENTORYITEM_DELETEDITEM,
    __module__ = 'POGOProtos.Inventory.InventoryItem_pb2'
    # @@protoc_insertion_point(class_scope:POGOProtos.Inventory.InventoryItem.DeletedItem)
    ))
  ,
  DESCRIPTOR = _INVENTORYITEM,
  __module__ = 'POGOProtos.Inventory.InventoryItem_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Inventory.InventoryItem)
  ))
_sym_db.RegisterMessage(InventoryItem)
_sym_db.RegisterMessage(InventoryItem.DeletedItem)


# @@protoc_insertion_point(module_scope)
