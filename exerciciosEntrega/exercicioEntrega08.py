#08 - Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário. Se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente , além da idade, com quantos anos a pessoa vai se aposentar. Considere que o trabalhador deve contribuir por 35 anos para se aposentar.

ano = 2021 # ano atual que estamos
dados = dict() # dicionário com os dados do usuário

dados['Nome'] = input('Nome: ') # chave 'Nome' recebe valor
dados['Idade'] = 2021 - int(input('Ano de nascimento: ')) # chave 'Idade' recebe ano de nascimento
dados['CTPS'] = int(input('Carteira de trabalho: ')) # chave 'CTPS' recebe carteira de trabalho

if dados['CTPS'] != 0: # se a carteira de trabalho for diferente de ZERO:
    dados['anoContratacao'] = int(input('Ano de contratação: ')) # o programa vai pedir ano de contratação e adicionar à chave 'anoContratacao'
    dados['Salário'] = int(input('Salário: ')) # o programa vai pedir salario e adicionar à chave 'Salário'
    aposentadoria = (dados['anoContratacao'] + 35) - 1998 # cria uma variável que recebe com quantos anos a pessoa vai se aposentar. Para isso, soma o ano de contratação + 35 anos de serviço - ano de nascimento   
    print(f'Você irá se aposentar com {aposentadoria} anos.')
else:
    print('Não sei quando você vai se aposentar...')
