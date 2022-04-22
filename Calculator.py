print("\n***Welcome to World Best Calculator***")
a=int(input("\n Enter a first number for calculation"))
b=int(input("\n Enter a second number for calculation"))
operator=(input("Enter single operator at a time of ur choice (+,-,*,/,%)\n"))

if operator  ==  "+":
    print(f"The Sum of the number is",a+b)

elif operator == "-" :
    print(f"The Subtraction is {a-b} ")
elif operator ==  "*":
    print(f"The Multiplication is {a*b}")
elif operator == "/":
    print(f"The Division is {a/b}")
elif operator  ==  "%":
    print(f"The Modulo is {a%b}")
else:
    print("Invalid choice")
