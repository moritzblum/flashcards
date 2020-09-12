import csv

class CardManager():
    def __init__(self):
        self.cards = []
        try:
            with open('flashcards.csv') as rf:
                spamreader = csv.reader(rf)
                for row in spamreader:
                    self.cards.append(row)
        except FileNotFoundError:
            print('No file found!')


    def create_card(self, front, back):
        self.cards.append([front, back])
        with open('flashcards.csv', 'a') as af:
            af.write(front.replace('\n', '') + ',' + back.replace('\n', '') + '\n')


