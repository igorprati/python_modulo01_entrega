#07 - Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

numeros = list() # lista geral contendo todos os números 
listaPar = list() # lista contendo apenas números pares
listaImpar = list() # lista contendo apenas números impares 

for i in range(0,7): # num intervalo de 0 a 7 
    num = int(input('Digite um número: ')) # recebe um input formato inteiro

    if num % 2 == 0: # valida se a divisão deste número por 2 dá resto zero, se sim, coloca esse número na lista par
        listaPar.append(num)
    else: # se condição acima não for atendida, significa que o número é impar. Então adiciona na lista impar  
        listaImpar.append(num)

# ao final do for, coloca a lista par e a lista impar dentro da lista geral de números  
numeros.append(listaPar)
numeros.append(listaImpar)

print(f'\nO valores pares são: {sorted(listaPar)}')
print(f'O valores impares são: {sorted(listaImpar)}\n')