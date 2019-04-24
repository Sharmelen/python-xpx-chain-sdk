"""
    block_info
    ==========

    Blockchain info describing stored data.

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

from .network_type import OptionalNetworkType
from ... import util

__all__ = ['BlockchainStorageInfo']


@util.inherit_doc
@util.dataclass(frozen=True)
class BlockchainStorageInfo(util.DTO):
    """
    Blockchain information describing stored data.

    :param num_blocks: Number of confirmed blocks.
    :param num_transactions: Number of confirmed transactions.
    :param num_accounts: Number accounts published in the blockchain.
    """

    num_blocks: int
    num_transactions: int
    num_accounts: int

    def to_dto(
        self,
        network_type: OptionalNetworkType = None,
    ) -> dict:
        return {
            "numBlocks": self.num_blocks,
            "numTransactions": self.num_transactions,
            "numAccounts": self.num_accounts
        }

    @classmethod
    def from_dto(
        cls,
        data: dict,
        network_type: OptionalNetworkType = None,
    ):
        num_blocks = data['numBlocks']
        num_transactions = data['numTransactions']
        num_accounts = data['numAccounts']
        return cls(num_blocks, num_transactions, num_accounts)
