import copy

class IncompatibleIngredients(Exception):
    pass

# base class
class Ingredient:
    def __init__(self, name, portion, portion_type, ingredients=None, handmade=True,
                 meat=False, fish=False, halal=False):

        self.name = name

        # assume handmade if there are sub_ingredients
        self.handmade = handmade
        self.ingredients = ingredients
        if ingredients is None:
            self.handmade = False

        self.portion = portion
        self.portion_type = portion_type  # g, ml, x (for amount)

        # if not handmade, provided tags suffice. otherwise check children
        self.vegetarian = not meat and not fish
        self.pescetarian = not meat
        self.halal = halal
        if handmade:
            self.vegetarian = self.get_type("vegetarian")
            self.pescetarian = self.get_type("pescetarian")
            self.halal = self.get_type("halal")

    # gets whether this ingredient is vegetarian, pescetarian or halal (depending on input)
    def get_type(self, searchval):
        if not self.handmade:
            return {"vegetarian": self.vegetarian, "pescetarian": self.pescetarian, "halal": self.halal}[searchval]
        for ingredient in self.ingredients:
            if not ingredient.get_type(searchval):
                return False
        return True

    # Recursively creates list of ingredients
    def get_ingredients(self) -> list:
        if not self.handmade:
            return [copy.copy(self)]

        value = []
        for ingredient in self.ingredients:
            for ing_ing in ingredient.get_ingredients():
                match_found = False
                for target in value:
                    try:
                        target += ing_ing
                        match_found = True
                        break
                    except IncompatibleIngredients:
                        pass

                if not match_found:
                    value.append(ing_ing)

        return value

    # pretty prints the list of ingredients
    def print_ingredients(self):
        ingredients = self.get_ingredients()
        print(f"--- Ingredients for {self.name} ---\n")
        for ing in ingredients:
            print(ing)
        return

    # makes it possible to multiply by int or float
    def __mul__(self, other):
        if not (isinstance(other, int) or isinstance(other, float)):
            raise TypeError(f"Ingredient Not multiplicable by {type(other)}, ({other})")
        new_ing = copy.copy(self)
        if not self.handmade:
            new_ing.portion *= other
        else:
            new_ing.ingredients = [ing * other for ing in new_ing.ingredients]
        return new_ing

    # makes it possible to add ingredients of same type together
    def __add__(self, other : Ingredient):
        if not self.handmade and not other.handmade:
            if self.name == other.name:
                if self.portion_type == other.portion_type:
                    self.portion += other.portion
                    return self
        raise IncompatibleIngredients(f"{self}, {other}")

    # prints what the ingredient is and its sub-ingredients
    def __repr__(self):
        if not self.handmade:
            return f"{self.name}: {self.portion}{self.portion_type}"
        return f"{self.name}: {[ing for ing in self.ingredients]}"

# extends Ingredient
class Pizza(Ingredient):
    def __init__(self, name, ingredients):
        super().__init__(
            name=name,
            portion=1,
            portion_type="x",
            ingredients=ingredients,
            handmade=True
        )

# extends Ingredient
class Menu(Ingredient):
    def __init__(self, pizzas):
        super().__init__(
            name="Menu",
            portion=None,
            portion_type=None,
            ingredients=pizzas,
            handmade=True
        )