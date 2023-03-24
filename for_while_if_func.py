                                # Home work
# (for)

# 1) 

# one = '*'
# for i in range(10):
#     print(" " *(10 - i),one * i * 2)

# 2)
# two = 'Urmat','Umar','Abdrahman','Janzat','Sezim','Aijarkyn'
# def one(two):
#     hi = two
#     for i in hi:
#         print(i,'hello')


# print(one(two))


# 3)
# for i in range(2011,2024):
#     if i == 2023:
#         print('rabbit year 2023')
#     print(i)


# 4)

# k = '*'
# for i in range(10):
#     print(i * k)


# 5)
# a = (3,1,9,8,5,54,55,44,2)
# def one(a):
#     two = a
#     for i in sorted(two):
#         print(i)

# print(one(a))


# 6)

# num = [3,4,8,10,6,2]
# for nums in num:
#     if nums %2 == 1:
#         print(nums)
#         break

# else:
#     print("Not find")


# 7)
# for i in range(1,11):
#     print(i,i**3)


# 8)
# for k in range(5,0,-1):
#  print ( k**2 )
               
         
# 9)
# mygroup =  {'4 group': 'Azat, Aizharkyn ,Kutbaiyr ,Urmat, Janzat, Sesim','3 group':''}
# mygroup['3 group']='Abdyrahman ,Umar'
# for i in mygroup:
#         print(i)
#         print(mygroup[i])


# 10)
# nums = [1, 2, 4, 6]
# sum_positives = 0
# for num in nums:
#     if num < 0:
#         continue
#     sum_positives += num
# print(f'Sum of Positive Numbers:', sum_positives)



        # while
# 1)
# a = 0
# while a < 100:
#     a += 2
#     print(a)
    

# 2)
# d = 2
# while d <= 2:
#    name = input('Салам родной сенин атын ким ? ')
#    print('Жакшы анда' , name )
#    age = int(input("Канча жаштасын ?"))
#    print(age)
#    if age <= 25:
#     print("Жаш турбайсынбы")
# print(name,age)


# 3)
# i = 0
# while i < 6:
#   i += 1
#   if i == 4:
#     break
#   print(i)


# 4)
# d = 2
# while d <= 3:
#     money = input("Кайсыл валютаны алмаштырасыз: ")
#     if money == 'долар':
#         change = int(input("Канча акча алмаштырас: "))
#         print(change * 80)
#     if money == "эвро":
#         money = int(input("Канча акча алмаштырас: "))
#         print(change * 100)
#     if money == 'рубль':
#         change = int(input("Канча акча алмаштырас: "))
#         print(change * 1.25)


# 5)
# k = 1
# while k <= 10 :
#  print ( 2**k )
#  k += 1


# 6)
# import random 
# number = random.randint(1, 25)
# choices = 0 
# while choices < 5:
#  print('1ден 25ке чейинки санды тап:') 
#  guess = int(input())
#  choices = choices + 1 
#  if guess == number: 
#     break


# 7)
# a = '*'
# while a <= '******':
#     print(a)
#     a +='*'


# 8)
# isHart = 1
# while isHart:
#     if input("whrite: ")== 'stop':
#         isHart = 0


# 9)
# a = 1 
# while a == 1:
#     b = input('Сенин атын ким? ')
#     print('Салам', b, 'кош келипсин!!!')



# 10)
# k=4  
# p=1040
# m=2
# while p != m*m:
#     k=k+1
#     p=p-4
#     m=m*2
# print (k,p,m)



#    function

# 1)
# pal = input("write palindrom word ")
# def first(pal):
#     pol = pal[::-1]
#     if pol == pal:
#         return("yes it is palindrom")
#     else:
#         return("it is not palindrom")
     
# print(first(pal))


# 2)
# mark = int(input('Введите свой бал '))
# def num(mark):
#   ort = mark
#   if ort >= 120:
#     return('Поздравляем вы прошли экзамен')
#   elif ort < 120:
#     return('Вы не прошли экзамен')

# print(num(mark))


# 3)
# def main_func():
#     name = 'Carnell'
#     def inner():
#         return('Hello',name)

#     return inner()

# print(main_func())


# 4)
# def hi (*my):
#     """Бул функция  салам жолдойт my"""
#     for i in my:
#       print(i,'hello')


# hi('Erlan','Mirlan','Marlen','Osmon')


# 5)
# def lend(pay):
#     paying = "Омурбек"
#     """Бул функция толомду эскертет"""
#     text = f""" Урмату {paying}! мырза сиздин толом убактыныз 
#     эртен 05.10.2022 эстен чыгарбаныз биздин банк {pay}  """
#     print(text)
#     return pay

# lend('BAKAI bank')


# 6)
# tup = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
# def string(tup):
#     str = ''.join(tup)
#     return str
# print(string(tup))


# 7)
# def num(last_num):
#     i = 1
#     while i > last_num:
#       print(i)
# print('finished!')


# 8)
# def hello(n):
#     counter = 0
#     while counter < n:
#         print('Hello!')
#         counter = counter + 1

# hello(3)


# 9)
# def multup(num):
#         return num * num
# for i in [1,2,3,4]:
#         result = multup(i)
#         print(i , result)


# 10)
# min = ["flower","flow","flight"]
# def ones(min):
#     one = ""
#     for i in range(len(min[0])):
#         for s in min:
#             if i == len(s) or s[i] != min [0][i]:
#                 return one
#         one += min [0][i]
# print(ones(min))




#     if_elif

# 1)
# test=int(input("Введите свой бал:"))
# if test <=80:
#     print("Вы не прошли сесию!")
# elif test>=80:
#         print("Вы прошли сесию поздравляем")
# else:
#     print("Программа заверщена")


# 2)
# x = 5
# if x < 10 and x % 3 == 0:
#  print('True')
# else:
#  print('False')


# 3)
# a = 5
# if a < 10 or a % 3 == 0:
#         print(True)
# else:
#         print(False)


# 4)
# for i in range(10):
#         s = 10
#         if i > 5:
#                 print('*'*(s-i))
#         else:
#                 print('*'*i)


# 5)
# for i in range(10):
#         if i > 5:
#                 print(i)


# 6)
# a = ['Aizharkyn','Azat','Urmat','Sesim','Kutbaiyr','Umar','Janzat','Abdyrahman']
# for i in a :
#     if i == a[6]:
#         print('Umar 4 группа')
#     if i == a[-1]:
#         print('Abdyrahman 5 группа')
#     print(i)


# 7)
# a=int(input('Өзүңүздүн жашыңызды киргизиңиз: '))
# if a >= 21:
#         print('Уруксат')
# elif a >= 18:
#         print('Жарым-жартылай уруксат')
# else:
#         print('Уруксат эмес')


# 8)
# def one():
#     d = 'Urmat'
#     def two():
#         return('hello',d)
#     return two()

# print(one())


# 9)
# import time
# a = (input(time ))
# def one(a):
#     s = a
#     if s == time.ctime():
#         print('it is right')
#     else:
#         if s != time: 
#             print(s,"it is not right")
#             return(time.ctime())
#     return s

# print(one(a))


# for i in range(1,10):
#     for f in range(1,10):
#         print(i * f ,end='\t')
#     print()


# import time
# a = (input(time ))
# def one(a):
#     s = a
#     if s == time.ctime():
#         print('it is right')
#     else:
#         if s != time: 
#             print(s,"it is not right")
#             return(time.ctime())
#     return s

# print(one(a))


