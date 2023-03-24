# 1) Python тилинде канча озуго камтыган функциясы бар?
# главный уч функция (print,input,type)

# 2) Python артыкчылыктары эмнеде?
# Pythonдун артыкчылыгы мен учун бул тил жаш , коп колдонулучу , уйронуго женил 

# 3) ZeroDivisionError - кандай учурда чыгат?
# int = 0
# print(int/0)

# 4) Функция жаратып уч тамганы бир бирине кошунуз..  a, b, c
# x,y,z=('a','b','c')
# print(x+y+z)

# Андан сон ушул эле тапшырманы lambda функциясында тузунуз
# s = lambda s, f , g : s + f + g
# print(s('a' , 'b' ,'c'))

# # # 5) Функция жаратып диалог тузунуз, параметрлер учтон аз болбошу шарт..
# def diyalog():
#     print("Кандайсын Айжаркын кайсыл жерге келдин?")
#     def inner():
#         return "Жакшы озун кандайсын ЦУМга келдим"
#     def welcome():
#         return "Батыраак бол кутуп калдык сени"

#     print(inner())
#     print(welcome())
#     print("Кечиресенер жумуштарым чыгып калды")

# diyalog()

# 6) Замыкание түзүп бериниз..
# def star():
#     sky = 'shany'
#     def claud():
#         print(sky , 'sun')
#     return claud ()

# star()

# 7) Функция жазып ага декоратор колдонунуз, (декоратордун параметрлери да болуш керек)
# def dekorator (hi_msg, bye_msg):
#     def inner_decorator(func):
#         def travel(*args, **kwargs):
#             print(hi_msg)
#             func(*args, **kwargs)
#             print(bye_msg)

#         return travel
#     return inner_decorator

# @dekorator('Cаякатка кайсыл олко ынгайлу сизге','Биз сиздерди кутобуз!!!')
# def ssyl (pas,tur,tai,kaz):
#     print(f'''Мамлекетердин ссылкасы:
#     Paris:{pas}
#     Turkey:{tur}
#     Tailant:{tai}
#     Kazakstan:{kaz}''')

# ssyl('hhtps://pas','hhtps://tur','hhtps://tai','hhtps://kaz')

# 8) try, except, finally колдонуп FileExistsError деген ошибканы,
# #  жонокой адам тушуно турган кылып озгортунуз
# try:
#     with open('fila.txt',encoding = 'uft8') as file:
#         d = file . readlines()
#         print(d)
# except FileNotFoundError:
#     print('Файлды туура жазыныз')

# 9) Бир команда менен рабочии столго 5 папка ачыныз(терминал аркылуу)
# дектошоп чыгып (md papka1,papka2,papka3,papka4,papka5) Enter

# 1)
# sun = 6
# while sun > 1:
#     sun -= 1

#     print(sun)

# language = ['Python','php','java']
# for i in language:
#     print(i)
#     if i =='Python':
#         break


# class Hpone:
#     def __init__(self,marka,color,vertion):
#         self.marka = marka
#         self.color = color 
#         self.vertion = vertion
        
#     def print_details(self):
#         details = f"Marka: {self.marka}, speed:{self.color}, color:{self.vertion}"
#         return details

# Tel = Hpone('samsung','blue',20)

# print(Tel.print_details())

# Tel = Hpone('samsung','blue',15\)
# print("marka:", Tel.marka)

# 3 класс  жаратып ар биринин ичине учтон метод жазышыбыз керек



# 1) home work
# class Notbook:
#     def __init__(self,marka,color,gb):
#         self.marka = marka
#         self.color = color
#         self.gb = gb

#     def print_moon(self):
#         moon = f"marka:{self.marka}, color:{self.color}, gb: {self.gb}"
#         return moon


# book = Notbook('samsung','black',16)
# print(book.print_moon())
# copybook = book
# print(type(copybook.print_moon))


# 2) home worke

# class Fridge:
#     def __init__(self,model,boxes,year):
#         self.model=model
#         self.boxes=boxes
#         self.year=year

#     def print_cold(self):
#         cold = f"model: {self.model}, boxes:{self.boxes}, year: {self.year}"
#         return cold

#     def cold(self, Fridge):
#         for x in Fridge:
#          if x == Fridge:
#             return x

# print(Fridge.cold)
# colder = Fridge("LG",6,2020)
# print(colder.print_cold())
 

# Машина тузу
# 1)
# class Car:
#     def __init__(self, speed,color):
#         self.speed = speed
#         self.color = color

#     def is_red(self):
#         if self.color == "Red":
#             return True
#         return False

#     def check_Speed(self):
#         if self.speed < 100:
#             return "slow car"
#         elif self.speed > 100 and self.speed <=200:
#             return "Car with avarage speed"
#         else:
#             return "Fast Car"

