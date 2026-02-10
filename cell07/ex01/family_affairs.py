persons = input()

text = persons.strip()[1:-1]
pairs = text.split(",")
a =[]
person_d = {}
for pair in pairs:
    key, value = pair.split(":")
    key = key.strip().strip('"')
    value = value.strip().strip('"')
    person_d[key] = value

for i in person_d.keys():
    if person_d[i] =="red":
        a.append(i)
print(a)
    
