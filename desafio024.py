cidade = str(input('Digite o nome da cidade: ')).upper().strip().split()

print('A cidade começa com SANTO? {}'.format('SANTO' in cidade[0]))

#OU

cidade = str(input('Digite o nome da cidade que você nasceu: ')).strip().upper()
print(cidade[:5] == 'SANTO')
