import sys
print("Enter the number less than 25:")
y = int(sys.argv[1])
if y > 25 :
    print("Error")
else :
    for i in range(y,26):
        print("Inside the loop, my variable is",i)
