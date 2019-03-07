"""
    namespace_name
    ==============

    Describes a namespace by name and identifier.

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
from .namespace_id import NamespaceId


class NamespaceName(util.Dto, util.Tie):
    """Namespace name and identifier."""

    __slots__ = (
        '_namespace_id',
        '_name',
    )

    def __init__(self, namespace_id: 'NamespaceId', name: str) -> None:
        """
        :param namespace_id: Namespace ID.
        :param name: Namespace name.
        """
        self._namespace_id = namespace_id
        self._name = name

    @classmethod
    def create_from_name(cls, name: str) -> 'NamespaceName':
        """
        Create namespace name and identifier from name.

        :param name: Namespace name.
        """
        namespace_id = NamespaceId(name)
        return cls(namespace_id, name)

    @property
    def namespace_id(self) -> 'NamespaceId':
        """Get the namespace ID."""
        return self._namespace_id

    namespaceId = util.undoc(namespace_id)

    @property
    def name(self) -> str:
        """Get the namespace name."""
        return self._name

    @util.doc(util.Tie.tie)
    def tie(self) -> tuple:
        return super().tie()

    @util.doc(util.Dto.to_dto)
    def to_dto(self) -> dict:
        return {
            'namespaceId': self.namespace_id.to_dto(),
            'name': self.name
        }

    @util.doc(util.Dto.from_dto)
    @classmethod
    def from_dto(cls, data: dict) -> 'Namespace':
        namespace_id = NamespaceId.from_dto(data['namespaceId'])
        name = data['name']
        return cls(namespace_id, name)
