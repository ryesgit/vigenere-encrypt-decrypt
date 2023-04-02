'''

Filename: vigenere_encrypt_decrypt.py

Allows encryption of text based on a key string.

Moreover, this program allows for decryption of Vigenére-encrypted characters.

Pseudocode:

Encryption

Take a string to encrypt (TEXT), and a key to which the encryption will be based on (KEY).
Take the numerical counterparts of both TEXT and KEY.
Add their numerical counterparts according to these methods:
    If TEXT is longer than KEY, naturally we will run add of KEY numbers to add to TEXT numbers. In such case, we go back from KEY's first number and from that number, we sequentially add the KEY numbers to the TEXT numbers again. Do this until all values of TEXT were added by KEY values.
    If TEXT is shorter than KEY, add KEY numbers only until the last TEXT number.
    If the number results larger than the length of the 'alphabet' dictionary, take the modulus of the result and the length of the dictionary.
Convert number set to string

Decryption
Take a string to decrypt, and a key from which we will base our decryption
Take the numerical counterparts of both TEXT and KEY
Subtract their numerical counterparts the same method as encryption
    If the difference results to a negative number, add length of dictionary
    If the number is neither larger than dict length nor below 0, retain
    If the number is larger than dict length, take modulus of result and dict length
Convert number set to string

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