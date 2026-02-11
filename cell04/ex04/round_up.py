import sys
x = sys.argv[1]

print(f"Give me first number:",x)
x = float(x)
ix = int(x)   

if x > 0:
    if x == ix:
        result = ix
    else:
        result = ix + 1
elif x < 0:
    result = ix
else:
    result = 0

print(result)
