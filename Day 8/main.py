import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

still_working = "Y"
print(logo.logo)


def caesar(direction, text, shift):

    while shift >= len(alphabet):
        shift -= len(alphabet)

    def encrypt(text, shift):
        new_text = []

        for letter in text:
            if not(letter in alphabet):
                new_text.append(letter)
            else:
                index_letter = alphabet.index(letter.lower())+shift
                if index_letter < len(alphabet):
                    new_letter = alphabet[index_letter]
                    new_text.append(new_letter)
                else:
                    index_letter -= len(alphabet)
                    new_letter = alphabet[index_letter]
                    new_text.append(new_letter)

        print("".join(new_text))

    def decrypt(text, shift):
        new_text = []
        for letter in text:
            if not(letter in alphabet):
                new_text.append(letter)
            else:
                index_letter = alphabet.index(letter.lower())-shift
                if index_letter >= 0:
                    new_letter = alphabet[index_letter]
                    new_text.append(new_letter)
                else:
                    index_letter += len(alphabet)
                    new_letter = alphabet[index_letter]
                    new_text.append(new_letter)

        print("".join(new_text))

    if direction == "encode":
        encrypt(text, shift)

    elif direction == "decode":
        decrypt(text, shift)


while still_working == "Y":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction == "decode" or direction == "encode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(direction=direction, text=text, shift=shift)
    else:
        print("Invalid argument")
    still_working = input("Wanna try again? (Y/N) ").upper()
    if still_working != "Y" and still_working != "N":
        print("Invalid argument. Exit of program.")
