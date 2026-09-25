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

# Load previous inventory
stock_quantity, transaction_history = load_inventory()


print("\n======== Inventory Auditor ========")
print(f"Current inventory: {stock_quantity} units")
print(f"Previous transaction history: {transaction_history}")


# Enter deliveries
while stock_quantity < 500:

    stock_input = input("\nPlease enter quantity (or 'quit' to exit): ")

    if stock_input.lower() == "quit":
        break

    try:
        stock_input = int(stock_input)

    except ValueError:
        print("Error: Please enter a valid integer!")
        continue

    if stock_input < 0:
        print("Error: Please enter a positive integer!")
        continue

    new_total = stock_quantity + stock_input

    if new_total > 500:
        print("Alert: Inventory has exceeded 500 units!")
        break

    # Add the delivery to transaction history
    transaction_history.append(stock_input)

    # Update inventory
    stock_quantity = new_total

    print(f"Current inventory: {stock_quantity} units")
    print(f"Transaction history: {transaction_history}")


print("\n===== Final Inventory =====")
print(f"Total inventory: {stock_quantity} units")
print(f"Transaction history: {transaction_history}")


# Load inventory data
stock_quantity, transaction_history = load_inventory()


# Display loaded inventory
print("\n======== Inventory Auditor ========")
print(f"Current inventory: {stock_quantity} units")
print(f"Previous transaction history: {transaction_history}")