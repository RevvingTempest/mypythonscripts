# Project #2 - Rock Paper Scissors Game
# Student: Rene Tejon
# Student ID: rt891
# Course CRN and Section: 31344 - L01
# Course: MSIT 501 - Foundations of Programming, Data Structures, and Algorithms
# Professor: Dr. Frank J Mitropoulos Ph.D.
# Due Date: February 6, 2022

import random
import sys
from time import sleep


def main():

    moves = ['r', 'p', 's']
    legend = {'r': 'Rock', 'p': 'Paper', 's': 'Scissor'}
    win = [['r', 's'], ['s', 'p'], ['p', 'r']]
    lose = [[y, x] for x, y in win]
    player = []
    computer = []
    choices = []
    results = []
    chant = 'Rock Paper Scissor SHOOT!'
    allowed_num_of_games = list(range(3, 12, 2))
    num_of_games = 0
    game_speed = 0.5

    # A simple game banner
    print('\n' + '*' * 47)
    print('* Welcome to the game of Rock-Paper-Scissors! *')
    print('*' * 47)

    # Player will select how many game sets to play based on allowed range
    while num_of_games not in allowed_num_of_games:
        try:
            num_of_games = eval(input('\nPlease select an odd number of games to play from 3-11: '))
            if num_of_games in allowed_num_of_games:
                continue
            else:
                print(f'{num_of_games} is not a valid input.')
        except (ValueError, NameError, SyntaxError, ZeroDivisionError):
            print('That is not a valid input.')

    # This is the main game loop
    for i in range(num_of_games):
        # Banner for current game set in play
        game_num = i + 1
        print("\nGame", game_num)
        print('-' * 7)

        # Player selects their move
        player_choice = input('Select (R)ock, (P)aper, or (S)cissor: ').lower()

        # If the first move by player is an invalid input, this loop will run until a valid input is made
        while player_choice not in moves:
            player_choice = input('\nInvalid Input. Please select (R)ock, (P)aper, or (S)cissor: ').lower()

        # The computer list will append a random move from the moves list
        # The player's chosen move will get added to the player list
        # Both moves are added to the choices list
        computer.append(random.choice(moves))
        player.append(player_choice)
        choices.insert(i, [player[i], computer[i]])

        # The game chant for entertainment purposes
        for w in chant.split():
            print(w, end=' ', flush=True)
            sleep(game_speed)

        # The players' choices from the choices list are calculated to determine a winner
        # The results of the winner are appended to the results list
        if choices[i] in win:
            print('\nComputer chose:', computer[i], '\nPlayer wins!')
            results.append([str(game_num), legend[player[i]], legend[computer[i]], 'Player'])

        elif choices[i] in lose:
            print('\nComputer chose:', computer[i], '\nComputer wins!')
            results.append([str(game_num), legend[player[i]], legend[computer[i]], 'Computer'])

        else:
            print('\nComputer chose:', computer[i], '\nDraw!')
            results.append([str(game_num), legend[player[i]], legend[computer[i]], 'Draw'])

        # Controls the pace of the game. Can be changed in the variable declaration.
        # A lower number speeds up the game
        sleep(game_speed)

    # The game results banner
    print('\n' + '-' * 55)
    print('Game\t\tPlayer\t\tComputer\tWinner')
    print('-' * 55)

    # This part shows the results of each game and counts up the wins, loss, draws
    # to display it numerically as well
    for i, j, k, l in results:
        print(f'Game {i}\t\t{j}\t\t{k}\t\t{l}')

    print('\nPlayer Wins:', sum(i.count('Player') for i in results))
    print('Computer Wins:', sum(i.count('Computer') for i in results))
    print('Draws:', sum(i.count('Draw') for i in results))

    # This will give the player the option to replay the game or quit
    replay = input('\nPlay again? Select \'y\' for YES and \'n\' for NO. Then press Enter. ').lower()

    # This loop ensures that the player inputs a 'y' or 'n'
    while True:
        if replay == 'y':
            main()
        elif replay == 'n':
            quit()
        else:
            replay = input('\nInvalid Input. Please select \'y\' for YES and \'n\' for NO. Then press Enter. ').lower()


if __name__ == '__main__':
    main()
