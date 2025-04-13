class ShoppingList:
    def __init__(self, list_name):
        # Initialize the shopping list with a name and an empty list
        self.list_name = list_name
        self.shopping_list = []

    def add_item(self, item):
        # Add an item to the shopping list if it's not already there
        if item not in self.shopping_list:
            self.shopping_list.append(item)
            print(f"'{item}' has been added to the shopping list.")
        else:
            print(f"'{item}' is already in the shopping list.")

    def remove_item(self, item):
        # Remove an item from the shopping list if it's in the shopping list
        if item in self.shopping_list:
            self.shopping_list.remove(item)
            print(f"'{item}' has been removed from the shopping list.")
        else:
            print(f"'{item}' not found in shopping list.")

    def view_List(self):
        # Display all items in the shopping list
        print(f"\n{self.list_name}: ")
        if self.shopping_list:
            for item in self.shopping_list:
                print(f"- {item}")
        else:
            print("The shopping list is empty.")

# Create an object of ShoppingList with the name "pet Store Shopping List"
pet_store_list = ShoppingList("Pet Store Shopping List")

# Add items to pet store shopping list
pet_store_list.add_item("dog food")
pet_store_list.add_item("frisbee")
pet_store_list.add_item("bowl")
pet_store_list.add_item("collars")
pet_store_list.add_item("flea collars")

# Remove flea collars using remove_item method
pet_store_list.remove_item("flea collars")

# Try to add "frisbee" again using the add_item method
pet_store_list.add_item("frisbee")

# Display the entire shopping list
pet_store_list.view_List()