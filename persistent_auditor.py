# Variables
stock_quantity = 0
transaction_history = []


def load_inventory():
    try:
        with open("inventory.txt", "r") as file:
            lines = file.readlines()

            total = int(lines[0].strip())
            history = []

            if len(lines) > 1 and lines[1].strip() != "":
                history = [
                    int(value)
                    for value in lines[1].strip().split(",")
                ]

        return total, history

    except FileNotFoundError:
        return 0, []


# Load inventory data
stock_quantity, transaction_history = load_inventory()


# Display loaded inventory
print("\n======== Inventory Auditor ========")
print(f"Current inventory: {stock_quantity} units")
print(f"Previous transaction history: {transaction_history}")