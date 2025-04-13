# Imports
import os 
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Load environment variables from .env file
load_dotenv()

# Get credentials from environment variables
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

# Check if any variable is missing
if not all([DB_HOST, DB_USER, DB_PASSWORD, DB_NAME]):
    raise ValueError("Missing database environment variables. Check your .env file. ")

# Secure database connection
engine = create_engine(f"mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}", echo=True)

# Create a Session
Session = sessionmaker(bind=engine)
session = Session()

# Create Base Class
Base = declarative_base()
 
# Define the recipe model
class Recipe(Base):
    __tablename__ = "final_recipes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))

    # Automatically set difficulty when a new recipe is created
    def __init__(self, name, ingredients, cooking_time):
        self.name = name
        self.ingredients = ingredients
        self.cooking_time = cooking_time
        self.calculate_difficulty() # Automatically calculates difficulty when create

    # Quick Info on the recipe
    def __repr__(self):
        return "<Recipe ID: " + str(self.id) + "-" + self.name + ">"

    # Full Info on the recipe
    def __str__(self):
        return (
            f"{'-'*10}\n"
            f"Dish: {self.name}\n"
            f"Ingredients: {self.ingredients}\n"
            f"Cooking Time: {self.cooking_time}\n"
            f"Difficulty {self.difficulty}\n"
            f"{'-'*10}\n"
            "Hop to it and Enjoy!"
        )

    # Automatically Calculate recipe difficulty based on ingredients and time
    def calculate_difficulty(self):
        if self.cooking_time < 10 and len(self.ingredients.split(", ")) < 4:
            self.difficulty = "Easy"
        elif self.cooking_time < 10 and len(self.ingredients.split(", ")) > 4:
            self.difficulty = "Intermediate"
        elif self.cooking_time > 10 and len(self.ingredients.split(", ")) > 4:
            self.difficulty = "Moderate"
        else: 
            self.difficulty = "Hard"

# Create the Table in MySQL
Base.metadata.create_all(engine)

print("Database and table successfully created.")

# Define the main functions 
def create_recipe():
    # Create session
    session = Session()

    # Collect and validate recipe name
    while True:
        name = input("Enter the name for your recipe: ")
        if len(name) > 50:
            print("Error: Name cannot be longer than 50 characters. Try Again.")
        elif not name.replace(" ", "").isalpha(): # Allow spaces in the name
            print("Error: Name must contain only letters. Try Again.")
        else:
            break

    # Collect ingredients 
    ingredients = []
    n = int(input("How many ingredients does the recipes have? "))

    for i in range(n):
        ingredient = input(f"Enter ingredient {i+1}: ")
        ingredients.append(ingredient)

    # convert ingredients list into a string
    ing_string = ", ".join(ingredients)
  
    # Collect and validate cooking time
    while True:
        cooking_time = input("Enter a cooking time (in minutes): ")
        if not cooking_time.isnumeric() or int(cooking_time) < 0: # Handle negative cooking time
            print("Error: Cooking time must be a positive number. Try Again.")
        else:
            cooking_time = int(cooking_time)
            break

    # Create new recipe object
    recipe_entry = Recipe(
        name = name,
        ingredients = ing_string,
        cooking_time = cooking_time
    )

    session.add(recipe_entry)
    session.commit()

    print("Recipe added successfully!")
    session.close()

def view_all_recipes():
    # Create session
    session = Session()

    # Retrieve all recipes in the database as a list
    recipes_list = session.query(Recipe).all()

    # Check if list is empty
    if not recipes_list:
        print("No recipes found in the database.")
        return None
    
    # Call __str__ method to print all recipes
    for recipe in recipes_list:
        print(recipe)

    # Close session
    session.close()

