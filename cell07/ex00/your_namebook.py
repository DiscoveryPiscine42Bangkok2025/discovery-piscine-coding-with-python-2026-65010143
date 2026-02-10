persons = input()

text = persons.strip()[1:-1]
pairs = text.split(",")
a =[]
person_d = {}
for i in pairs:
    key, value = i.split(":")
    key = key.strip().strip('"')
    value = value.strip().strip('"')
    w = key.capitalize()+" "+value.capitalize()
    a.append(w)
print(a)
