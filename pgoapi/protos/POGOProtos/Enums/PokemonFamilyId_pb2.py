# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: POGOProtos/Enums/PokemonFamilyId.proto

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
  name='POGOProtos/Enums/PokemonFamilyId.proto',
  package='POGOProtos.Enums',
  syntax='proto3',
  serialized_pb=_b('\n&POGOProtos/Enums/PokemonFamilyId.proto\x12\x10POGOProtos.Enums*\xfa\x0c\n\x0fPokemonFamilyId\x12\x10\n\x0c\x46\x41MILY_UNSET\x10\x00\x12\x14\n\x10\x46\x41MILY_BULBASAUR\x10\x01\x12\x15\n\x11\x46\x41MILY_CHARMANDER\x10\x04\x12\x13\n\x0f\x46\x41MILY_SQUIRTLE\x10\x07\x12\x13\n\x0f\x46\x41MILY_CATERPIE\x10\n\x12\x11\n\rFAMILY_WEEDLE\x10\r\x12\x11\n\rFAMILY_PIDGEY\x10\x10\x12\x12\n\x0e\x46\x41MILY_RATTATA\x10\x13\x12\x12\n\x0e\x46\x41MILY_SPEAROW\x10\x15\x12\x10\n\x0c\x46\x41MILY_EKANS\x10\x17\x12\x12\n\x0e\x46\x41MILY_PIKACHU\x10\x19\x12\x14\n\x10\x46\x41MILY_SANDSHREW\x10\x1b\x12\x19\n\x15\x46\x41MILY_NIDORAN_FEMALE\x10\x1d\x12\x17\n\x13\x46\x41MILY_NIDORAN_MALE\x10 \x12\x13\n\x0f\x46\x41MILY_CLEFAIRY\x10#\x12\x11\n\rFAMILY_VULPIX\x10%\x12\x15\n\x11\x46\x41MILY_JIGGLYPUFF\x10\'\x12\x10\n\x0c\x46\x41MILY_ZUBAT\x10)\x12\x11\n\rFAMILY_ODDISH\x10+\x12\x10\n\x0c\x46\x41MILY_PARAS\x10.\x12\x12\n\x0e\x46\x41MILY_VENONAT\x10\x30\x12\x12\n\x0e\x46\x41MILY_DIGLETT\x10\x32\x12\x11\n\rFAMILY_MEOWTH\x10\x34\x12\x12\n\x0e\x46\x41MILY_PSYDUCK\x10\x36\x12\x11\n\rFAMILY_MANKEY\x10\x38\x12\x14\n\x10\x46\x41MILY_GROWLITHE\x10:\x12\x12\n\x0e\x46\x41MILY_POLIWAG\x10<\x12\x0f\n\x0b\x46\x41MILY_ABRA\x10?\x12\x11\n\rFAMILY_MACHOP\x10\x42\x12\x15\n\x11\x46\x41MILY_BELLSPROUT\x10\x45\x12\x14\n\x10\x46\x41MILY_TENTACOOL\x10H\x12\x12\n\x0e\x46\x41MILY_GEODUDE\x10J\x12\x11\n\rFAMILY_PONYTA\x10M\x12\x13\n\x0f\x46\x41MILY_SLOWPOKE\x10O\x12\x14\n\x10\x46\x41MILY_MAGNEMITE\x10Q\x12\x14\n\x10\x46\x41MILY_FARFETCHD\x10S\x12\x10\n\x0c\x46\x41MILY_DODUO\x10T\x12\x0f\n\x0b\x46\x41MILY_SEEL\x10V\x12\x11\n\rFAMILY_GRIMER\x10X\x12\x13\n\x0f\x46\x41MILY_SHELLDER\x10Z\x12\x11\n\rFAMILY_GASTLY\x10\\\x12\x0f\n\x0b\x46\x41MILY_ONIX\x10_\x12\x12\n\x0e\x46\x41MILY_DROWZEE\x10`\x12\x10\n\x0c\x46\x41MILY_HYPNO\x10\x61\x12\x11\n\rFAMILY_KRABBY\x10\x62\x12\x12\n\x0e\x46\x41MILY_VOLTORB\x10\x64\x12\x14\n\x10\x46\x41MILY_EXEGGCUTE\x10\x66\x12\x11\n\rFAMILY_CUBONE\x10h\x12\x14\n\x10\x46\x41MILY_HITMONLEE\x10j\x12\x15\n\x11\x46\x41MILY_HITMONCHAN\x10k\x12\x14\n\x10\x46\x41MILY_LICKITUNG\x10l\x12\x12\n\x0e\x46\x41MILY_KOFFING\x10m\x12\x12\n\x0e\x46\x41MILY_RHYHORN\x10o\x12\x12\n\x0e\x46\x41MILY_CHANSEY\x10q\x12\x12\n\x0e\x46\x41MILY_TANGELA\x10r\x12\x15\n\x11\x46\x41MILY_KANGASKHAN\x10s\x12\x11\n\rFAMILY_HORSEA\x10t\x12\x12\n\x0e\x46\x41MILY_GOLDEEN\x10v\x12\x11\n\rFAMILY_STARYU\x10x\x12\x12\n\x0e\x46\x41MILY_MR_MIME\x10z\x12\x12\n\x0e\x46\x41MILY_SCYTHER\x10{\x12\x0f\n\x0b\x46\x41MILY_JYNX\x10|\x12\x15\n\x11\x46\x41MILY_ELECTABUZZ\x10}\x12\x11\n\rFAMILY_MAGMAR\x10~\x12\x11\n\rFAMILY_PINSIR\x10\x7f\x12\x12\n\rFAMILY_TAUROS\x10\x80\x01\x12\x14\n\x0f\x46\x41MILY_MAGIKARP\x10\x81\x01\x12\x12\n\rFAMILY_LAPRAS\x10\x83\x01\x12\x11\n\x0c\x46\x41MILY_DITTO\x10\x84\x01\x12\x11\n\x0c\x46\x41MILY_EEVEE\x10\x85\x01\x12\x13\n\x0e\x46\x41MILY_PORYGON\x10\x89\x01\x12\x13\n\x0e\x46\x41MILY_OMANYTE\x10\x8a\x01\x12\x12\n\rFAMILY_KABUTO\x10\x8c\x01\x12\x16\n\x11\x46\x41MILY_AERODACTYL\x10\x8e\x01\x12\x13\n\x0e\x46\x41MILY_SNORLAX\x10\x8f\x01\x12\x14\n\x0f\x46\x41MILY_ARTICUNO\x10\x90\x01\x12\x12\n\rFAMILY_ZAPDOS\x10\x91\x01\x12\x13\n\x0e\x46\x41MILY_MOLTRES\x10\x92\x01\x12\x13\n\x0e\x46\x41MILY_DRATINI\x10\x93\x01\x12\x12\n\rFAMILY_MEWTWO\x10\x96\x01\x12\x0f\n\nFAMILY_MEW\x10\x97\x01\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_POKEMONFAMILYID = _descriptor.EnumDescriptor(
  name='PokemonFamilyId',
  full_name='POGOProtos.Enums.PokemonFamilyId',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FAMILY_UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_BULBASAUR', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_CHARMANDER', index=2, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_SQUIRTLE', index=3, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_CATERPIE', index=4, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_WEEDLE', index=5, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_PIDGEY', index=6, number=16,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_RATTATA', index=7, number=19,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_SPEAROW', index=8, number=21,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_EKANS', index=9, number=23,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_PIKACHU', index=10, number=25,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_SANDSHREW', index=11, number=27,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_NIDORAN_FEMALE', index=12, number=29,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_NIDORAN_MALE', index=13, number=32,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_CLEFAIRY', index=14, number=35,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_VULPIX', index=15, number=37,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_JIGGLYPUFF', index=16, number=39,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_ZUBAT', index=17, number=41,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_ODDISH', index=18, number=43,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_PARAS', index=19, number=46,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_VENONAT', index=20, number=48,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_DIGLETT', index=21, number=50,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_MEOWTH', index=22, number=52,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_PSYDUCK', index=23, number=54,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_MANKEY', index=24, number=56,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_GROWLITHE', index=25, number=58,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_POLIWAG', index=26, number=60,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_ABRA', index=27, number=63,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_MACHOP', index=28, number=66,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_BELLSPROUT', index=29, number=69,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_TENTACOOL', index=30, number=72,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_GEODUDE', index=31, number=74,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_PONYTA', index=32, number=77,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_SLOWPOKE', index=33, number=79,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_MAGNEMITE', index=34, number=81,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_FARFETCHD', index=35, number=83,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_DODUO', index=36, number=84,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_SEEL', index=37, number=86,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_GRIMER', index=38, number=88,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_SHELLDER', index=39, number=90,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_GASTLY', index=40, number=92,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_ONIX', index=41, number=95,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_DROWZEE', index=42, number=96,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_HYPNO', index=43, number=97,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_KRABBY', index=44, number=98,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_VOLTORB', index=45, number=100,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_EXEGGCUTE', index=46, number=102,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_CUBONE', index=47, number=104,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_HITMONLEE', index=48, number=106,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_HITMONCHAN', index=49, number=107,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_LICKITUNG', index=50, number=108,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_KOFFING', index=51, number=109,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_RHYHORN', index=52, number=111,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_CHANSEY', index=53, number=113,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_TANGELA', index=54, number=114,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_KANGASKHAN', index=55, number=115,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_HORSEA', index=56, number=116,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_GOLDEEN', index=57, number=118,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_STARYU', index=58, number=120,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_MR_MIME', index=59, number=122,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_SCYTHER', index=60, number=123,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_JYNX', index=61, number=124,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_ELECTABUZZ', index=62, number=125,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_MAGMAR', index=63, number=126,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_PINSIR', index=64, number=127,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_TAUROS', index=65, number=128,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_MAGIKARP', index=66, number=129,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_LAPRAS', index=67, number=131,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_DITTO', index=68, number=132,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_EEVEE', index=69, number=133,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_PORYGON', index=70, number=137,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_OMANYTE', index=71, number=138,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_KABUTO', index=72, number=140,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_AERODACTYL', index=73, number=142,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_SNORLAX', index=74, number=143,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_ARTICUNO', index=75, number=144,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_ZAPDOS', index=76, number=145,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_MOLTRES', index=77, number=146,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_DRATINI', index=78, number=147,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_MEWTWO', index=79, number=150,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAMILY_MEW', index=80, number=151,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=61,
  serialized_end=1719,
)
_sym_db.RegisterEnumDescriptor(_POKEMONFAMILYID)

