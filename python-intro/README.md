# **Python-Intro**

### A personal learning project covering Python fundamentals, data structures, file handling, and basic CRUD operations using SQLAlchemy and MySQL. This repo showcases progression through multiple tasks — from simple scripting to building a functional command-line recipe application.

## **Project Overview**
- Task 1: Set up and run a simple Python script.

- Task 2: Experiment with Python data structures to organize recipe data.

- Task 3: Gather and display recipes from user input.

- Task 4+: Develop a fully functional command-line recipe app with persistent storage using MySQL and SQLAlchemy.

## ** Mini Pickle Demo**
Used Python's pickle module to serialize a recipe dictionary:

```python
# Save dictionary to binary files
with open("recipe_binary.bin", "wb") as binary_file:
    pickle.dump(recipe, binary_file)

# Load and display the recipe
with open("recipe_binary.bin", "rb") as binary_file:
    loaded_recipe = pickle.load(binary_file)
```

## **Full Recipe App with SQLAlchemy + MySQL**
A terminal-based application with the ability to:
- Add recipes
- View all recipes
- Search recipes by ingredients
- Edit existing recipes
- Delete recipes
**Tech Stack**
- Python
- SQLAlchemy (ORM)
- MySQL
- python-dotenv for environment variables
**Database Structure**
```python
class Recipe(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))
```

## **Features**
- Difficulty is automatically calculated based on cooking time and ingredient count.

- Ingredient search allows filtering by multiple criteria.

- Data validation and user-friendly prompts for each input.

## **Running the App**
1. Set up your .env file with your DB credentials
`DB_HOST=localhost`
`DB_USER=your_username`
`DB_PASSWORD=password`
`DB_NAME=recipe_db`
2. Install dependencies
`pip install -r requirements.txt`
3. Run the app
`python recipe_app.py`

## **Dependencies**
- sqlalchemy
- pymysql or mysql-connector-python (whichever you're using for the DB connection)
- python-dotenv
- pickleshare (if used for testing or convenience)

## **Known Issues**
- No authentication or user management (all recipes are globally editable)
- No logging or error handling beyond basic input validation
- Only works in a terminal/command-line environment
- Data must be entered manually (no import feature yet)

## **Future Ideas**
- add CLI enhancements (e.g., better menus, pagination)
- Export recipes to JSON/CSV
- Integrate Flask for a web version of the app

## **License**
This project is licensed under the MIT License — feel free to use, modify, and distribute. See the LICENSE file for full details.