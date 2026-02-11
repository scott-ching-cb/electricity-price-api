import datetime

from dataclasses import dataclass, field

from dataclass_csv import dateformat


@dataclass
@dateformat('%Y-%m-%d')
class Price:
    state: str
    price: float
    timestamp: datetime.datetime = field(metadata={"dateformat": "%Y-%m-%d %H:%M:%S"})
