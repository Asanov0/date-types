# Тема: Итератор и итерируемый обьект!

# Интерация (iterable)- это общий термин, который описывает прцедууру взятия 
# элементов чего-то по очереди.
#В Python за ролучение итератора отвечает функйия iter():


# s = ('яблоко',"банан",'вишня')
# myit = iter(s)
# print(next(myit))
# print(next(myit))
# print(next(myit))

#Бул (next) кийиeнкиге жылдыру 

# Интерируемый обьект (iterable)-это обьект, который способен завершать элементы по одному.
# Кроме этого, это обьект, из которого можно получать итератор.

# Примеры интерируемых обьектов.
#   все последовательсности: список, строка,кортеж.
#словар 
# файл

# animals ={1:'pig',2:'egele',3:'baet'}
# a = iter(animals)
# print(next(a))
# print(next(a))
# print(next(a))


# frist = 'i want to speak English','and you ?'
# def one(frist):
#     two = iter(frist)
#     print(next(two))
#     return(next(two))
    

# print(one(frist))

















