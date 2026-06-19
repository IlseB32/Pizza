
class pizza:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def is_vegetarian(self):
        # List of all meats and fish - these items make it non-vegetarian
        meats = ['salami', 'worst', 'parmaham', 'spek', 'kip', 'tonijn',
                 'shoarma', 'ham', 'köttbullar', 'tandoori kip','coppa','gehakt']
        for item in self.ingredients.keys():
            if item in meats:
                return False
        return True

    def is_pescetarian(self):
        # List of all meats - these items make it non-pescetarian
        meats = ['salami', 'worst', 'parmaham', 'spek', 'kip',
                 'shoarma', 'ham', 'köttbullar', 'tandoori kip','coppa','gehakt']
        for item in self.ingredients.keys():
            if item in meats:
                return False
        return True

    def possible_halal(self):
        # List of all pig meats - these items make it non-halal
        haram_items = ['parmaham', 'spek', 'ham', 'shoarma', 'köttbullar']
        # notice that salami and worstje arent included because beef/chicken options exist
        for item in self.ingredients.keys():
            if item in haram_items:
                return False
        return True

    def detailed_ingredients(self):
        sub_recipes = {
            'tandoori kip': {'kippendijen': 2, 'tandoori kruiden': 1, 'yoghurt': 1},
            'pesto': {'verse basilicum': 2, 'pijnboompitten': 1, 'parmezaan': 1, 'knoflook': 1},
            'shoarma': {'vleesreepjes': 2, 'shoarmakruiden': 1},
            'bruschetta': {'tomaten': 2, 'knoflook': 1, 'olijfolie': 1, 'basilicum': 1}
        }
        detailed_dict = {}
        for item, amount in self.ingredients.items():
            if item in sub_recipes:
                # It is a compound item, break it down
                for sub_item, sub_amount in sub_recipes[item].items():
                    # .get(sub_item, 0) means: "Fetch the current amount, or default to 0 if it doesn't exist yet"
                    detailed_dict[sub_item] = detailed_dict.get(sub_item, 0) + (sub_amount * amount)
            else:
                # It is a standard ingredient
                detailed_dict[item] = detailed_dict.get(item, 0) + amount

        return detailed_dict

