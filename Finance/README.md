# Expense Tracker
CLI (Command Line Interface) project to track daily expenses.


## 📁 Project Structure

```
├── venv/ # Virtual environment (ignored by Git)
├── src/ # Source code directory
│ ├── data/ # JSON files for balance and transactions
│ │ ├── balance.json
│ │ └── expenses.json
│ ├── tracker/ # Business logic for tracking
│ │ ├── Expense.py # Expense class definition
│ │ └── Tracker.py # Core tracking logic
│ ├── utils/ # Utility functions
│ │ ├── FileOperations.py# Read/write helpers for JSON files
│ └── main.py # Entry point of the application
├── .gitignore # Files/folders to be ignored by Git
├── requirements.txt # Project dependencies
└── README.md # Project documentation
```
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
