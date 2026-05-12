# ---------------------------------------------------
# E-commerce Order Processing System
# ---------------------------------------------------

orders = [

    [
        (101, "Laptop", 999.99, 1),
        (102, "Mouse", 25.50, 2),
        (103, "Keyboard", 75.00, 1)
    ],

    [
        (101, "Laptop", 999.99, 2),
        (104, "Monitor", 299.99, 1),
        (105, "Webcam", 89.99, 1)
    ],

    [
        (102, "Mouse", 25.50, 3),
        (103, "Keyboard", 75.00, 2),
        (106, "Headphones", 199.99, 1)
    ]

]

threshold_value = 1000.00


# ---------------------------------------------------
# 1. Calculate Total Value of Each Order
# ---------------------------------------------------

order_totals = []

print("Order Totals:\n")

for i, order in enumerate(orders, start=1):

    total = sum(price * quantity for _, _, price, quantity in order)

    order_totals.append(total)

    print(f"Order {i} Total: ${total:.2f}")


# ---------------------------------------------------
# 2. Find Most Expensive Single Item
# ---------------------------------------------------

most_expensive = max(

    (item for order in orders for item in order),

    key=lambda x: x[2]

)

print("\nMost Expensive Item:")

print(f"{most_expensive[1]} (${most_expensive[2]})")


# ---------------------------------------------------
# 3. Product Quantity Summary
# ---------------------------------------------------

product_summary = {}

for order in orders:

    for product_id, product_name, price, quantity in order:

        if product_name in product_summary:

            product_summary[product_name] += quantity

        else:
            product_summary[product_name] = quantity

print("\nProduct Quantity Summary:\n")

for product, qty in product_summary.items():

    print(f"{product}: {qty} units")


# ---------------------------------------------------
# 4. Orders Exceeding Threshold
# ---------------------------------------------------

print(f"\nOrders Exceeding ${threshold_value}:\n")

for i, total in enumerate(order_totals, start=1):

    if total > threshold_value:

        print(f"Order {i}: ${total:.2f}")


# ---------------------------------------------------
# 5. Unique Products Ordered
# ---------------------------------------------------

unique_products = {}

for order in orders:

    for product_id, product_name, price, quantity in order:

        unique_products[product_id] = product_name

print("\nUnique Products Ordered:\n")

for pid, pname in unique_products.items():

    print(f"{pid}: {pname}")