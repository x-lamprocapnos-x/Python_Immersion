# Import the mysql connector module
import os
from dotenv import load_dotenv
import mysql.connector

# Load environment variables
load_dotenv()

# Get database credentials from environment variables
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

# Check if any variable is missing
if not all([DB_HOST, DB_USER, DB_PASSWORD, DB_NAME]):
    raise ValueError("Missing database environment variables. Check your .env file. ")

# Function to initialize the database
def initialize_database():
    # Connect to the MySQL server
    connection = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    cursor = connection.cursor()

    # Create database if it does not exist
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")

    # Use the database
    cursor.execute(f"USE {db_name}")

    # Create Recipes table if it does not already exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Recipes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    ingredients TEXT NOT NULL,
    cooking_time INT NOT NULL,
    difficulty VARCHAR(20) NOT NULL
    )
    """)
    connection.commit()
    return connection

class Recipe:
    # Initialize the recipe with a name, ingredients and cooking time
    def __init__(self, name, ingredients, cooking_time):
        self.name = name
        self.ingredients = ingredients
        self.cooking_time = cooking_time
        self.difficulty = self.calculate_difficulty()

    # Calculate recipe difficulty
    def calculate_difficulty(self):
        if self.cooking_time < 10 and len(self.ingredients) < 4:
            return "Easy"
        elif self.cooking_time < 10:
            return "Medium"
        elif len(self.ingredients) < 4:
            return "Intermediate"
        else:
            return "Hard"

    # Add recipe to database
    def add_to_database(self, connection):
        try:
            cursor = connection.cursor()
            ingredients_str = ", ".join(self.ingredients)
            query = "INSERT INTO Recipes (name, ingredients, cooking_time, difficulty) VALUES (%s, %s, %s, %s)"
            values = (self.name, ingredients_str, self.cooking_time, self.difficulty)
            cursor.execute(query, values)
            connection.commit()
            print(f"Recipe added to database! Recipe ID: {cursor.lastrowid}")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    # Search recipe by ingredient
    def search_by_ingredient(connection):
        try:
            cursor = connection.cursor()

            # Fetch all ingredients from the database
            cursor.execute("SELECT ingredients FROM Recipes")
            results = cursor.fetchall()

            # Extract unique ingredients
            all_ingredients = []
            for row in results:
                ingredients = row[0].split(", ")
                for ingredient in ingredients:
                    if ingredient not in all_ingredients:
                        all_ingredients.append(ingredient)
                
            
            # Display the list of unique ingredients
            print("\nAvailable ingredients: ")
            for i, ingredient in enumerate(sorted(all_ingredients), start=1):
                print(f"{i}. {ingredient}")
            
            # Prompt user to choose ingredient
            try:
                choice = int(input("Choose an ingredient by number: "))
                if choice < 1 or choice > len(all_ingredients):
                    print("Invalid choice. Please try again")
                    return
            except ValueError:
                print("Invalid input. Please enter a number.")
                return

            # Get the selected ingredient
            search_ingredient = all_ingredients[choice - 1]

            # Search for recipes containing the selected ingredient
            query = "SELECT * FROM Recipes WHERE ingredients LIKE %s"
            values = (f"%{search_ingredient}%",)
            cursor.execute(query, values)
            results = cursor.fetchall()

            # Display results
            if results:
                print(f"\nRecipes containing '{search_ingredient}':")
                for recipe in results:
                    print(f"ID: {recipe[0]}, name: {recipe[1]}, ingredient: {recipe[2]}, Cooking Time: {recipe[3]}, Difficulty: {recipe[4]}")
            else:
                print(f"No recipes found for that ingredient: {search_ingredient}")
        except (ValueError, IndexError):
                print("Invalid selection.")
        except mysql.connector.Error as err:
                print(f"Database Error: {err}")

    # Update recipe
    def update_recipe(connection, recipe_id):
        try:
            cursor = connection.cursor()

            # Display available recipes
            cursor.execute("SELECT id, name FROM Recipes")
            recipes = cursor.fetchall()
            if recipes:
                print("\nAvailable Recipes:")
                for recipe in recipes:
                    print(f"ID:{recipe[0]}, Name: {recipe[1]}")
            else:
                print("No recipes available.")
                return

            # Ask for recipe ID
            recipe_id = int(input("\nEnter the Recipe ID to update: "))
            cursor.execute("SELECT * FROM Recipes WHERE id = %s", (recipe_id,))
            recipe = cursor.fetchone()
            if not recipe:
                print("Recipe not found.")
                return

            # Display current details and prompt for update
            print(f"Current Recipe: ID={recipe[0]}, Name={recipe[1]}, Ingredients={recipe[2]}, Cooking Time={recipe[3]}, Difficulty={recipe[4]}")
            print("What would you like to update?")
            print("1. Name")
            print("2. Ingredients")
            print("3. Cooking Time")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                new_name = input("Enter the new recipe name: ")
                cursor.execute("UPDATE Recipes SET name = %s WHERE id = %s", (new_name, recipe_id))
            elif choice == 2:
                new_ingredients = input("Enter the new ingredients (comma-seperated): ").split(", ")
                ingredients_str = ", ".join(new_ingredients)
                difficulty = Recipe("", new_ingredients, recipe[2]).calculate_difficulty()
                cursor.execute("UPDATE Recipes SET ingredients = %s, difficulty = %s WHERE id = %s", (ingredients_str, difficulty, recipe_id))
            elif choice == 3:
                new_cooking_time = int(input("Enter the new cooking time:"))
                difficulty = Recipe("", recipe[3].split(", "), new_cooking_time).calculate_difficulty()
                cursor.execute("UPDATE Recipes SET cooking_time = %s, difficulty = %s WHERE id = %s", (new_cooking_time, difficulty, recipe_id))  
            else:
                print("Invalid choice, try again.")

            connection.commit()
            print("Recipe updated!")

        except ValueError:
            print("Invalid input. Update cancelled")
        except mysql.connector.Error as err:
            print(f"Database Error: {err}")

    # Delete recipe
    def delete_recipe(connection):
        try:
            cursor = connection.cursor()

            # Display all recipes
            cursor.execute("SELECT id, name FROM Recipes")
            recipes = cursor.fetchall()
            if not recipes:
                print("No recipes available to delete")
                return

            print("n\Available Recipes:")
            for recipe in recipes:
                print(f"ID: {recipe[0]}, Name: {recipe[1]}")

            recipe_id = int(input("Enter the recipe ID to delete: "))
            cursor.execute("DELETE FROM Recipes WHERE id = %s", (recipe_id,))
            connection.commit()
            print("Recipe deleted!")
        except ValueError:
            print("Invalid input.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

# Main Menu logic
def main():
    connection = initialize_database()

    try:
        # Print the menu with options
        while True:
            print("\nRecipe App Menu:")
            print("1. Create a new recipe")
            print("2. Search for recipes by ingredient")
            print("3. Update an existing recipe")
            print("4. Delete a recipe")
            print("5. Exit")

            choice = input("Enter your choice: ")

            # Add recipes
            if choice == "1":
                # Prompt user for number of recipes to add
                try:
                    num_recipes = int(input("How many recipes would you like to add? "))
                    if num_recipes <=0:
                        print("Please enter a positive number.")
                        continue
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
                    continue

                # Add multiple recipes
                for i in range(num_recipes):
                    print(f"\nEntering recipe {i + 1} of {num_recipes}:")
                    name = input("Enter the recipe name: ")
                    ingredients = input("Enter the ingredients (comma-separated): ").split(", ")
                    cooking_time = int(input("Enter the cooking time in minutes: "))
                    recipe = Recipe(name, ingredients, cooking_time)
                    recipe.add_to_database(connection)

            # Search for a recipe by ingredient
            elif choice == "2":
                ingredient = input("Enter the ingredient to search for: ")
                Recipe.search_by_ingredient(connection)

            # Update a recipe
            elif choice == "3":
                recipe_id = int(input("Enter the recipe ID to update: "))
                new_name = input("Enter the new recipe name: ")
                new_ingredients = input("Enter the new ingredients (comma-separated): ").split(", ")
                new_cooking_time = int(input("Enter the new cooking time in minutes: "))
                Recipe.update_recipe(connection, recipe_id)

            # Delete a recipe
            elif choice == "4":
                recipe_id = int(input("Enter the recipe ID to delete: "))
                Recipe.delete_recipe(connection)

            # Exit menu
            elif choice == "5":
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")
    finally:
        if connection.is_connected():
            connection.close()

if __name__ == "__main__":
    main()





