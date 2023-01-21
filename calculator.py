#!/usr/bin/python3

i = 0

while i == 0:

    num1 = input("Please enter the first number: ")
    num2 = input("please enter the second number: ")
    num1 = int(num1)
    num2 = int(num2)

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit program")
    choice = input("Please pick one: ")
    choice = int(choice)

    if choice == 1:
        print(num1 + num2)
    elif choice == 2:
        print(num1 - num2)
    elif choice == 3:
        print(num1 * num2)
    elif choice == 4:
        print(num1 / num2)
    elif choice == 5:
        print("Bye")
        break
    elif choice > 5 or choice < 1:
        print("Please pick a valid choice!")
    i = 0
        
    
