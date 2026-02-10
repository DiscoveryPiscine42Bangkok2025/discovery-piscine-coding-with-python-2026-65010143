persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}
a =[]
for k,v in persons.items():
    w = k.capitalize()+" "+v.capitalize()
    a.append(w)
print(a)
