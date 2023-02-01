import pickle
import DataClass
import argparse
import GameClass

parser = argparse.ArgumentParser()

parser.add_argument("-n", "--new_save", action='store_true')

args = parser.parse_args()

game_client = GameClass.Game(args.new_save)

last_pokemon = ''
last_type = ''
last_result = ''

user_input = ''

while user_input != 'q':
    user_input = input("\nq: \quit\n\
    1: add pokemon interaction\n\
    2: add pokemon\n\
    3: Pokemon data type\n\
    4: pokechart\n\
    s: Save\n>")
    game_client.action_on_input(user_input)

game_client.save()

    
