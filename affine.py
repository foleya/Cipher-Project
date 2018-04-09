import string

from ciphers import Cipher


class Affine(Cipher):
    def __init__(self, alpha=5, beta=8):
        """
        Define variables necessary for Affine encryption/decryption.
        
        Args: int, int (the alpha/beta in the formuala...5 and 8 by default)
        """
        self.alpha = alpha
        self.beta = beta

        # Create a true alphabet string
        self.true_alphabet = string.ascii_uppercase

        # Create transposed alphabet string using affine formula:
        # Where Cipher Value = (alpha * True Value + beta) % 26 for each letter
        # Values, correspond with a characters index in a string.
        self.encrypted_alphabet = (
            ''.join([chr(((alpha*i + beta) % 26) + 65) for i in range(26)])
        )

    def encrypt(self, text):
        """
        Perform Affine encryption on a string of characters
        
        The Affine Cipher is ultimately just a transposition cipher, so
        encryption takes the index (0-25) of a character in the alphabet, then
        retrieves the character with the same index from an encrypted
        (or transposed) string (also 0-25). Transposition of letters in the
        encrypted string is based on the Affine Formula: (a*i + b) % 26
        
        Arg: string (a message)
        Returns: string (an encrypted message)
        """
        output = []
        text = text.upper()

        # For every char in message, get its true alphabet index, then
        # append the char with that index from the encrypted alphabet string.
        for char in text:
            if char.isalpha():
                index = self.true_alphabet.index(char)
                output.append(self.encrypted_alphabet[index])
            else:
                output.append(char)
        return ''.join(output)

    def decrypt(self, text):
        """
        Perform Affine decryption on a string of characters
        
        The Affine Cipher is ultimately just a transposition cipher, so
        decryption takes the index (0-25) of a character in a transposed
        string (0-25), then retrieves the character with the same index
        in a normal alphabet string (0-25). Transposition of letters in the
        encrypted string is based on the Affine Formula: (a*i + b) % 26
        
        Arg: string (an encrypted message)
        Returns: string (a decrypted message)
        """
        output = []
        text = text.upper()

        # For every char in message, get its encrypted alphabet index, then
        # append the char with that index from the true alphabet string.
        for char in text:
            if char.isalpha():
                index = self.encrypted_alphabet.index(char)
                output.append(self.true_alphabet[index])
            else:
                output.append(char)
        return ''.join(output)


