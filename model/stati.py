from dataclasses import dataclass
from datetime import datetime


@dataclass
class Stato:
    id: str
    Name: str
    Capital: str
    Lat: float
    Lng: float
    Area: int
    Population: int
    Neighbors: str

    def __hash__(self):
        return self.id
    def __str__(self):
        return self.Name
