import sys

y = sys.argv[1:]

if len(y) >= 2:
    for i in reversed(y):
        print(i)
else:
    print("none")
