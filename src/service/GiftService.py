from src.model.Gift import Gift
from src.model.GiftType import GiftType

GST_PERCENTAGE = 5

gift_store_items = [
    Gift(GiftType.STANDARD, "Teddy bear", 600),
    Gift(GiftType.STANDARD, "Chocolates", 1000),
    Gift(GiftType.STANDARD, "Novel", 800),
    Gift(GiftType.PREMIUM, "Photo frame", 1500),
    Gift(GiftType.PREMIUM, "Ornaments", 2000),
    Gift(GiftType.PREMIUM, "Personalized Caricature", 1800)
]


class GiftService:

    def __init__(self):
        super().__init__()

    def calculate_price(self, transaction):
        # TODO: logic to calculate the price of items purchased
        return 0
