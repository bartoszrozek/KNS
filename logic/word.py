import random
import copy


class word:

    def __init__(self, alphabet_length, endPoint):
        alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"]

        self.letters = []
        self.length = 0
        self.alphabet = alphabet[0:alphabet_length]
        self.endPoint = endPoint

    def show(self):
        print(("".join(["{" + str(i) + ":^5}" for i in range(self.length)])).format(*self.letters))
        print(
            ("".join(["{" + str(i) + ":<5}" for i in range(self.length + 1)])).format(*list(range(0, self.length + 1))))

    def add_letter(self, letter, place):
        try:
            if (letter not in self.alphabet):
                raise ValueError('Letter is not from alphabet')
            self.letters.insert(place, letter)
            self.length += 1
        except ValueError as err:
            print(err)

    def check_repetition(self):
        for i in range(self.length - 1):
            for j in range(min(i + 1, self.length - i - 1)):
                if (self.letters[i - j:i + 1] == self.letters[i + 1:i + j + 2]):
                    return [True, i, j]
        return [False]

    def computer_move(self, place):
        letters = list(self.alphabet)
        random.shuffle(letters)
        for letter in letters:
            temp = copy.deepcopy(self)
            temp.add_letter(letter, place)
            if (not temp.check_repetition()[0]):
                self.letters = temp.letters
                self.length = temp.length
                return
        self.letters = temp.letters
        self.length = temp.length

    def loosing_position(self, place):
        letters = list(self.alphabet)
        random.shuffle(letters)
        for letter in letters:
            temp = copy.deepcopy(self)
            temp.add_letter(letter, place)
            if not temp.check_repetition()[0]:
                return False
        return True

    def ext_computer_move(self, place):
        letters = list(self.alphabet)
        random.shuffle(letters)
        for letter in letters:
            temp = copy.deepcopy(self)
            temp.add_letter(letter, place)
            if (not temp.check_repetition()[0]):
                computer_is_loosing = False
                for human_choice in range(temp.length + 1):
                    if temp.loosing_position(human_choice):
                        computer_is_loosing = True
                        break
                if not computer_is_loosing:
                    self.letters = temp.letters
                    self.length = temp.length
                    return
        self.letters = temp.letters
        self.length = temp.length
