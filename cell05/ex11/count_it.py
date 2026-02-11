import sys

y = sys.argv[1:]

if len(y) == 0:
    print('none')
else:
    print(f'parameters: {len(y)}')
    for i in y:
        print(f'{i}: {len(i)}')
