my_dict = {"Игорь": 1994, 'Вася': 2000, 'Максим': 2012}
print('Dict:', my_dict)
print('Existing value:', my_dict['Вася'])
print('Not existing value:', my_dict.get('Анна', 'Такого имени нет'))
print(my_dict.get('Вася', 'Такого имени нет'))
key_1 = my_dict.get('Игорь', 'Такого имени нет')
print(key_1)
my_dict.update({'Анна': 2001,
                'Влад': 1999})
print('Modified dictionary:', my_dict)
i_dict = my_dict.pop('Игорь')
print('Deleted value:', i_dict)
print(my_dict)

my_set = {1, 1, 2, 2, 5, 'str', 'str', False, True, True}
print('Set:', my_set)
my_set.add(3)
my_set.add(4)
my_set.discard(5)
print('Modified set:', my_set)
