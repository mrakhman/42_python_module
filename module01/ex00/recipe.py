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
                raise ValueError("name must be a string") from None
            
        @property
        def cooking_lvl(self):
            return self._cooking_lvl
        
        @name.setter
        def cooking_lvl(self, value):
            if value <= 1 or value >= 5: # not working
                raise ValueError("kooling_lvl must be from 1 to 5") from None
            try:
                self._cooking_lvl = int(value)
            except ValueError:
                raise ValueError("name must be a string") from None

        

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
