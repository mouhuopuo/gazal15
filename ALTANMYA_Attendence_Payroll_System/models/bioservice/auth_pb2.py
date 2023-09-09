# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: auth.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import err_pb2 as err__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='auth.proto',
  package='auth',
  syntax='proto3',
  serialized_options=_b('\n\027com.supremainc.sdk.authP\001Z\024biostar/service/auth'),
  serialized_pb=_b('\n\nauth.proto\x12\x04\x61uth\x1a\terr.proto\">\n\x08Operator\x12\x0e\n\x06userID\x18\x01 \x01(\t\x12\"\n\x05level\x18\x02 \x01(\x0e\x32\x13.auth.OperatorLevel\"@\n\x0c\x41uthSchedule\x12\x1c\n\x04mode\x18\x01 \x01(\x0e\x32\x0e.auth.AuthMode\x12\x12\n\nscheduleID\x18\x02 \x01(\r\"\xf1\x02\n\nAuthConfig\x12)\n\rauthSchedules\x18\x01 \x03(\x0b\x32\x12.auth.AuthSchedule\x12\x14\n\x0cuseGlobalAPB\x18\x02 \x01(\x08\x12:\n\x13globalAPBFailAction\x18\x03 \x01(\x0e\x32\x1d.auth.GlobalAPBFailActionType\x12\x18\n\x10useGroupMatching\x18\x04 \x01(\x08\x12\x16\n\x0eusePrivateAuth\x18\x05 \x01(\x08\x12\x34\n\x12\x66\x61\x63\x65\x44\x65tectionLevel\x18\x06 \x01(\x0e\x32\x18.auth.FaceDetectionLevel\x12\x19\n\x11useServerMatching\x18\x07 \x01(\x08\x12\x15\n\ruseFullAccess\x18\x08 \x01(\x08\x12\x14\n\x0cmatchTimeout\x18\t \x01(\r\x12\x13\n\x0b\x61uthTimeout\x18\n \x01(\r\x12!\n\toperators\x18\x0b \x03(\x0b\x32\x0e.auth.Operator\"$\n\x10GetConfigRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\"5\n\x11GetConfigResponse\x12 \n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x10.auth.AuthConfig\"F\n\x10SetConfigRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12 \n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x10.auth.AuthConfig\"\x13\n\x11SetConfigResponse\"L\n\x15SetConfigMultiRequest\x12\x11\n\tdeviceIDs\x18\x01 \x03(\r\x12 \n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x10.auth.AuthConfig\"B\n\x16SetConfigMultiResponse\x12(\n\x0c\x64\x65viceErrors\x18\x01 \x03(\x0b\x32\x12.err.ErrorResponse*\xdb\x0e\n\x08\x41uthMode\x12\x1c\n\x18\x41UTH_MODE_BIOMETRIC_ONLY\x10\x00\x12\x1b\n\x17\x41UTH_MODE_BIOMETRIC_PIN\x10\x01\x12\x17\n\x13\x41UTH_MODE_CARD_ONLY\x10\x02\x12\x1c\n\x18\x41UTH_MODE_CARD_BIOMETRIC\x10\x03\x12\x16\n\x12\x41UTH_MODE_CARD_PIN\x10\x04\x12#\n\x1f\x41UTH_MODE_CARD_BIOMETRIC_OR_PIN\x10\x05\x12 \n\x1c\x41UTH_MODE_CARD_BIOMETRIC_PIN\x10\x06\x12\x1a\n\x16\x41UTH_MODE_ID_BIOMETRIC\x10\x07\x12\x14\n\x10\x41UTH_MODE_ID_PIN\x10\x08\x12!\n\x1d\x41UTH_MODE_ID_BIOMETRIC_OR_PIN\x10\t\x12\x1e\n\x1a\x41UTH_MODE_ID_BIOMETRIC_PIN\x10\n\x12\x13\n\x0e\x41UTH_MODE_NONE\x10\xff\x01\x12\x19\n\x14\x41UTH_MODE_PROHIBITED\x10\xfe\x01\x12\x1b\n\x17\x41UTH_EXT_MODE_FACE_ONLY\x10\x0b\x12\"\n\x1e\x41UTH_EXT_MODE_FACE_FINGERPRINT\x10\x0c\x12\x1a\n\x16\x41UTH_EXT_MODE_FACE_PIN\x10\r\x12)\n%AUTH_EXT_MODE_FACE_FINGERPRINT_OR_PIN\x10\x0e\x12&\n\"AUTH_EXT_MODE_FACE_FINGERPRINT_PIN\x10\x0f\x12\"\n\x1e\x41UTH_EXT_MODE_FINGERPRINT_ONLY\x10\x10\x12\"\n\x1e\x41UTH_EXT_MODE_FINGERPRINT_FACE\x10\x11\x12!\n\x1d\x41UTH_EXT_MODE_FINGERPRINT_PIN\x10\x12\x12)\n%AUTH_EXT_MODE_FINGERPRINT_FACE_OR_PIN\x10\x13\x12&\n\"AUTH_EXT_MODE_FINGERPRINT_FACE_PIN\x10\x14\x12\x1b\n\x17\x41UTH_EXT_MODE_CARD_ONLY\x10\x15\x12\x1b\n\x17\x41UTH_EXT_MODE_CARD_FACE\x10\x16\x12\"\n\x1e\x41UTH_EXT_MODE_CARD_FINGERPRINT\x10\x17\x12\x1a\n\x16\x41UTH_EXT_MODE_CARD_PIN\x10\x18\x12*\n&AUTH_EXT_MODE_CARD_FACE_OR_FINGERPRINT\x10\x19\x12\"\n\x1e\x41UTH_EXT_MODE_CARD_FACE_OR_PIN\x10\x1a\x12)\n%AUTH_EXT_MODE_CARD_FINGERPRINT_OR_PIN\x10\x1b\x12\x31\n-AUTH_EXT_MODE_CARD_FACE_OR_FINGERPRINT_OR_PIN\x10\x1c\x12\'\n#AUTH_EXT_MODE_CARD_FACE_FINGERPRINT\x10\x1d\x12\x1f\n\x1b\x41UTH_EXT_MODE_CARD_FACE_PIN\x10\x1e\x12\'\n#AUTH_EXT_MODE_CARD_FINGERPRINT_FACE\x10\x1f\x12&\n\"AUTH_EXT_MODE_CARD_FINGERPRINT_PIN\x10 \x12.\n*AUTH_EXT_MODE_CARD_FACE_OR_FINGERPRINT_PIN\x10!\x12.\n*AUTH_EXT_MODE_CARD_FACE_FINGERPRINT_OR_PIN\x10\"\x12.\n*AUTH_EXT_MODE_CARD_FINGERPRINT_FACE_OR_PIN\x10#\x12\x19\n\x15\x41UTH_EXT_MODE_ID_FACE\x10$\x12 \n\x1c\x41UTH_EXT_MODE_ID_FINGERPRINT\x10%\x12\x18\n\x14\x41UTH_EXT_MODE_ID_PIN\x10&\x12(\n$AUTH_EXT_MODE_ID_FACE_OR_FINGERPRINT\x10\'\x12 \n\x1c\x41UTH_EXT_MODE_ID_FACE_OR_PIN\x10(\x12\'\n#AUTH_EXT_MODE_ID_FINGERPRINT_OR_PIN\x10)\x12/\n+AUTH_EXT_MODE_ID_FACE_OR_FINGERPRINT_OR_PIN\x10*\x12%\n!AUTH_EXT_MODE_ID_FACE_FINGERPRINT\x10+\x12\x1d\n\x19\x41UTH_EXT_MODE_ID_FACE_PIN\x10,\x12%\n!AUTH_EXT_MODE_ID_FINGERPRINT_FACE\x10-\x12$\n AUTH_EXT_MODE_ID_FINGERPRINT_PIN\x10.\x12,\n(AUTH_EXT_MODE_ID_FACE_OR_FINGERPRINT_PIN\x10/\x12,\n(AUTH_EXT_MODE_ID_FACE_FINGERPRINT_OR_PIN\x10\x30\x12,\n(AUTH_EXT_MODE_ID_FINGERPRINT_FACE_OR_PIN\x10\x31*v\n\rOperatorLevel\x12\x17\n\x13OPERATOR_LEVEL_NONE\x10\x00\x12\x18\n\x14OPERATOR_LEVEL_ADMIN\x10\x01\x12\x19\n\x15OPERATOR_LEVEL_CONFIG\x10\x02\x12\x17\n\x13OPERATOR_LEVEL_USER\x10\x03*c\n\x12\x46\x61\x63\x65\x44\x65tectionLevel\x12\x17\n\x13\x46\x41\x43\x45_DETECTION_NONE\x10\x00\x12\x19\n\x15\x46\x41\x43\x45_DETECTION_NORMAL\x10\x01\x12\x19\n\x15\x46\x41\x43\x45_DETECTION_STRICT\x10\x02*|\n\x17GlobalAPBFailActionType\x12\x1f\n\x1bGLOBAL_APB_FAIL_ACTION_NONE\x10\x00\x12\x1f\n\x1bGLOBAL_APB_FAIL_ACTION_SOFT\x10\x01\x12\x1f\n\x1bGLOBAL_APB_FAIL_ACTION_HARD\x10\x02\x32\xcf\x01\n\x04\x41uth\x12<\n\tGetConfig\x12\x16.auth.GetConfigRequest\x1a\x17.auth.GetConfigResponse\x12<\n\tSetConfig\x12\x16.auth.SetConfigRequest\x1a\x17.auth.SetConfigResponse\x12K\n\x0eSetConfigMulti\x12\x1b.auth.SetConfigMultiRequest\x1a\x1c.auth.SetConfigMultiResponseB1\n\x17\x63om.supremainc.sdk.authP\x01Z\x14\x62iostar/service/authb\x06proto3')
  ,
  dependencies=[err__pb2.DESCRIPTOR,])