# test = Car(260,"Red")
# print(test.is_red())
# print(test.check_Speed())
        

# 2)   
# class Car:
#     car_list = []

#     def __init__(self, speed,color):
#         self.speed = speed
#         self.color = color

#     def is_red(self):
#         if self.color == "Red":
#             return True
#         return False

#     def check_Speed(self):
#         if self.speed < 100:
#             return "slow car"
#         elif self.speed > 100 and self.speed <=200:
#             return "Car with avarage speed"
#         else:
#             return "Fast Car"

#     def populate_list(self,car_list):
#         car_list.append(self.color)
#         # car_list.pop()
#         return car_list


# test = Car(260,"Red")
# carlst=[]
# print(test.is_red())
# print(test.check_Speed())
# print(test.populate_list(carlst))
        


# 1) Наследование

# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)


# class Student(Person):
#     pass

# x = Student("Umar","Nurlanbekov")
# x.printname())


# 1) home worke 2022.12.22
# class Book:
#     def __init__(self,interesting,leaf,name):
#         self.interesting = interesting
#         self.leaf = leaf
#         self.name = name
    
#     def kopy_book(self):
#         if self.interesting == "yes interesting":
#             return True 
            

#     def how_many_leaves(self):
#         if  self.leaf <= 200:
#             return "ok this norm"
#         elif self.leaf <= 50 and self.leaf <=100:
#             return " for the interesting book this is few"
#         else:
#             return "not really"
#         # while leaf > 1:
#         #     leaf -= 1
        

#     def taime(self):
#         if self.name == "Taime management":
#             return  "i know this a book"
    

#     def welcome(self):
#         print("welcome","i recommend this book to you")

# books = Book("yes interesting",180,"Taime management")
# print(books.kopy_book())
# print(books.how_many_leaves())
# print(books.taime())
# print(books.welcome())


# 2) Home worke 

# class Hose:
#     def __init__(self,floor,room):
#         self.floor = floor
#         self.room = room

#     def flet(self):
#         self.flets = 1
#         flets = 20
#         while flets > 1:
#                 flets = 1

#         return flets

#     def apetment(self):
#         if self.floor == 2:
#             return 2

# city = Hose(2,"15")
# print(city.flet())
# print(city.apetment())

# class Stor(Hose):
#     def __init__(self,flet):
#         self.flet = flet

#     def edd(self):
#        if self.flet == 20:
#         return "great"
    
# shop = Stor("ok")
# print(shop.edd())

# class Holl(shop):
#     def __init__(self, flets):
#         self.flets = flets
#         return flets

# ofis = Holl(2,"great")
# print(ofis.apetment())
# print(ofis.flets())




# d = '*'
# s = '*'
# a = '*'
# j = '*'
# if d == '*':
#     print('*')
# if s == '*':
#     print(s*2)
# if a == '*':
#     print(a*3)
# if j == '*':
#     print(j*4)


# a = 6
# for i in range (6):
#     print(i)

 
# i = '*'
# while i <='*''*''*''*''*':
#     print(i)
#     i += '*'


# isHart = True
# while isHart:
#     if input("whrite: ")== 'stop':
#         isHart = False


# f = '*'
# while f <= '*****':
#     print(f)
#     f +='*'


# a = 5
# print(a**3)

# aza = 'bugun kundun altynchy kunu'
# def lastword(last):
#     return(len (last[21:25]))


# lastword()



# def lastword(test):
#     word = test .split()
#     return len (word[-1])

    
# lastword("kjfldzk hjckv mvlvklk")



# fruits = [34,54,67,34]

# def lukelike(fruits):
#     return len(set(fruits)) == len(fruits)


# print(lukelike(fruits))

# f = '*'
# while f <= '*****':
#     print(f)
#     f +='*'


# aza = [34,56,34,67]
# def lukelike(aza):
#     return len (set(aza)) == len (aza)

# print(lukelike(aza))


# a = [76545,6544,245,4543,543,67,6,78,7,65,34,65]
# def second(a):
#     return set(a) == (a)

# print(second(a))


# #---------------------------------------------------------------------
# import calendar
# input_year = int(input('Enter year:'))

# if calendar.isleap(input_year):
#     print('it is a leap year')
# else:
#     print('it is a not leap year')



# import calendar
# one = int(input('Enter year'))
# if calendar.isleap(one):
#     print('it is a leap year')
# else:
#     print('it is a not leap year')


# test = 'i need a lot of practice'
# def lastword(test):
#     return (test[::-1])
    
# print(lastword(test))


# s = "kazak"
# def palindrom(s):
#     if len(s) <=1: 
#         return "Да палиндром"
#     if s[0] != s[-1]:
#         return "Не палиндром"
#     return palindrom(s[1: -1])

