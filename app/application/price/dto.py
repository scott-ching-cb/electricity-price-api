import datetime

from dataclasses import dataclass

from app.application.common.dto import DTO


@dataclass(frozen=True)
class Price(DTO):
    state: str
    price: float
    timestamp: datetime.datetime
