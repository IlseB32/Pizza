
formaggi = {'tomatensaus': 1, 'mozzarella': 1, 'brie': 1, 'gorgonzola': 1}
extravaganza = {'tomatensaus': 1, 'mozzarella': 1, 'champignon': 1, 'ui': 1, 'paprika': 1, 'salami': 1, 'worst': 1}
tartufo = {'tomatensaus': 1, 'mozzarella': 1, 'parmaham': 1, 'rucola': 1, 'truffelsaus': 1, 'pijnboompitten': 1}
romeo = {'tomatensaus': 1, 'mozzarella': 1, 'worst': 1, 'ui': 1}
tonno = {'tomatensaus': 1, 'mozzarella': 1, 'tonijn': 1, 'ui': 1, 'kappertjes': 1}
agnese = {'mozzarella': 1.5, 'ui': 1, 'spek': 1, 'creme fraiche': 1, 'kappertjes': 1}
limone = {'tomatensaus': 1, 'mozzarella': 1, 'citroen ricotta': 1, 'pistache': 1, 'basilicum': 1, 'rucola': 1}
pera = {'mozzarella': 1.5, 'peer': 1, 'kappertjes': 1, 'brie': 1, 'gorgonzola': 1, 'rucola': 1}
mexicano = {'tomatensaus': 1, 'mozzarella': 1, 'mex kruiden': 1, 'cheddar': 1, 'paprika': 1, 'mais': 1, 'guacamole': 1,
            'tortilla chips': 1}
bruschetta = {'bruschetta': 1}
pesto = {'pesto': 4, 'mozzarella': 1, 'tomaatjes': 1, 'rucola': 1, 'pijnboompitten': 1, 'balsamico': 1}
verdure = {'tomatensaus': 1, 'mozzarella': 1, 'groentemix': 1}
parma = {'tomatensaus': 1, 'mozzarella': 1, 'parmaham': 1, 'rucola': 1, 'burrata': 1}
renzo = {'tomatensaus': 1, 'mozzarella': 1, 'ham': 1, 'pesto': 1}
carne = {'tomatensaus': 1, 'mozzarella': 1, 'salami': 1, 'ham': 1, 'spek': 1, 'ui': 1}
spicy_salami = {'tomatensaus': 1, 'mozzarella': 1, 'salami': 1, 'ui': 1, 'chili vlokken': 1}
shoarma = {'tomatensaus': 1, 'mozzarella': 1, 'shoarma': 1, 'paprika': 1, 'knoflooksaus': 1, 'rucola': 1}
pesca = {'mozzarella': 1.5, 'perzik': 1, 'basilicum': 1, 'burrata': 1, 'honing': 1, 'balsamico': 1}
marmellata = {'jam': 2, 'mozzarella': 1, 'spek': 1, 'rucola': 1, 'pistache': 1, 'balsamico': 1, 'honing': 1}
basilico = {'tomatensaus': 1, 'mozzarella': 1, 'basilicum': 2, 'basilicum olie': 1}
autunno = {'pompoenpuree': 1, 'parmezaan': 1, 'mozzarella': 1, 'geitenkaas': 1, 'spek': 1, 'ui': 1, 'pistache': 1,
           'salie': 1, 'basilicum olie': 1}
flammkuchen = {'mozzarella': 1.5, 'ui': 1, 'spek': 1, 'creme fraiche': 1, 'kappertjes': 1}
greco = {'tomatensaus': 1, 'knoflook': 2, 'mozzarella': 1, 'olijven': 1, 'tomaatjes': 1, 'ui': 1, 'feta': 1}
vuurvogel = {'tomatensaus': 1, 'mozzarella': 1, 'paprika': 1, 'gele paprika': 1, 'ui': 1}
speziato = {'tomatensaus': 1, 'mozzarella': 1, 'diverse hete pepers': 1, 'ui': 1, 'ham': 1}
fico = {'mozzarella': 1.5, 'vijgen': 1, 'basilicum': 1, 'burrata': 1, 'honing': 1, 'balsamico': 1}
spinaci = {'mozzarella': 1.5, 'spinazie': 2, 'ui': 1, 'feta': 1}
margarita = {'tomatensaus': 1, 'mozzarella': 1, 'basilicum': 1}
nutella = {'nutella': 1}
funghi = {'tomatensaus': 1, 'mozzarella': 1, 'champignon': 1}
focaccia = {'rosemarijn': 1, 'olijfolie': 1}
tartufo_formaggi_miele = {"mozzarella": 1, 'brie': 1, 'gorgonzola': 1, 'truffelhoning': 1, 'rucola': 1}
cranberbrie = {'tomatensaus': 1, 'mozzarella': 1, 'brie': 1, 'cranberrie': 1, 'rucola': 1}
kip_pa_pes = {'tomatensaus': 1, 'mozzarella': 1, 'kip': 1, 'paprika': 1, 'pesto': 1}
bbq_kip = {'tomatensaus': 1, 'mozzarella': 1, 'kip': 1, 'ui': 1, 'bbq saus': 1}