_AUTHMODE = _descriptor.EnumDescriptor(
  name='AuthMode',
  full_name='auth.AuthMode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='AUTH_MODE_BIOMETRIC_ONLY', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTH_MODE_BIOMETRIC_PIN', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTH_MODE_CARD_ONLY', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTH_MODE_CARD_BIOMETRIC', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTH_MODE_CARD_PIN', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTH_MODE_CARD_BIOMETRIC_OR_PIN', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTH_MODE_CARD_BIOMETRIC_PIN', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTH_MODE_ID_BIOMETRIC', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTH_MODE_ID_PIN', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTH_MODE_ID_BIOMETRIC_OR_PIN', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTH_MODE_ID_BIOMETRIC_PIN', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTH_MODE_NONE', index=11, number=255,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTH_MODE_PROHIBITED', index=12, number=254,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTH_EXT_MODE_FACE_ONLY', index=13, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTH_EXT_MODE_FACE_FINGERPRINT', index=14, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTH_EXT_MODE_FACE_PIN', index=15, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTH_EXT_MODE_FACE_FINGERPRINT_OR_PIN', index=16, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTH_EXT_MODE_FACE_FINGERPRINT_PIN', index=17, number=15,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTH_EXT_MODE_FINGERPRINT_ONLY', index=18, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTH_EXT_MODE_FINGERPRINT_FACE', index=19, number=17,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTH_EXT_MODE_FINGERPRINT_PIN', index=20, number=18,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTH_EXT_MODE_FINGERPRINT_FACE_OR_PIN', index=21, number=19,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTH_EXT_MODE_FINGERPRINT_FACE_PIN', index=22, number=20,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTH_EXT_MODE_CARD_ONLY', index=23, number=21,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTH_EXT_MODE_CARD_FACE', index=24, number=22,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTH_EXT_MODE_CARD_FINGERPRINT', index=25, number=23,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTH_EXT_MODE_CARD_PIN', index=26, number=24,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTH_EXT_MODE_CARD_FACE_OR_FINGERPRINT', index=27, number=25,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTH_EXT_MODE_CARD_FACE_OR_PIN', index=28, number=26,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTH_EXT_MODE_CARD_FINGERPRINT_OR_PIN', index=29, number=27,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTH_EXT_MODE_CARD_FACE_OR_FINGERPRINT_OR_PIN', index=30, number=28,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTH_EXT_MODE_CARD_FACE_FINGERPRINT', index=31, number=29,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTH_EXT_MODE_CARD_FACE_PIN', index=32, number=30,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTH_EXT_MODE_CARD_FINGERPRINT_FACE', index=33, number=31,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTH_EXT_MODE_CARD_FINGERPRINT_PIN', index=34, number=32,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTH_EXT_MODE_CARD_FACE_OR_FINGERPRINT_PIN', index=35, number=33,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTH_EXT_MODE_CARD_FACE_FINGERPRINT_OR_PIN', index=36, number=34,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTH_EXT_MODE_CARD_FINGERPRINT_FACE_OR_PIN', index=37, number=35,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTH_EXT_MODE_ID_FACE', index=38, number=36,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTH_EXT_MODE_ID_FINGERPRINT', index=39, number=37,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTH_EXT_MODE_ID_PIN', index=40, number=38,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTH_EXT_MODE_ID_FACE_OR_FINGERPRINT', index=41, number=39,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTH_EXT_MODE_ID_FACE_OR_PIN', index=42, number=40,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTH_EXT_MODE_ID_FINGERPRINT_OR_PIN', index=43, number=41,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTH_EXT_MODE_ID_FACE_OR_FINGERPRINT_OR_PIN', index=44, number=42,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTH_EXT_MODE_ID_FACE_FINGERPRINT', index=45, number=43,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTH_EXT_MODE_ID_FACE_PIN', index=46, number=44,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTH_EXT_MODE_ID_FINGERPRINT_FACE', index=47, number=45,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTH_EXT_MODE_ID_FINGERPRINT_PIN', index=48, number=46,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTH_EXT_MODE_ID_FACE_OR_FINGERPRINT_PIN', index=49, number=47,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTH_EXT_MODE_ID_FACE_FINGERPRINT_OR_PIN', index=50, number=48,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTH_EXT_MODE_ID_FINGERPRINT_FACE_OR_PIN', index=51, number=49,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=866,
  serialized_end=2749,
)
_sym_db.RegisterEnumDescriptor(_AUTHMODE)

