# CodeAlpha_Stock-Portfolio-Tracker
# 💹 Stock Portfolio Tracker — CodeAlpha Internship (Task 2)

This is a simple **console-based Stock Portfolio Tracker** built in Python as part of my internship at **CodeAlpha**. The program allows users to input stock symbols and quantities, calculates the total investment value based on predefined stock prices, and optionally exports the portfolio to a `.csv` file.

---

## ✅ Features

- 📈 Input stock symbol and quantity
- 🧠 Validates user input and handles errors gracefully
- 🗃 Uses a hardcoded dictionary for stock prices (e.g., AAPL, TSLA, GOOGL, MSFT)
- 🧮 Calculates and displays total investment summary
- 📁 Option to export the data into a CSV file

---

## 🧱 Technologies Used

- Python 3
- Built-in libraries: `csv`, `input()`, `dict`, `loops`, `conditionals`

---

## 🚀 How It Works

1. Run the script.
2. Enter stock symbols (e.g., `AAPL`, `TSLA`) and quantities.
3. Type `done` when finished.
4. View the investment summary.
5. Choose to export results as a `.csv`.

---

## 📦 Example Stocks (Hardcoded)

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2700,
    "MSFT": 330
}

---

## Sample Output

Enter stock symbol and quantity (type 'done' to finish):
Stock Symbol: AAPL
Quantity: 5
Stock Symbol: TSLA
Quantity: 2
Stock Symbol: done

Investment Summary:
• AAPL x 5 @ $180 = $900
• TSLA x 2 @ $250 = $500

Total Investment: $1400

Do you want to save this to CSV? (y/n):

---

## 📁 File Structure

stock_portfolio_tracker/
├── investment_summary.csv   # (Generated after saving)
└── stock_tracker.py         # Main script

---
## 🧠 What I Learned

Handling user input and data validation

Working with dictionaries and basic arithmetic

Writing data to CSV files using Python's csv module

Building logic-driven applications with clean structure

---

## 📌 How to Run

python stock_portfolio_tracker.py

---

## 🔗 Connect with Me

Let's connect on LinkedIn 🚀
Feel free to ⭐️ this repo if you found it helpful!
