class Gift:
    def __init__(self, gift_type, item, price_in_rupees):
        self.gift_type = gift_type
        self.item = item
        self.price_in_rupees = price_in_rupees

    def __str__(self):
        return f"Gift item: {self.item} of type: ${self.gift_type} and price: ₹{self.price_in_rupees}"
