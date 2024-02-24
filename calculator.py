def calculate(num1, num2, op):

  if op == "+":
    return num1 + num2
  elif op == "-":
    return num1 - num2
  elif op == "*":
    return num1 * num2
  elif op == "/":
    if num2 == 0:
      return "Error: Division by zero"
    else:
      return num1 / num2
  else:
    return "Invalid operation"

while True:
  # Get user input
  try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    op = input("Choose an operation (+, -, *, /): ")
  except ValueError:
    print("Invalid input. Please enter numbers and valid operations.")
    continue

  # Perform calculation and display result
  result = calculate(num1, num2, op)
  print(result)

  # Ask if user wants to continue
  choice = input("Do you want to calculate again? (y/n): ")
  if choice.lower() != "y":
    break
