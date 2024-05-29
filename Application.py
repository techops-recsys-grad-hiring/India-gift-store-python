from src.model.Transaction import Transaction
from src.service.GiftService import GiftService


def main():
    print("Welcome to Gift Store!")

    number_of_gifts = int(input("Enter number of gifts: "))
    gifts_input = input("Enter gift names: ")
    gifts = [gift.strip() for gift in gifts_input.split(",")]
    if len(gifts) != number_of_gifts:
        print("Please enter correct number of gifts!")
        exit()

    transaction = Transaction(gifts)
    transaction_amount = GiftService().calculate_price(transaction)

    print("Thanks for Transaction of amount: ₹ ", transaction_amount)


if __name__ == "__main__":
    main()
