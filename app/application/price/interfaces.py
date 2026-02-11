import abc

from typing import Protocol

from . import dto


class PriceGateway(Protocol):


    @abc.abstractmethod
    def get_historical_prices(self, state: str) -> list[dto.Price]:
        raise NotImplementedError