AuthMode = enum_type_wrapper.EnumTypeWrapper(_AUTHMODE)
_OPERATORLEVEL = _descriptor.EnumDescriptor(
  name='OperatorLevel',
  full_name='auth.OperatorLevel',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OPERATOR_LEVEL_NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPERATOR_LEVEL_ADMIN', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPERATOR_LEVEL_CONFIG', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPERATOR_LEVEL_USER', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2751,
  serialized_end=2869,
)
_sym_db.RegisterEnumDescriptor(_OPERATORLEVEL)

OperatorLevel = enum_type_wrapper.EnumTypeWrapper(_OPERATORLEVEL)
_FACEDETECTIONLEVEL = _descriptor.EnumDescriptor(
  name='FaceDetectionLevel',
  full_name='auth.FaceDetectionLevel',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FACE_DETECTION_NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FACE_DETECTION_NORMAL', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FACE_DETECTION_STRICT', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2871,
  serialized_end=2970,
)
_sym_db.RegisterEnumDescriptor(_FACEDETECTIONLEVEL)

FaceDetectionLevel = enum_type_wrapper.EnumTypeWrapper(_FACEDETECTIONLEVEL)
_GLOBALAPBFAILACTIONTYPE = _descriptor.EnumDescriptor(
  name='GlobalAPBFailActionType',
  full_name='auth.GlobalAPBFailActionType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='GLOBAL_APB_FAIL_ACTION_NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GLOBAL_APB_FAIL_ACTION_SOFT', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GLOBAL_APB_FAIL_ACTION_HARD', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2972,
  serialized_end=3096,
)
_sym_db.RegisterEnumDescriptor(_GLOBALAPBFAILACTIONTYPE)

