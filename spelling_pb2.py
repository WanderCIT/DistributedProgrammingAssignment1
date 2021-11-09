# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spelling.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='spelling.proto',
  package='unary',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0espelling.proto\x12\x05unary\"U\n\x16SpellingBeeWordRequest\x12\x0c\n\x04word\x18\x01 \x01(\t\x12\x0f\n\x07letters\x18\x02 \x03(\t\x12\r\n\x05score\x18\x03 \x01(\x05\x12\r\n\x05words\x18\x04 \x03(\t\"d\n\x17SpellingBeeWordResponse\x12\x0c\n\x04word\x18\x01 \x01(\t\x12\r\n\x05valid\x18\x02 \x01(\t\x12\x0e\n\x06reason\x18\x03 \x01(\t\x12\r\n\x05score\x18\x04 \x01(\x05\x12\r\n\x05words\x18\x05 \x03(\t\"\x0f\n\rLetterRequest\"\"\n\x0fSpellingLetters\x12\x0f\n\x07letters\x18\x01 \x03(\t\"\x1d\n\x0cWordsRequest\x12\r\n\x05words\x18\x01 \x03(\t\"\x1e\n\rWordsResponse\x12\r\n\x05words\x18\x01 \x03(\t2\xd2\x01\n\x0bSpellingBee\x12<\n\nGetLetters\x12\x14.unary.LetterRequest\x1a\x16.unary.SpellingLetters\"\x00\x12L\n\tCheckWord\x12\x1d.unary.SpellingBeeWordRequest\x1a\x1e.unary.SpellingBeeWordResponse\"\x00\x12\x37\n\x08GetWords\x12\x13.unary.WordsRequest\x1a\x14.unary.WordsResponse\"\x00\x62\x06proto3'
)




_SPELLINGBEEWORDREQUEST = _descriptor.Descriptor(
  name='SpellingBeeWordRequest',
  full_name='unary.SpellingBeeWordRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='word', full_name='unary.SpellingBeeWordRequest.word', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='letters', full_name='unary.SpellingBeeWordRequest.letters', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='score', full_name='unary.SpellingBeeWordRequest.score', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='words', full_name='unary.SpellingBeeWordRequest.words', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=25,
  serialized_end=110,
)


_SPELLINGBEEWORDRESPONSE = _descriptor.Descriptor(
  name='SpellingBeeWordResponse',
  full_name='unary.SpellingBeeWordResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='word', full_name='unary.SpellingBeeWordResponse.word', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='valid', full_name='unary.SpellingBeeWordResponse.valid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reason', full_name='unary.SpellingBeeWordResponse.reason', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='score', full_name='unary.SpellingBeeWordResponse.score', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='words', full_name='unary.SpellingBeeWordResponse.words', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=112,
  serialized_end=212,
)


_LETTERREQUEST = _descriptor.Descriptor(
  name='LetterRequest',
  full_name='unary.LetterRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
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
  serialized_start=214,
  serialized_end=229,
)


_SPELLINGLETTERS = _descriptor.Descriptor(
  name='SpellingLetters',
  full_name='unary.SpellingLetters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='letters', full_name='unary.SpellingLetters.letters', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=231,
  serialized_end=265,
)


_WORDSREQUEST = _descriptor.Descriptor(
  name='WordsRequest',
  full_name='unary.WordsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='words', full_name='unary.WordsRequest.words', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=267,
  serialized_end=296,
)


_WORDSRESPONSE = _descriptor.Descriptor(
  name='WordsResponse',
  full_name='unary.WordsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='words', full_name='unary.WordsResponse.words', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=298,
  serialized_end=328,
)

DESCRIPTOR.message_types_by_name['SpellingBeeWordRequest'] = _SPELLINGBEEWORDREQUEST
DESCRIPTOR.message_types_by_name['SpellingBeeWordResponse'] = _SPELLINGBEEWORDRESPONSE
DESCRIPTOR.message_types_by_name['LetterRequest'] = _LETTERREQUEST
DESCRIPTOR.message_types_by_name['SpellingLetters'] = _SPELLINGLETTERS
DESCRIPTOR.message_types_by_name['WordsRequest'] = _WORDSREQUEST
DESCRIPTOR.message_types_by_name['WordsResponse'] = _WORDSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SpellingBeeWordRequest = _reflection.GeneratedProtocolMessageType('SpellingBeeWordRequest', (_message.Message,), {
  'DESCRIPTOR' : _SPELLINGBEEWORDREQUEST,
  '__module__' : 'spelling_pb2'
  # @@protoc_insertion_point(class_scope:unary.SpellingBeeWordRequest)
  })
_sym_db.RegisterMessage(SpellingBeeWordRequest)

SpellingBeeWordResponse = _reflection.GeneratedProtocolMessageType('SpellingBeeWordResponse', (_message.Message,), {
  'DESCRIPTOR' : _SPELLINGBEEWORDRESPONSE,
  '__module__' : 'spelling_pb2'
  # @@protoc_insertion_point(class_scope:unary.SpellingBeeWordResponse)
  })
_sym_db.RegisterMessage(SpellingBeeWordResponse)

LetterRequest = _reflection.GeneratedProtocolMessageType('LetterRequest', (_message.Message,), {
  'DESCRIPTOR' : _LETTERREQUEST,
  '__module__' : 'spelling_pb2'
  # @@protoc_insertion_point(class_scope:unary.LetterRequest)
  })
_sym_db.RegisterMessage(LetterRequest)

SpellingLetters = _reflection.GeneratedProtocolMessageType('SpellingLetters', (_message.Message,), {
  'DESCRIPTOR' : _SPELLINGLETTERS,
  '__module__' : 'spelling_pb2'
  # @@protoc_insertion_point(class_scope:unary.SpellingLetters)
  })
_sym_db.RegisterMessage(SpellingLetters)

WordsRequest = _reflection.GeneratedProtocolMessageType('WordsRequest', (_message.Message,), {
  'DESCRIPTOR' : _WORDSREQUEST,
  '__module__' : 'spelling_pb2'
  # @@protoc_insertion_point(class_scope:unary.WordsRequest)
  })
_sym_db.RegisterMessage(WordsRequest)

WordsResponse = _reflection.GeneratedProtocolMessageType('WordsResponse', (_message.Message,), {
  'DESCRIPTOR' : _WORDSRESPONSE,
  '__module__' : 'spelling_pb2'
  # @@protoc_insertion_point(class_scope:unary.WordsResponse)
  })
_sym_db.RegisterMessage(WordsResponse)



_SPELLINGBEE = _descriptor.ServiceDescriptor(
  name='SpellingBee',
  full_name='unary.SpellingBee',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=331,
  serialized_end=541,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetLetters',
    full_name='unary.SpellingBee.GetLetters',
    index=0,
    containing_service=None,
    input_type=_LETTERREQUEST,
    output_type=_SPELLINGLETTERS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CheckWord',
    full_name='unary.SpellingBee.CheckWord',
    index=1,
    containing_service=None,
    input_type=_SPELLINGBEEWORDREQUEST,
    output_type=_SPELLINGBEEWORDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetWords',
    full_name='unary.SpellingBee.GetWords',
    index=2,
    containing_service=None,
    input_type=_WORDSREQUEST,
    output_type=_WORDSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SPELLINGBEE)

DESCRIPTOR.services_by_name['SpellingBee'] = _SPELLINGBEE

# @@protoc_insertion_point(module_scope)
