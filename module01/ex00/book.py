from recipe import Recipe
from datetime import datetime
from pprint import pprint

# Input validation
def is_valid_name(name):
    if not isinstance(name, str) or name == "":
        print("Error: name must be a string, not empty")
        return False
    return True



class Book:
    def __init__(self, name):
        if is_valid_name(name):
            now = datetime.now()
            self.name = name
            self.last_update = now
            self.creation_date = now
            self.recipes_list = {'starter': [], 'lunch': [], 'dessert': []}
        else:
            return

    
    def get_recipe_by_name(self, name):
        """Prints a recipe with the name {name} and returns the instance"""
        if not is_valid_name(name):
            return None
        for key in self.recipes_list:
            for recipe in self.recipes_list[key]:
                if recipe.name == name:
                    print(str(recipe))
                    return recipe
        print(f"No recipe with name {name} found")
        return None


    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type"""
        if not recipe_type in self.recipes_list.keys():
            print(f"Error: recipe_type {recipe_type} does not exist. Types are: starter, lunch, dessert")
            return
        if len(self.recipes_list[recipe_type]) == 0:
            print(f"Recipes of type {recipe_type}: no recepies yet")
            return
        else:
            recepies_names = [recipe.name for recipe in self.recipes_list[recipe_type]]
            print(f"Recipes of type {recipe_type}: {', '.join(recepies_names)}")
            return recepies_names


    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if not isinstance(recipe, Recipe):
            print("Error: recipe must be an instance of Recipe")
            return
        if self.recipes_list[recipe.recipe_type]:
            print(f"Error: recipe {recipe.name} already exists")
            return
        else:
            self.recipes_list[recipe.recipe_type].append(recipe)
            self.last_update = datetime.now()



# new_book = Book('aaa')
# pprint(vars(new_book))

# rec = Recipe('eggs', 2, 4, ['q', 'p'], None, "lunch")
# new_book.add_recipe(rec)
# new_book.add_recipe(rec)
# new_book.add_recipe(rec)
# pprint(vars(new_book))
# print()

# new_book.get_recipes_by_types('aaa')
# new_book.get_recipes_by_types('starter')
# new_book.get_recipes_by_types('lunch')
# print()

# found_recipe = new_book.get_recipe_by_name('nope')
# print(found_recipe)
# found_recipe = new_book.get_recipe_by_name('')
# print(found_recipe)
# found_recipe = new_book.get_recipe_by_name(1)
# print(found_recipe)
# print()
# found_recipe = new_book.get_recipe_by_name('eggs')
# print(found_recipe.name, found_recipe.cooking_lvl)
