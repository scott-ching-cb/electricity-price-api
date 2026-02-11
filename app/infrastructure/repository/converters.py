from app.application.price import dto
from app.infrastructure.repository import models


def convert_price_model_to_dto(price_model: models.Price) -> dto.Price:
    return dto.Price(
        state = price_model.state,
        price = price_model.price,
        timestamp = price_model.timestamp,
    )
