# **Intro-to-python**

## **Third Task**
- Initialize two empty lists: recipes_list and ingredients_list.
- Define a function called take_recipe, which takes input from the user. 
- In the main section of your code, ask the user how many recipes they would like to enter. Their response will be linked to a variable n.
- Run a for loop, which runs n times to perform the following steps:
- Run take_recipe() and store its return output (a dictionary) in a variable called recipe.
- Run another for loop inside this loop, which iterates through recipe’s ingredients list, where it picks out elements one-by-one as ingredient. 
- Once you’ve finished adding ingredients, append recipe to recipes_list.
- Run another for loop that iterates through recipes_list, picks out each element (a dictionary) as recipe.
- Display the recipe using values from each dictionary (recipe) obtained from recipes_list:recipes list
- Next, you’ll have to display all the ingredients that you’ve come across so far in all of the recipes that you’ve just entered.
- Print them in alphabetical order.
