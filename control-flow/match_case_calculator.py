number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))
operation = input("Choose the operation (+, -, *, /): ")
result = 0

match operation:
    case "+":
        result = number_1 + number_2
    case "-":
        result = number_1 - number_2
    case "*":
        result = number_1 * number_2
    case "/":
        result = number_1 / number_2
    case _:
        result = "Invalid operation"

print("The result is ", result)