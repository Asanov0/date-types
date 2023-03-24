# Тема:
# Декораторы
# Декораторы!- важная часть Python.Если коротко:они являются функцями, которые изменяют  работу других 
# функцей. Они помагают делать код короче и более "Питонистчным"

# 1) Декораторы-Бул функциянын ичине функция болот

# Для начало краткая ретроспектива функций в Python:

# def hi (name = "Ray "):
#     return "Привет "+name

# print(hi()) # Привет Ray

# -----------------------------------------------------------------------

# Определение функций внутри функций!
# Итак, это были основы работы с функциями. Теперь продвинемся на шаг дальше.
# В Python разрешено объявлять функции внутри других функций:

# def hi():
#     print("Мы внутри функции hi()")
#     def inner():
#         return "Мы внутри функции inner()"
#     def welcome():
#         return "Мы внутри функции welcome()"

#     print(inner())
#     print(welcome())
#     print("Мы внутри функции hi()")

# hi()



# Вывод: Мы внутри функции hi()
#        Мы внутри функции ineer()
#        Мы внутри фции welcome()
#        Мы внутри функции hi()

# Пример демонстрирует, что при вызове hi() вызываются также функции inner() и welcome(),
# Кроме того, две последние функции недоступны извне hi():

# Если вызывим функцию inner()
# inner() # Вывод NameError: name 'inner' is not defaind!

# Теперь мы знаем, что возможно определять функции внутри других функций. 
# Другими словами: мы можем создавать вложенные функции.
# Теперь вам нужно познакомиться с еще одной возможностью функций: возвращать другие функции.
# def py (func):
#     def wrapper():
#         print('Всем привет, я декоратор')
#         func()
#         print('Мы с тобой еще все поладим!')
#     return wrapper
# @py
# def links():
#     print('''Ссылка на социалные сети:
#     ВКантакте: https....
#     Инстаграм: https....
#     Телеграм: https .... ''')
# links() # Теперь просто вызываем саму функцию

# @py
# def links2():
#     print('''
#         Ватсап:https....
#         Твиттер:https....
#         Tiktok:https....''')
# links2()


# 2)

# def aza (sun):
#     def muve ():
#         print('Баарынарга салам мен декоратор')
#         sun()
        
#     return muve
# @aza
# def links2():
#     print('''
#     Ватсап:https....
#     Твиттер:https....
#     Tiktok:https....''')
# links2()

# def tyn ():
#     print('''
#     урмат:jhfdk...
#     тыке:igkg...
#     омур:oggll...''')
# tyn()
# print('Биз дагы жолугабыз')


# 3) Обычный декоратор с сообщением!

# def decorator (func):
#     def wrapper():
#         print('Всем привет,как ваши дела?')
#         func()
#         print('До скорой встречи, на следуюшим презентации!')

#     return wrapper


# @decorator
# def links():
#     print('''Сылки на соцсети :
#     Facebook:https:/...
#     instagram: https:''')
        

# links()


# 4)
# Декоратор с параметром!

# def decorator (hi_msg, bye_msg):
#     def inner_decorator(func):
#         def wrapper(*args, **kwargs):
#             print(hi_msg)
#             func(*args, **kwargs)
#             print(bye_msg)

#         return wrapper
#     return inner_decorator

# @decorator('Привет!','До встречи!!!')
# def links (vk,tg, ins,tw):
#     print(f'''Вотссылки на соцсети:
#     wk:{vk}
#     Telegram:{tg}
#     Instagram:{ins}
#     Twetter:{tw}''')

# links('hhtps://wk','hhtps://t.me','hhtps://ins','hhtps://tw')



# def header(func):
#     def inner(*args,**kwargs):
#         print('<h1>')
#         func(*args,**kwargs)
#         print('</h1>')

#     return inner

# def table(func):
#     def inner(*args,**kwargs):
#         print('<table>')
#         func(*args,**kwargs)
#         print('</table>')
#     return inner

# @header
# def say(name, surname,age):
#     print('hello',name,surname,age)



# say('Vasya','Ivan',23)
