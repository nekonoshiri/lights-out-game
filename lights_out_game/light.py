from __future__ import annotations

from enum import Enum, auto


class Light(Enum):
    ON = auto()
    OFF = auto()

    @property
    def is_on(self) -> bool:
        return self == Light.ON

    @property
    def is_off(self) -> bool:
        return self == Light.OFF

    @property
    def toggled(self) -> Light:
        if self.is_on:
            return Light.OFF
        else:
            return Light.ON
