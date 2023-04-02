'''

Filename: vigenere_encrypt_decrypt.py

Allows encryption of text based on a key string.

Moreover, this program allows for decryption of Vigenére-encrypted characters.

'''

# Create dictionary for conversion from text to num and num to text

TEXT_KEYS = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 
               'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 
               'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 
               'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 
               'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}

NUM_KEYS = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 
               6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 
               11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 
               16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 
               21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}

def encrypt(text, key):
    resultant_num = []

    text.lower()
    key.lower()
    # Take the numerical counterparts of both TEXT and KEY.
    
    numberified_text = convert_to_num(text)
    numberified_keys = convert_to_num(key)

    key_len = len(numberified_keys)
    for (text_index, text_num) in enumerate(numberified_text):
        # If string is not a number, retain
        if not str(text_num).isdigit():
            resultant_num.append(text_num)
        # If text length is longer than key length, always go back to key length[0] every time we run out of key digits
        elif (text_index + 1 > key_len):
            offset = text_index % key_len
            resultant_num.append(text_num + numberified_keys[offset])
        # Key indices within key length can be used as is
        else:
            resultant_num.append(text_num + numberified_keys[text_index])

    # Convert result number to text
    encrypted_word = convert_to_text(resultant_num)

    return encrypted_word.upper()

def decrypt(text, key):
    resultant_num = []

    text.lower()
    key.lower()
    # Take the numerical counterparts of both TEXT and KEY.

    numberified_text = convert_to_num(text)
    numberified_key = convert_to_num(key)

    for (index, num) in enumerate(numberified_text):
        # Retain spaces
        if (str(num).isspace()):
            resultant_num.append(' ')
        
        # If text length > key length, always go back to key length[0]
        elif(index + 1 > len(numberified_key)):
            offset = index % len(numberified_key)
            difference = (num - numberified_key[offset]) + 26
            resultant_num.append(difference)
        
        # If key length > text length, execute only until text is traversed
        else:
            difference = (num - numberified_key[index]) + 26
            resultant_num.append(difference)
    decrypted_word = convert_to_text(resultant_num)    

    return decrypted_word.upper()

# Helper functions

# Text to number converter
def convert_to_num(text):
    text_to_num = []

    for letter in text.lower():

        if letter.isalpha():
            text_to_num.append(TEXT_KEYS[letter])

        else:
            text_to_num.append(letter)

    return text_to_num

# Number to text converter
def convert_to_text(resultant_num):
    completed_word = ''

    for num in resultant_num:
        # If character is not a string, retain
        if (not str(num).isdigit()):
            completed_word += num

        elif(num > 25):
            completed_word += NUM_KEYS[(num % 26)]

        else:
            completed_word += NUM_KEYS[num]

    return completed_word