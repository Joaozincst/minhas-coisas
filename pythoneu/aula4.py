#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Converted from Jupyter Notebook: joao.ipynb
Conversion Date: 2025-10-31T17:52:58.783Z
"""

stark=["arya","sansa","rickon","bran","robb"]
stark.append("theon")
for v in range (1,6):
    print(stark)

targaryen=["daenerys","jaeherys","maegor","aegon"]
for nome in targaryen:
    if nome.endswith('erys'):
        print(nome)

bilubilu=input('informe para mim o valor inicial')
bolo=input('informe para mim o valor final')
fogo=input('informe para mim o valor de passo')
for bilubilu in range