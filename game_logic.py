import random
from decouple import config


def logic():
    money = config('MY_MONEY', cast=int)
    balance = money
    while True:
        number = int(input('Choose a number from 1 to 30: \n'))

        try:
            if number not in range(1, 31):
                print('Enter only a number from 1 to 30')
                continue
        except ValueError:
            print('Enter only integer number')
            continue

        bet = int(input('Choose a bet: \n'))
        try:
            if bet > balance:
                print(f'Bet is greater than available balance: {balance}!')
                continue
        except ValueError:
            print('Enter only integer number')
            continue

        slot = random.randint(1, 31)
        if slot == number:
            cash = bet * 2
            balance += cash
        else:
            balance -= bet
        play_again = input("\nPlay again? Yes - enter Y / No - enter N: ")
        if play_again == 'Y':
            continue
        if play_again == 'N':
            print(f'Balance: {balance}')
            break


if __name__ == "__main__":
    logic()
