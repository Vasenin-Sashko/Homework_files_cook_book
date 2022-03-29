from unicodedata import name


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
    return cook_book

create_book('food.txt')
