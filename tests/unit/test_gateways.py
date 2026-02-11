import csv
import os
import unittest

from app.application.price.exceptions import InternalDatabaseConnectionException, InvalidStateException
from app.repository.gateways.price import PriceGatewayImpl


class TestConverters(unittest.TestCase):
    price_gateway: PriceGatewayImpl = None
    test_file_location: str = None


    @classmethod
    def setUpClass(cls):
        cls.test_file_location = "tests/resources/test_price_converter_df.csv"
        test_data = [
            [ "state", "price", "timestamp" ],
            [ "Vic", 81.52, "2025-06-24 00:00:00" ],
        ]
        with open(cls.test_file_location, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(test_data)


    @classmethod
    def tearDownClass(cls):
        os.remove(cls.test_file_location)


    def setUp(self):
        self.price_gateway = PriceGatewayImpl()
        self.price_gateway.file_location = "tests/resources/test_price_converter_df.csv"


    def test_price_gateway_invalid_filepath(self):
        self.price_gateway.file_location = "invalid-file-location.csv"
        self.assertRaises(InternalDatabaseConnectionException, self.price_gateway.get_historical_prices, "Vic")


    def test_price_gateway_invalid_state(self):
        invalid_test_state = "Qbe"
        self.assertRaises(InvalidStateException, self.price_gateway.get_historical_prices, invalid_test_state)


    def test_price_gateway_success(self):
        historical_victoria_prices = self.price_gateway.get_historical_prices("Vic")
        self.assertEqual(len(historical_victoria_prices), 1)
        historical_record = historical_victoria_prices[0]
        self.assertEqual(historical_record.price, 81.52)
        self.assertEqual(historical_record.timestamp.strftime("%Y-%m-%d %H:%M:%S"), "2025-06-24 00:00:00")
        self.assertEqual(historical_record.state, "Vic")
