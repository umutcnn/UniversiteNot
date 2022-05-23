from dataclasses import dataclass

from .degerlendirme import Degerlendirme



@dataclass
class Not:
    degerlendirme: Degerlendirme
    puan: float
    
