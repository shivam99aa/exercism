# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman:
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.word = word
        self.guessed_char_list = []
        self.masked_word = ['_' for i in word]

    def guess(self, char):
        if self.status != STATUS_ONGOING:
            raise ValueError(char)

        if char in self.word and char not in self.guessed_char_list:
            self.guessed_char_list.append(char)
            if set(self.word) == set(self.guessed_char_list):
                self.status = STATUS_WIN
        elif char in self.guessed_char_list or char not in self.word:
            self.remaining_guesses -= 1

        if self.remaining_guesses < 0:
            self.status = STATUS_LOSE

    def get_masked_word(self):
        for i in range(len(self.word)):
            if self.word[i] in self.guessed_char_list:
                self.masked_word[i] = self.word[i]
        return ''.join(self.masked_word)

    def get_status(self):
        return self.status
