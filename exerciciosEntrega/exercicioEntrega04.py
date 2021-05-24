#04 - Utilizando funções e listas faça um programa que receba uma data no formato DD/MM/AAAA e devolva uma string no formato DD de mesPorExtenso de AAAA. Opcional: valide a data e retorne 'data inválida' caso a data seja inválida.

from os import system

def mesPorExtenso():
    system('cls') # limpa o prompt de comando
    dia = int(input('Digite o dia[DD]: ')) # usuário digita um dia válido [1 - 31]
    mes = int(input('Digite o mês[MM]: ')) # usuário digita um mes válido [1 - 12]
    ano = int(input('Digite o ano[AAAA]: ')) # usuário digita um ano válido
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'] # lista com todos os meses, por extenso

    for i, m in enumerate(meses): # i = índice , m = meses por extenso
        if mes == i +1: # se o mes for igual a i + 1...
            mes = m # mes recebe o mes por extenso correspondente ao seu i

    if dia > 29 and mes == 'Fevereiro': # se o dia for maior que 29 e o mes for fevereiro...
        print('\nData Inválida! Fevereiro só pode ter até 29 dias!\n')

    elif dia > 31: # se o dia for maior que 31 ...
        print('\nData Inválida! Os meses só podem ter até 31 dias (exceto fevereiro)\n')
        
    elif mes not in meses: # se o mes não estiver dentro da lista de meses...
        print('\nData inválida! Meses só vão até 12!\n')

    elif ano < 0: # se o ano for negativo...
        print(f'\n-=-=-=-=-=-=-=-=-=-\n{dia} de {mes} de {ano * -1} a.C\n=-=-=-=-=-=-=-=-=-\n')
        
    else: # se nenhuma das condições acima for atendida ...
        print(f'\n-=-=-=-=-=-=-=-=-=-\n{dia} de {mes} de {ano}\n=-=-=-=-=-=-=-=-=-\n')


mesPorExtenso()

