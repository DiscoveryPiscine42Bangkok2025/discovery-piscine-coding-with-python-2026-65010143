x = input()
y = x.split("'")
y = x.split('"')
y = list(filter(lambda i:i !=" " and i!="",y))
if len(y) == 1:
    ans = input(f'What was the parameter? ')
    if y[0] == ans:
        print("Good job!")
    else:   
        print("Nope, sorry...")
else:
    print("none")
