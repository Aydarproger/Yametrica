# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: game.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ngame.proto\x12\x04game\"\x1f\n\x0c\x42\x61seResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x1e\n\rRatingRequest\x12\r\n\x05limit\x18\x01 \x01(\r\"K\n\x0eRatingResponse\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x10\n\x08username\x18\x02 \x01(\t\x12\r\n\x05score\x18\x03 \x01(\r\x12\x0c\n\x04rank\x18\x04 \x01(\r\"$\n\x13UpdateRatingRequest\x12\r\n\x05score\x18\x01 \x01(\r\"\x1d\n\x0cLevelRequest\x12\r\n\x05level\x18\x01 \x01(\r\"\x1f\n\rLevelResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\x32\xbb\x01\n\x04Game\x12:\n\tGetRating\x12\x13.game.RatingRequest\x1a\x14.game.RatingResponse\"\x00\x30\x01\x12?\n\x0cUpdateRating\x12\x19.game.UpdateRatingRequest\x1a\x12.game.BaseResponse\"\x00\x12\x36\n\tOpenLevel\x12\x12.game.LevelRequest\x1a\x13.game.LevelResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'game_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_BASERESPONSE']._serialized_start=20
  _globals['_BASERESPONSE']._serialized_end=51
  _globals['_RATINGREQUEST']._serialized_start=53
  _globals['_RATINGREQUEST']._serialized_end=83
  _globals['_RATINGRESPONSE']._serialized_start=85
  _globals['_RATINGRESPONSE']._serialized_end=160
  _globals['_UPDATERATINGREQUEST']._serialized_start=162
  _globals['_UPDATERATINGREQUEST']._serialized_end=198
  _globals['_LEVELREQUEST']._serialized_start=200
  _globals['_LEVELREQUEST']._serialized_end=229
  _globals['_LEVELRESPONSE']._serialized_start=231
  _globals['_LEVELRESPONSE']._serialized_end=262
  _globals['_GAME']._serialized_start=265
  _globals['_GAME']._serialized_end=452
# @@protoc_insertion_point(module_scope)
