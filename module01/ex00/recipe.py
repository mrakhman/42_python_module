# Input validation functions
def is_valid_recipe(name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
    def is_valid_name(name):
        if not isinstance(name, str) or name == "":
            print("Error: name must be a string, not empty")
            return False
        return True

    def is_valid_cooking_lvl(cooking_lvl):
        if not isinstance(cooking_lvl, int) or isinstance(cooking_lvl, bool):
            print("Error: cooking_lvl must be an integer")
            return False
        if not (cooking_lvl >= 1 and cooking_lvl <= 5):
            print("Error: cooking_lvl must be an integer from 1 to 5")
            return False
        return True

    def is_valid_cooking_time(cooking_time):
        if not isinstance(cooking_time, int) or isinstance(cooking_time, bool):
            print("Error: cooking_time must be an integer")
            return False
        if cooking_time < 0:
            print("Error: cooking_time must be a positive integer")
            return False
        return True

    def is_valid_ingredients(ingredients):
        if not isinstance(ingredients, list) or len(ingredients) == 0 or not all(isinstance(ingredient, str) for ingredient in ingredients):
            print("Error: ingredients must be a list of strings")
            return False
        return True

    def is_valid_description(description):
        if description == None or description == "":
            return True
        if not isinstance(description, str):
            print("Error: description must be a string")
            return False
        return True

    def is_valid_recipe_type(recipe_type):
        recipe_types = ("starter", "lunch", "dessert")
        if not recipe_type in recipe_types:
            print("Error: recipe_type must be starter, lunch or dessert")
            return False
        return True


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
            self._name = name
            self._cooking_lvl = cooking_lvl
            self._cooking_time = cooking_time
            self._ingredients = ingredients
            self._description = description
            self._recipe_type = recipe_type
        else:
            return

    # The __str__ method in Python represents the class objects as a string – it can be used for classes.
    # This method is also used as a debugging tool when the members of a class need to be checked.
    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = f"""This is the recipe:
Name: {self._name}
Cooking level: {self._cooking_lvl}
Cooking time: {self._cooking_time}
Ingredients: {', '.join(self._ingredients)}
Description: {self._description}
Recipe type: {self._recipe_type}
"""
        return txt



# valid_recipe = Recipe('er', 2, 4, ['q', 'p'], None, "starter")
# to_print = str(valid_recipe)
# print(to_print)


# invalid_recepie1 = Recipe('', 2, 4, ['q', 'p'], "", "starter")
# invalid_recepie2 = Recipe('aaa', 0, 4, ['q', 'p'], "", "starter")
# invalid_recepie3 = Recipe('aaa', 5, 'lala', ['q', 'p'], "", "starter")
# invalid_recepie4 = Recipe('aaa', 5, 12, ['one', 2], "", "starter")
# invalid_recepie5 = Recipe('aaa', 5, 12, ['one', 'two'], 5, "starter")
# invalid_recepie6 = Recipe('aaa', 5, 12, ['one', 'two'], "a b c d", "else")



