income = int(input('Enter your monthly income: '))
expenses = int(input('Enter your total monthly expenses: '))

savings = income - expenses
annual_rate = 0.05

projected_savings = (savings * 12) + (savings * 12 * annual_rate)
print(f"Your monthly savings are ${savings}.")
print(f"Projected savings after one year, with interest, is: ${int(projected_savings)}.")
