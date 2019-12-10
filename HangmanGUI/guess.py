class Guess:
    def __init__(self, word):
        self.numTries = 0
        self.guessedChars = []
        self.secretWord = word
        self.currentStatus = "_" * len(self.secretWord)

    def displayCurrent(self):
        result = ""
        for i in range(len(self.currentStatus)):
            result += self.currentStatus[i]
            if i == len(self.currentStatus) - 1:
                break
            result += " "
        return result
        # print(self.secretWord)

    def displayGuessed(self):
        result = ""
        for char in self.guessedChars:
            result += char + " "
        return result

    def guess(self, character):
        self.guessedChars.append(character)

        if character not in self.secretWord:
            self.numTries += 1
            return False

        for i in range(len(self.secretWord)):
            if character == self.secretWord[i]:
                self.currentStatus = self.currentStatus[:i] + character + self.currentStatus[i+1:]

        return True

    def finished(self):
        return "_" not in self.currentStatus