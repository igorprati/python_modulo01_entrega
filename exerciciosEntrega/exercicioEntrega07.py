#07 - Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

numeros = list()
listaPar = list()
listaImpar = list()

for i in range(0,7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        listaPar.append(num)
    else:
        listaImpar.append(num)
numeros.append(listaPar)
numeros.append(listaImpar)

print(f'\nO valores pares são: {sorted(listaPar)}')
print(f'O valores impares são: {sorted(listaImpar)}\n')