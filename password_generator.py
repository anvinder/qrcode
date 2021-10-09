import random


class PasswordGenerator:
    def __init__(self):
        self.length_password = 48

    def generate_password(self):
        lower = 'abcdefghijklmnopqrstuvwxyz'
        upper = lower.upper()
        numbers = '1234567890'
        symbols = '!@#$%^&*()_+~[]{}:;,./<>'
        all_characters = lower + upper + numbers + symbols
        password = ''.join(random.sample(all_characters, self.length_password))
        print(password)


if __name__ == '__main__':
    object_PasswordGenerator = PasswordGenerator()
    object_PasswordGenerator.generate_password()