def search_by_ingredients():
    # Create session
    session = Session()

    # Check for table entries
    recipe_count = session.query(Recipe).count()
    if recipe_count == 0:
        print("No recipes found in the database.")
        return None

    # Retrieve ingredients column only
    results = session.query(Recipe.ingredients).all()

    # Initialize empty ingredients list
    all_ingredients = []

    # Split ingredients into list, append to all ingredients if not already there
    for result in results:
        ingredients_list = result[0].split(", ")
        for ingredient in ingredients_list:
            if ingredient not in all_ingredients:
                all_ingredients.append(ingredient)

    # Display available ingredients and ask which to search
    print("\nAvailable ingredients: ")
    for idx, ingredient in enumerate(all_ingredients, start=1):
        print(f"{idx}. {ingredient}")
    selected_ingredients = input("Enter the numbers of ingredients you would like to search for: ")

    # Check if user input is valid
    try:
        selected_indices = [int(i) for i in selected_ingredients.split()]
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return None

    if any (i < 1 or i > len(all_ingredients) for i in selected_indices):
        print("Error: Invalid selection. Please enter numbers from the displayed options.")
        return None
    
    # Make a list of the selected ingredients to search for
    search_ingredients = [all_ingredients[i-1] for i in selected_indices]

    # Initialize empty conditions list
    conditions = []

    # Loop through search_ingredients and create like() conditions
    for ing in search_ingredients:
        like_term = f'%{ing}%'
        conditions.append(Recipe.ingredients.like(like_term))

    # Retrieve recipes from the database using filter() with conditions
    # Use 'and_' to combine the conditions so that all ingredients must be present
    from sqlalchemy import and_
    matching_recipes = session.query(Recipe).filter(and_(*conditions)).all()

    if not matching_recipes:
        print("No recipes found including all your selected ingredients.")
    else:
        for recipe in matching_recipes:
            print(recipe)

    # Close session
    session.close()

def edit_recipe():
    session = Session()

    # Get all recipes to show the user
    recipes = session.query(Recipe.id, Recipe.name).all()

    if not recipes:
        print("No recipes found in the database.")
        session.close()
        return None

    # Show recipes
    print("\nAvailable recipes: ")
    for recipe_id, recipe_name in recipes:
        print(f"{recipe_id}. {recipe_name}")

    # Ask the user for the recipe ID to edit
    try:
        recipe_id = int(input("n\Enter the ID of the recipe you want to edit: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        session.close()
        return None

    # Retrieve the recipe from the database
    recipe_to_edit = session.query(Recipe).filter_by(id=recipe_id).first()

    if not recipe_to_edit:
        print("Recipe not found.")
        session.close()
        return None

    # Ask user what to edit 
    print("\nWhat would you like to edit?")
    print("1. Name")
    print("2. Ingredients")
    print("3. Cooking Time")

    choice = input("Enter the number of the field you want to edit:")

    if choice == "1":
        new_name = input("Enter new recipe name: ")
        if len(new_name) <= 50:
            recipe_to_edit.name = new_name
        else:
            print("Error: Name cannot exeed 50 characters.")
    elif choice == "2":
        new_ingredients = input("Enter new ingredients (comma-seperated): ")
        recipe_to_edit.ingredients = new_ingredients
    elif choice == "3":
        try:
            new_cooking_time = int(input("Enter new cooking time (in minutes): "))
            recipe_to_edit.cooking_time = new_cooking_time
        except ValueError:
            print("Error: Cooking time must be a number.")
            session.close()
            return None

        else:
            print("Invalid choice. No changes were made.")
            session.close()
            return None

        # Recalculate difficulty and commit changes
        recipe_to_edit.calculate_difficulty()
        session.commit()
        print("Recipe updated successfully!")

        session.close()

def delete_recipe():
    session = Session()

    # Get all recipes
    recipes = session.query(Recipe.id, Recipe.name).all()

    if not recipes:
        print("No recipes found in the database.")
        session.close()
        return None

    # Show available recipes
    print("\n Available recipe:")
    for recipe_id, recipe_name in recipes:
        print(f"{recipe_id}. {recipe_name}")

    # Ask the user which recipe to delete
    try:
        recipe_id = int(input("\nEnter the ID of the recipe you want to delete: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        session.close()
        return None

    # Retrieve the recipe
    recipe_to_delete = session.query(Recipe).filter_by(id=recipe_id).first()

    if not recipe_to_delete:
        print("Recipe not found.")
        session.close()
        return None

    # Confirm deletion
    confirm = input(f"Are you sure you want to delete {recipe_to_delete.name}? (yes/no): ").strip().lower()
    if confirm == "yes":
        session.delete(recipe_to_delete)
        session.commit()
        print("Recipe deleted successfully!")
    else:
        print("Deletion canceled.")

    session.close()

def main_menu():
    # Menu Options
    while True:
        print("\nRecipe App - Main Menu")
        print("1. Add a new recipe")
        print("2. View all recipes")
        print("3. Search recipes by ingredients")
        print("4. Edit a recipe")
        print("5. Delete a recipe")
        print("6. Quit")

        # Ask user to choose from the menu
        choice = input("Enter your choice: ")

        if choice == "1":
            create_recipe()
        elif choice == "2":
            view_all_recipes()
        elif choice == "3":
            search_by_ingredients()
        elif choice == "4":
            edit_recipe()
        elif choice == "5":
            delete_recipe()
        elif choice == "6":
            print("Good-bye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1-6.")

# Run the app
if __name__ == "__main__":
    main_menu()



    


