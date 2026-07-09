#Variable
#string
first_name = "Bro"
food = "Shrimp"
email = "Bro123@gmail.com"
print(f"Hello {first_name}")
print(f"You like {food}")
print(f"Your gmail is {email}")
#integer
age = 12
quantity = 3.5
num_of_students = 30
print(f"You are buying {quantity} items")
print(f"Your age is {age}")
print(f"your class has {num_of_students} students")
#float
price = 10.99
gpa = 3.4
distance = 5.5
print(f"the price is ${price}")
print(f"your gpa is {gpa}")
print(f"you ran {distance}km")
#boolean
is_student=True
for_sale = False

if is_student:
    print("You are a student")
else:
    print("You are not a student")

if for_sale:
    print("Item is for sale")
else:
    print("Itme not for sale")

#Typecasting

name = "Bro Code"
age = 25
gpa = 3.2
is_student = True
name = bool(name)
gpa = int(gpa)
age = str(age)
age += "1"
print(type(name))

#userinput
name =input("What is your name?: ")
age = int(input("How old are you?: "))

#age = int(age)
age = age + 1

print(f"Hello {name}!")
print(f"Hello you are {age} years old")
print("HAPPY BIRTHDAY")

# Exercise 1 Rectangle Area Calc

length = float(input("Enter the length: "))
width = float(input ("Enter the width: "))
area = length * width

print(f"The area is: {area}cm²")

# Exercise 2 Shopping Cart Program

item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))
total = price * quantity

print(f"You have bought {quantity} X {item}/s")
print(f"Your total is: {total}$")

#Matlibs game
#word game where you create a story by filling in the blanks
adjective1 = input("Enter an adjective(description): ")
adjective2 = input("Enter an adjective(description): ")
adjective3 = input("Enter an adjective(description): ")
noun1 = input("Enter an noun(person, place, thing): ")
verb1 = input("Enter a verb ending with 'ing': ")
print(f"Today i went to a {adjective1} zoo.")
print(f"In a exhibit, I saw a {noun1}")
print(f"{noun1} was {adjective2} and {verb1}")
print(f"I was {adjective3}!")

#