import os, time


directory = os.getcwd()


for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file)
        if os.path.isfile(file):
            # filetime = os.stat(file).st_mtime
            file_time = os.path.getmtime(file)
            formatted_time = time.strftime('%d.%m.%Y.%H:%M', time.localtime(file_time))
            file_size = os.path.getsize(file)
            parent_dir = os.path.dirname(file)
            print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {file_size} байт, Время изменения: {formatted_time},'
              f'Родительская директория: {parent_dir}')