import csv

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2700,
    "MSFT": 330
}

def get_user_input():
    print("Enter stock symbol and quantity (type 'done' to finish):")
    portfolio = {}
    while True:
        symbol = input("Stock Symbol: ").strip().upper()
        if symbol == 'DONE':
            break
        if symbol not in stock_prices:
            print(f"'{symbol}' not found. Available stocks: {', '.join(stock_prices.keys())}")
            continue
        try:
            quantity = int(input("Quantity: ").strip())
            if quantity <= 0:
                print("Quantity must be a positive number.")
                continue
            portfolio[symbol] = portfolio.get(symbol, 0) + quantity
        except ValueError:
            print("Invalid quantity. Please enter a number.")
    return portfolio

def calculate_investment(portfolio):
    print("\nInvestment Summary:")
    total_value = 0
    for symbol, quantity in portfolio.items():
        price = stock_prices[symbol]
        value = price * quantity
        total_value += value
        print(f"• {symbol} x {quantity} @ ${price} = ${value}")
    print(f"\nTotal Investment: ${total_value}")
    return total_value

def save_to_csv(portfolio, filename="investment_summary.csv"):
    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Stock", "Quantity", "Price", "Total Value"])
            for symbol, quantity in portfolio.items():
                price = stock_prices[symbol]
                total = price * quantity
                writer.writerow([symbol, quantity, price, total])
        print(f"Portfolio saved to '{filename}'")
    except Exception as e:
        print(f"Failed to save file: {e}")

def main():
    portfolio = get_user_input()
    if portfolio:
        calculate_investment(portfolio)
        save = input("\nDo you want to save this to CSV? (y/n): ").strip().lower()
        if save == 'y':
            save_to_csv(portfolio)
    else:
        print("No data entered. Exiting...")

if __name__ == "__main__":
    main()