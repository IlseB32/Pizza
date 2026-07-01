import classes as c
import csv

full_menu = {"ingredients": {}, "pizzas": {}, 'menu':{}}
all_made = {}

class MissingIngredient(Exception):
    pass

def load_ingredients(filename, type):
    ing_file = filename

    made_ingredients = {}
    ingredient_data = {}
    with open(ing_file) as f:
        reader = csv.DictReader(f)
        for row in reader:
            ingredient_data[row["name"]] = row


    def make_ingredient(name):
        name = name.strip()

        if name in made_ingredients:
            return made_ingredients[name]

        if name in full_menu["ingredients"]:
            return full_menu["ingredients"][name]

        if name in ingredient_data:
            data = ingredient_data[name]

            # collect sub-ingredients
            sub_ingredients_list = None
            if data['sub_ingredients'] != "":
                sub_ingredients_list = []
                sub_ingredients = data['sub_ingredients'].split(",")
                for item in sub_ingredients:
                    if "*" in item:
                        sub_name, multiplier = item.split("*")
                        sub_name = sub_name.strip()
                        try:
                            multiplier = float(multiplier.strip())
                            if multiplier.is_integer():
                                multiplier = int(multiplier)
                        except ValueError:
                            print(f"Invalid multiplier, {multiplier} in {sub_name}, defaulting to 1")
                            multiplier = 1
                    else:
                        sub_name = item.strip()
                        multiplier = 1
                    sub_ingredient = make_ingredient(sub_name)

                    if multiplier != 1:
                        sub_ingredients_list.append(sub_ingredient * multiplier)
                    else:
                        sub_ingredients_list.append(sub_ingredient)

            # turn portion string into int or float
            portion_str = data["portion"].strip()
            if portion_str == "":
                print(f"Warning: no portion size specified for {name}, defaulting to 0")
                portion_val = 0.0
            else:
                portion_val = float(portion_str)
            if portion_val.is_integer():
                portion_val = int(portion_val)

            # handle handmade, meat, fish, halal
            is_handmade = (data["handmade"] == "1" or data["handmade"].strip().lower() == "true" or data["handmade"] == "")
            is_meat = (data["meat"] == "1" or data["meat"].strip().lower() == "true")
            is_fish = (data["fish"] == "1" or data["fish"].strip().lower() == "true")
            is_halal = (data["halal"] == "1" or data["halal"].strip().lower() == "true")

            # handle aisle
            if data["aisle"] == "":
                aisle = "other"
            else:
                aisle = data["aisle"].strip().lower()

            # turn into Ingredient object
            ingredient_item = c.Ingredient(name=name,
                                           portion=portion_val,
                                           portion_type=data["portion_type"],
                                           sub_ingredients=sub_ingredients_list,
                                           handmade=is_handmade,
                                           meat=is_meat,
                                           fish=is_fish,
                                           halal=is_halal,
                                           aisle=aisle)

            made_ingredients[name] = ingredient_item
            all_made[name] = ingredient_item
            return ingredient_item

        else:
            raise MissingIngredient("Missing ingredient {}".format(name))


    def make_pizza(name):
        name = name.strip()
        if name in made_ingredients:
            return made_ingredients[name]
        if name in full_menu["ingredients"]:
            return full_menu["ingredients"][name]

        if name in ingredient_data:
            data = ingredient_data[name]

            # collect sub-ingredients
            sub_ingredients_list = None
            if data['sub_ingredients'] != "":
                sub_ingredients_list = []
                sub_ingredients = data['sub_ingredients'].split(",")
                for item in sub_ingredients:
                    if "*" in item:
                        sub_name, multiplier = item.split("*")
                        sub_name = sub_name.strip()
                        try:
                            multiplier = float(multiplier.strip())
                            if multiplier.is_integer():
                                multiplier = int(multiplier)
                        except ValueError:
                            print(f"Invalid multiplier, {multiplier} in {sub_name}, defaulting to 1")
                            multiplier = 1
                    else:
                        sub_name = item.strip()
                        multiplier = 1
                    sub_ingredient = make_ingredient(sub_name)

                    if multiplier != 1:
                        sub_ingredients_list.append(sub_ingredient * multiplier)
                    else:
                        sub_ingredients_list.append(sub_ingredient)

            # turn portion string into int or float
            # turn into Ingredient object
            ingredient_item = c.Pizza(name=name,
                                      ingredients=sub_ingredients_list)

            made_ingredients[name] = ingredient_item
            all_made[name] = ingredient_item
            return ingredient_item

        else:
            raise MissingIngredient("Missing ingredient {}".format(name))


    for name in ingredient_data:
        if type == "ingredients":
            make_ingredient(name)
        if type == "pizzas":
            make_pizza(name)
    full_menu[type] = made_ingredients


load_ingredients("ingredients.csv", "ingredients")
load_ingredients("pizzas.csv", "pizzas")

menu = c.Menu(full_menu["pizzas"].values())
menu.print_ingredients()