pizzas = [[formaggi], [extravaganza], [tartufo], [romeo], [tonno], [agnese], [limone], [pera],
          [mexicano], [pesto], [bruschetta], [verdure], [parma], [renzo], [nutella], [funghi],
          [carne], [spicy_salami], [shoarma], [pesca], [marmellata], [basilico], [autunno],
          [flammkuchen], [greco], [vuurvogel], [speziato], [fico], [spinaci], [margarita],
          [focaccia], [tartufo_formaggi_miele],[cranberbrie],[kip_pa_pes], [bbq_kip]]
ingredients = set()

for pizza in pizzas:
    for ingredient in pizza[0].keys():
        ingredients.add(ingredient)
print(ingredients)
with open('pizzas.txt', 'r') as file:
    for pizza in pizzas:
        amount = file.readline()
        temp, number = amount.split(':')
        number.strip()
        pizza.append(int(number))

tasks = {'snijden': set(), 'raspen': set(), 'bak nodig voor': set(), 'bestek nodig voor': set(), 'bak in pan': set(),
         'uitlekken': set(), 'maken': set()}

def check_for_tasks(ingredient):
    if ingredient in ['perzik', 'rosemarijn', 'worst', 'champignon', 'peer', 'groentemix', 'diverse hete pepers',
                      'knoflook', 'vijgen', 'tortilla chips', 'salie', 'ui', 'mozzarella', 'gele paprika', 'tomaatjes']: # snijden
        tasks['snijden'].add(ingredient)
    elif ingredient in ['parmezaan', 'pistache']: # raspen
        tasks['raspen'].add(ingredient)
    elif ingredient in ['perzik', 'worst', 'champignon', 'peer', 'diverse hete pepers', 'knoflook', 'spinazie',
                        'tomatensaus', 'vijgen', 'shoarma', 'salie', 'ui', 'mozzarella', 'gele paprika', 'tomaatjes']: # bak nodig voor
        tasks['bak nodig voor'].add(ingredient)
    elif ingredient in ['kappertjes', 'brie', 'burrata', 'paprika', 'olijven', 'truffelhoning', 'jam', 'nutella',
                        'mais', 'knoflooksaus', 'geitenkaas', 'feta', 'tonijn', 'creme fraiche', 'gorgonzola']: # bestek nodig voor
        tasks['bestek nodig voor'].add(ingredient)
    elif ingredient in ['worst', 'spinazie', 'shoarma']: # bak in pan
        tasks['bak in pan'].add(ingredient)
    elif ingredient in ['burrata', 'paprika']: # uitlekken
        tasks['uitlekken'].add(ingredient)
    elif ingredient in ['bruschetta', 'pesto', 'guacamole', 'mex kruiden', 'basilicum olie',
                        'citroen ricotta', 'pompoenpuree']: # maken
        tasks['maken'].add(ingredient)

# ingredient subclass
maakcitroenricotta = {'ricotta': 1, 'citroen': 1}
maakpesto = {'basilicum': 1, 'pijnboompitten': 1, 'parmezaan': 1, 'olijfolie': 1, 'knoflook': 0.5}
maakguacamole = {'avocado': 1, 'guac kruiden': 1, 'diverse hete pepers': 1, 'tomaten': 1, 'limoen': 1}
maakbruschetta = {'tomaten': 3, 'basilicum': 2, 'knoflook': 2}
shopping_list = {}
def make_ingredient(ingredient, amount):
    selected_ingredient = ['pesto', 'citroen ricotta', 'guacamole', 'bruschetta'].index(ingredient)
    selected_ingredient = [maakpesto, maakcitroenricotta, maakguacamole, maakbruschetta][selected_ingredient]
    for i in range(amount):
        for sub_ingredient in selected_ingredient:
            if sub_ingredient in shopping_list.keys():
                shopping_list[sub_ingredient] += selected_ingredient[sub_ingredient]
            else:
                shopping_list[sub_ingredient] = selected_ingredient[sub_ingredient]


for pizza in pizzas:
    for iterations in range(pizza[1]):
        for ingredient in pizza[0].keys():
            check_for_tasks(ingredient)
            if ingredient in ['pesto', 'citroen ricotta', 'guacamole', 'bruschetta']:
                make_ingredient(ingredient, pizza[0][ingredient])
            else:
                if ingredient in shopping_list.keys():
                    shopping_list[ingredient] += pizza[0][ingredient]
                else:
                    shopping_list[ingredient] = pizza[0][ingredient]

shopping_list = dict(sorted(shopping_list.items(), key=lambda item: item[1], reverse=True))
with open('shoppinglist.txt', 'w') as file:
    file.write("SHOPPING LIST:\n")
    for item in shopping_list.keys():
        value = int(shopping_list[item]) if shopping_list[item] % 1 == 0 else shopping_list[item]
        file.write(f'{value}x {item}\n')

with open('tasks.txt', 'w') as file:
    for task in tasks.keys():
        file.write(f'{task}:\n')
        for item in tasks[task]:
            file.write(f"{item}\n")
        file.write('\n')