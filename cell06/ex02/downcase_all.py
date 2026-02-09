def downcase_it(x):
    y = x.split("'")
    y = x.split('"')
    y = list(filter(lambda i:i !=" " and i!="",y))
    if len(y) == 0:
        print("none")
    else:
        for i in y:
            print(i.lower())
x = input()
downcase_it(x)
