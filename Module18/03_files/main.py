bad_symbols_list = "@№$%^&\*()"
file_name = input("Введите название файла: ")

if file_name[0] in bad_symbols_list:
    print("Ошибка: название начинается на один из специальных символов.")
else:
    if file_name.endswith(".txt"):
        print("Файл назван верно.")
    elif file_name.endswith(".docx"):
        print("Файл назван верно.")
    else:
        print("Ошибка: неверное расширение файла. Ожидалось .txt или .docx.")