number_3= '3'
print(number_3)
number_three= 3
print(number_three)

response = type(number_3)
print(response)

response = type(number_three)
print(response)

var1=123
result =type(var1)
print('This is an integer:', result)

#Integer base
bin_number = 0b10
print(bin_number)

oct_number = 0o10
print(oct_number)

hex_number = 0x10
print(hex_number)

#Integer Operations
print('Sum of 2+8 is : ' ,bin_number + oct_number)

#add method
print('Sum of 2+8 is : ' ,bin_number.__add__(oct_number))
print('Sum of 2+8 is : ' ,oct_number.__add__(bin_number))

#difference
print('Dif of 8-2 is: ', oct_number - bin_number)
print('Dif of 8-2 is: ', oct_number.__sub__(bin_number))

#mul method
print('multiplication 2 * 8 is :' , bin_number.__mul__(oct_number))
print('multiplication 2 * 8 is :' , oct_number * (bin_number))

print(3*3*3)
print(number_three.__mul__(number_three).__mul__(number_three))
print((3).__mul__(3).__mul__(3))

#raise to power
print("Power of: ")
number_3= 3
print(number_3 ** 3 )
print((number_3).__pow__(3))
pow(number_3 ,3)
print(pow(number_3 ,3))

# division
print("Division")
result = number_3 / 3
print(type(result))
print(result)
print('Trude div is :', number_3.__truediv__(3))

#Exercise
a = 3
b = 4
c = 5

#1
x = (-b - ((b ** 2 - 4 * a * c) ** (1 / 2))) / (2 * a)
print(x)
print(type(x))




# ex using methods
_4ac = (4).__mul__(a.__mul__(c))
b_sqr = b.__pow__(2)
sqr_result = b_sqr.__sub__(_4ac)
sqrt_result = pow(sqr_result, (1).__truediv__(2))
minus_b = (0).__sub__(b)
# div_up = minus_b.__add__(sqrt_result)
div_up = sqrt_result.__add__(minus_b)
div_down = (2).__mul__(a)
result = div_up.__truediv__(div_down)
print(result)

#Strings
string1 = 'My string\nThis is a new line'
print(string1)

string2 = "My string2"
print(string2)

string3 = '''My string3
This is a new line
This is another new line'''
print(string3)

print(type(string1), type(string2), type(string3))
#methods
print(string1 + string2)
print(string1.__add__(string2))

#exercise
# Write: This is my code 100 times on a new line
x= "This is my code\n"
print(x * 100)
print(x.__mul__(100))
print((100).__mul__(x)) #this is not implemented so it will do x.__mull__(100)

#String Types
formatable_string = f'Start : {string1} End: {string2}'
print(formatable_string)

#EX
nume = 'Airini'
prenume = 'Michel'
formatable_string = f'Subsemnatul {nume} {prenume} \neste rugat sa se prezinte ...'
print(formatable_string)

raw_string=r'\nThere is no new line\n'
print(raw_string)

#String Methods

string1= "My string: {}"
result = string1.format("String Name")
print(result)

string1 = "Subsemnatul {} {} \n declar : "
result = string1.format("Airini", "Michel")
print(result)

string = "My string {}"
result = string.replace('{', '(')
result.replace('}', ')')
print(result)