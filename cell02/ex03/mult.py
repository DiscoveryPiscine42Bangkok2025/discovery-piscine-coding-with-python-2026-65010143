first = input(("Enter the first number:\n"))
sec = input(("Enter the second number:\n"))
result = int(first) * int(sec)
print(f"{first} x {sec} = {result}")
if result < 0:
    print("This number is negative.")
elif result > 0:
    print("This number is positive.")
else:
    print("This number is both positive and negative.")
