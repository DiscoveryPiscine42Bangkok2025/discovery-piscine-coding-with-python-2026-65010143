import sys
x = sys.argv[1]
x = int(x)
print(f"Please tell me your age:",x)

for i in [10,20,30]:
    print(f"In {i} years, you'll be {x+i} years old")