# Define pizzas with ingredients
pizza_menu = {
    'formaggi': pizza('Formaggi', {'tomatensaus': 1, 'mozzarella': 1, 'brie': 1, 'gorgonzola': 1}),
    'extravaganza': pizza('Extravaganza', {'tomatensaus': 1, 'mozzarella': 1, 'champignon': 1, 'ui': 1, 'paprika': 1, 'salami': 1, 'worst': 1}),
    'tartufo': pizza('Tartufo', {'tomatensaus': 1, 'mozzarella': 1, 'parmaham': 1, 'rucola': 1, 'truffelsaus': 1}),
    'romeo': pizza('Romeo', {'tomatensaus': 1, 'mozzarella': 1, 'worst': 1, 'ui': 1}),
    'tonno': pizza('Tonno', {'tomatensaus': 1, 'mozzarella': 1, 'tonijn': 1, 'ui': 1, 'kappertjes': 1}),
    'agnese': pizza('Agnese', {'mozzarella': 1.5, 'ui': 1, 'spek': 1, 'creme fraiche': 1, 'kappertjes': 1}),
    'limone': pizza('Limone', {'tomatensaus': 1, 'mozzarella': 1, 'citroen ricotta': 1, 'pistache': 1, 'basilicum': 1, 'rucola': 1}),
    'pera': pizza('Pera', {'mozzarella': 1.5, 'peer': 1, 'kappertjes': 1, 'brie': 1, 'gorgonzola': 1, 'rucola': 1}),
    'mexicano': pizza('Mexicano', {'tomatensaus': 1, 'mozzarella': 1, 'mex kruiden': 1, 'cheddar': 1, 'paprika': 1, 'mais': 1, 'guacamole': 1, 'tortilla chips': 1}),
    'bruschetta': pizza('Bruschetta', {'bruschetta': 1}),
    'pesto': pizza('Pesto', {'pesto': 4, 'mozzarella': 1, 'tomaatjes': 1, 'rucola': 1, 'pijnboompitten': 1, 'balsamico': 1}),
    'verdure': pizza('Verdure', {'tomatensaus': 1, 'mozzarella': 1, 'groentemix': 1}),
    'parma': pizza('Parma', {'tomatensaus': 1, 'mozzarella': 1, 'parmaham': 1, 'rucola': 1, 'burrata': 1}),
    'renzo': pizza('Renzo', {'tomatensaus': 1, 'mozzarella': 1, 'ham': 1, 'pesto': 1}),
    'carne': pizza('Carne', {'tomatensaus': 1, 'mozzarella': 1, 'salami': 1, 'ham': 1, 'spek': 1, 'ui': 1}),
    'spicy_salami': pizza('Spicy Salami', {'tomatensaus': 1, 'mozzarella': 1, 'salami': 1, 'ui': 1, 'chili vlokken': 1}),
    'shoarma': pizza('Shoarma', {'tomatensaus': 1, 'mozzarella': 1, 'shoarma': 1, 'paprika': 1, 'knoflooksaus': 1, 'rucola': 1}),
    'pesca': pizza('Pesca', {'mozzarella': 1.5, 'perzik': 1, 'basilicum': 1, 'burrata': 1, 'honing': 1, 'rucola': 1}),
    'marmellata': pizza('Marmellata', {'jam': 2, 'mozzarella': 1, 'spek': 1, 'rucola': 1, 'pistache': 1, 'balsamico': 1, 'honing': 1}),
    'basilico': pizza('Basilico', {'tomatensaus': 1, 'mozzarella': 1, 'basilicum': 2, 'basilicum olie': 1}),
    'autunno': pizza('Autunno', {'pompoenpuree': 1, 'parmezaan': 1, 'mozzarella': 1, 'geitenkaas': 1, 'spek': 1, 'ui': 1, 'pistache': 1, 'salie': 1, 'basilicum olie': 1}),
    'greco': pizza('Greco', {'tomatensaus': 1, 'knoflook': 2, 'mozzarella': 1, 'olijven': 1, 'tomaatjes': 1, 'ui': 1, 'feta': 1}),
    'vuurvogel': pizza('Vuurvogel', {'tomatensaus': 1, 'mozzarella': 1, 'paprika': 1, 'gele paprika': 1, 'ui': 1}),
    'speziato': pizza('Speziato', {'tomatensaus': 1, 'mozzarella': 1, 'diverse hete pepers': 1, 'ui': 1, 'ham': 1}),
    'fico': pizza('Fico', {'mozzarella': 1.5, 'vijgen': 1, 'basilicum': 1, 'burrata': 1, 'honing': 1, 'balsamico': 1}),
    'spinaci': pizza('Spinaci', {'mozzarella': 1.5, 'spinazie': 2, 'ui': 1, 'feta': 1}),
    'margarita': pizza('Margarita', {'tomatensaus': 1, 'mozzarella': 1, 'basilicum': 1}),
    'nutella': pizza('Nutella', {'nutella': 1}),
    'funghi': pizza('Funghi', {'tomatensaus': 1, 'mozzarella': 1, 'champignon': 1}),
    'focaccia': pizza('Focaccia', {'rozemarijn': 1, 'olijfolie': 1}),
    'tartufo_formaggi_miele': pizza('Tartufo Formaggi Miele', {'mozzarella': 1, 'brie': 1, 'gorgonzola': 1, 'truffelhoning': 1, 'rucola': 1}),
    'ilae': pizza('Ilae', {'tomatensaus': 1, 'mozzarella': 1, 'brie': 1, 'cranberrie': 1, 'rucola': 1}),
    'kip_pa_pes': pizza('Kip Pa Pes', {'tomatensaus': 1, 'mozzarella': 1, 'kip': 1, 'paprika': 1, 'pesto': 1}),
    'bbq_kip': pizza('Bbq Kip', {'tomatensaus': 1, 'mozzarella': 1, 'kip': 1, 'ui': 1, 'bbq saus': 1}),
    'kip_tandoori': pizza('Kip Tandoori', {'tomatensaus': 1, 'mozzarella': 1, 'tandoori kip': 1, 'ui': 1, 'peterselie': 1, 'yoghurt': 1}),
    'barbietola': pizza('Barbietola', {'mozzarella': 1, 'rode biet': 1, 'feta': 1, 'lente ui': 1, 'honing': 1}),
    'carciofi': pizza('Carciofi', {'tomatensaus': 1, 'mozzarella': 1, 'artisjok': 1}),
    'svezia': pizza('Svezia', {'tomatensaus': 1, 'mozzarella': 1, 'cranberrie': 1, 'köttbullar': 1, 'jus': 1})
}