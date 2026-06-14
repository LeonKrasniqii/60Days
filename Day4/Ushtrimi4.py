# ---Grade Checker---
 
grade = int(input("Write your grade :"))
if grade < 0 or grade > 100:
    print("Invalid grade")
if grade >= 90:
    print("Your grade is A")
elif grade == 80:
    print("Your grade is B")
elif grade >= 70:
    print("Your grade is B")
elif grade == 60:
    print("Your grade is C")
elif grade == 50:
    print("Your grade is D")
elif grade < 40:
    print("Your grade is F")