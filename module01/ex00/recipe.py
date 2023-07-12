class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        try:
            self._name = str(value)
        except ValueError:
            raise ValueError("name must be a string")
        
    @property
    def cooking_lvl(self):
        return self._cooking_lvl
    
    @cooking_lvl.setter
    def cooking_lvl(self, value):
        try:
            int_value = int(value)
            if int_value < 1 or int_value > 5:
                raise ValueError("cooking_lvl must be from 1 to 5")
            self._cooking_lvl = int_value
        except ValueError:
            raise ValueError("cooking_lvl must be an integer from 1 to 5")
    

    # def __str__(self):
    #     """Return the string to print with the recipe info"""
    #     txt = ""
    #     """Your code here"""
    #     return txt


    # name (str): name of the recipe,
    # cooking_lvl (int): range from 1 to 5,
    # cooking_time (int): in minutes (no negative numbers),
    # ingredients (list): list of all ingredients each represented by a string,
    # description (str): description of the recipe, Csn be empty
    # recipe_type (str): can be "starter", "lunch" or "dessert".

rec = Recipe(6, 8, 4, 3, 2, 1)
print(rec.name)
rec.name = 11
print(rec.name)
print(rec.cooking_lvl)
rec.cooking_lvl = 'rerer'
print(rec.cooking_lvl)
print(rec.cooking_lvl)
