#05 - Refatore o exercício 2, para que uma função receba a frase, faça todo o tratamento necessário e retorne o resultado. Depois mostre na tela o resultado e a quantidade de letras foram retiradas da frase original.

def tirarVogais(frase): # função que vai tirar as vogais da frase
    frase = frase.lower().strip() # força a frase ficar em caixa baixa e tira os espaços antes e depois
    vogais = 'aeiouáàãâéèêíóòôõúù' # essas são as vogais
    qntVogais = 0 # contador de vogais

    for i in frase: 
        if i in vogais: # o "i" vai passar pela frase, e toda vez que encontrar uma vogal...
            qntVogais += 1 # vai adicionar 1 ao contador
            frase = frase.replace(i, "") # vai trocar a vogal por vazio, ou seja, ""  
            
    print(f'Esta é a frase sem vogais: {frase}')
    print(f'Foram retiradas {qntVogais} vogais')


tirarVogais('Olá, meu nome é igor')
