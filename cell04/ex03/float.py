x = input(f"Give me first number: ")
try:
    x = int(x)
    print("This number is an integer.")
except:
    try:
        x = float(x)
        print("This number is a decimal.")
    except:
        print("This is a text.")
