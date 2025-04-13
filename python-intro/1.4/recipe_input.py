# Import the pickle module
import pickle

# Function to take recipe input from the user
def take_recipe():
    name = input("Enter the recipe name: ")

    # Validate cooking time input
    while True:
        try:
            cooking_time = int(input("Enter the cooking time (in minutes): "))
            if cooking_time < 0:
                print("Cooking time must be a positive number. Please try again.")
                continue
            break  # Exit loop if input is valid
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Prompt user for ingredients
    ingredients = input("Enter the ingredients, separated by commas: ").split(", ")

    # Return the recipe dictionary
    recipe = {
        "name": name,
        "cooking_time": cooking_time,
        "ingredients": ingredients
    }
    return recipe

# Function to calculate recipe difficulty
def calc_difficulty(recipe):
    cooking_time = recipe["cooking_time"]
    num_ingredients = len(recipe["ingredients"])

    if cooking_time < 10 and num_ingredients < 4:
        return "Easy"
    elif cooking_time < 10 and num_ingredients >= 4:
        return "Medium"
    elif cooking_time >= 10 and num_ingredients >= 4:
        return "Intermediate"
    else:
        return "Hard"

# Main program logic
# Initialize empty lists
recipes_list = []
ingredients_set = set()

# Ask user for a filename and attempt to load data
filename = input("Enter the filename to store recipes (e.g., recipe_binary.bin): ")

try:
    # Try to load existing data
    with open(filename, "rb") as file:
        data = pickle.load(file)
        recipes_list = data.get("recipes_list", [])
        ingredients_set = set(data.get("all_ingredients", []))
except FileNotFoundError:
    print(f"File '{filename}' not found. A new file will be created.")
    recipes_list = []
    ingredients_set = set()
except Exception as e:
    print(f"An error occurred: {e}")
    recipes_list = []
    ingredients_set = set()

# Ask user how many recipes they would like to add
while True:
    try:
        n = int(input("How many recipes would you like to add? "))
        if n < 0:
            print("Please enter a positive number.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

# Collect recipes and process them
for i in range(n):
    recipe = take_recipe()
    difficulty = calc_difficulty(recipe)
    recipe["difficulty"] = difficulty

    # Update recipes list
    recipes_list.append(recipe)

    # Update ingredients set
    for ingredient in recipe["ingredients"]:
        ingredients_set.add(ingredient)

# Save updated data back to the file
data = {
    "recipes_list": recipes_list,
    "all_ingredients": list(ingredients_set)
}

with open(filename, "wb") as file:
    pickle.dump(data, file)

print("\nRecipes have been saved successfully!")

# Display all recipes
print("\nRecipes List:")
for recipe in recipes_list:
    print(f"Name: {recipe['name']}")
    print(f"Cooking Time: {recipe['cooking_time']} minutes")
    print(f"Ingredients: {', '.join(recipe['ingredients'])}")
    print(f"Difficulty: {recipe['difficulty']}")
    print("-" * 30)

# Display sorted ingredients list
print("\nAll Ingredients:")
for ingredient in sorted(ingredients_set):
    print(ingredient)
