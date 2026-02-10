women_scientists = {
"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

def  famous_births(x):
    result ={}
    for k,v in x.items():
        name_l = v['name']
        birth_l = v['date_of_birth']
        result[name_l] = birth_l
        result_sorted = dict(sorted(result.items(), key=lambda item: item[1]))
    for k,v in result_sorted.items():
        print(f'{k} is a great scientist born in {v}.') 

famous_births(women_scientists)
