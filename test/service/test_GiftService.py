import unittest

from src.model.Transaction import Transaction
from src.service.GiftService import GiftService


class GiftServiceTest(unittest.TestCase):
    def test_should_calculate_transaction_amount_for_given_gifts(self):
        transaction = Transaction(["Teddy bear", "Ornaments", "Novel"])
        expected_transaction_amount = 3570

        actual_transaction_amount = GiftService().calculate_price(transaction)

        self.assertEqual(actual_transaction_amount, expected_transaction_amount)

    def test_should_raise_exception_for_invalid_number_of_gifts(self):
        transaction = Transaction([])

        with self.assertRaises(Exception) as exception:
            GiftService().calculate_price(transaction)
        self.assertEqual(str(exception), "Invalid number of gifts, it should be >= 1")

