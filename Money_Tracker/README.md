# 💰 Money Tracker

A simple yet powerful **command-line personal finance tracker** built with Python.  
It helps you record income, expenses, transfers, and view insightful summaries — all stored neatly in Excel (`Money Tracker.xlsx`) and JSON files.

---

## 🚀 Features

- **Add Income & Expenses**  
  Categorize every transaction easily.

- **Account Management**  
  Supports multiple account types (Cash, Bank, etc.) with live balance tracking.

- **Transfer Between Accounts**  
  Move money securely between accounts with validation.

- **Dynamic Categories**  
  Add or modify income and expense categories anytime.

- **Automatic Excel Logging**  
  Every transaction is saved to `Money Tracker.xlsx`.

- **Insightful Summary View**
  - Total Income, Expense, and Net Savings  
  - Account-wise balances  
  - Category-wise spending  
  - Monthly income vs expense  
  - Last 5 recent transactions

---

## 🗂 Folder Structure

Money_Tracker/
│
├── Money_Tracker.py # Main script (run this)
├── Money Tracker.xlsx # Auto-created Excel log
├── Accounts.json # Stores accounts and balances
├── Income_category.json # Income categories
├── Expense_category.json # Expense categories
└── requirements.txt # Dependencies

---

## ⚙️ Installation

1. **Clone or download** the project folder.  
2. Make sure you have Python **3.10+** installed.  
3. Install dependencies:
   ```bash
   pip install -r requirements.txt