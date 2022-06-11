from dataclasses import dataclass
from datetime import date
@dataclass
class Userbase:
    date : date
    users: int
