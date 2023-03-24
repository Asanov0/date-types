# 1) object (for)


# 1)
# f = 10
# for i in range(1,7):
#     f = f + i
#     print(f)


# 2)
# for i in range(1,11):
#     for f in range(1,11):
#         print(i*f , end = ' ')
#     print()


# 3)
# for i in range(100,10,-10):
#     print(i)


# 4)
# for i in range(10):
#         s = 10
#         if i > 5:
#                 print('*'*(s-i))
#         else:
#                 print('*'*i)


# 5)
# for i in range(10):
#     if i > 5:
#                 print(i)


# 6)
# a = ['Aizharkyn','Azat','Urmat','Sesim','Kutbaiyr','Umar','Janzat','Abdyrahman']
# for i in a:
#     if i == 'Umar':
#         continue
#     if i == 'Abdyrahman':
#         continue
#     print(i)
        

# 7)
# import random
# number = random.randint(1, 25)
# print(number)
# for i in range(number):
#     print(i)


# 8)
# for i in range(10):
#     print('*'*i)


# 9)
# for i in range(3,30,3):
#     print(i)

# 10
# for i in range(1,20):
#     if i < 15:
#         print(i+i)


# 11)


# 12)
# s = 5
# for i in range(1,3):
#     s = s + 4 *i
#     print(s)


# 13)
# a = 4
# for i in range(a*60):
#         print(i)


# 15)
# for i in range(20,10,-1):
#     if i > 10:
#         i=i + i
#     print(i)


# 16)
# star = int(input('whrite num:'))
# def two(star):
#     for i in range(star):
#         print(i)
# two(star)

# 17)
# 


# 18)
# for i in range(7):	 	
#     if i==0 or i==6:	 	 
#         for j in range(20):	
#             print('0',end='')
#     else:	 	 	 	 	 
#         print('0',end='') 
#         for j in range(1,19):	 
#             print('l',end='') 
#         print('0',end='')
#     print()


# 19
# a = 5
# s = 10
# d = 15
# f = a*5, s*3, d*3
# for i in f:
#     print(i)
    

# 20)
# a = [i for i in range(10)]
# print(a)


# 21)



# --------------------------------------------------------------------------------------------------

# 2) object (if else)

# 1)
# a = '*'
# s = '*'
# d = '*'
# f = '*'
# j = '*'
# if a == a:
#     print(a)
# if s == s:
#     print(s*2)
# if d == d:
#     print(d*3)
# if f == f:
#     print(f*4)
# if j == j:
#     print(j*5)


# 2)
# a = '*'
# s = '*'
# d = '*'
# f = '*'
# j = '*'
# if a == a:
#     print(a)
# if s == s:
#     print(s*2)
# if d == d:
#     print(d*3)
# if f == f:
#     print(f*4)
# if j == j:
#     print(j*5)
# if a == a:
#     print(a*4)
# if s == s:
#     print(s*3)
# if d == d:
#     print(d*2)
# if j == j:
#     print(j*1)


# 3)
# for i in range(13):
#     if i == 8:
#         continue
#     print(i)


# 4)
# t = int (input ('Температураны киргизгиле: '))
# if t > 250:
# 	print ('Мештеги температура өтө жогору')
# if 200 <= t <= 250:
# 	print ('Мештеги температура нормада')
# else:
# 	print ('Мештеги температура нормадан төмөн')


# 5)
# mashin = 4
# if mashin == 4:
#     print(4*60)
# if mashin == 240:
#     print(240 / 60)
# print(mashin)


# 6)
# for i in range(10):
#     s = 10
#     if i > 5:
#         print('*'*(s-i))
#     else:
#         print('*'*i)


# 7)
# a  = int(input('whrite gradus: '))
# if a > 250:
#     print('hit tempratrue')
# else:
#     if a >= 200 or a <=250:
#         print('norml temprature')



# 8)
# for i in range(1,10):
#     if i < 5:
#         print(i*2)
#     else:
#         print(i*3)


# 9)



# -----------------------------------------------------------------------------------------------
# 3) object (function)


