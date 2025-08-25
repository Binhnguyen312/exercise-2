import random

your_money = 100
pay_each_game = 5
wins = 0
losses = 0
while True:
    print(f'Your money is $ {your_money}.')
    print(f'Your pay each game is $ {pay_each_game}.')
    if your_money < pay_each_game:
        print('---------------------')
        print('Game over.You are running out of money.')
        print('----------------------')
        break
    your_money -= pay_each_game
    comp_number = random.randint(1, 100)
    your_num = int(input('Enter guessing number (1-100):'))
    if comp_number == your_num:
        print('Correct!')
        your_money += pay_each_game * 4
        wins += 1
    else:
        print(f'the computer number is {comp_number}')
        if your_num > comp_number:
                print('too high!')
                losses += 1
        if your_num < comp_number:
                print('too low!')
                losses += 1
    print(f'Wins: {wins}\nLosses: {losses},\nMoney left: {your_money}')
    print('-----------------------------')






