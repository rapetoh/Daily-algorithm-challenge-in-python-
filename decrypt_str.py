# x = chr(ord('A'))
# print(x)
import re

def format_control(crypted_message):
    controller = re.compile(r'^([a-z]\d+)+$', re.IGNORECASE)
    return controller.match(crypted_message)

def decrypt_message(crypted_message):
    decrypted_message = ""
    if format_control(crypted_message):
        for letter_index in range(0, len(crypted_message)-1, 2):
            current_letter = crypted_message[letter_index]
            next_digit = int(crypted_message[letter_index + 1])
            decrypted_message += chr(ord(current_letter) + next_digit)

    return decrypted_message

# Appel de la fonction et affichage du résultat
resultat = decrypt_message('a3b2c4d1')
print(resultat)
