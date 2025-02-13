from __future__ import annotations
import datetime
from typing import Literal

from pydantic.dataclasses import dataclass

from ..._database import Session as m_Session
from ..._database._database import _Nothing


@dataclass
class User:
    id: str
    name: str
    email: str | None
    creation_datetime: datetime.datetime


@dataclass
class ForeignUser:
    name: str
    creation_datetime: datetime.datetime

    @classmethod
    def from_user(cls, user: User) -> ForeignUser:
        return cls(
            name=user.name,
            creation_datetime=user.creation_datetime
        )


@dataclass
class CreateUser:
    name: str
    password: str
    email: str = None


@dataclass
class UpdateUser:
    name: str = _Nothing
    email: str = _Nothing
    password: str = _Nothing


@dataclass
class Session:
    creation_datetime: datetime.datetime
    expiration_datetime: datetime.datetime | None


@dataclass
class CreateSession:
    owner_name: str
    password: str
    lifetime: datetime.timedelta = m_Session.DEFAULT_LIFETIME


@dataclass
class FileMetadata:
    uploader_id: str | None
    upload_datetime: datetime.datetime
    expiration_datetime: datetime.datetime | None
    filename: str | None
    decrypted_data_hash: str | None
    mime_type: str
    data_access_count: int
    max_access_count: int | None
    file_size: int
    meta_access_count: int


@dataclass
class OAuth2LoginInfo:
    access_token: str
    token_type: Literal["bearer"] = "bearer"


@dataclass
class Meta:
    lifetime_guest: float
    lifetime: float
    file_maxsize_guest: int
    file_maxsize: int
