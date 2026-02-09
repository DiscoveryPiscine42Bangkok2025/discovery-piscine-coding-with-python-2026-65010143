x= input(("Enter the number less than 25:\n"))
x = int(x)
if x > 25 :
    print("Error")
else :
    for i in range(x,26):
        print("Inside the loop, my variable is",i)
