nome = str(input('Digite o seu nome completo: ')).strip()
priNome = nome.split()
print('Todas as letras maiúsculas: {}'.format(nome.upper()))
print('Todas as letras minúsculas: {}'.format(nome.lower()))
print('Total de letras no nome: {}'.format(len(nome) - nome.count(' ')))
print('Total de letras no primeiro nome: {}'.format(priNome[0]))