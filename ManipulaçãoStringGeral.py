nome = str(input('Digite o seu nome completo: ')).upper().strip()
primeiro = nome.split()
print('O seu nome completo é: {}'.format(nome))
print('O seu primeiro nome é: {}'.format(primeiro[0]))
print('O seu sobrenome é: {}'.format(primeiro[len(primeiro)-1]))
print('O seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
print('A letra "A" aparece primeiro na posição {}'.format(nome.find('A')+1))
print(('A letra "A" aparece na ultima vez na posição {}'.format(nome.rfind("A")+1)))
