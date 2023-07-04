class colors:
    '''Colors class:reset all colors with colors.reset; two
    sub classes fg for foreground
    and bg for background; use as colors.subclass.colorname.
    i.e. colors.fg.red or colors.bg.greenalso, the generic bold, disable,
    underline, reverse, strike through,
    and invisible work with the main class i.e. colors.bold'''

    reset = '\033[0m'
    bold = '\033[01m'
    disable = '\033[02m'
    underline = '\033[04m'
    reverse = '\033[07m'
    strikethrough = '\033[09m'
    invisible = '\033[08m'

    class fg:
            black = '\033[30m'
            red = '\033[31m'
            green = '\033[32m'
            orange = '\033[33m'
            blue = '\033[34m'
            purple = '\033[35m'
            cyan = '\033[36m'
            lightgrey = '\033[37m'
            darkgrey = '\033[90m'
            lightred = '\033[91m'
            lightgreen = '\033[92m'
            yellow = '\033[93m'
            lightblue = '\033[94m'
            pink = '\033[95m'
            lightcyan = '\033[96m'

    class bg:
        black = '\033[40m'
        red = '\033[41m'
        green = '\033[42m'
        orange = '\033[43m'
        blue = '\033[44m'
        purple = '\033[45m'
        cyan = '\033[46m'
        lightgrey = '\033[47m'

# print(colors.bg.green, "SKk", colors.fg.red, "Amartya")
# print(colors.bg.lightgrey, "SKk", colors.fg.red, "Amartya")


# Part 1
cookbook = {
    'sandwich': {
        'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
        'meal': 'lunch',
        'prep_time': 10,
    },
    'cake': {
        'ingredients': ['flour', 'sugar', 'eggs'],
        'meal': 'dessert',
        'prep_time': 60,
    },
    'salad': {
        'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
        'meal': 'lunch',
        'prep_time': 15,
    }
}


# Part 2
def print_cookbook():
    names = ', '.join(name for name in cookbook.keys())
    print(colors.fg.green + f"Recipes names: {names}", colors.reset)


def print_recipe_details(name):
    recipe = cookbook.get(name)
    if not recipe:
        return print(colors.fg.green + f"{name} does not exist in cookbook", colors.reset)
    print(colors.fg.green + f"Recipe of {name}")
    print(f"Ingredients: {', '.join(name for name in recipe['ingredients'])}")
    print(f"Meal: {recipe['meal']}")
    print(f"Prep time: {recipe['prep_time']}", colors.reset)


def del_recipe(name):
    if name in cookbook.keys():
        del cookbook[name]
        print(colors.fg.green + f"{name} deleted from cookbook", colors.reset)
    else:
        print(colors.fg.green + f"{name} does not exist in cookbook", colors.reset)


def add_recipe():
    # name
    print(colors.fg.green + "Enter name:", colors.reset)
    name = input()
    if name in cookbook.keys():
        return print(colors.fg.green + f"{name} already exists", colors.reset)
    
    # ingredients
    print(colors.fg.green + "Enter ingredients:", colors.reset)
    ingredients = []
    while True:
        ingredient = input()
        if ingredient == "":
            break
        ingredients.append(ingredient)

    # meal
    print(colors.fg.green + "Enter meal type:", colors.reset)
    meal = input()

    # prep_time
    print(colors.fg.green + "Enter preparation time (int):", colors.reset)
    prep_time = None
    while True:
        prep_time = input()
        if not prep_time.isdigit():
            print(colors.fg.green + "Preparation time should be an integer. Enter preparation time", colors.reset)
            continue
        else:
            prep_time = int(prep_time)
            break
    
    # put to cookbook
    cookbook[name] = {'ingredients': ingredients, 'meal': meal, 'prep_time': prep_time}
    print(colors.fg.green + f"{name} added to cookbook", colors.reset)


# Part 3
def run_cookbook():
    template = colors.fg.blue + '''List of available options:
1: Add a recipe
2: Delete a recipe
3: Print a recipe
4: Print the cookbook
5: Quit

Please select an option:
'''

    print(colors.fg.green + "Welcome to the Python Cookbook!\n")
    print(template, colors.reset)

    while True:
        option = input()
        if not option.isdigit() or (int(option) < 1 or int(option) > 5):
            print(colors.fg.green + "\nSorry, this option does not exist.\n")
            print(template, colors.reset)
            continue

        else:
            option = int(option)
            if option == 1:
                    add_recipe()
            elif option == 2:
                    print(colors.fg.green + "Recipe name to delete:", colors.reset)
                    name = input()
                    del_recipe(name)
            elif option == 3:
                    print(colors.fg.green + "Recipe name:", colors.reset)
                    name = input()
                    print_recipe_details(name)
            elif option == 4:
                    print_cookbook()
            elif option == 5:
                    print(colors.fg.green + "Cookbook closed. Goodbye!", colors.reset)
                    break
            else:
                break
            print(f"\n{template}", colors.reset)



run_cookbook()