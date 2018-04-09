import string

from ciphers import Cipher


class Atbash(Cipher):
    def __init__(self):
        """
        Define variables necessary for Atbash encryption
        
        You need a normal alphabet string and a reversed alphabet string
        """
        self.truechar = string.ascii_uppercase
        self.encryptedchar = string.ascii_uppercase[::-1]

    def encrypt(self, text):
        """
        Perform Atbash encryption on a string of characters
        
        The Atbash Cipher is ultimately just a transposition cipher, so
        encryption takes the index (0-25) of a character in the alphabet, then
        retrieves the character with the same index from a reversed
        alphabet string (also 0-25).
        
        Arg: string (a message)
        Returns: string (an encrypted message)
        """
        output = []
        text = text.upper()

        # Get the true alphabet index of every char in the message,
        # then append the char from the reversed alphabet string
        # with that same index.
        for char in text:
            if char.isalpha():
                index = self.truechar.index(char)
                output.append(self.encryptedchar[index])
            else:
                output.append(char)
        return ''.join(output)

    def decrypt(self, text):
        """
        Perform Atbash decryption on a string of characters
        
        The Atbash Cipher is ultimately just a transposition cipher, so
        encryption takes the index (0-25) of a character in a reversed
        alphabet string, then retrieves the character with the same index
        from a normal alphabet string (also 0-25).
        
        Arg: string (an encrypted message)
        Returns: string (a decrypted message)
        """
        output = []
        text = text.upper()

        # Get the reversed alphabet index of every char in the message,
        # then append the char from the true alphabet string
        # with that same index.
        for char in text:
            if char.isalpha():
                index = self.encryptedchar.index(char)
                output.append(self.truechar[index])
            else:
                output.append(char)
        return ''.join(output)


