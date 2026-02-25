from dataclasses import dataclass
from datetime import date

@dataclass(frozen=True)
class Pacote:
    id: int
    destino: str
    preco: float
    ida: date
    volta: date