# 1)
# s = [1,6,3,2,5,9,6,8,10,4,5,7]
# def one (s):
#     return set(s) or sorted(s)

# print(one(s))


# 2)
# a = [2,6,1,10,4,3,11,5,4,33,7,8]
# def num (a):
#     return(set(a) and sorted(a))
   
# print(num(a))


# 3)
# star = int(input('whrite num:'))
# def two(star):
#     for i in range(star):
#         print(i)
# two(star)


# 4)
# one = 9
# two = 9
# def numb(one,two):
#     for i in range(one):
#         for f in range(two):
#             print(i*f,end=' ')

# print(numb(one ,two))


# 5)
# def error():
#  print ('Программада ката')
# n = int (input()) 
# if n < 0:
#     print(n)
   
# error()


# 6)
# def rectangle():
#  a = float(input('Туурасы: '))
#  b = float(input('Бийиктиги: '))
#  s = a*b
#  print('Аянты: ', s)

# rectangle()


# 7)
# a = ['*', '**', '***','****','*****']
# def one(a):
#     for i in a:
#         print(i)

# one(a)


# 8)
# def print_сhar(s, n): 
#     k = n
#     while k > 0:
#         print (s, end = '') 
#         k -= 1 
# print_сhar ('-', 10)


# 9)
# s = 10
# def num (s):
#     for i in range(s):
#         for f in range(10):
#             print(i*f)

# num(s)


# 10)
# d = int(input())
# def one (d):
#     for i in range(d):
#         print(i)

# one(d)


# 11)
# def repeat(lst,num):
#     lst =[1,1,2,3,3,3,3,56,5,3,345]
#     s = lst.count(num)
#     return s

# print(repeat(1,3))

# 12)
# def num(s):
#     if s % 2 == 0:
#         print(s,'corect')
#     else:
#         print(s,'wrong')
# for i in range(15,30):
#     num(i)


# 13)
# def rectangle():
#  a = float(input('Туурасы: '))
#  b = float(input('Бийиктиги: '))
#  s = a*b
#  print('Аянты: ', s)

# def triangle():
#     a = float(input('Негизи: '))
#     h = float(input('Бийиктиги: '))
#     s = 0.5*a*h
#     print('Аянты: ', s)
# figure = input('1-тик бурчтук, 2-тик бурчтук:')
# if figure == '1':
#  rectangle()
# elif figure == '2':
#  triangle()


# 14)

# -------------------------------------------------------------------------------------------------
# 4) object (while)


# 1)
# a = 4
# s = 55
# d = 3
# while a != d*d:
#     a=a+1
#     s=s-4
#     d=d+5
# print(a,s,d)


# 2)
# a = '*'
# while a <= '******':
#     print(a)
#     a += '*'


# 3)
# a = True
# while a == True:
#     t = int (input ('Температураны киргизгиле: '))
#     if t > 250:
#         print ('Мештеги температура өтө жогору')
#     if 200 <= t <= 250:
#         print ('Мештеги температура нормада')
#     if t > 250:
#         print('Мештеги температура нормадан абдан жогору')
#     else:
#         print ('Мештеги температура нормадан төмөн')


# 4)
# a = 25
# s = '_'
# while a > 0:
#     print(s,end='')
#     a -= 1


# 5)
# for i in range(10):
#         if i > 5:
#                 print(i)


# 6)
# for i in range(2,101):
#     s = False
#     for f in range(2,i):
#         if i % f == 0:
#             s = True
#             break
#     if not s:
#         print(i)


# 7)
# n = int(input('Санды киргизиңиз: '))
# def digits_sum (n):
# 	total = 0
# 	while n > 0:
# 		total += n%10
# 		n = n // 10
# 	return total
# print(digits_sum(n))
    

# # 8)
# def sum(n):
#  sum = 0 
#  while n>0:
#     sum += n % 10 
#     n = n // 10 
#  return sum
# k = int(input('Санды киргизиңиз: '))
# while k > 9: 
#  k = sum(k) 
# if k%3==0:
#  print ('Сан 3кө бөлүнөт')
# else:
#  print ('Сан 3кө бөлүнбөйт')


