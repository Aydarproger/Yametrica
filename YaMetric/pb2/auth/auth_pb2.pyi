from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AuthRequest(_message.Message):
    __slots__ = ("id", "username", "utm_source")
    ID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    UTM_SOURCE_FIELD_NUMBER: _ClassVar[int]
    id: int
    username: str
    utm_source: str
    def __init__(self, id: _Optional[int] = ..., username: _Optional[str] = ..., utm_source: _Optional[str] = ...) -> None: ...

class AuthResponse(_message.Message):
    __slots__ = ("status", "access_token")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    status: bool
    access_token: str
    def __init__(self, status: bool = ..., access_token: _Optional[str] = ...) -> None: ...
