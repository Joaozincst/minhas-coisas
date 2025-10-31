#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Converted from Jupyter Notebook: notebook.ipynb
Conversion Date: 2025-10-31T17:48:06.909Z
"""

# #João Victor Machado de Castro


%%writefile João.txt
eu tenho 17 anos, gosto de jogar fut e meu jogo preferido é the witcher 3

arquivo= open('João.txt','a')
arquivo.write('engraçado, cheiroso, engraçado, inteligente')

arquivo= open('João.txt')
arquivo.read()


# #Desafio


entrada=float(input('informe quando você entrou no jogo'))
jogo=float(input('informe quando você saiu do jogo'))
tempodejogo=jogo-entrada
print(f'O tempo de jogo foi de:{tempodejogo}')