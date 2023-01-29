import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import numpy as np

class data:
    effects = {0:'0', 0.5:'-', 1:'1', 2:'+'}  # Translates effectivness of moves into str
    inv_effects = {'0':0, '-':0.5, '1':1, '+':2} # ^ inverse
    
    def __init__(self):
        self.typesDict = {} # Stores known types, and corresponding place in multipliers
        self.multipliers = -np.ones((18,18)) # Stores the matchups of types
        self.pokeType = {} # Stores pokemon of known type, and their type
        self.pokemons = {} # Stores seen pokemon, and their responses to moves
    
    def getPokemonMoves(self, name):
        if name in self.pokemons:
            return self.pokemons[name]
        return []
    
    def getPokemonType(self, name):
        if name in self.pokeType:
            return self.pokeType[name]
        return [] 
    
    def setMultiplier(self, attackType, defendType, val):
        self.multipliers[self.typesDict[attackType]][self.typesDict[defendType]] = val
        
    def getMultiplier(self, attackType, defendType):
        # If one of the types unknown, the multiplier will be unknown
        if attackType not in self.typesDict or defendType not in self.typesDict:
            return -1
        return self.multipliers[self.typesDict[attackType]][self.typesDict[defendType]]
    
    # Show multipliers as a heatmap
    def getMultipliers(self):
        # Create a custom colorscheme
        cm = matplotlib.colors.ListedColormap(['powderblue', 'black', 'tab:red','silver', 'tab:green'])
        # Plot heatmap
        ax = sns.heatmap(self.multipliers, cmap = cm,linewidth=0.5, xticklabels = self.typesDict.keys(), yticklabels = self.typesDict.keys())
        ax.xaxis.tick_top()
        plt.xticks(rotation=90)
        plt.show(block=True)
        
    def checkSpelling(self, var, message):
        usr = ''
        while usr != 'y':
            print(message)
            usr = input('New val: ' + str(var) + ' Is it correct? y/n\n>')
            if usr == 'n':
                var = input('Retype:\n>')
        return var
        
#--------------- More complex ---------------#       
        
    # Add a new type    
    def addType(self, t):
    # Returns given type in case it was modified 
        if t not in self.typesDict:
                t = self.checkSpelling(t, 'Adding type!')
                self.typesDict[t] = len(self.typesDict)
        return t
    
        
    # Add pokemon to data base
    def addPokemon(self, pokemon, types):
        for t in types:
            tmp = self.addType(t)
            types[types.index(t)] = tmp
                    
        if pokemon in self.pokeType:
            if self.pokeType[pokemon] == types:
                print('Already in the data base!')
                return
            print('Previous entry:', self.pokeType[pokemon])
            print('New entry:', types)
            
            if self.checkSpelling('n', 'Replace? y/n') == 'n':
                return

        self.pokeType[pokemon] = [types[0]]

        if len(types) == 2:
            self.pokeType[pokemon].append(types[1])
            
        print(pokemon, ':', self.pokeType[pokemon])
        
        # If it's a pokemon we fought, we can fill the multipliers array
        # provided it has one type, cba to make it more complicated
        if pokemon in self.pokemons:
            self.updateMultipliers(pokemon)
   
    
    def updateMultipliers(self, pokemon):
        # Only update if pokemon has 1 type
        if len(self.pokeType[pokemon]) > 1:
            return
        moves = self.pokemons[pokemon]
        type_ = self.pokeType[pokemon][0]
        
        for move in moves:
            
            if self.getMultiplier(move[1:], type_) == -1:
                self.setMultiplier(move[1:], type_, self.inv_effects[move[0]])
                
            elif self.getMultiplier(move[1:], type_) != float(self.inv_effects[move[0]]):
                usr = ''
                while usr not in ['y','n']:
                    usr = input('Conflict! ' + str(move[1:]) +' : ' + str(type_) + ' \nOld: ' + str(self.getMultiplier(move[1:], type_)) + ' New: ' + str(self.inv_effects[move[0]]) + '\n Replace? y/n\n>')
                    if usr == 'y':
                        self.setMultiplier(move[1:], type_, self.inv_effects[move[0]])
            else:
                print(str(move[1:]) +' : ' + str(type_) + ' \nOld: ' + str(self.getMultiplier(move[1:], type_)) + ' New: ' + str(self.inv_effects[move[0]]))
                print('Already known!')
                return 
                    

        self.getMultipliers()
        
    def addInteraction(self, pokemon, toAdd):
        for move in self.getPokemonMoves(pokemon):
            if toAdd[1:] == move[1:]: 
                print('Conflict! ' + toAdd + ' vs ' + move)
                tmp = self.checkSpelling(toAdd[0], 'Change interaction!')
                toAdd = tmp + toAdd[1:]
                self.pokemons[pokemon][self.pokemons[pokemon].index(move)] = toAdd
                return      
        self.pokemons[pokemon].append(toAdd)
    
    def addEntry(self, moveType, targetPokemon, result):
        
        while result not in ['0', '0.5', '1', '2']:
            result = input('Incorrect result: ' + str(result) + ' type new\n>')
        
        result = float(result)
        toWrite = self.effects[result] + moveType

        if moveType not in self.typesDict:
            moveType = self.addType(moveType)

        if targetPokemon not in self.pokemons:
            targetPokemon = self.checkSpelling(targetPokemon, 'New Pokemon!')
            self.pokemons[targetPokemon] = [ toWrite ]
        else:
            if toWrite not in self.pokemons[targetPokemon]:
                self.addInteraction(targetPokemon, toWrite)
                    
        if targetPokemon in self.pokeType:
            self.updateMultipliers(targetPokemon)
            
        print(targetPokemon, self.getPokemonMoves(targetPokemon))
