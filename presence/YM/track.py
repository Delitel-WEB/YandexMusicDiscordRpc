from dataclasses import dataclass
from typing import List

@dataclass
class Track:
    artists: List[str]
    name: str
    preview: str
    link: str
    duration: str