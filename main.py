# gerador-de-senhas
# gerador de senhas, senha "segura" 

import random 
import os
import time

os.system('pkg install python && pkg install pip && pip install tqmd')
lower_case = 'abcdefghijklmnopqrstuvwxyz'
upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
number = '0123456789'
symbols = '#'
User_for = lower_case + upper_case + number + symbols
length_for_pass = 12
password = "".join(random.sample(User_for, length_for_pass))
password2 = "".join(random.sample(User_for, length_for_pass))
password3 = "".join(random.sample(User_for, length_for_pass))
password4 = "".join(random.sample(User_for, length_for_pass))
password5 = "".join(random.sample(User_for, length_for_pass))
password6 = "".join(random.sample(User_for, length_for_pass))
os.system('cls||clear')
time.sleep(1)
print('gerando senha, aguarde')
time.sleep(3)
os.system('cls||clear')
print('suas senhas:')
print('senha 1: {}'.format(password))
print('senha 2: {}'.format(password2))
print('senha 3: {}'.format(password3))
print('senha 4: {}'.format(password4))
print('senha 5: {}'.format(password5))
print('senha 6: {}'.format(password6))
fim = input('Volte sempre =) *aperte enter para sair*')
os.system('cls||clear')
