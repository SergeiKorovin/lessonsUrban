def custom_write(file_name, strings):
    count = 0
    strings_positions = dict()
    file = open(file_name, 'a', encoding='utf-8')
    for i_strings in strings:
        bait_ = file.tell()
        file.write(i_strings + '\n')
        count += 1
        strings_positions[(count,bait_)] = i_strings
    file.close()
    return strings_positions


info = ['Text for tell.', 'Используйте кодировку utf-8.', 'Because there are 2 languages!', 'Спасибо!']

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)