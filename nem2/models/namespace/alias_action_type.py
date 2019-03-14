"""
    alias_action_type
    =================

    Enumerations for alias action types.

    License
    -------

    Copyright 2019 NEM

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

import enum
import struct
import typing

from nem2 import util


@util.inherit_doc
class AliasActionType(util.Catbuffer, util.EnumMixin, enum.IntEnum):
    """Alias action type."""

    LINK = 0
    UNLINK = 1
    CATBUFFER_SIZE: typing.ClassVar[int]

    def description(self) -> str:
        return DESCRIPTION[self]

    def to_catbuffer(self) -> bytes:
        return struct.pack('<B', int(self))

    @classmethod
    def from_catbuffer(cls, data: bytes) -> typing.Tuple['AliasActionType', bytes]:
        assert len(data) >= cls.CATBUFFER_SIZE
        inst = cls(struct.unpack('<B', data[:cls.CATBUFFER_SIZE])[0])
        return inst, data[cls.CATBUFFER_SIZE:]


AliasActionType.CATBUFFER_SIZE = 1

DESCRIPTION = {
    AliasActionType.LINK: "Link an alias.",
    AliasActionType.UNLINK: "Unlink an alias.",
}
