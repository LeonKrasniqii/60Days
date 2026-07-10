# ----- Variable -----
# ----- string -----
# first_name = "Bro"
# food = "Shrimp"
# email = "Bro123@gmail.com"
# print(f"Hello {first_name}")
# print(f"You like {food}")
# print(f"Your gmail is {email}")
# ----- integer -----
# age = 12
# quantity = 3.5
# num_of_students = 30
# print(f"You are buying {quantity} items")
# print(f"Your age is {age}")
# print(f"your class has {num_of_students} students")
# # ----- float -----
# price = 10.99
# gpa = 3.4
# distance = 5.5
# print(f"the price is ${price}")
# print(f"your gpa is {gpa}")
# print(f"you ran {distance}km")
# ----- boolean -----
# is_student=True
# for_sale = False

# if is_student:
#     print("You are a student")
# else:
#     print("You are not a student")

# if for_sale:
#     print("Item is for sale")
# else:
#     print("Itme not for sale")

# ----- Typecasting -----

# name = "Bro Code"
# age = 25
# gpa = 3.2
# is_student = True
# name = bool(name)
# gpa = int(gpa)
# age = str(age)
# age += "1"
# print(type(name))

# userinput
# name =input("What is your name?: ")
# age = int(input("How old are you?: "))

# #age = int(age)
# age = age + 1

# print(f"Hello {name}!")
# print(f"Hello you are {age} years old")
# print("HAPPY BIRTHDAY")

# Exercise 1 Rectangle Area Calc

# length = float(input("Enter the length: "))
# width = float(input ("Enter the width: "))
# area = length * width

# print(f"The area is: {area}cm²")

# Exercise 2 Shopping Cart Program

# item = input("What item would you like to buy?: ")
# price = float(input("What is the price?: "))
# quantity = int(input("How many would you like?: "))
# total = price * quantity

# print(f"You have bought {quantity} X {item}/s")
# print(f"Your total is: {total}$")

#  ----- Matlibs game -----
# #word game where you create a story by filling in the blanks
# adjective1 = input("Enter an adjective(description): ")
# adjective2 = input("Enter an adjective(description): ")
# adjective3 = input("Enter an adjective(description): ")
# noun1 = input("Enter an noun(person, place, thing): ")
# verb1 = input("Enter a verb ending with 'ing': ")
# print(f"Today i went to a {adjective1} zoo.")
# print(f"In a exhibit, I saw  a {noun1}")
# print(f"{noun1} was {adjective2} and {verb1}")
# print(f"I was {adjective3}!")

# ----- arithmatic & math -----

# friends  = 10
# friends = friends + 1
# friends += 1
# friends = friends - 2
# friends -= 2 
# friends = friends * 3
# friends *= 3
# friends = friends / 2
# friends /= 2
# friends = friends ** 2
# friends **= 2
# remainder = friends % 2

# print(friends)

# x = 3.14
# y = -4
# z = 5

# result = round(x)
# result =  abs(y)
# result = pow(4,3)
# result = max(x,y,z)
# result = min(x,y,z)
# print(result)

# import math

# x = 9

# print(math.pi)
# print(math.e)

# result = math.sqrt(x)
# result = math.ceil(x)
# result = math.floor(x)

# print(result)

# radius = float(input('Enter the radius of a circle'))

# circumfrence = 2 * math.pi * radius

# print(f"The circumfrence is : {round(circumfrence, 2)}cm")

# radius = float(input("Enter the radius of a circle"))

# area = math.pi * pow(radius, 2)

# print(f"The area of the circle is: {round(area, 2)}cm^2")

# a = float(input("Enter sie A: "))
# b = float(input("Enter sie B: "))

# a = math.sqrt(pow(a, 2) + pow(b,2))

# print(f"Side C = {c}")

#  ----- If Statment ------

# age = int(input("Enter your age: "))

# if age >= 18:
#     print("You are now singed up!")
# elif age < 0:
#     print("You havent been born yet!")
# elif age >= 70:
#     print("You are too old to sign up")
# else:
#     print("You must be 18+ to sign up!")

# response = input("Would you like food? (Y/N): ")

# if response == "Y":
#     print("What food would you like to eat?")
# elif response == "N":
#     print("No food for you!")

# for_sale = True
# online = False

# if online:
#     print("The user is onlien")
# else:
#     print("The user is NOT online!")

# if for_sale:
#     print("This item is for sale!")
# else:
#     print("This item is NOT for sale!")


# ----- Calculator Program -----

# operator = input("Enter an operator (+ - * /): ")
# num1 = float(input("Enter the 1st number: "))
# num2 = float(input("Enter the 2nd number: "))

# if operator == "+":
#     result = num1+num2
#     print(round(result, 3))
# elif operator == "-":
#     result = num1-num2
#     print(round(result, 3))
# elif operator == "*":
#     result = num1*num2
#     print(round(result, 3))
# elif operator == "/":
#     result = num1/num2
#     print(round(result, 3))
# else:
#     print(f"{operator} is not a valid operator")

# ----- PYTHON WEIGHT CONVERTER -----

# weight = float(input("Enter your weight"))
# unit = input("Kilograms or Pounds? (K or L): ")

# if unit == "K":
#     weight  = weight * 2.205
#     unit = "LBs."
#     print(f"Your weight is : {round(weight, 1)} {unit}")
# elif unit == "L":
#     weight = weight / 2.205
#     unit == "Kgs."
#     print(f"Your weight is : {round(weight, 1)} {unit}")
# else:
#     print(f"{unit} was not valid")

# ----- Temperature converter program -----

# unit  = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
# temp = float(input("Enter the temperature: "))

# if unit == "C":
#     temp = round((9 * temp) / 5 + 32, 1)
#     print(f"The temperature in Fahrenheit is: {temp}F")
# elif unit == "F":
#     temp = round((temp - 32) * 5 + 32, 1)
#     print(f"The temperature in Celsius is: {temp}C")
# else:
#     print(f"{unit} is an invalid unit of measurment")

# ----- Logical operators / or/and/not -----
# or = at least one condition is true
# temp = 25
# is_raining = False

# if temp > 35 or temp < 0 or is_raining:
#     print("The outdoor event is cancelled")
# else:
#     print("The outdoor event is still scheduled")

# and = both of the conditions are true

# not = inverts the condition (not False,not True)
# temp = 20
# is_sunny = False

# if temp >= 28 and is_sunny:
#     print("It is HOT outside !")
#     print("It IS SUNNY !")
# elif temp <= 0 and is_sunny:
#     print("It is COLD outside !")
#     print("It is SUNNY")
# elif 28 > temp > 0 and is_sunny:
#     print("It is WARMoutside !")
#     print("It is SUNNY")
# elif temp>= 28 and not is_sunny:
#     print("It is HOT outside !")
#     print("It IS CLOUDY !")
# elif temp <= 0 and not is_sunny:
#     print("It is COLD outside !")
#     print("It is CLOUDY")
# elif 28 > temp > 0 and not is_sunny:
#     print("It is WARMoutside !")
#     print("It is CLOUDY")