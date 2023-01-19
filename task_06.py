def rps_game_winner(Players):
    size = len(Players)
    if size > 2:
        print('WrongNumberOfPlayersError')
        return
    if is_exists_strategy_player(Players[0][1]) == False or is_exists_strategy_player(Players[1][1]) == False:
        print('NoSuchStrategyError')
        return
    if win_first_player(Players) == True:
        print(Players[0][0]+ ' '+Players[0][1])
    else:
        print(Players[1][0]+ ' '+Players[1][1])
#Функция проверки на существования стратегии        
def is_exists_strategy_player(St):
    if St == 'R' or St == 'P' or St == 'S':
        return True
    else:
        return False
#Функция для определения победителя
def win_first_player(Players):
    if Players[0][1] == Players[1][1]:
        return True
    if Players[0][1] == 'P' and Players[1][1] == 'R':
        return True
    elif Players[0][1] == 'R' and Players[1][1] == 'S':
        return True
    elif Players[0][1] == 'S' and Players[1][1] == 'P':
        return True
    else:
        return False
