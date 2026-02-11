import unittest

from datetime import datetime

from app.infrastructure.repository.converters import convert_price_model_to_dto
from app.infrastructure.repository.models import Price
from app.application.price.dto import Price as PriceDto


class TestConverters(unittest.TestCase):
    price_model: Price = None


    def setUp(self):
        test_state = "Vic"
        static_datetime = "2025-06-24 00:00:00"
        format_string = "%Y-%m-%d %H:%M:%S"
        test_datetime = datetime.strptime(static_datetime, format_string)
        test_price = 11.99
        self.price_model = Price(test_state, test_price, test_datetime)


    def test_convert_price_model_to_dto(self):
        output_dto = convert_price_model_to_dto(self.price_model)
        assert isinstance(output_dto, PriceDto)
        self.assertEqual(output_dto.state, "Vic")
        self.assertEqual(output_dto.price, 11.99)
        self.assertEqual(output_dto.timestamp.strftime("%Y-%m-%d %H:%M:%S"), "2025-06-24 00:00:00")


if __name__ == "__main__":
    unittest.main()