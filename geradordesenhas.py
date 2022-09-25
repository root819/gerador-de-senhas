# gerador-de-senhas
# gerador de senhas, senha "segura" 

import random 
import os
import time
from tqdm import tqdm

bemvindo = input('aperte enter para instalar os requisitos')
os.system('pkg install python && pkg install pip && pip install tqmd')
lower_case = 'abcdefghijklmnopqrstuvwxyz'
upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
number = '0123456789'
symbols = '#'
User_for = lower_case + upper_case + number + symbols
length_for_pass = 12
password = "".join(random.sample(User_for, length_for_pass))
os.system('cls||clear')
time.sleep(1)
print('gerando senha, aguarde')
for i in tqdm(range(100)):
    time.sleep(0.07)
time.sleep(3)
os.system('cls||clear')
print('sua senha: {}'.format(password))
print('Volte sempre =)')
