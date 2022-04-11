quantity = 1 #количество рецептов в файле
recipe = 1 #переменная для цикла по количесву рецептов в файле
cook_book = {} #файл в формате словаря

with open('recipes.txt', 'r', encoding='utf-8') as file:
    for line in file:
        if line == '\n':
            quantity += 1

print(f'\nКоличество рецептов в файле: {quantity} шт')

file = open('recipes.txt', 'r', encoding='utf-8')
def file_worker():
    dictionary = {}
    key = file.readline().strip()
    number_of_ingredients = int(file.readline().strip())
    values = []
    quantity = 0
    while quantity < number_of_ingredients:
        dict_ingredients = {}
        data = file.readline().split('|')
        dict_ingredients['ingredient_name'] = data[0]
        dict_ingredients['quantity'] = int(data[1])
        dict_ingredients['measure'] = data[2].strip()
        values.append(dict_ingredients)
        quantity += 1
        dictionary[key] = values
    empty_string = file.readline().strip()
    return dictionary

while recipe <= quantity:
    result = file_worker()
    recipe += 1
    cook_book.update(result)
file.close()

print(f'\ncook_book = {cook_book}') #проверка результата

def get_shop_list_by_dishes(dishes:list, person_count:int):
    shop_list = {}
    for dish in dishes:
        quantity_element = dishes.count(dish)
        for name_dish, composition_dish in cook_book.items():
            if name_dish == dish:
                for element in composition_dish:
                    ingredients = {}
                    ingredient_name = element.get('ingredient_name')
                    measure = element.get('measure')
                    quantity = element.get('quantity')*person_count*quantity_element
                    ingredients['measure'] = measure
                    ingredients['quantity'] = quantity
                    shop_list[ingredient_name] = ingredients
    return shop_list

#ДЛЯ ИНТЕРФЕЙСА________________________________________________________________________________________________________#
list = ''
for k, v in cook_book.items():
    list += k + '; '
print(f'\nСписок блюд: {list}')

dishes_input = input('\nВведите блюдо из списка через запятую: ')
person_count = int(input('Введите количество персон: '))
dishes = dishes_input.split(',')
#______________________________________________________________________________________________________________________#

print(f'\n{get_shop_list_by_dishes(dishes, person_count)}')