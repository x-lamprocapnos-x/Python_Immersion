# Initialize empty lists to store recipes and ingredients
recipes_list = [] # Stores all recipe dictionaries 
ingredients_set = set() # Stores ingredients

# Function to take the user's recipe input and return it as a dictionary
def take_recipes():
    # Prompt user for recipe name
    name = input("Enter the recipe name: ") 

    # Validate cooking time input
    while True:
        try:
            cooking_time = int(input("Enter the cooking time (minutes): "))
            if cooking_time <= 0:
                print("Cooking time must be a positive number. Try again.")
                continue
            break # Exit loop if input is valid
        except ValueError:
            print("Invalid input. Please enter a positive number for cooking time.")

    # Prompt user for ingredients and split into a list
    ingredients = input("Enter the ingredients, serperated by commas: ").split(", ")

    # Create and return the recipe dictionary
    recipe = {
        "name": name,
        "cooking_time": cooking_time,
        "ingredients": ingredients
    }
    return recipe

# Main program logic
while True:
    try: 
        # Prompt the user for how many recipes they would like to add
        n = int(input("How many recipes would you like to add?"))
        if n <= 0:
            print("Please enter a positive number of recipes.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a positive number.")

for i in range(n):
    # Collect recipe from user
    recipe = take_recipes()

    # Update ingredients set
    for ingredient in recipe["ingredients"]:
        # Add ingredient to the set if not already present
        ingredients_set.add(ingredient)

    # Add the recipe to recipes_list
    recipes_list.append(recipe)
    

# Detemine difficulty levels for each recipe
for recipe in recipes_list:
    cooking_time = recipe["cooking_time"]
    num_ingredients = len(recipe["ingredients"])

    # Determine difficulty level based on conditions
    if cooking_time < 10 and num_ingredients < 4:
        difficulty = "Easy"
    elif cooking_time < 10 and num_ingredients > 4:
        difficulty = "Medium"
    elif cooking_time >= 10 and num_ingredients > 4:
        difficulty = "Intermediate"
    else:
        difficulty = "Hard"

    # Add the difficulty to the recipe dictionary
    recipe["difficulty"] = difficulty

# Print the results
print("\nRecipes List: ")
for recipe in recipes_list:
    print("Recipe: ", recipe["name"])
    print("Cooking time (minutes): ", recipe["cooking_time"])
    print("Ingredients: ", ", ".join(recipe["ingredients"]))
    print("Difficulty: ", recipe["difficulty"])
    print("-" * 30) # Recipe end indication

# Sort ingredients alphabetically
ingredients_list = sorted(ingredients_set)

# Print all ingredients
print("\nIngredients List: ")
for ingredient in ingredients_list:
    print(ingredient)
