"""
    cosignature_signed_transaction
    ==============================

    Cosignature signed transaction.

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


@util.inherit_doc
@util.dataclass(frozen=True)
class CosignatureSignedTransaction(util.Dto):
    """
    Cosignature signed transaction.

    :param parent_hash: Hash of parent aggregate transaction.
    :param signature: Signature generated by signing the parent hash.
    :param signer: Public key of the transaction signer.
    """

    parent_hash: str
    signature: str
    signer: str

    def to_dto(self) -> dict:
        return {
            'parentHash': self.parent_hash,
            'signature': self.signature,
            'signer': self.signer,
        }

    @classmethod
    def from_dto(cls, data: dict) -> 'CosignatureSignedTransaction':
        return cls(
            parent_hash=data['parentHash'],
            signature=data['signature'],
            signer=data['signer'],
        )
