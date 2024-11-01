morse_code_dict = {"A": ".-",
                   "B": "-...",
                   "C": "-.-.",
                   'D': '-..',
                   'E': '.',
                   'F': '..-.',
                   'G': '--.',
                   'H': '....',
                   'I': '..',
                   'J': '.---',
                   'K': '-.-',
                   'L': '.-..',
                   'M': '--',
                   'N': '-.',
                   'O': '---',
                   'P': '.--.',
                   'Q': '--.-',
                   'R': '.-.',
                   'S': '...',
                   'T': '-',
                   'U': '..-',
                   'V': '...-',
                   'W': '.--',
                   'X': '-..-',
                   'Y': '-.--',
                   'Z': '--..',
                   '0': '-----',
                   '1': '.----',
                   '2': '..---',
                   '3': '...--',
                   '4': '....-',
                   '5': '.....',
                   '6': '-....',
                   '7': '--...',
                   '8': '---..',
                   '9': '----.',
                   }

morse_code_on = True


def morse_code():
    encoded_message = ""
    decoded_message = ""
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    if direction == 'encode':
        message = input("Place secret message here: ").upper()
        for letter in message:
            for (key, value) in morse_code_dict.items():
                if letter == key:
                    encoded_message = f'{encoded_message} {value}'
        return encoded_message
    elif direction == 'decode':
        coded_text = input('Place encoded message here: ').split()
        for encrypted_letter in coded_text:
            for (key, value) in morse_code_dict.items():
                if encrypted_letter == value:
                    decoded_message = f'{decoded_message}{key}'
        return decoded_message


while morse_code_on:
    user_answer = input("Type 'yes' to use Morse Code Generator, else type 'no': ").lower()
    if user_answer == 'no':
        morse_code_on = False
        print('Bye!')
    elif user_answer == 'yes':
        en_message = morse_code()
        print(en_message)
        dec_message = morse_code().lower()
        print(dec_message)
    else:
        print('Invalid option')
