import random
import sys


def bot_move_generator():
    moves = ['Rock','Paper','Scissors']
    return random.choice(moves)



def win_check(player_move,bot_move):
    #if it's a tie the function returns 0
    if player_move==bot_move:
        return 0

    #The rest of the situations are being checked
    #If the player wins the function returns 1
    #If the bot wins the function returns 2
    if player_move=='Rock':
        if bot_move=='Paper':
            return 2
        else:
            return 1
    elif player_move=='Paper':
        if bot_move=='Rock':
            return 1
        else:
            return 2
    elif player_move=='Scissors':
        if bot_move=='Rock':
            return 2
        else:
            return 1


def ask_to_play():
    print('1.Play')
    print('2.Quit\n')
    print('Please enter the number left to your preferable option ')

    while True:
        game_option = input().strip()
        if not game_option:
            print('Empty input. Please try again ')
        elif game_option not in ['1', '2']:
            print('Invalid input. Please try again ')
        elif game_option == '1':
            return True
        else:
            return False

print('Rock Paper Scissors \n')

if not ask_to_play():
    sys.exit()



valid_moves = {
    'r': 'Rock',
    'p': 'Paper',
    's': 'Scissors'
}


#Initializing wins for the score
player_wins=0
bot_wins=0


while True:
    #Input validation
    while True:
        move = input('Enter R for Rock, P for Paper or S for Scissors ').strip().lower()
        player_move = valid_moves.get(move)

        if not player_move:
            print('\nInvalid input.Try again ')
        else:
            print('\nYour move: ' + player_move)
            break


    bot_move = bot_move_generator()
    print('Bot\'s move: ' + bot_move)

    result=win_check(player_move,bot_move)
    if result==1:
        print('\nYou win')
        player_wins += 1
        print(f'The score is {player_wins}:{bot_wins}\n')
    elif result==2:
        print('\nBot wins')
        bot_wins += 1
        print(f'The score is {player_wins}:{bot_wins}\n')
    else:
        print('\nTie\n')
        continue


    if not ask_to_play():
        sys.exit()


