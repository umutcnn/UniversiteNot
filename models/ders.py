from typing import List

from dataclasses import dataclass

from .degerlendirme import Degerlendirme


@dataclass
class Ders:
    ders_adi: str
    degerlendirmeler : List[Degerlendirme]
