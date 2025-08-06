# Personal Finance Tracker (Flask)

A simple **personal finance management web app** built entirely with Python using **Flask**, **Jinja2 templates**, and **Bootstrap 5**.  
Users can add income and expenses, view a running balance, and test currency conversions.

---

## **Features**
- Add, view, and delete transactions (income or expenses).
- Summary cards: Total Income, Total Expense, and Balance.
- Currency conversion test (USD → CAD by default).
- Server-side rendered templates with Bootstrap 5.
- SQLite database (can switch to PostgreSQL or MySQL easily).
- `.env` file support for secret keys and API configuration.

---

## **Tech Stack**
- **Backend:** Flask 3, SQLAlchemy ORM.
- **Frontend:** Jinja2 templates + Bootstrap 5.
- **Database:** SQLite (default).
- **Utilities:** Flask-WTF forms, Requests (for currency conversion).

---

## **Installation**

### **1. Clone this repository**
```bash
git clone https://github.com/drax001/personal-finance-flask.git
cd personal-finance-flask
