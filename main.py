from random import randint
from math import sqrt
print('Poszukujesz klucza na polu o wymiarach [x, y]')
print('Podaj wielkość pola do przeszukania: ')

while True:
    try:
        x_max = int(input('Podaj wartość maksymalną w poziomie [x]: '))
        break
    except ValueError:
        print('Podaj liczbę')

while True:
    try:
        y_max = int(input('Podaj wartość maksymalną w pionie [y]: '))
        break
    except ValueError:
        print('Podaj liczbę')

x = randint(0, x_max)
y = randint(0, y_max)

player_x = 0
player_y = 0

found = False

steps = 0

while not found:
    distance_0 = sqrt((x - player_x) ** 2 + (y - player_y) ** 2)
    steps += 1
    print()
    print('Możesz udać się w kierunkach [W - góra / A - lewo / S - dół / D - prawo] lub zakończyć grę [Q]: ')

    move = input('Dokąd idziesz? ')
    match move.lower():
        case 'w':
            player_y += 1
            if player_y > y_max:
                print('Wyszedłeś poza pole')
                player_y = y_max
        case 'a':
            player_x -= 1
            if player_x < 0:
                print('Wyszedłeś poza pole')
                player_x = 0
        case 's':
            player_y -= 1
            if player_y < 0:
                print('Wyszedłeś poza pole')
                player_y = 0
        case 'd':
            player_x += 1
            if player_x > x_max:
                print('Wyszedłeś poza pole')
                player_x = x_max
        case 'q':
            print('Koniec gry')
            quit()
        case _:
            print()
            print('Nie wiem dokąd chcesz pójść. Użyj właściwego klawisza.')
            continue

    distance = sqrt((x - player_x) ** 2 + (y - player_y) ** 2)

    if player_x == x and player_y == y:
        print(f'Brawo!!! Znalazłeś klucz na polu x = {player_x}, y = {player_y}, po {steps} ruchach.')
        quit()

    if distance > distance_0:
        print('Niestety oddalasz się od klucza')
    elif distance == distance_0:
        print('Spróbuj jeszcze raz')
    else:
        print('Jesteś coraz bliżej')


    print(f'Jesteś na polu x = {player_x}, y = {player_y}')
