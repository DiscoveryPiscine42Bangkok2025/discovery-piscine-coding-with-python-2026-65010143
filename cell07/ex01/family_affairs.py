dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}
a =[]
for i in dupont_family.keys():
    if dupont_family[i] =="red":
        a.append(i)
print(a)
    
