Name = "Leon",
Age = 16,
Height = 1.80

name =input("Enter your name :")
age = int(input("Enter your age :"))
underage = "Your not an adult"
print("Hello",name)
print("Your age is :",age)


if age < 18:
    print(underage)

else:
    print("Your good to go")
