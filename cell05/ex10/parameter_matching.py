import sys

y = sys.argv[1:]

if len(y) == 1:
    ans = input(f'What was the parameter? ')
    if y[0] == ans:
        print("Good job!")
    else:   
        print("Nope, sorry...")
else:
    print("none")
