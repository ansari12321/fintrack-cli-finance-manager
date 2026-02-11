from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import ForeignKey, create_engine, text

engine=create_engine("sqlite:///fintrack.db")
Base=declarative_base()
Session=sessionmaker(bind=engine)
session=Session()

class Category(Base):
    __tablename__="categories"
    id=Column(Integer,primary_key=True)
    name=Column(String)
    expenses=relationship("Expense",back_populates="category")

class Expense(Base):
    __tablename__="expenses"
    id=Column(Integer,primary_key=True)
    title=Column(String)
    date=Column(String)
    amount=Column(Float)

    category_id=Column(Integer,ForeignKey("categories.id"))
    category=relationship("Category",back_populates="expenses")

class Budget(Base):
    __tablename__="budgets"
    id=Column(Integer,primary_key=True)
    month=Column(String)
    limit=Column(Float)

class Subscription(Base):
    __tablename__="subscriptions"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    amount = Column(Float)
    next_date = Column(String)

Base.metadata.create_all(engine)

#creat functions
def add_category():
    name=input("category name: ")
    session.add((Category(name=name)))
    session.commit()
    print("Category added successfully")

def add_expense():
    title=input("Expense title: ")
    amount=float(input("Amount: "))
    date=input("Date (yyyy-mm-dd): ")
    category_id=int(input("Category id: "))
    session.add(Expense(title=title,amount=amount,category_id=category_id))
    session.commit()
    print("Expense added successfully: ")

def update_expense():
    ex_id=int(input("Expense id: "))
    expense=session.query(Expense).filter(Expense.id==ex_id).first()

    if expense:
        expense.title=input("New title: ")
        expense.amount=float(input("New amount: "))
        session.commit()
        print("Expense updated")
    else:
        print("Expense nit found")

def delete_expense():
    ex_id=int(input("expense id: "))
    expense=session.query(Expense).filter(Expense.id==ex_id).first()

    if expense:
        session.delete(expense)
        session.commit()
        print("Expense deleted successfully:")
    else:
        print("Expense not sound")

def search_by_date():
    date=input("Enter date: ")
    expenses=session.query(Expense).filter(Expense.date==date).all()
    print("\n Expenses....")
    for e in expenses:
        print(e.id,"-",e.title,"-",e.amount,"-",e.category.name)

def add_subscription():
    name = input("Subscription name: ")
    amount = float(input("Amount: "))
    next_date = input("Next payment date: ")

    session.add(Subscription(name=name,amount=amount,next_date=next_date))
    session.commit()

    print("Subscription added")

def view_subscriptions():
    subs = session.query(Subscription).all()
    print("\n Subscriptions...")
    for s in subs:
        print(s.id, "-", s.name, "-", s.amount, "-", s.next_date)

def category_report():
    sql = text(""" SELECT c.name, SUM(e.amount) FROM categories c JOIN expenses e ON c.id = e.category_id GROUP BY c.name """)
    result=session.execute(sql)
    print("\n Category Expense Report...")
    for row in result:
        print(row[0], "→", row[1])

def set_budget():
    month = input("Enter month: ")
    limit = float(input("Enter spending limit: "))

    # create and save budget
    budget = Budget(month=month, limit=limit)
    session.add(budget)
    session.commit()

    print("Budget saved successfully")


while True:
    print("\n=== FinTrack Pro ===")
    print("1. Add Category")
    print("2. Add Expense")
    print("3. Update Expense")
    print("4. Delete Expense")
    print("5. Search by Date")
    print("6. Set Budget")
    print("7. Add Subscription")
    print("8. View Subscriptions")
    print("9. Category Report")
    print("10. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        add_category()

    elif choice == "2":
        add_expense()

    elif choice == "3":
        update_expense()

    elif choice == "4":
        delete_expense()

    elif choice == "5":
        search_by_date()

    elif choice == "6":
        set_budget()

    elif choice == "7":
        add_subscription()

    elif choice == "8":
        view_subscriptions()

    elif choice == "9":
        category_report()

    elif choice == "10":
        break

    else:
        print("Invalid choice")



