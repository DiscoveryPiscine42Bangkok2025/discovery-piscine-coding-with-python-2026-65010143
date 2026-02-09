x = input()
y= x.split(" ")
y_new = list(filter(lambda i: i != "",y))
print(f"Number of parameters: {len(y_new)}")
