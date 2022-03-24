cook_book = {}

with open('food.txt', 'r', encoding='utf-8') as file:
    for line in file:
        print(line.strip())
