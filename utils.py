from csv import DictReader
from random import sample

usuarios = []

with open('usuarios.csv', 'r') as arquivo:
    leitor = DictReader(arquivo)
    next(leitor)
    for linha in leitor:
        usuarios.append(linha)


class Authentication():

    def __init__(self: object, username: str, password: str) -> None:
        self.__password = password
        self.__username = username

    def lenght(self: object) -> bool:
        if len(self.__password) >= 8:
            return True

    def lower(self: object) -> bool:
        lower = any(char.islower() for char in self.__password)
        return lower

    def upper(self: object) -> bool:
        upper = any(char.isupper() for char in self.__password)
        return upper

    def digit(self: object) -> bool:
        digit = any(char.isdigit() for char in self.__password)
        return digit

    def validate(self: object) -> bool:
        validate = all([self.lenght(), self.lower(),
                       self.upper(), self.digit()])
        return validate

    def exist(self: object) -> bool:
        achei = False
        for user in usuarios:
            if self.__username == user['username']:
                achei = True
                break
        return achei

    def login_authentication(self: object) -> bool:
        achei = False
        for user in usuarios:
            if self.__username == user['username'] and self.__password == user['password']:
                achei = True
                break
        return achei


def pass_gen() -> str:
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!?@#$%&*'
    all = lower + upper + numbers + symbols
    generated_password = ''.join(sample(all, 8))
    return generated_password
