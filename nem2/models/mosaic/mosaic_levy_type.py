"""
    mosaic_levy_type
    ================

    Constants for the mosaic levy type.

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


# TODO(ahuszagh) This is not yet implemented in Catapult.
# Subject to change
class MosaicLevyType(util.IntEnumDto):
    """Mosaic levy type."""

    ABSOLUTE = 1
    CALCULATED = 2

    def description(self) -> str:
        """Describe enumerated values in detail."""

        return DESCRIPTION[self]

    @util.doc(util.Dto.to_dto)
    def to_dto(self) -> int:
        return int(self)

    @util.doc(util.Dto.from_dto)
    @classmethod
    def from_dto(cls, data: int) -> 'MosaicLevyType':
        return cls(data)


DESCRIPTION = {
    MosaicLevyType.ABSOLUTE: "The levy is an absolute fee. The field 'fee' states how many sub-units of the specified mosaic will be transferred to the recipient.",
    MosaicLevyType.CALCULATED: "The levy is calculated from the transferred amount. The field 'fee' states how many percentiles of the transferred quantity will transferred to the recipient.",
}
