# 1
# with open(r"C:\Users\Honor\Desktop\Работа с файлами\24.12.txt", "r", encoding="UTF-8") as file:
#     lines = file.readlines()
#     for line in lines:
#         print(line)
#     print(lines[2])
#     third_line = lines[2]

# with open(r"new.txt", "w", encoding="UTF-8") as file_1:
#     file_1.write(third_line[::-1][1:])

# 2
# with open(r"C:\Users\Honor\Desktop\Работа с файлами\24.12.txt", "r", encoding="UTF-8") as file:
#     lines = file.readlines()

# new_line = "В лесу родилась елочка\n"

# lines.insert(2, new_line)

# with open(r"C:\Users\Honor\Desktop\Работа с файлами\24.12.txt", "w", encoding="UTF-8") as file:
#     file.writelines(lines)


#3
# def func(path, row_num):
#     with open(path, 'r', encoding='UTF-8') as file:
#         for index, line in enumerate(file):
#             if index == row_num:
#                 exit()
#             print(line)

# func(r"C:\Users\Honor\Desktop\Работа с файлами\24.12.txt", 3)