GlobalAPBFailActionType = enum_type_wrapper.EnumTypeWrapper(_GLOBALAPBFAILACTIONTYPE)
AUTH_MODE_BIOMETRIC_ONLY = 0
AUTH_MODE_BIOMETRIC_PIN = 1
AUTH_MODE_CARD_ONLY = 2
AUTH_MODE_CARD_BIOMETRIC = 3
AUTH_MODE_CARD_PIN = 4
AUTH_MODE_CARD_BIOMETRIC_OR_PIN = 5
AUTH_MODE_CARD_BIOMETRIC_PIN = 6
AUTH_MODE_ID_BIOMETRIC = 7
AUTH_MODE_ID_PIN = 8
AUTH_MODE_ID_BIOMETRIC_OR_PIN = 9
AUTH_MODE_ID_BIOMETRIC_PIN = 10
AUTH_MODE_NONE = 255
AUTH_MODE_PROHIBITED = 254
AUTH_EXT_MODE_FACE_ONLY = 11
AUTH_EXT_MODE_FACE_FINGERPRINT = 12
AUTH_EXT_MODE_FACE_PIN = 13
AUTH_EXT_MODE_FACE_FINGERPRINT_OR_PIN = 14
AUTH_EXT_MODE_FACE_FINGERPRINT_PIN = 15
AUTH_EXT_MODE_FINGERPRINT_ONLY = 16
AUTH_EXT_MODE_FINGERPRINT_FACE = 17
AUTH_EXT_MODE_FINGERPRINT_PIN = 18
AUTH_EXT_MODE_FINGERPRINT_FACE_OR_PIN = 19
AUTH_EXT_MODE_FINGERPRINT_FACE_PIN = 20
AUTH_EXT_MODE_CARD_ONLY = 21
AUTH_EXT_MODE_CARD_FACE = 22
AUTH_EXT_MODE_CARD_FINGERPRINT = 23
AUTH_EXT_MODE_CARD_PIN = 24
AUTH_EXT_MODE_CARD_FACE_OR_FINGERPRINT = 25
AUTH_EXT_MODE_CARD_FACE_OR_PIN = 26
AUTH_EXT_MODE_CARD_FINGERPRINT_OR_PIN = 27
AUTH_EXT_MODE_CARD_FACE_OR_FINGERPRINT_OR_PIN = 28
AUTH_EXT_MODE_CARD_FACE_FINGERPRINT = 29
AUTH_EXT_MODE_CARD_FACE_PIN = 30
AUTH_EXT_MODE_CARD_FINGERPRINT_FACE = 31
AUTH_EXT_MODE_CARD_FINGERPRINT_PIN = 32
AUTH_EXT_MODE_CARD_FACE_OR_FINGERPRINT_PIN = 33
AUTH_EXT_MODE_CARD_FACE_FINGERPRINT_OR_PIN = 34
AUTH_EXT_MODE_CARD_FINGERPRINT_FACE_OR_PIN = 35
AUTH_EXT_MODE_ID_FACE = 36
AUTH_EXT_MODE_ID_FINGERPRINT = 37
AUTH_EXT_MODE_ID_PIN = 38
AUTH_EXT_MODE_ID_FACE_OR_FINGERPRINT = 39
AUTH_EXT_MODE_ID_FACE_OR_PIN = 40
AUTH_EXT_MODE_ID_FINGERPRINT_OR_PIN = 41
AUTH_EXT_MODE_ID_FACE_OR_FINGERPRINT_OR_PIN = 42
AUTH_EXT_MODE_ID_FACE_FINGERPRINT = 43
AUTH_EXT_MODE_ID_FACE_PIN = 44
AUTH_EXT_MODE_ID_FINGERPRINT_FACE = 45
AUTH_EXT_MODE_ID_FINGERPRINT_PIN = 46
AUTH_EXT_MODE_ID_FACE_OR_FINGERPRINT_PIN = 47
AUTH_EXT_MODE_ID_FACE_FINGERPRINT_OR_PIN = 48
AUTH_EXT_MODE_ID_FINGERPRINT_FACE_OR_PIN = 49
OPERATOR_LEVEL_NONE = 0
OPERATOR_LEVEL_ADMIN = 1
OPERATOR_LEVEL_CONFIG = 2
OPERATOR_LEVEL_USER = 3
FACE_DETECTION_NONE = 0
FACE_DETECTION_NORMAL = 1
FACE_DETECTION_STRICT = 2
GLOBAL_APB_FAIL_ACTION_NONE = 0
GLOBAL_APB_FAIL_ACTION_SOFT = 1
GLOBAL_APB_FAIL_ACTION_HARD = 2



