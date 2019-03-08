"""
    network_type
    ============

    Constants for the network type.

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

from nem2 import util


class NetworkType(util.IntEnumDto):
    """Identifier for the network type."""

    MAIN_NET    = 0x68
    TEST_NET    = 0x98
    MIJIN       = 0x60
    MIJIN_TEST  = 0x90

    def description(self) -> str:
        """Describe enumerated values in detail."""

        return DESCRIPTION[self]

    def identifier(self) -> bytes:
        """Get address identifier from type."""

        return TO_IDENTIFIER[self]

    @classmethod
    def create_from_identifier(cls, identifier: bytes) -> 'NetworkType':
        """
        Identify and create the network type from the raw address identifier.

        :param identifier: First character of the raw address.
        """

        assert len(identifier) == 1
        return FROM_IDENTIFIER[identifier]

    createFromIdentifier = util.undoc(create_from_identifier)

    @classmethod
    def create_from_raw_address(cls, address: str) -> 'NetworkType':
        """
        Identify and create the network type from the raw address.

        :param address: Base32-decoded, upper-case, stripped address.
        """

        assert len(address) == 40
        return NetworkType.create_from_identifier(address[0].encode('ascii'))

    createFromRawAddress = util.undoc(create_from_raw_address)

    @util.doc(util.Dto.to_dto)
    def to_dto(self) -> int:
        return int(self)

    @util.doc(util.Dto.from_dto)
    @classmethod
    def from_dto(cls, data: int) -> 'NetworkType':
        return cls(data)


DESCRIPTION = {
    NetworkType.MAIN_NET: "Main network",
    NetworkType.TEST_NET: "Test network",
    NetworkType.MIJIN: "Mijin network",
    NetworkType.MIJIN_TEST: "Mijin test network",
}

TO_IDENTIFIER = {
    NetworkType.MAIN_NET: b"N",
    NetworkType.TEST_NET: b"T",
    NetworkType.MIJIN: b"M",
    NetworkType.MIJIN_TEST: b"S",
}

FROM_IDENTIFIER = {
    b"N": NetworkType.MAIN_NET,
    b"T": NetworkType.TEST_NET,
    b"M": NetworkType.MIJIN,
    b"S": NetworkType.MIJIN_TEST,
}
