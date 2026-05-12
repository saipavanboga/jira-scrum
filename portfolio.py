# ---------------------------------------------------
# Stock Portfolio Management System
# ---------------------------------------------------

transactions = [

    ("AAPL", "BUY", 100, 150.00, "2023-01-15"),

    ("GOOGL", "BUY", 50, 2800.00, "2023-01-20"),

    ("AAPL", "BUY", 50, 160.00, "2023-02-10"),

    ("MSFT", "BUY", 75, 300.00, "2023-02-15"),

    ("AAPL", "SELL", 75, 170.00, "2023-03-05"),

    ("GOOGL", "SELL", 20, 2900.00, "2023-03-10"),

    ("TSLA", "BUY", 40, 800.00, "2023-03-15"),

    ("MSFT", "SELL", 25, 320.00, "2023-04-01"),

    ("TSLA", "SELL", 15, 750.00, "2023-04-10"),

    ("AAPL", "BUY", 25, 155.00, "2023-04-15")

]

current_prices = {

    "AAPL": 175.00,

    "GOOGL": 2850.00,

    "MSFT": 310.00,

    "TSLA": 780.00

}

# ---------------------------------------------------
# Dictionaries for calculations
# ---------------------------------------------------

holdings = {}
investment = {}
realized_pl = {}
trading_volume = {}

# ---------------------------------------------------
# Process Transactions
# ---------------------------------------------------

for stock, transaction_type, quantity, price, date in transactions:

    # Initialize dictionaries
    if stock not in holdings:

        holdings[stock] = 0
        investment[stock] = 0
        realized_pl[stock] = 0
        trading_volume[stock] = 0

    # Trading Volume
    trading_volume[stock] += quantity

    # BUY Transaction
    if transaction_type == "BUY":

        holdings[stock] += quantity

        investment[stock] += quantity * price

    # SELL Transaction
    elif transaction_type == "SELL":

        holdings[stock] -= quantity

        sell_value = quantity * price

        avg_buy_price = investment[stock] / (holdings[stock] + quantity)

        realized_profit = (price - avg_buy_price) * quantity

        realized_pl[stock] += realized_profit

        investment[stock] -= avg_buy_price * quantity


# ---------------------------------------------------
# 1. Current Holdings
# ---------------------------------------------------

print("Current Portfolio Holdings:\n")

for stock, qty in holdings.items():

    print(f"{stock}: {qty} shares")


# ---------------------------------------------------
# 2. Stock Performance Analysis
# ---------------------------------------------------

print("\nStock Performance Analysis:\n")

stock_total_pl = {}

for stock in holdings:

    current_value = holdings[stock] * current_prices[stock]

    unrealized_pl = current_value - investment[stock]

    total_pl = realized_pl[stock] + unrealized_pl

    stock_total_pl[stock] = total_pl

    print(f"{stock}:")

    print(f"- Total Investment: ${investment[stock]:.2f}")

    print(f"- Current Value: ${current_value:.2f}")

    print(f"- Realized P&L: ${realized_pl[stock]:.2f}")

    print(f"- Unrealized P&L: ${unrealized_pl:.2f}")

    print(f"- Total P&L: ${total_pl:.2f}")

    print()


# ---------------------------------------------------
# 3. Best and Worst Performing Stocks
# ---------------------------------------------------

best_stock = max(stock_total_pl, key=stock_total_pl.get)

worst_stock = min(stock_total_pl, key=stock_total_pl.get)

print(f"Best Performing Stock: {best_stock} "
      f"(${stock_total_pl[best_stock]:.2f})")

print(f"Worst Performing Stock: {worst_stock} "
      f"(${stock_total_pl[worst_stock]:.2f})")


# ---------------------------------------------------
# 4. Portfolio Summary
# ---------------------------------------------------

total_investment = sum(investment.values())

current_portfolio_value = sum(
    holdings[stock] * current_prices[stock]
    for stock in holdings
)

total_realized_pl = sum(realized_pl.values())

total_unrealized_pl = current_portfolio_value - total_investment

overall_pl = total_realized_pl + total_unrealized_pl

return_percentage = (overall_pl / total_investment) * 100

print("\nPortfolio Summary:\n")

print(f"Total Investment: ${total_investment:.2f}")

print(f"Current Portfolio Value: "
      f"${current_portfolio_value:.2f}")

print(f"Total Realized P&L: ${total_realized_pl:.2f}")

print(f"Total Unrealized P&L: "
      f"${total_unrealized_pl:.2f}")

print(f"Overall P&L: ${overall_pl:.2f}")

print(f"Return Percentage: {return_percentage:.2f}%")


# ---------------------------------------------------
# 5. Trading Volume
# ---------------------------------------------------

print("\nTrading Volume (Total Shares Traded):\n")

for stock, volume in trading_volume.items():

    print(f"{stock}: {volume} shares")