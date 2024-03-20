# Calculate the amount of fuel left in your vehicle as a decimal

while True:
    f = input("Fraction: ")

    try:
        x, y = f.split("/")
        x = int(x)
        y = int(y)
        p = x / y

        if p <= 1:
            break

    except ValueError:
            pass
    except ZeroDivisionError:
            pass
p = p * 100
p = round(p)

if p >= 99:
    print("F")

elif p <= 1:
     print("E")

else:
    print(f"{p}%")

