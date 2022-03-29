from unicodedata import name

# Задача №1.
def create_book(import_file):
    cook_book = {}
    
    with open(import_file, encoding='utf-8') as file:
        food = [line.strip() for line in file]

        for n, elemant in enumerate(food):
            if elemant.isdigit():
                cook_book[food[n-1]] = []
                for position in food[n+1 : n+int(elemant)+1]:
                    ingredient_name = position.split('|')[0]
                    quantity = int(position.split('|')[1])
                    measure = position.split('|')[2]
                    cook_book[food[n-1]].append({'ingredient_name':ingredient_name, 'quantity':quantity, 'measure':measure})
    print(cook_book)
    print()
    return cook_book

create_book('food.txt')

# Задача №2.

def get_shop_list_by_dishes(dishes, person_count, book = create_book('food.txt')): 
    dict_ingredients ={}

    for key in book.keys():
        for dish in dishes:
            if key == dish:
                for lst_ingr in book[key]:
                    name_ingr = lst_ingr['ingredient_name']
                    dict_ingredients[name_ingr] = {'measure': lst_ingr['measure'], 'quantity': lst_ingr['quantity'] * person_count}
    print(dict_ingredients)
    return dict_ingredients

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2) 
