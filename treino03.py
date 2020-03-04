nomeCid = str(input("Digite o nome da cidade: ")).upper().strip()
print('O nome da cidade é: {} '.format(nomeCid))
print('Possui SANTO no começo? {} '.format('SANTO' in nomeCid.split()[0]))
