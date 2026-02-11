import sys
print("Enter a number")
x = int(sys.argv[1])
for i in range(0,x+1):
    print(f"{i} x {x} = {i*x}")
