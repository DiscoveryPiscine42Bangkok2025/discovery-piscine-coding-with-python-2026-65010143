import sys

x = sys.argv[1]
x = int(x)
for i in range(0,x+1):
    print("Table de",i,":",end=" ")
    for j in range(0,11):
        if j != 10 :
            print(j*i,end=" ")
        else:
            print(j*i,end="\n")
