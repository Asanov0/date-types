# file = open('file.txt',encoding='utf-8') # файлды ачу жана окуу жолу

# print(file.readline (),end='')
# print(file.readline(), end='')
# print(file.readline (),end='')
# print(file.readline(), end='')


# for line in file:
#     print(line,end='')

# file .close()
# print(file.closed)

# Файл менен иштоо жана функция "Open" ()
# Функция Open() - Бул файл менен иштешу жолун алып барат,
# Ал Python тилинин встроенный функцясы 
# Open() функциясынын методдорун карап королу 

# 1) read- бул файлдын окуу жаатын алып барат 
# 2) readline - бул файлдын бир гана линиясын окууйт 
# 3) readlines - бул файлдын маалыматын бир гана строчкага жыйнайт 

# encoding - бул кодировка (utf - 8)
# файлды жабуу жолу:
# функция close() жана closed()


# Под Тема: Оператор (try, except, finally)
# try-except конструкциясы озгочо учурларды иштетуу учун колдонулат.
# try блогунда биз озгочолукту таштай турган операторду аткарабыз ,ал эми башка
# блокто аларды кармайбыз. Бул учурда озгочолуктун озу да, анын тукумдары да кармалат .

# try 
     # Оператордун блогу 
     # жана критичискии код 
# except [Исключение]:
     # обработка блогу
# finally:
     # Бул блок аткарат
     # ошибка чыкса деле   


# try:
#     file = open('file.txt',encoding='utf-8')
#     s = file . readlines()
#     print(s)
#     file.close()
# except FileNotFoundError:
#     print('Невозможно открыт файл !')


# 2)

# try:
#     file = open('file.txt', encoding='utf-8')
#     try:
#         s = file.readlines()
#         int(s)
#         print(s)
#     finally:
#         file.close()
# except FileNotFoundError:
#     print('Невозможно открыт файл !')
# except:
#     print('Ошибка при  работа с файлом')


# 3) 

# try:
#     with  open ('file.txt',encoding='utf-8') as file:
#         s = file .readlines()
#         print(s)
# except FileNotFoundError:
#     print('Невозможно открыт файл !')
# except:
#     print('Ошибка при работа с файлом')
# finally:
#     print(file.closed)





