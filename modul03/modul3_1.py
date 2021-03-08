# n= int(input("un numar:"))
# if n<10 :
#     print("prea mic")
# elif n>10 :
#     print("prea mare")
# else n==10 :
#     print("just rightmm")

# #type
# my_string = "text"
# print(type(my_string))
# mtype = type(my_string)
# print(type(mtype))
#
# print(type(my_string) == str)

# print(ord("0"))
# print(ord("9"))

# var = input("Enter Something: ")
# if  47<ord(var[0])  :
#     print(type(var))
#     if  ord(var[0])<=57 :
#         result = int(var)
# print(result)

# var= input()
# if var :
#     print("succes")

#for loop
# for value in range(1, 10 ,2) :
#     print(value)
#     if value == 3 : #try 2
#         break
#         print("this will never be printed")
# else:
#     print("This is else :",  value)
# print("This is outside for", value)

# for letter in my_text:
#      print("letter is :",letter )

# for number in 123:
#     print("letter is :",number )

 #Interable objects
str_iter = "my_text".__iter__()
 # int_iter = (123).__iter__() # not iterable

print(type(str_iter))
print(next(str_iter))
print(next(str_iter))
print(next(str_iter))
print(next(str_iter))
print(next(str_iter))
print(next(str_iter))
print(next(str_iter))
# print(next(str_iter)) # Stop Iteration

# n = 21
# for number in range(2,21) :
#     print(number)
#     if n%number == 0:
#         print("nr nu este prim")
#         break
# else :
#     print("nr este prim")
# str_iter = range(1,21).__iter__()
# print(str_iter)



# n = int(input("n = "))
# for number in range(2, n):
#     if n % number == 0:
#         print("nr nu este prim")
#         break
# else:
#     print(f"{n} este prim")
#
#
# n = int(input("n = "))
# for nr in range(1,n+1):
#     if nr<3 :
#         print("f{nr} este prim")
#         continue
#     for number in range(2, n):
#             if n % number == 0:
#                 print("nr nu este prim")
#                 break
#     else:
#             print(f"{nr} este prim")


a = str(input)
for i in a :
    i_nr = ord(i) +129
    print(chr(i_nr), end="")

a = "a"
b = "b"
print(a and b)

if a:
    if b :
        print(b)
else :
    print(a)

a=0
b=1
print("resoult:",a or b)
if a:
    print(a)
else:
    print(b)


