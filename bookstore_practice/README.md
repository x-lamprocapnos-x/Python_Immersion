# **Django Bookstore App**

### A simple Django-based inventory and sales management system for a bookstore. This app handles books, customers, sales tracking, and salesperson profiles.

## **Features**
- ***Book Management***
Add, categorize, and manage books with support for multiple genres and formats.

- ***Customer Records***
Keep notes and records for each customer.

- ***Sales Tracking***
Record sales by quantity, price, and timestamp.

- ***Salesperson Profiles***
Manage profiles linked to Django's built-in User model.

- ***Testing***
Basic unit tests implemented for the Book model.

## **Apps Overview**
| App | Purpose |
|---|---|
| `books` | Manages book data and genres |
| `customers` | Stores customer details and notes |
| `sales` | Tracks sales of books |
| `salesperson` | Profiles linked to Django users |

## **Tech Stack**
- Backend: Django 4.2
- Database: SQLite3
- Language: Python 3.x

## **Installation**
1. Clone the repo
`git clone https://github.com/your-username/bookstore.git`
`cd bookstore`

2. Create and activate a virtual environment
`python -m venv env`
`source env/bin/activate`  # On Windows use `env\Scripts\activate`

3. Install dependencies
`pip install -r requirements.txt`

4. Apply migrations and run the server
`python manage.py migrate`
`python manage.py runserver`

**Example Model**
```python
class Book(models.Model):
    name = models.CharField(max_length=120)
    price = models.FloatField(help_text='in US dollars $')
    genre = models.CharField(max_length=12, choices=genre_choices, default='cl')
    book_type = models.CharField(max_length=12, choices=book_type_choices, default='hc')
```
**Run Tests**
`python manage.py test`

## **Dependencies**
- Django
- MySQLClient
- SQLAlchemy
- Python-dotenv


