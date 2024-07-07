# Example Input     Example Output
# text = hello      The encoded text is mjqqt
# shift = 5
#
# Example Input     Example Output
# text = zulu       The encoded text is ezqz
# shift = 5

from alphabet import alphabet
from art import logo

print(logo)


def user_text_input():
    input_text = input("Type your message: ").lower()
    return input_text


def encrypt(plain_text, shift_amount):
    cipher_text = ""

    for letter in plain_text:
        if letter == " ":
            cipher_text += " "
        elif letter in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            cipher_text += letter
        else:
            position = alphabet.index(letter) + shift_amount
            if position > len(alphabet) - 1:
                position = position % len(alphabet)
            cipher_text += alphabet[position]

    print(f"\nThe encoded text is {cipher_text}\n")


def decrypt(cipher_text, shift_amount):
    plain_text = ""
    alphabet_lenth = len(alphabet)

    for letter in cipher_text:
        if letter == " ":
            plain_text += " "
        elif letter in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            plain_text += letter
        else:
            position = alphabet.index(letter) - shift_amount
            if position < 0:
                position = alphabet_lenth - ((position * -1) % alphabet_lenth)
            plain_text += alphabet[position]

    print(f"\nThe decoded text is {plain_text}\n")


def do_again():
    is_end = ""
    while is_end not in ["yes", "no"]:
        is_end = input("Type 'yes' if you want to go again or 'no' to exit: ").lower()
    return is_end


def caesar_cipher():
    again = ""
    while again != "no":
        direction = ""
        while direction not in ["encode", "decode"]:
            direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt: ")

        text = user_text_input()

        shift = int(input("Type the shift number: "))

        if direction == "encode":
            encrypt(text, shift)
        elif direction == "decode":
            decrypt(text, shift)

        again = do_again()


caesar_cipher()
