import random

print('Bem vindo ao gerador de senha')
caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*0123456789'
numero =  int(input('Quantas senhas serão geradas? '))
length = int(input('Quantos caracteres você deseja? '))


print('\nAqui estão os exemplos de senha para você: ')
for pwd in range (numero):
    passwords = ''
    for c in range (length):
        passwords += random.choice(caracteres)
    print(passwords)
