#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Converted from Jupyter Notebook: Aula8.ipynb
Conversion Date: 2025-10-31T17:52:08.445Z
"""

first_tupla = ('segunda','terça','quarta','quinta','sexta')
print(first_tupla[1])

for k in first_tupla:
    print(f'O dia de hoje é {k}')

folha=('naruto', 'sasuke', 
       'sakura', 'lee', 
       'neji', 'hinata', 
       'choji', 'shikamaru',
       'ino','kiba', 
       'tenten','shino')
print(folha[0:4])
print(folha[-4:])
print(folha[5:8])
sorted(folha)

nomes=set()
for x in range(1,4):
    nomes.add('maria')
for v in nomes:
    print(f'Essa será a variável removida {v}')
    nomes.pop
    print(nomes)
print(nomes)