_OPERATOR = _descriptor.Descriptor(
  name='Operator',
  full_name='auth.Operator',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='userID', full_name='auth.Operator.userID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='level', full_name='auth.Operator.level', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=31,
  serialized_end=93,
)


_AUTHSCHEDULE = _descriptor.Descriptor(
  name='AuthSchedule',
  full_name='auth.AuthSchedule',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mode', full_name='auth.AuthSchedule.mode', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scheduleID', full_name='auth.AuthSchedule.scheduleID', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=95,
  serialized_end=159,
)


_AUTHCONFIG = _descriptor.Descriptor(
  name='AuthConfig',
  full_name='auth.AuthConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='authSchedules', full_name='auth.AuthConfig.authSchedules', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='useGlobalAPB', full_name='auth.AuthConfig.useGlobalAPB', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='globalAPBFailAction', full_name='auth.AuthConfig.globalAPBFailAction', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='useGroupMatching', full_name='auth.AuthConfig.useGroupMatching', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='usePrivateAuth', full_name='auth.AuthConfig.usePrivateAuth', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='faceDetectionLevel', full_name='auth.AuthConfig.faceDetectionLevel', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='useServerMatching', full_name='auth.AuthConfig.useServerMatching', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='useFullAccess', full_name='auth.AuthConfig.useFullAccess', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='matchTimeout', full_name='auth.AuthConfig.matchTimeout', index=8,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='authTimeout', full_name='auth.AuthConfig.authTimeout', index=9,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operators', full_name='auth.AuthConfig.operators', index=10,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=162,
  serialized_end=531,
)


