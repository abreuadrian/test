import random

class Generetor:
    """
    A class used to generate random passwords.

    Methods
    -------
    password_gen(lenght_capital=2, lenght_tiny=3, lenght_num=4, length_esp=1)
        Generates a random password with the specified number of capital letters, tiny letters, numbers, and special characters.
    """

    @staticmethod
    def password_gen (lenght_capital=2, lenght_tiny=3, lenght_num=4, length_esp=1):
        """
        Generates a random password with the specified number of capital letters, tiny letters, numbers, and special characters.

        Parameters:
        lenght_capital : int, optional
            The number of capital letters in the password (default is 2)
        lenght_tiny : int, optional
            The number of tiny letters in the password (default is 3)
        lenght_num : int, optional
            The number of numbers in the password (default is 4)
        length_esp : int, optional
            The number of special characters in the password (default is 1)

        Returns a randomly generated password
        """

        capital_characteres = 'ABCDEFGHIJKLMNOPQRSTUVXWYZ'
        tiny_characteres = 'abcdefghijklmnopqrstuvxwyz'
        num_characteres = '1234567890'
        esp_characteres = '!@#$%¨;:<>*][}{?'

        password = (
            [random.choice(capital_characteres) for _ in range (lenght_capital)] +
            [random.choice(tiny_characteres) for _ in range(lenght_tiny)] +
            [random.choice(num_characteres) for _ in range (lenght_num)] +
            [random.choice(esp_characteres) for _ in range (length_esp)])
        
        random.shuffle(password)
        password_shuflled =''.join(password)
        return password_shuflled


res = Generetor.password_gen()
print(res)
