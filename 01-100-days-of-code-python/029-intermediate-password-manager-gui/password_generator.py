import random

LETTERS = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
SYMBOLS = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]
NUMBERS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# 6 letter, 4 symbol, 4 number


class PasswordGenerator:
    def generate_password(self):
        password_list = self._letters_list()
        password_list += self._symbols_list()
        password_list += self._numbers_list()
        random.shuffle(password_list)
        return "".join(password_list)

    @staticmethod
    def _letters_list():
        return [random.choice(LETTERS) for _ in range(6)]

    @staticmethod
    def _symbols_list():
        return [random.choice(SYMBOLS) for _ in range(4)]

    @staticmethod
    def _numbers_list():
        return [random.choice(NUMBERS) for _ in range(4)]


if __name__ == "__main__":
    password = PasswordGenerator()
    print(password.generate_password())