_GETCONFIGREQUEST = _descriptor.Descriptor(
  name='GetConfigRequest',
  full_name='auth.GetConfigRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='deviceID', full_name='auth.GetConfigRequest.deviceID', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=533,
  serialized_end=569,
)


_GETCONFIGRESPONSE = _descriptor.Descriptor(
  name='GetConfigResponse',
  full_name='auth.GetConfigResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='config', full_name='auth.GetConfigResponse.config', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=571,
  serialized_end=624,
)


_SETCONFIGREQUEST = _descriptor.Descriptor(
  name='SetConfigRequest',
  full_name='auth.SetConfigRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='deviceID', full_name='auth.SetConfigRequest.deviceID', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='config', full_name='auth.SetConfigRequest.config', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=626,
  serialized_end=696,
)


_SETCONFIGRESPONSE = _descriptor.Descriptor(
  name='SetConfigResponse',
  full_name='auth.SetConfigResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=698,
  serialized_end=717,
)


_SETCONFIGMULTIREQUEST = _descriptor.Descriptor(
  name='SetConfigMultiRequest',
  full_name='auth.SetConfigMultiRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='deviceIDs', full_name='auth.SetConfigMultiRequest.deviceIDs', index=0,
      number=1, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='config', full_name='auth.SetConfigMultiRequest.config', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=719,
  serialized_end=795,
)


_SETCONFIGMULTIRESPONSE = _descriptor.Descriptor(
  name='SetConfigMultiResponse',
  full_name='auth.SetConfigMultiResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='deviceErrors', full_name='auth.SetConfigMultiResponse.deviceErrors', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=797,
  serialized_end=863,
)

_OPERATOR.fields_by_name['level'].enum_type = _OPERATORLEVEL
_AUTHSCHEDULE.fields_by_name['mode'].enum_type = _AUTHMODE
_AUTHCONFIG.fields_by_name['authSchedules'].message_type = _AUTHSCHEDULE
_AUTHCONFIG.fields_by_name['globalAPBFailAction'].enum_type = _GLOBALAPBFAILACTIONTYPE
_AUTHCONFIG.fields_by_name['faceDetectionLevel'].enum_type = _FACEDETECTIONLEVEL
_AUTHCONFIG.fields_by_name['operators'].message_type = _OPERATOR
_GETCONFIGRESPONSE.fields_by_name['config'].message_type = _AUTHCONFIG
_SETCONFIGREQUEST.fields_by_name['config'].message_type = _AUTHCONFIG
_SETCONFIGMULTIREQUEST.fields_by_name['config'].message_type = _AUTHCONFIG
_SETCONFIGMULTIRESPONSE.fields_by_name['deviceErrors'].message_type = err__pb2._ERRORRESPONSE
DESCRIPTOR.message_types_by_name['Operator'] = _OPERATOR
DESCRIPTOR.message_types_by_name['AuthSchedule'] = _AUTHSCHEDULE
DESCRIPTOR.message_types_by_name['AuthConfig'] = _AUTHCONFIG
DESCRIPTOR.message_types_by_name['GetConfigRequest'] = _GETCONFIGREQUEST
DESCRIPTOR.message_types_by_name['GetConfigResponse'] = _GETCONFIGRESPONSE
DESCRIPTOR.message_types_by_name['SetConfigRequest'] = _SETCONFIGREQUEST
DESCRIPTOR.message_types_by_name['SetConfigResponse'] = _SETCONFIGRESPONSE
DESCRIPTOR.message_types_by_name['SetConfigMultiRequest'] = _SETCONFIGMULTIREQUEST
DESCRIPTOR.message_types_by_name['SetConfigMultiResponse'] = _SETCONFIGMULTIRESPONSE
DESCRIPTOR.enum_types_by_name['AuthMode'] = _AUTHMODE
DESCRIPTOR.enum_types_by_name['OperatorLevel'] = _OPERATORLEVEL
DESCRIPTOR.enum_types_by_name['FaceDetectionLevel'] = _FACEDETECTIONLEVEL
DESCRIPTOR.enum_types_by_name['GlobalAPBFailActionType'] = _GLOBALAPBFAILACTIONTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Operator = _reflection.GeneratedProtocolMessageType('Operator', (_message.Message,), dict(
  DESCRIPTOR = _OPERATOR,
  __module__ = 'auth_pb2'
  # @@protoc_insertion_point(class_scope:auth.Operator)
  ))
