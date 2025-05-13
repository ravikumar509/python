# Expense Tracker
CLI (Command Line Interface) project to track daily expenses.


## 📁 Project Structure

├── venv/ # Virtual environment (ignored by Git)
├── src/ # Source code directory
│ └── data
│       └── balance.json
│       └── expenses.json
│ └── tracker
│       └── Expense.py
│       └── Tracker.py
│ └── utils
│       └── FileOperations.py
│       └── Tracker.py
│ └── main.py
├── .gitignore
├── requirements.txt # Project dependencies
└── README.md



## 🚀 Getting Started

### 1. Clone the Repository

```
bash
```
git clone https://github.com/ravikumar509/python.git
cd python 

### 2. Create and Activate a Virtual Environment
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

### 3. Install Dependencies
pip install -r requirements.txt

### 4.Run the Application
python Finance/src/main.py

🛑 Git Ignore
The .gitignore file ensures that development environment files like venv/ are not tracked by Git.
venv/
__pycache__/
*.pyc
*.log
.env


## 📦 Modules

### `data/balance.json`
Stores the final calculated balance of all transactions. Format: JSON.  
Used for quick access to the current account status.

### `data/expense.json`
Holds detailed transaction history, including income and expenses.  
Each entry is stored in JSON format with attributes such as type, amount, category, and date.

### `tracker/Tracker.py`
Contains the `Expense` class, which models a single transaction.

#### 🧾 `Expense` Class
A simple data model for an income or expense entry.

**Constructor:**
```python
def __init__(self, expense_type, amount, category, date):

-Attributes:

-expense_type: "income" or "expense"

-amount: Transaction amount (float or int)

-category: Expense category (e.g., "food", "salary", "transport")

-date: Date of the transaction (string or date object)

-Purpose:
-Used to create structured transaction records that can be saved to or read from expense.json.

