"""
    mosaic_supply_change_transaction
    ================================

    Mosaic supply change transaction.

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

from __future__ import annotations
import typing

from .deadline import Deadline
from .inner_transaction import InnerTransaction
from .registry import register_transaction
from .transaction import Transaction
from .transaction_info import TransactionInfo
from .transaction_type import TransactionType
from .transaction_version import TransactionVersion
from ..account.public_account import PublicAccount
from ..blockchain.network_type import NetworkType
from ..mosaic.mosaic_id import MosaicId
from ..mosaic.mosaic_supply_type import MosaicSupplyType
from ... import util

__all__ = [
    'MosaicSupplyChangeTransaction',
    'MosaicSupplyChangeInnerTransaction',
]


@util.inherit_doc
@util.dataclass(frozen=True)
@register_transaction('MOSAIC_SUPPLY_CHANGE')
class MosaicSupplyChangeTransaction(Transaction):
    """
    Mosaic supply change transaction.

    :param network_type: Network type.
    :param version: Transaction version.
    :param deadline: Deadline to include transaction.
    :param max_fee: Max fee for the transaction. Higher fees increase priority.

    :param nonce: Mosaic nonce (random data for mosaic uniqueness).
    :param mosaic_id: Identifier for mosaic.
    :param mosaic_properties: Mosaic properties.

    :param signature: (Optional) Transaction signature (missing if embedded transaction).
    :param signer: (Optional) Account of transaction creator.
    :param transaction_info: (Optional) Transaction metadata.
    """

    mosaic_id: MosaicId
    direction: MosaicSupplyType
    delta: int

    def __init__(
        self,
        network_type: NetworkType,
        version: TransactionVersion,
        deadline: Deadline,
        mosaic_id: MosaicId,
        direction: MosaicSupplyType,
        delta: int,
        max_fee: typing.Optional[int] = None,
        fee_strategy: typing.Optional[util.FeeCalculationStrategy] = util.FeeCalculationStrategy.ZERO,
        signature: typing.Optional[str] = None,
        signer: typing.Optional[PublicAccount] = None,
        transaction_info: typing.Optional[TransactionInfo] = None,
    ) -> None:
        super().__init__(
            TransactionType.MOSAIC_SUPPLY_CHANGE,
            network_type,
            version,
            deadline,
            max_fee,
            fee_strategy,
            signature,
            signer,
            transaction_info,
        )
        self._set('mosaic_id', mosaic_id)
        self._set('direction', direction)
        self._set('delta', delta)

    @classmethod
    def create(
        cls,
        deadline: Deadline,
        mosaic_id: MosaicId,
        direction: MosaicSupplyType,
        delta: int,
        network_type: NetworkType,
        max_fee: typing.Optional[int] = None,
        fee_strategy: typing.Optional[util.FeeCalculationStrategy] = util.FeeCalculationStrategy.ZERO
    ):
        """
        Create new mosaic supply change transaction.

        :param deadline: Deadline to include transaction.

        :param nonce: Mosaic nonce (random data for mosaic uniqueness).
        :param mosaic_id: Identifier for mosaic.
        :param mosaic_properties: Mosaic properties.

        :param network_type: Network type.
        :param max_fee: (Optional) Max fee defined by sender.
        """
        return cls(
            network_type,
            TransactionVersion.MOSAIC_SUPPLY_CHANGE,
            deadline,
            direction,
            delta,
            max_fee,
            mosaic_id,
        )

    # CATBUFFER

    def catbuffer_size_specific(self) -> int:
        id_size = util.U64_BYTES
        direction_size = MosaicSupplyType.CATBUFFER_SIZE
        delta_size = util.U64_BYTES
        return id_size + direction_size + delta_size

    def to_catbuffer_specific(
        self,
        network_type: NetworkType,
    ) -> bytes:
        """Export mosaic supply change-specific data to catbuffer."""

        # uint64 mosaic_id
        # MosaicSupplyChange direction
        # uint64 delta
        mosaic_id = util.u64_to_catbuffer(int(self.mosaic_id))
        direction = self.direction.to_catbuffer(network_type)
        delta = util.u64_to_catbuffer(self.delta)
        return mosaic_id + direction + delta

    def load_catbuffer_specific(
        self,
        data: bytes,
        network_type: NetworkType,
    ) -> bytes:
        """Load mosaic supply change-specific data data from catbuffer."""

        # uint64 mosaic_id
        # MosaicSupplyChange direction
        # uint64 delta
        mosaic_id = MosaicId(util.u64_from_catbuffer(data[:8]))
        direction = MosaicSupplyType.create_from_catbuffer(data[8:9], network_type)
        delta = util.u64_from_catbuffer(data[9:17])
        data = data[17:]

        self._set('mosaic_id', mosaic_id)
        self._set('direction', direction)
        self._set('delta', delta)

        return data

    # DTO

    @classmethod
    def validate_dto_specific(cls, data: dict) -> bool:
        required_keys = {'mosaicId', 'direction', 'delta'}
        return cls.validate_dto_required(data, required_keys)

    def to_dto_specific(
        self,
        network_type: NetworkType,
    ) -> dict:
        return {
            'mosaicId': util.u64_to_dto(int(self.mosaic_id)),
            'direction': self.direction.to_dto(network_type),
            'delta': util.u64_to_dto(self.delta),
        }

    def load_dto_specific(
        self,
        data: dict,
        network_type: NetworkType,
    ) -> None:
        mosaic_id = MosaicId(util.u64_from_dto(data['mosaicId']))
        direction = MosaicSupplyType.create_from_dto(data['direction'], network_type)
        delta = util.u64_from_dto(data['delta'])
        self._set('mosaic_id', mosaic_id)
        self._set('direction', direction)
        self._set('delta', delta)


@register_transaction('MOSAIC_SUPPLY_CHANGE')
class MosaicSupplyChangeInnerTransaction(InnerTransaction, MosaicSupplyChangeTransaction):
    """Embedded mosaic supply change transaction."""

    __slots__ = ()
