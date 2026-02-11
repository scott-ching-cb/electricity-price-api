from dataclasses import dataclass

from app.application.common.exceptions import GatewayException, ValidationException


class PriceGatewayException(GatewayException):
    pass



class PriceValidationException(ValidationException):
     pass


@dataclass(eq=False)
class EmptyStateException(PriceValidationException):

    @property
    def title(self) -> str:
        return f'A state is required to calculate historical prices'


@dataclass(eq=False)
class InvalidStateException(PriceGatewayException):
    state: str

    @property
    def title(self) -> str:
        return f'The provided state is either invalid or does not have any price history'

@dataclass(eq=False)
class InternalDatabaseConnectionException(PriceGatewayException):

    @property
    def title(self) -> str:
        return f'An error occurred whilst attempting to retrieve historical state-price data'
