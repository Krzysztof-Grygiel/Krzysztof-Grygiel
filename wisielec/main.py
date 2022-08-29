import sys

nr_tries = 5
word ="kammilka"
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
            sys.exit(0)

    else:
        for index in found_indexes:
            user_word[index] = letter

        if "".join(user_word) == word:
            print("Brawo. To jest to słowo")
            sys.exit(0)

    show_state_of_game()