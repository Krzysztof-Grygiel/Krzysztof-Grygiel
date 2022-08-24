#korzystamy z PySide6
#licencja GPL od LGPL różni się tym, że w przypadku GPL trzeba udostępniać wraz z kodem źródłowym

import sys
from PySide6.QtWidgets import QWidget, QLabel, QApplication, QGridLayout, QLineEdit, QPushButton
# from PySide6.QtCore import
from PySide6.QtGui import QFont, QIcon
#QVBoxLayout - do wprowadzania label tekstowego



#tworzymy klasę, któa będzie przechowywała label i enter
class Translation():
    def __init__(self, to_translate, input_form, translated, correct):
        self.to_translate = to_translate
        self.input_form = input_form
        self.translated = translated
        self.correct = correct


# tworzymy widżet za pomoca klasy
class AppWidget(QWidget):
    def __init__(self, words):      #wywołanie init (nie korzystając z QWidget gdzie też jest init)
        super().__init__()        #linijka (super) żeby init z QWidget też został wykonany (dodajemy a nie nadpisujemy)
        self.words = words
        self.state = []   #przechowanie w liście
        self.layout = self.initial()    #korzystamy z metody initial
        self.setLayout(self.layout)               #AppWidget ustawiamy na tym layoucie

    def admit(self):    #akcja do uruchamiania po naciśnięciu przycisku "Sprawdź"
        print('Boom')

    def initial(self):                      #funkcja (metoda) do inicjalizacji layoutu
        row = 0     #wiersz dodawanych elementów (do pętli for)
        grid = QGridLayout()      #w jakich komórkach (grid dzieli pole okna na części- w pionie i poziomie)

        for key, correct in self.words.items():
            to_translate = QLabel(key)  # tworzymy komponent etykiety (label) ze słówkami z words (może byc z tekstem)
            to_translate.setFont(QFont('SansSerif', 15))  # ustawiamy wielkość label (font)
            input_form = QLineEdit()     #komponent wprowadzania tekstu
# tworzymy rozmieszczenie etykiet (label) i pól (enter), może być także(4 kolumny):(0,0)(0,1)(0,2)(0,3)
            self.state.append(Translation(to_translate, input_form, '', correct))
            grid.addWidget(to_translate, row, 0)
            grid.addWidget(input_form, row, 1)
            row += 1
#dodajemy przycisk do sprawdzania odpowiedzi (umiejscawiamy go)
        submit = QPushButton('Sprawdź')
        submit.clicked.connect(self.admit)   #metoda przypisana do przycisku (uchwyt do metody)
        grid.addWidget(submit, row, 1)

        return grid


if __name__ == '__main__':
    #tworzymy słownik słówek do tłumaczenia
    words = {
        'dog': 'pies',
        'cat': 'kot',
        'snake': 'wąż',
        'cow': 'krowa'
    }

    app = QApplication([])
    app.setApplicationDisplayName('Nauka słówek')     #zmieniamy nazwę okienka (z python na "Nauka słówek")
    app.setWindowIcon(QIcon('kg.ico'))     #wstawiamy ikonkę do okienka
    appWidget = AppWidget(words)     #tworzymy widżet appWidget i dodajemy do main (przenosimy do niego słownik)
    appWidget.resize(800, 600)               #skalujemy (wymiarujemy) appWidget
    appWidget.show()                        #pokazujemy appWidget
    sys.exit(app.exec())
