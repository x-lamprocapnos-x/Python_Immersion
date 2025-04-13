# Import the pickle module to work with binary files
import pickle

# Function to display a recipe
def display_recipe(recipe):
    """Display all details of a recipe in a readable format."""
    print("Recipe Name:", recipe["name"])
    print("Cooking Time (minutes):", recipe["cooking_time"])
    print("Ingredients:", ", ".join(recipe["ingredients"]))
    print("Difficulty Level:", recipe["difficulty"])
    print("-" * 40)  # Separator for better readability

# Function to search for recipes containing a specific ingredient
def search_ingredient(data):
    """Search for recipes containing a specific ingredient."""
    all_ingredients = data["all_ingredients"]

    # Display the list of all ingredients
    print("\nAvailable Ingredients:")
    for i, ingredient in enumerate(all_ingredients, start=1):
        print(f"{i}. {ingredient}")

    # Prompt the user to select an ingredient
    while True:
        try:
            ingredient_index = int(input("\nEnter the number corresponding to the ingredient: ")) - 1
            if ingredient_index < 0 or ingredient_index >= len(all_ingredients):
                print("Invalid choice. Please try again.")
                continue
            ingredient_searched = all_ingredients[ingredient_index]
            break  # Exit the loop if a valid input is provided
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Search for recipes containing the selected ingredient
    print(f"\nRecipes containing '{ingredient_searched}':")
    found_recipes = False
    for recipe in data["recipes_list"]:
        if ingredient_searched in recipe["ingredients"]:
            display_recipe(recipe)
            found_recipes = True

    if not found_recipes:
        print(f"No recipes found containing '{ingredient_searched}'.")

# Main program logic
def main():
    # Prompt the user for the binary file containing recipe data
    filename = input("Enter the name of the binary file with the recipe data: ")

    # Try to open the file and load its contents
    try:
        with open(filename, "rb") as file:
            data = pickle.load(file)  # Load the binary file into a dictionary
    except FileNotFoundError:
        print(f"File '{filename}' not found. Please check the filename and try again.")
        return  # Exit the program if the file isn't found
    except Exception as e:
        print(f"An error occurred: {e}")
        return  # Exit the program if any other error occurs
    else:
        # Call the search_ingredient function with the loaded data
        search_ingredient(data)

# Run the script
if __name__ == "__main__":
    main()
