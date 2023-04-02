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