PokemonFamilyId = enum_type_wrapper.EnumTypeWrapper(_POKEMONFAMILYID)
FAMILY_UNSET = 0
FAMILY_BULBASAUR = 1
FAMILY_CHARMANDER = 4
FAMILY_SQUIRTLE = 7
FAMILY_CATERPIE = 10
FAMILY_WEEDLE = 13
FAMILY_PIDGEY = 16
FAMILY_RATTATA = 19
FAMILY_SPEAROW = 21
FAMILY_EKANS = 23
FAMILY_PIKACHU = 25
FAMILY_SANDSHREW = 27
FAMILY_NIDORAN_FEMALE = 29
FAMILY_NIDORAN_MALE = 32
FAMILY_CLEFAIRY = 35
FAMILY_VULPIX = 37
FAMILY_JIGGLYPUFF = 39
FAMILY_ZUBAT = 41
FAMILY_ODDISH = 43
FAMILY_PARAS = 46
FAMILY_VENONAT = 48
FAMILY_DIGLETT = 50
FAMILY_MEOWTH = 52
FAMILY_PSYDUCK = 54
FAMILY_MANKEY = 56
FAMILY_GROWLITHE = 58
FAMILY_POLIWAG = 60
FAMILY_ABRA = 63
FAMILY_MACHOP = 66
FAMILY_BELLSPROUT = 69
FAMILY_TENTACOOL = 72
FAMILY_GEODUDE = 74
FAMILY_PONYTA = 77
FAMILY_SLOWPOKE = 79
FAMILY_MAGNEMITE = 81
FAMILY_FARFETCHD = 83
FAMILY_DODUO = 84
FAMILY_SEEL = 86
FAMILY_GRIMER = 88
FAMILY_SHELLDER = 90
FAMILY_GASTLY = 92
FAMILY_ONIX = 95
FAMILY_DROWZEE = 96
FAMILY_HYPNO = 97
FAMILY_KRABBY = 98
FAMILY_VOLTORB = 100
FAMILY_EXEGGCUTE = 102
FAMILY_CUBONE = 104
FAMILY_HITMONLEE = 106
FAMILY_HITMONCHAN = 107
FAMILY_LICKITUNG = 108
FAMILY_KOFFING = 109
FAMILY_RHYHORN = 111
FAMILY_CHANSEY = 113
FAMILY_TANGELA = 114
FAMILY_KANGASKHAN = 115
FAMILY_HORSEA = 116
FAMILY_GOLDEEN = 118
FAMILY_STARYU = 120
FAMILY_MR_MIME = 122
FAMILY_SCYTHER = 123
FAMILY_JYNX = 124
FAMILY_ELECTABUZZ = 125
FAMILY_MAGMAR = 126
FAMILY_PINSIR = 127
FAMILY_TAUROS = 128
FAMILY_MAGIKARP = 129
FAMILY_LAPRAS = 131
FAMILY_DITTO = 132
FAMILY_EEVEE = 133
FAMILY_PORYGON = 137
FAMILY_OMANYTE = 138
FAMILY_KABUTO = 140
FAMILY_AERODACTYL = 142
FAMILY_SNORLAX = 143
FAMILY_ARTICUNO = 144
FAMILY_ZAPDOS = 145
FAMILY_MOLTRES = 146
FAMILY_DRATINI = 147
FAMILY_MEWTWO = 150
FAMILY_MEW = 151


DESCRIPTOR.enum_types_by_name['PokemonFamilyId'] = _POKEMONFAMILYID


# @@protoc_insertion_point(module_scope)
