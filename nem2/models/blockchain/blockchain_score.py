"""
    block_info
    ==========

    Blockchain data describing the block difficulty.

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


# TODO(ahuszagh) Need Dto?
class BlockchainScore(util.Tie):
    """Blockchain score describing the block difficulty."""

    _score: int

    def __init__(self, score: int) -> None:
        """
        :param score: Blockchain score.
        """
        self._score = score

    @property
    def score(self) -> int:
        """Get the blockchain score."""
        return self._score

    @property
    def score_low(self) -> int:
        """Get the low 64-bits of the blockchain score."""
        return util.uint128_low(self.score)

    scoreLow = util.undoc(score_low)

    @property
    def score_high(self) -> int:
        """Get the high 64-bits of the blockchain score."""
        return util.uint128_high(self.score)

    scoreHigh = util.undoc(score_high)
