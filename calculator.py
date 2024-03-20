# A simple calculator
expression = input("Expression: ")

x, y, z = expression.split(" ")

x = float(x)

z = float(z)

if y == "+":
    outcome = x + z
elif y == "-":
    outcome = x - z
elif y == "*":
    outcome = x * z
elif y == "/":
    outcome = x/z

print(round(outcome, 1))
