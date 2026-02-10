women_scientists = {
"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}
def  famous_births(x):
    for k,v in x.items():
        name_l = v['name']
        birth_l = v['date_of_birth']
        print(f'{name_l} is a great scientist born in {birth_l}.')

famous_births(women_scientists)
