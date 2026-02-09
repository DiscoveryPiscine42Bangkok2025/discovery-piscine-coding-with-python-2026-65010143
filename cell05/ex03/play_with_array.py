x =  [2, 8, 9, 48, 8, 22, -12, 2]
new = []
for i in x:
    if i not in new and i > 5:
        new.append(i)
y = list(map(lambda i: i + 2,new))
result = [y[-1]] + y[:-1]
print(y)
print(result)
