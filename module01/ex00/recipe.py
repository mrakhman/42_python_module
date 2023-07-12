import sys
from pprint import pprint

# Input validation functions
def is_valid_recipe(name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
    def is_valid_name(name):
        if not isinstance(name, str) or name == "":
            print("Error: name must be a string, not empty")
            return False
        return name

    def is_valid_cooking_lvl(cooking_lvl):
        if not isinstance(cooking_lvl, int) or isinstance(cooking_lvl, bool):
            print("Error: cooking_lvl must be an integer")
            return False
        if not (cooking_lvl >= 1 and cooking_lvl <= 5):
            print("Error: cooking_lvl must be an integer from 1 to 5")
            return False
        return cooking_lvl

    def is_valid_cooking_time(cooking_time):
        if not isinstance(cooking_time, int) or isinstance(cooking_time, bool):
            print("Error: cooking_time must be an integer")
            return False
        if cooking_time < 0:
            print("Error: cooking_time must be a positive integer")
            return False
        return cooking_time

    def is_valid_ingredients(ingredients):
        if not isinstance(ingredients, list) or len(ingredients) == 0 or not all(isinstance(ingredient, str) for ingredient in ingredients):
            print("Error: ingredients must be a list of strings")
            return False
        return ingredients

    def is_valid_description(description):
        if description == None or description == "":
            return "No description"
        if not isinstance(description, str):
            print("Error: description must be a string")
            return False
        return description

    def is_valid_recipe_type(recipe_type):
        recipe_types = ("starter", "lunch", "dessert")
        if not recipe_type in recipe_types:
            print("Error: recipe_type must be starter, lunch or dessert")
            return False
        return recipe_type


    if not is_valid_name(name) \
        or not is_valid_cooking_lvl(cooking_lvl) \
        or not is_valid_cooking_time(cooking_time) \
        or not is_valid_ingredients(ingredients) \
        or not is_valid_description(description) \
        or not is_valid_recipe_type(recipe_type):
        return False
    return True



class Recipe:
    def __init__(self,
                 name,
                 cooking_lvl,
                 cooking_time,
                 ingredients,
                 description,
                 recipe_type):
        if is_valid_recipe(name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
            self.name = name
            self.cooking_lvl = cooking_lvl
            self.cooking_time = cooking_time
            self.ingredients = ingredients
            self.description = description
            self.recipe_type = recipe_type
        else:
            sys.exit()

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = f"""This is the recipe:
Name: {self.name}
Cooking level: {self.cooking_lvl}
Cooking time: {self.cooking_time}
Ingredients: {', '.join(self.ingredients)}
Description: {self.description}
Recipe type: {self.recipe_type}
"""
        return txt



valid_recepie = Recipe('er', 2, 4, ['q', 'p'], None, "starter")
# pprint(vars(valid_recepie))
print()
to_print = str(valid_recepie)
print(to_print)

# invalid_recepie1 = Recipe('', 2, 4, ['q', 'p'], "", "starter")
# invalid_recepie2 = Recipe('aaa', 0, 4, ['q', 'p'], "", "starter")
# invalid_recepie3 = Recipe('aaa', 5, 'lala', ['q', 'p'], "", "starter")
# invalid_recepie4 = Recipe('aaa', 5, 12, ['one', 2], "", "starter")
# invalid_recepie5 = Recipe('aaa', 5, 12, ['one', 'two'], 5, "starter")
# invalid_recepie6 = Recipe('aaa', 5, 12, ['one', 'two'], "a b c d", "else")



