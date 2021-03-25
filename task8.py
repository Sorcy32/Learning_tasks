"""Написать функцию XOR_cipher, принимающая 2 аргумента: строку, которую нужно зашифровать, и ключ шифрования,
которая возвращает строку, зашифрованную путем применения функции XOR (^) над символами строки с ключом. Написать
также функцию XOR_uncipher, которая по зашифрованной строке и ключу восстанавливает исходную строку. """


def XOR_cipher(message, key):
    ord_message = ""
    ord_key = ""
    crypted_message = ''
    for x in message:
        ord_message = ord_message + str(ord(x)) + " "
    for x in key:
        ord_key = ord_key + str(ord(x))
    for x in ord_message.split():
        crypted_message = crypted_message + str(int(x) ^ int(ord_key)) + " "
    return crypted_message


def XOR_uncipher(message, key):
    ord_key = ""
    ord_message = ''
    decrypted = ''
    for x in key:
        ord_key = ord_key + str(ord(x))
    for x in message.split():
        ord_message = ord_message + str(int(x) ^ int(ord_key)) + ' '
    for x in ord_message.split():
        decrypted = decrypted + (chr(int(x)))
    return decrypted
