from app.application.price.exceptions import EmptyStateException
from app.application.price.interfaces import PriceGateway
from app.repository.gateways.price import PriceGatewayImpl


class GetPriceByStateUseCase:

    def __init__(self, state: str):
        self.price_gateway: PriceGateway = PriceGatewayImpl()
        self.state = state

    def validate(self) -> None:
        if len(self.state) == 0:
            raise EmptyStateException()
        return

    def prepare(self):
        self.validate()

    def get_average_state_price(self, state: str) -> float:
        self.prepare()
        historical_state_prices = self.price_gateway.get_historical_prices(state)
        sum_of_historical_state_prices = sum(record.price for record in historical_state_prices)
        return round(sum_of_historical_state_prices / len(historical_state_prices), 2)