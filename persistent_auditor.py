# Variables
stock_quantity = 0
failed_entries = 0
transaction_history = []

orders = [
    [1001, "Wireless Mouse", 2],
    [1002, "Keyboard", 1],
    [1003, "USB Cable", 3],
]


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


def save_inventory(total, history):
    with open("inventory.txt", "w") as file:
        file.write(str(total) + "\n")
        file.write(",".join(map(str, history)))


def load_orders():
    orders = []

    try:
        with open("orders.txt", "r") as file:
            for line in file:
                order_id, product_name, quantity = line.strip().split(",")

                orders.append([
                    int(order_id.strip()),
                    product_name.strip(),
                    int(quantity.strip())
                ])

    except FileNotFoundError:
        orders = [
            [1001, "Wireless Mouse", 2],
            [1002, "Keyboard", 1],
            [1003, "USB Cable", 3]
        ]

    return orders


def save_orders(orders):
    with open("orders.txt", "w") as file:
        for order_id, product_name, quantity in orders:
            file.write(
                f"{order_id},{product_name},{quantity}\n"
            )


# Retrieve and validate input
def get_valid_input():
    failed_attempts = 0

    while True:
        product_item = input("Please enter product name: ")

        if product_item.lower() == "quit":
            return "quit", None, failed_attempts

        stock_input = input("Please enter quantity: ")

        if stock_input.lower() == "quit":
            return "quit", None, failed_attempts

        # Integer check
        try:
            stock_input = int(stock_input)

        except ValueError:
            print("\nError: Please enter a valid integer!")
            failed_attempts += 1
            continue

        # Negative value check
        if stock_input < 0:
            print("\nError: Please enter a positive integer!")
            failed_attempts += 1
            continue

        return product_item, stock_input, failed_attempts


# Process delivery
def process_delivery(current_total, new_value):
    new_total = current_total + new_value
    return new_total


# Calculate tax on this delivery
def calculate_tax(amount):
    tax = amount * 0.10
    return tax


# Final report summary
def generate_reports(total_units, failed_attempts, history):
    print("\n===== Final Report Summary =====")
    print(f"Total units processed: {total_units}")
    print(f"Total failed entries: {failed_attempts}")
    print(f"Transaction history: {history}")


# Load inventory
stock_quantity, transaction_history = load_inventory()

# Load orders
orders = load_orders()

print("\n======== Current Orders ========")

for order_id, product_name, quantity in orders:
    print(
        f"{order_id}, {product_name}, {quantity}"
    )

print("\n======== Inventory Auditor ========")
print(f"Current inventory: {stock_quantity} units")
print(
    f"Previous transaction history: {transaction_history}"
)


# Stock validation
while stock_quantity < 500:

    product_item, stock_input, new_failures = get_valid_input()

    failed_entries += new_failures

    # User exits program
    if product_item == "quit":
        break

    # Calculate new inventory total
    new_total = process_delivery(
        stock_quantity,
        stock_input
    )

    # Overstock check
    if new_total > 500:
        print(
            "Alert: Inventory has exceeded 500 units!"
        )
        break

    # Generate new order ID
    new_order_id = orders[-1][0] + 1

    # Create new order
    new_order = [
        new_order_id,
        product_item,
        stock_input
    ]

    # Add order
    orders.append(new_order)

    print("\nNew Order Added:")
    print(
        f"{new_order[0]}, "
        f"{new_order[1]}, "
        f"{new_order[2]}"
    )

    print("\nOrders successfully saved to orders.txt")

    # Track transaction history
    transaction_history.append(stock_input)

    print("\nInventory units successfully saved to inventory.txt")

    # Calculate tax
    tax = calculate_tax(stock_input)

    # Update stock quantity
    stock_quantity = new_total


    print("\n===== Current Delivery Summary =====")

    # Delivery quantity
    if stock_input == 1:
        print(
            f"Total delivery amount: {stock_input} unit"
        )
    else:
        print(
            f"Total delivery amount: {stock_input} units"
        )

    # Tax
    print(
        f"Tax (10%) for this delivery: {tax:.2f}"
    )

    # Inventory quantity
    if stock_quantity == 1:
        print(
            f"Total inventory is {stock_quantity} unit"
        )
    else:
        print(
            f"Total inventory is {stock_quantity} units"
        )

    print("\n======== Current Orders ========")

    for order_id, product_name, quantity in orders:
        print(
        f"{order_id}, {product_name}, {quantity}"
        )   

    print(
    f"\nTransaction history: {transaction_history}"
    )
    # Save files
    
    save_inventory(
    stock_quantity,
    transaction_history
    )

    save_orders(orders)

# Generate final report
generate_reports(
    stock_quantity,
    failed_entries,
    transaction_history
)