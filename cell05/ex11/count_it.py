x = input()
y = x.split("'")
y = x.split('"')
y = list(filter(lambda i:i !=" " and i!="",y))
if len(y) == 0:
    print('none')
else:
    print(f'parameters: {len(y)}')
    for i in y:
        print(f'{i}: {len(i)}')
