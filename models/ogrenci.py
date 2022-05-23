from typing import List

from dataclasses import dataclass

from .degerlendirme_notu import Not


@dataclass
class Ogrenci:
    adi: str
    numara: str
    notlar = List[Not]
