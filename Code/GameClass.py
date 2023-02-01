import DataClass


class Game:

    def __init__(self, new_save: bool):
        # TODO: Realistically, these two should also be saved
        self.last_type = ''
        self.last_pokemon = ''
        self.data = DataClass.Data()
        if not new_save:
            self.data.open_save()

    def save(self):
        self.data.save()

    def action_on_input(self, user_input: str):
        match user_input:
            case '1':
                print('\nAdding interaction!\nIf you want to quit press q at any time\n')

                name = input('Whats the target pokemon? Use previous one: ' + self.last_pokemon + ' press ENTER\n>')
                if name == 'q': return
                if name == '': name = self.last_pokemon
                self.last_pokemon = name

                type_ = input('Whats the move type? Use previous one: ' + self.last_type + ' press ENTER\n>')
                if type_ == 'q': return
                if type_ == '': type_ = self.last_type
                self.last_type = type_

                res = input('Whats the result? 0: immune, 0.5: weak, 1: even, 2: strong\n>')
                if res == 'q': return
                self.data.addEntry(type_, name, res)
                print(self.data.pokemons[name])

            case '2':
                print('\nAdding Pokemon type!\nIf you want to quit press q at any time\n')

                name = input('Whats the pokemon name?\n>')
                if name == 'q': return

                type_ = input('Whats the pokemon type?\n>')
                if type_ == 'q': return
                tmp = input('Whats the second pokemon type? If one type only, press ENTER\n>')
                if tmp == 'q': return
                type_ = [type_]
                if tmp != '': type_.append(tmp)

                self.data.addPokemon(name, type_)
                print(self.data.pokeType[name])

            case '3':
                tmp = input('Pokemon name: \n>')
                print(self.data.getPokemonMoves(tmp))
            case '4':
                self.data.getMultipliers()
            case 's':
                self.data.save()

            case '6':
                for p in self.data.pokemons:
                    print(p, ':', self.data.pokemons[p])
            case '7':
                for p in self.data.pokeType:
                    print(p, ':', self.data.pokeType[p])
