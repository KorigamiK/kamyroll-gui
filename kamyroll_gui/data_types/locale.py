from dataclasses import dataclass



@dataclass
class Locale:
    name: str
    bcp_47: str
    iso_639_2: str
