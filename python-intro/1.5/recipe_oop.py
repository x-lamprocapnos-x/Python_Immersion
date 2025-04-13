class Recipe:
    # Class attribute to keep track of all unique ingredients
    all_ingredients = set()

    def __init__(self, name):
        # Initialize the recipe with a name, empty ingredients list, cooking time, and difficulty
        self.name = name
        self.ingredients = []
        self.cooking_time = 0
        self.difficulty = None

    def set_name(self, name):
        # Set the recipe name
        self.name = name

    def get_name(self):
        # Get the recipe name
        return self.name

    def set_cooking_time(self, cooking_time):
        # Set the cooking time
        self.cooking_time = cooking_time
        # Recalculate difficulty when cooking time is updated
        self.calculate_difficulty()

    def get_cooking_time(self):
        # Get the cooking time
        return self.cooking_time

    def add_ingredients(self, *ingredients):
        # Add ingredients to the recipe
        for ingredient in ingredients:
            if ingredient not in self.ingredients:
                self.ingredients.append(ingredient)
        self.update_all_ingredients()

    def get_ingredients(self):
        # Get the list of ingredients
        return self.ingredients

    def calculate_difficulty(self):
        # Calculate the difficulty of the recipe
        if self.cooking_time < 10:
            if len(self.ingredients) < 4:
                self.difficulty = "Easy"
            else:
                self.difficulty = "Medium"
        else:
            if len(self.ingredients) < 4:
                self.difficulty = "Intermediate"
            else:
                self.difficulty = "Hard"
    
    def get_difficulty(self):
        # Get the difficulty of the recipe
        if self.difficulty is None:
            self.calculate_difficulty()
        return self.difficulty

    def search_ingredient(self, ingredient):
        # Check if the ingredient exists in the recipe
        return ingredient in self.ingredients

    def update_all_ingredients(self):
        # Update the class level all_ingredients set
        for ingredient in self.ingredients:
            Recipe.all_ingredients.add(ingredient)

    def __str__(self):
        # Return a string representing the recipe
        return (f"Recipe Name: {self.name}\n"
                f"Cooking Time: {self.cooking_time} minutes\n"
                f"Ingredients: {', '.join(self.ingredients)}\n"
                f"Difficulty: {self.get_difficulty()}")
    
# Define the recipe_search function
def recipe_search(data, search_term):
    # Search for recipes containing specific ingredients
    print(f"Recipe containing '{search_term}': ")
    found = False
    for recipe in data:
        if recipe.search_ingredient(search_term):
            print(recipe)
            found = True
    if not found:
        print(f"No recipes found with the ingredients '{search_term}'")
    print("-" * 40)

# Main code
if __name__ == "__main__":
    # Create recipes
    tea = Recipe("Tea")
    tea.add_ingredients("Tea Leaves", "Sugar", "Water")
    tea.set_cooking_time(5)

    coffee = Recipe("Coffee")
    coffee.add_ingredients("Coffee Powder", "Sugar", "Water")
    coffee.set_cooking_time(5)

    cake = Recipe("Cake")
    cake.add_ingredients("Sugar", "Butter", "Eggs", "Vanilla Essence", "Flour", "Baking Powder", "Milk")
    cake.set_cooking_time(50)

    banana_smoothie = Recipe("Banana Smoothie")
    banana_smoothie.add_ingredients("Bananas", "Milk", "Peanut Butter", "Sugar", "Ice Cubes")
    banana_smoothie.set_cooking_time(5)

    # Create list of recipes
    recipes_list = [tea, coffee, cake, banana_smoothie]

    # Display recipes
    for recipe in recipes_list:
        print(recipe)
        print("-" * 40)

    # Search for recipes containing specific ingredients
    for ingredient in ["water", "Sugar"]:
        recipe_search(recipes_list, ingredient)