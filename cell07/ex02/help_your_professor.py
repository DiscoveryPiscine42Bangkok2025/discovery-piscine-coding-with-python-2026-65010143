class_3B = {
"marine": 18,
"jean": 15,
"coline": 8,
"luc": 9
}
class_3C = {
"quentin": 17,
"julie": 15,
"marc": 8,
"stephanie": 13
}

def average(x):
    n = 0
    for k,v in x.items():
        n+=int(v)
    return n/len(x.items())
print(f"Average for class 3B: {average(class_3B)}.")
