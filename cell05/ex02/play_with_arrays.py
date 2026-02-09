x =  [2, 8, 9, 48, 8, 22, -12, 2]
y = list(filter(lambda i: i>5,x))
y = list(map(lambda i: i+2,y))
print(f'Original array: {x}')
print(f'New array: {y}')
