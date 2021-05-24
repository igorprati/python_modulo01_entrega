#02 - Utilizando estruturas de repetição com variável de controle, faça um programa que receba uma string com uma frase informada pelo usuário e conte quantas vezes aparece as vogais a,e,i,o,u e mostre na tela, depois mostre na tela essa mesma frase sem nenhuma vogal.

from os import system
system('cls') # limpa o terminal

frase = str(input('Digite uma frase: ')).strip().lower() # recebe a frase, tira os espaços antes dela e coloca em caixa baixa
frase1 = frase # separei frase de frase1 para poder mostrar a frase antes e depois de tirar as vogais
vogais = 'aeiouáàãâéèêíóòôõúù' # essa são as vogais
qntVogais = 0 #contador de vogais

for i in frase: # i passa por toda a frase digitada, string por string
    if i in vogais: # caso o i esteja dentro da variavel vogal, ou seja, aeiou:
        qntVogais += 1 # soma 1 ao contador de vogais
        frase = frase.replace(i, "") # i será trocado por espaço vazio, ou seja, ""   

system('cls') # limpa o terminal

print('=-=' * 8)
print(f'''
    Esta foi a frase digitada: {frase1}
    Esta é a frase sem vogais: {frase}
    Foram retiradas {qntVogais} vogais
''')
print('=-=' * 8)


