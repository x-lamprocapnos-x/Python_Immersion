# Import pickle
import pickle

# Create recipe dictionary 
recipe = {
    "Name": "Tea",
    "Ingredients": ["Tea leaves, Water, Sugar"],
    "Cooking Time": 5,
    "Difficulty": "Easy"
}

# Store the dictionary in a binary file
with open("recipe_binary.bin", "wb") as binary_file:
    pickle.dump(recipe, binary_file)

# Load data back into script
with open("recipe_binary.bin", "rb") as binary_file:
    loaded_recipe = pickle.load(binary_file)

print("Recipe Information:")
print(f"Name: {loaded_recipe['Name']}")
print(f"Ingredients: {','.join(loaded_recipe['Ingredients'])}")
print(f"Cooking Time: {loaded_recipe['Cooking Time']} minutes")
print(f"Difficulty: {loaded_recipe['Difficulty']}")