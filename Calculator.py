#User input
num1 = float(input("Enter first digit "))
num2 = float(input("Enter second digit "))
user_input = input("Enter the operation(+, -, /, *): ")

#Executing the operation
if user_input == "+":
    result = num1 + num2
elif user_input == "-":
    result = num1 - num2
elif user_input == "*":
    result = num1 * num2
elif user_input == "/":
    result = num1 / num2
else:
    result = "Invalid operation."

 #Displaying results
print(f" {num1}  {user_input}  {num2} is: {result}")
