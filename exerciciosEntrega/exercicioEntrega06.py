#06 - Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
   # "Telefonou para a vítima?"
   # "Esteve no local do crime?"
   # "Mora perto da vítima?"
   # "Devia para a vítima?"
   # "Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
   # Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
   # Entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
   # Caso contrário, ele será classificado como "Inocente".  

r1 = input("Telefonou para a vítima?: ").lower() # pergunta 1
r2 = input("Esteve no local do crime?: ").lower() # pergunta 2  
r3 = input("Mora perto da vítima?: ").lower() # pergunta 3  
r4 = input("Devia para a vítima?: ").lower() # pergunta 4
r5 = input("Já trabalhou com a vítima?: ").lower() # pergunta 5

lista = [r1, r2, r3, r4, r5] # coloca as respostas todas em uma lista
contadorSim = 0 # contador de respostas 'Sim'

for i in lista: # para cada resposta na lista...
    if i == "sim": # se a resposta for "sim"...
        contadorSim = contadorSim + 1 # adiciona 1 ao contador

if contadorSim == 2: # se o contador for 2...
    print("Suspeita")

elif contadorSim > 2 and contadorSim < 5: # se o contador for entre 2 ou 5 ...
    print("Cúmplice")

elif contadorSim == 5: # se o contador for 5...
    print("Assassino")
    
else: # se não for nenhuma das condições acima ...
    print("Inocente")