# print(palindrom(s))



# list = [3,1,9,8,5,54,55,44,2]
# for i in range(0,len(list)):
#     for j in range(i+1,len(list)):
#         if list[i] >= list[j]:
#             list[i] , list[j] = list[j] , list[i]
        

# print(list)


# min = ["flower","flow","flight"]
# def ones(min):
#     one = ""
#     for i in range(len(min[0])):
#         for s in min:
#             if i == len(s) or s[i] != min [0][i]:
#                 return one
#         one += min [0][i]
# print(ones(min))





# Калкульятор
# from tkinter import Tk, Entry, Button, StringVar

# class Calculator:
#     def __init__(self,master):
#         master.title('Calculator')
#         master.geometry('357x420+0+0')
#         master.config(bg='gray')
#         master.resizable(False,False)

#         self.equation=StringVar()
#         self.entry_value=''
#         Entry(width=17,bg='#ccddff',font=('Arial Blod',28),textvariable=self.equation).place(x=0,y=0)

#         Button(width=11,height=4,text='(',relief='flat',bg='white',command=lambda:self.show('(')).place(x=0,y=50)
#         Button(width=11,height=4,text=')',relief='flat',bg='white',command=lambda:self.show(')')).place(x=90,y=50)
#         Button(width=11,height=4,text='%',relief='flat',bg='white',command=lambda:self.show('%')).place(x=180,y=50)
#         Button(width=11,height=4,text='1',relief='flat',bg='white',command=lambda:self.show(1)).place(x=0,y=125)
#         Button(width=11,height=4,text='2',relief='flat',bg='white',command=lambda:self.show(2)).place(x=90,y=125)
#         Button(width=11,height=4,text='3',relief='flat',bg='white',command=lambda:self.show(3)).place(x=180,y=125)
#         Button(width=11,height=4,text='4',relief='flat',bg='white',command=lambda:self.show(4)).place(x=0,y=200)
#         Button(width=11,height=4,text='5',relief='flat',bg='white',command=lambda:self.show(5)).place(x=90,y=200)
#         Button(width=11,height=4,text='6',relief='flat',bg='white',command=lambda:self.show(6)).place(x=180,y=200)
#         Button(width=11,height=4,text='7',relief='flat',bg='white',command=lambda:self.show(7)).place(x=0,y=275)
#         Button(width=11,height=4,text='8',relief='flat',bg='white',command=lambda:self.show(8)).place(x=180,y=275)
#         Button(width=11,height=4,text='9',relief='flat',bg='white',command=lambda:self.show(9)).place(x=90,y=275)
#         Button(width=11,height=4,text='0',relief='flat',bg='white',command=lambda:self.show(0)).place(x=90,y=350)
#         Button(width=11,height=4,text='.',relief='flat',bg='white',command=lambda:self.show('.')).place(x=180,y=350)
#         Button(width=11,height=4,text='+',relief='flat',bg='white',command=lambda:self.show('+')).place(x=270,y=275)
#         Button(width=11,height=4,text='-',relief='flat',bg='white',command=lambda:self.show('-')).place(x=270,y=200)
#         Button(width=11,height=4,text='/',relief='flat',bg='white',command=lambda:self.show('/')).place(x=270,y=50)
#         Button(width=11,height=4,text='x',relief='flat',bg='white',command=lambda:self.show('*')).place(x=270,y=125)
#         Button(width=11,height=4,text='=',relief='flat',bg='lightblue',command=self.solve).place(x=270,y=350)
#         Button(width=11,height=4,text='c',relief='flat',command=self.clear).place(x=0,y=350)
                                                   
                      

#     def show(self,value):
#         self.entry_value+=str(value)
#         self.equation.set(self.entry_value)

#     def clear(self):
#         self.entry_value=''
#         self.equation.set(self.entry_value)

#     def solve(self):
#         result = eval(self.entry_value)
#         self.equation.set(result)


# root = Tk()
# Calculator=Calculator(root)
# root.mainloop()



# print((lambda s,d: s+d)(44,5))




	
# def main():
# 	x,y = 10,8
# 	st = "x is more than y" if (x > y) else "x is greater than or equal to y"
# 	print(st)
	
# if __name__ == "__main__":
# 	main()
        

# ()
# def SwitchExample():
#     switcher = {
#         0: " This is Case Zero ",
#         1: " This is Case One ",
#         2: " This is Case Two ",
#     }
#     return switcher.get(0)

# print(SwitchExample())


# -----------------------------------------------------------------------------------------

# проверка (type)
# print(isinstance(5,object))



class Person:
    name = 'Ivat'
    age = 30

a = Person()

print(delattr,a.age)