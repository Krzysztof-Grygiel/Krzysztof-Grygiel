# python main.py --add "Wstaw ziemniaki"
# python main.py --list
# python main.py --toggle 1

import sqlite3
from argparse import ArgumentParser

parser = ArgumentParser(description='Mała aplikacja TODO')
parser.add_argument('--install', help='Instalacja! Uwaga, wyczyści bazę danych', action='store_true')
parser.add_argument('--add', help='Dodaj nowe zadanie')
parser.add_argument('--list', help='Wypisz tematy do zrobienia', action='store_true')
parser.add_argument('--toggle', help='Zmień status zadania')
args = parser.parse_args()

connection = sqlite3.connect('todo.db')
cursor = connection.cursor()

if args.install:
    print('Instalujemy program')
    cursor.execute('drop table todos')
    cursor.execute('Create table todos(id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, is_done BOOLEAN)')
    connection.commit()

if args.add is not None:
    print('Dodajemy...')
    title = args.add
    cursor.execute('insert into todos(title, is_done) values(?, false)', (title,))
    connection.commit()

if args.toggle is not None:
    print('Przełączamy...')
    query = cursor.execute('select is_done from todos where id=?', (args.toggle,))
    is_done = query.fetchone()
    if is_done is None:
        print('Nie mam takiego zadania')
        quit()
    elif is_done[0] == 1:
        print(f'Zamieniam status zadania {args.toggle} na niezrobione')
        new_is_done = 0
    elif is_done[0] == 0:
        print(f'Zamieniam status zadania {args.toggle} na zrobione')
        new_is_done = 1

    cursor.execute('update todos set is_done=? where id=?', (new_is_done, args.toggle))
    connection.commit()

if args.list:
    print('Lista spraw do zrobienia:')
    for todo_id, title, is_done in cursor.execute('select id, title, is_done from todos'):
        print(f'{todo_id} \t {title} \t {"[v]" if is_done else "[ ]"}')
