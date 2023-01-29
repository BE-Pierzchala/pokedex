import pickle

from data import data


try:
    print('Loaded old pokedex!')
    with open('pokedex.pickle', 'rb') as file2:
        record = pickle.load(file2)
except:
    print('Didnt find a save file')
    record = data()

last_pokemon = ''
last_type = ''
last_result = ''

usr = ''

while( usr != 'q'):
    usr = input("\nq: quit\n1: add pokemon interaction\n2: add pokemon\n3: Pokemon data type\n4: pokechart\ns: Save\n>")
    if( usr == '1'):
        print('\nAdding interaction!\nIf you want to quit press q at any time\n')
        
        name = input('Whats the target pokemon? Use previous one: ' + last_pokemon + ' press ENTER\n>')
        if name == 'q': continue
        if name == '': name = last_pokemon
        last_pokemon = name
        
        type_ = input('Whats the move type? Use previous one: ' + last_type + ' press ENTER\n>')
        if type_ == 'q': continue
        if type_ == '': type_ = last_type
        last_type = type_
        
        res = input('Whats the result? 0: immune, 0.5: weak, 1: even, 2: strong\n>')
        if res == 'q': continue

        record.addEntry(type_, name, res)
        print(record.pokemons[name])
        
    elif( usr == '2' ):
        print('\nAdding Pokemon type!\nIf you want to quit press q at any time\n')
        
        name = input('Whats the pokemon name?\n>')
        if name == 'q': continue
        
        type_ = input('Whats the pokemon type?\n>')
        if type_ == 'q': continue
        tmp = input('Whats the second pokemon type? If one type only, press ENTER\n>')
        if tmp == 'q': continue
        type_ = [type_]
        if tmp != '': type_.append(tmp)
        
        record.addPokemon(name, type_)
        print(record.pokeType[name])
    elif usr == '3':
        tmp = input('Pokemon name: \n>')
        print(record.getPokemonMoves(tmp))
    elif( usr == '4' ):
        record.getMultipliers()
    elif( usr == 's' ):
        with open('pokedex.pickle', 'wb') as file:
            pickle.dump(record, file)
        
    elif( usr == '5' ):
        for p in record.pokemons:
            print(p, ':', record.pokemons[p])
    elif( usr == '6' ):
        for p in record.pokeType:
            print(p, ':', record.pokeType[p])

with open('pokedex.pickle', 'wb') as file:
    pickle.dump(record, file)
    
