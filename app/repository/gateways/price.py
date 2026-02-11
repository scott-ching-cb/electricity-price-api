from dataclass_csv import DataclassReader

from app.application.price.exceptions import InvalidStateException, InternalDatabaseConnectionException
from app.infrastructure.repository import models
from app.application.price.interfaces import PriceGateway


class PriceGatewayImpl(PriceGateway):


    def __init__(self) -> None:
        self.file_location = "repository/gateways/data/coding_challenge_prices.csv"


    def _get_csv_price_data(self) -> list[models.Price]:
        try:
            with open(self.file_location, "r") as f:
                reader = DataclassReader(f, models.Price)
                return list(reader)
        except FileNotFoundError:
            raise InternalDatabaseConnectionException()


    def get_historical_prices(self, state: str) -> list[models.Price]:
        historical_price_data = self._get_csv_price_data()
        state_historical_price_data = list(filter(lambda price_data: price_data.state == state, historical_price_data))
        if len(state_historical_price_data) == 0:
            raise InvalidStateException(state)
        return state_historical_price_data
