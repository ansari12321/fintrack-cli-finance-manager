FinTrack Pro — Python CLI Expense Manager

FinTrack Pro is a simple command-line finance tracking application built using Python and SQLAlchemy ORM with SQLite. It allows users to manage categories, expenses, subscriptions, and budgets in an organized way.

This project demonstrates practical use of:

SQLAlchemy ORM relationships

CRUD database operations

SQLite persistence

CLI menu-driven application design

🚀 Features

✔ Add and manage expense categories
✔ Record daily expenses
✔ Update or delete expenses
✔ Search expenses by date
✔ Set monthly budgets
✔ Manage subscriptions
✔ Generate category-wise expense reports
✔ Persistent SQLite database storage

🛠 Technologies Used

Python 3.x

SQLAlchemy ORM

SQLite database

📂 Project Structure
FinTrack-Pro/
│
├── fintrack.py      # Main application file
├── fintrack.db      # SQLite database (auto-created)
└── README.md        # Project documentation

⚙ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/your-username/fintrack-pro.git
cd fintrack-pro

2️⃣ Create virtual environment (recommended)
python -m venv venv


Activate it:

Windows

venv\Scripts\activate


Mac/Linux

source venv/bin/activate

3️⃣ Install dependencies
pip install sqlalchemy

4️⃣ Run the application
python fintrack.py


The database will be created automatically on first run.

📌 How to Use

When you run the program, you’ll see a menu:

=== FinTrack Pro ===
1. Add Category
2. Add Expense
3. Update Expense
4. Delete Expense
5. Search by Date
6. Set Budget
7. Add Subscription
8. View Subscriptions
9. Category Report
10. Exit


Simply enter the number corresponding to the action you want.

🧠 Database Design
Category

Stores expense categories.

Expense

Tracks expenses with:

Title

Amount

Date

Linked category

Budget

Stores monthly spending limits.

Subscription

Tracks recurring payments.

Relationships are handled using SQLAlchemy ORM.

📊 Example Workflow

Add categories (Food, Travel, Bills)

Record expenses under categories

Search expenses by date

Generate category report

Manage subscriptions

🔮 Future Improvements

Budget alerts

Monthly analytics

GUI interface

CSV export

Authentication system

🤝 Contributing

Contributions are welcome!

Steps:

Fork the repo

Create a new branch

Commit changes

Submit a pull request

📜 License

This project is open-source and free to use for learning purposes.

👨‍💻 Author

Developed as a Python + SQLAlchemy learning project.
