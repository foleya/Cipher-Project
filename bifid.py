import string

from ciphers import Cipher


class Bifid(Cipher):
    def __init__(self):
        """
        Define variables necessary for Bifid encryption
        
        Bifid encryption utilizes a polybius square, which is basically a
        5x5 grid of letters from the alphabet. Since there are only 25
        spaces in such a grid, the character 'J' is removed (and is replaced
        with 'I' for encryption/decryption puproses).
        
        After creating a dictionary matching characters to their
        coordinates in the polybius square, I create a reverse dictionary
        that matches coordinates to their characters to enable easy
        translation between letters and their coordinates.
        """
        self.coordinates = [(x, y) for x in range(1, 6) for y in range(1, 6)]
        self.alphabet = [
            char for char in string.ascii_uppercase if char != 'J'
        ]
        self.polybius = {
            char: coord for char, coord in zip(self.alphabet, self.coordinates)
        }
        self.rpolybius = {
            coord: char for coord, char in zip(self.coordinates, self.alphabet)
        }

    def encrypt(self, text):
        """
        Perform Bifid encryption on a string of characters
        
        The Bifid cypher has 5 steps. First, every character in the message
        is translated into a set of coordinates (x, y) using a polybius square.
        Second, all the x coordinates are put into a list, and all of the y
        coordinates are put into a list. Third, the lists of x coordinates and
        y coordinates are added togehter (x-list + y-list). Fourth, every pair
        of letters from the new list are used to create new coordinates. Fifth,
        and finally, those new coordinates are used to reference letters in
        the polybius square and create an encrypted message.
        
        Arg: string (a message)
        Returns: string (an encrypted message)
        """
        output = []
        xlist = []
        ylist = []
        text = text.upper().replace('J', 'I')

        # Create lists of the x, and y coordinates for each character
        # in the message.
        for char in text:
            if char.isalpha():
                xlist.append(self.polybius[char][0])
                ylist.append(self.polybius[char][1])

        # Add the x and y coordinate lists together to form a new list.
        linear = xlist + ylist

        # Use zip to create new coordinate pairings, by every two numbers.
        linear_pairs = list(zip(linear[::2], linear[1::2]))

        # Use the new coordinates to retrieve encrypted characters.
        for coord in linear_pairs:
            output.append(self.rpolybius[coord])
        return ''.join(output)

    def decrypt(self, text):
        """
        Perform Bifid decryption on a string of characters
        
        Essentially performs the steps of Bifid encryption in reverse.
        
        Arg: string (an encrypted message)
        Returns: string (a decrypted message)
        """
        output = []
        linear = []
        text = text.upper().replace('J', 'I')

        # Create a list of the x, and y coordinates for each character
        # in the message.
        for char in text:
            if char.isalpha():
                linear.append(self.polybius[char][0])
                linear.append(self.polybius[char][1])

        # Use floor division to split that list in half, thus recovering
        # the original x-list + y-lists
        xlist = linear[:len(linear)//2]
        ylist = linear[len(linear)//2:]

        # Zip the x-list and y-list to recover the true coordinate pairs.
        decrypt_coord = list(zip(xlist, ylist))

        # Use the true coordinates to retrieve the decrypted characters.
        for coord in decrypt_coord:
            output.append(self.rpolybius[coord])
        return ''.join(output)


