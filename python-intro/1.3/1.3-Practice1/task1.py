num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
operator = input("Enter your desired operator (+ or -): ")

if operator == "+":
    result = num1 + num2
    print(f"The sum is: {result}")

elif operator == "-":
    result = num1 - num2
    print(f"The difference is: {result}")

else: 
    print("Unknown operator. Please use + or - and try again.")