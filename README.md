# Vigenére Encrypt Decrypt
Allows encryption of text based on a key string.

Moreover, this program allows for decryption of Vigenére-encrypted characters.
## How Does It Work?
### Encryption
1. Take a string to encrypt (TEXT), and a key to which the encryption will be based on (KEY).
2. Take the numerical counterparts of both TEXT and KEY.
3. Add their numerical counterparts according to these methods:
    - If TEXT is longer than KEY, naturally we will run add of KEY numbers to add to TEXT numbers.
    In such case, we go back from KEY's first number and from that number, we sequentially add the KEY numbers to the TEXT numbers again.
    Do this until all values of TEXT were added by KEY values.
    - If TEXT is shorter than KEY, add KEY numbers only until the last TEXT number.
4. If the number results larger than the length of the 'alphabet' dictionary, take the modulus of the result and the length of the dictionary.
5. Convert number set to string

### Decryption
1. Take a string to decrypt, and a key from which we will base our decryption
2. Take the numerical counterparts of both TEXT and KEY
3. Subtract their numerical counterparts the same method as encryption
    - If the difference results to a negative number, add length of dictionary
    - If the number is neither larger than dict length nor below 0, retain
    - If the number is larger than dict length, take modulus of result and dict length
4. Convert number set to string