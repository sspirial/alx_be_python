number_1 = input("Enter the first number: ")
number_2 = input("Enter the second number: ")
operation = input("Choose the operation (+, -, *, /): ")
result = 0

match operation:
    case "+":
        result = int(number_1) + int(number_2)
    case "-":
        result = int(number_1) - int(number_2)
    case "*":
        result = int(number_1) * int(number_2)
    case "/":
        result = int(number_1) / int(number_2)
    case _:
        result = "Invalid operation"

print("The result is ", result)