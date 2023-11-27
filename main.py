from IPython.display import clear_output
import random

def display_board(board):
    
    clear_output()
    print('')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |') 
    print(' ')
def player_input():
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input ('Player 1: Voce deseja ser X ou O?').upper()

    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')

def choose_first():
    if random.randint(0,1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'
    
def space_check(board, position):
    try:
        return board[position] == ' '
    except:
        return False
    
def player_choice (board):
    position = 0
    while position  not in ('1 2 3 4 5 6 7 8 9').split(' ') or not space_check(board, int(position)):
        position = str(input('Escolha uma posição (1-9)'))
        print(position  not in ('1 2 3 4 5 6 7 8 9').split())
        print(('1 2 3 4 5 6 7 8 9').split())
        print(not space_check(board, int(position)))

    return int (position)

def place_marker (board, market, position):
    board[position] = market

def win_check (board, marker):
    return ((board[1]== marker and board[2]== marker and board[3] == marker) or
            (board[4]== marker and board[5]== marker and board[6] == marker) or 
            (board[7]== marker and board[8]== marker and board[9] == marker) or
            (board[1]== marker and board[4]== marker and board[7] == marker) or
            (board[2]== marker and board[5]== marker and board[8] == marker) or
            (board[3]== marker and board[6]== marker and board[9] == marker) or 
            (board[1]== marker and board[5]== marker and board[9] == marker) or 
            (board[3]== marker and board[5]== marker and board[7] == marker) 
            )

def full_board_check (board):
    for i in range (1,10):
        if space_check (board, i):
            return False
        
def replay():
    return str(input('Quer jogar novamente? "SIM" ou "NÃO"')).lower().startswith('s')

while True:
    #criando o tabuleiro
    board=[' ']*10
    #escolhendo os marcadores
    player1_marker, player2_marker = player_input()
    #escohendo quem comeca o jogo
    turn = choose_first()
    print(turn +' começa!')

    #define que o jogo comecou
    game_on = True

    while game_on:
        #Vez jogador 1
        if turn == 'Player 1':
            display_board(board)
            position= player_choice(board)
            place_marker(board,player1_marker, position)
            display_board(board)

            #Checa vitória
            if win_check(board, player1_marker):
                display_board(board)
                print('Parabéns! Jogador 1 venceu!')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('Empate!')
                    break
                else:
                    turn = 'Player 2'
        
        #Vez do jogador 2
        if turn == 'Player 2':
            display_board(board)
            position= player_choice(board)
            place_marker(board,player2_marker, position)
        #Checa vitória
            if win_check(board, player2_marker):
                display_board(board)
                print('Parabéns! Jogador 2 venceu!')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('Empate!')
                    break
                else:
                    turn = 'Player 1'



    if not replay():
        break
