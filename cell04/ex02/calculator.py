import sys
x1 = sys.argv[1]
x2 = sys.argv[2]
x1 = int(x1)
x2 = int(x2)
print(f"Give me the first number:",x1)
print(f"Give me the second number:",x2)

print("Thank you!")
print(f"{x1} + {x2} = {int(x1+x2)}")
print(f"{x1} - {x2} = {int(x1-x2)}")
print(f"{x1} / {x2} = {int(x1/x2)}")
print(f"{x1} * {x2} = {int(x1*x2)}")
