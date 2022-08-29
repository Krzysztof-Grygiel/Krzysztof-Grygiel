import sys
import random

words5 = ('szafa', 'galon')
words6 = ('miasto', 'kelner', 'beczka', 'papier')
words7 = ('bandyta', 'zegarek', 'telefon', 'okulary', 'kominek')
words8 = ('szlachta', 'świeczka')

while True:
    try:
        difficulty = int(input('Ile liter ma mieć słowo <5, 6, 7 czy 8>? Wpisz cyfrę: '))

        match int(difficulty):
            case 5:
                word = random.choice(words5)
                nr_tries = 4
            case 6:
                word = random.choice(words6)
                nr_tries = 5
            case 7:
                word = random.choice(words7)
                nr_tries = 6
            case 8:
                word = random.choice(words6)
                nr_tries = 7
            case _:
                print()
                print('Wpisz cyfrę 5 lub 6 lub 7 lub 8!!!')
                continue
        break

# można także zamiast funkcji match skorzystać z poniższego kodu
        # if difficulty == 5:
        #     word = random.choice(words5)
        #     nr_tries = 3
        # elif difficulty == 6:
        #     word = random.choice(words6)
        #     nr_tries = 4
        # elif difficulty == 7:
        #     word = random.choice(words6)
        #     nr_tries = 5
        # elif difficulty == 8:
        #     word = random.choice(words6)
        #     nr_tries = 6
        # break

    except (ValueError, NameError):
        print('Wpisz cyfrę 5 lub 6 lub 7 lub 8!!!')

print(f'Możesz popełnić {nr_tries} błędów')

used_letters = []

user_word = []

def find_indexes(word, letter):
    indexes = []

    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)

    return indexes

def show_state_of_game():
    print()
    print(user_word)
    print("Pozostało prób:", nr_tries)
    print("Użyte litery:", used_letters)
    print()

def end_game():
    print('Czy chcesz zagrać jeszcze raz? (tak lub nie)')
    if not input('> ').lower().startswith('t'):
        sys.exit(0)

for _ in word:              #zmiennej _ nie wykorzystujemy w kodzie dalej
    user_word.append("_")

while True:
    letter = input("Podaj literę: ")
    used_letters.append(letter)

    found_indexes = find_indexes(word, letter)

    if len(found_indexes) == 0:
        print("Nie ma takiej litery")
        nr_tries -= 1

        if nr_tries == 0:
            print("Koniec gry :(")
            end_game()

    else:
        for index in found_indexes:
            user_word[index] = letter

        if "".join(user_word) == word:
            print("Brawo. To jest to słowo")
            end_game()

    show_state_of_game()