import random

print('Bem vindo ao gerador de senha')
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*0123456789'
number = input('Quantas senhas serão geradas? ')
number = int(number)

length = input('Quantos caracteres você deseja? ')
length = int(length)

print('\nAqui estão os exemplos de senha para você: ')
for pwd in range (number):
    passwords = ''
    for c in range (length):
        passwords += random.choice(chars)
    print(passwords)