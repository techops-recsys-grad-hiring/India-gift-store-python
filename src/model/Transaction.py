class Transaction:
    def __init__(self, gifts):
        self.gifts = gifts

    def __str__(self):
        return f"{self.gifts} gifts: {self.gifts}"