_sym_db.RegisterMessage(Operator)

AuthSchedule = _reflection.GeneratedProtocolMessageType('AuthSchedule', (_message.Message,), dict(
  DESCRIPTOR = _AUTHSCHEDULE,
  __module__ = 'auth_pb2'
  # @@protoc_insertion_point(class_scope:auth.AuthSchedule)
  ))
_sym_db.RegisterMessage(AuthSchedule)

AuthConfig = _reflection.GeneratedProtocolMessageType('AuthConfig', (_message.Message,), dict(
  DESCRIPTOR = _AUTHCONFIG,
  __module__ = 'auth_pb2'
  # @@protoc_insertion_point(class_scope:auth.AuthConfig)
  ))
_sym_db.RegisterMessage(AuthConfig)

GetConfigRequest = _reflection.GeneratedProtocolMessageType('GetConfigRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETCONFIGREQUEST,
  __module__ = 'auth_pb2'
  # @@protoc_insertion_point(class_scope:auth.GetConfigRequest)
  ))
_sym_db.RegisterMessage(GetConfigRequest)

GetConfigResponse = _reflection.GeneratedProtocolMessageType('GetConfigResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETCONFIGRESPONSE,
  __module__ = 'auth_pb2'
  # @@protoc_insertion_point(class_scope:auth.GetConfigResponse)
  ))
_sym_db.RegisterMessage(GetConfigResponse)

SetConfigRequest = _reflection.GeneratedProtocolMessageType('SetConfigRequest', (_message.Message,), dict(
  DESCRIPTOR = _SETCONFIGREQUEST,
  __module__ = 'auth_pb2'
  # @@protoc_insertion_point(class_scope:auth.SetConfigRequest)
  ))
_sym_db.RegisterMessage(SetConfigRequest)

SetConfigResponse = _reflection.GeneratedProtocolMessageType('SetConfigResponse', (_message.Message,), dict(
  DESCRIPTOR = _SETCONFIGRESPONSE,
  __module__ = 'auth_pb2'
  # @@protoc_insertion_point(class_scope:auth.SetConfigResponse)
  ))
_sym_db.RegisterMessage(SetConfigResponse)

SetConfigMultiRequest = _reflection.GeneratedProtocolMessageType('SetConfigMultiRequest', (_message.Message,), dict(
  DESCRIPTOR = _SETCONFIGMULTIREQUEST,
  __module__ = 'auth_pb2'
  # @@protoc_insertion_point(class_scope:auth.SetConfigMultiRequest)
  ))
_sym_db.RegisterMessage(SetConfigMultiRequest)

SetConfigMultiResponse = _reflection.GeneratedProtocolMessageType('SetConfigMultiResponse', (_message.Message,), dict(
  DESCRIPTOR = _SETCONFIGMULTIRESPONSE,
  __module__ = 'auth_pb2'
  # @@protoc_insertion_point(class_scope:auth.SetConfigMultiResponse)
  ))
_sym_db.RegisterMessage(SetConfigMultiResponse)


DESCRIPTOR._options = None

_AUTH = _descriptor.ServiceDescriptor(
  name='Auth',
  full_name='auth.Auth',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=3099,
  serialized_end=3306,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetConfig',
    full_name='auth.Auth.GetConfig',
    index=0,
    containing_service=None,
    input_type=_GETCONFIGREQUEST,
    output_type=_GETCONFIGRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SetConfig',
    full_name='auth.Auth.SetConfig',
    index=1,
    containing_service=None,
    input_type=_SETCONFIGREQUEST,
    output_type=_SETCONFIGRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SetConfigMulti',
    full_name='auth.Auth.SetConfigMulti',
    index=2,
    containing_service=None,
    input_type=_SETCONFIGMULTIREQUEST,
    output_type=_SETCONFIGMULTIRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_AUTH)

DESCRIPTOR.services_by_name['Auth'] = _AUTH

# @@protoc_insertion_point(module_scope)