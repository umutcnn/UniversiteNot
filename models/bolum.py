from typing import List
from dataclasses import dataclass

from .ders import Ders


@dataclass
class Bolum:
    bolum_adi: str
    dersler: List[Ders]
