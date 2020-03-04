from time import sleep
num = int(input('Digite um número: '))

if num == 404:
    print('\n\033[31mError\033[m')

else:
    print('''\nEscolha a forma de conversão deste número:

[  1  ] para BINÁRIO
[  2  ] para OCTAL
[  3  ] para HEXADECIMAL''')

    if num == 666:
        print('[  4  ] para VENDER SUA ALMA')

    opção = int(input('\nDigite o número da opção: '))

    if opção == 1:
        print('\nO número {} convertido para BINÁRIO é: {}'.format(num,bin(num)[2:]))
    elif opção == 2:
        print('\nO número {} convertido para OCTAL é: {}'.format(num,oct(num)[2:]))
    elif opção == 3:
        print('\nO número {} convertido para HEXADECIMAL é: {}'.format(num,hex(num)[2:]))
    elif num == 666 and opção == 4:
        sleep(2)
        print('\n\033[31mSUA ALMA FOI ACEITA!\nVOCÊ NÃO TERÁ DIREITO DE DEVOLUÇÃO!\033[m')
        escolha = int(input(''''\nO que deseja como troca de sua alma?
[  1  ] Dinheiro
[  2  ] Fama
[  3  ] Mulher
[  4  ] A morte
\nDigite a sua escolha: '''))
        if escolha == 1:
            print('\nO valor de \033[34mR$999.999.999,00\033[m foi depositado em sua conta por \033[31mSATAN\033[m')
            print('Obrigado pelo pacto!')
        elif escolha == 2:
            print('\nVocê acaba de ganhar \033[34m500 Milhões\033[m de seguidores na sua conta Instagram')
            print('Divirta-se!')
        elif escolha == 3:
            mulher = input('''\nInsira o nome da mulher que você deseja: ''')
            print('\n{} está poucos metros de sua localização atual e está chegando...'.format(mulher))
            print('Se prepare, e tenha um bom encontro!')
        elif escolha == 4:
            morte = input('''\nInsira o nome da pessoa que deseja que morra
[  0  ] para a sua própria morte: ''')
            if '0' in morte:
                print('''\nTudo feito, basta aguardar
Sua vida acaba de ser absurdamente encurtada.''')
            else:
                print('''\n{} vai morrer em menos de 24h
Nos vemos por aí...'''.format(morte))
        else:
            print('''\n\033[31mDígito inválido!\033[m
\nVocê não ganhará nada em troca e sua alma não será ressacida
Até logo...''')
    elif num == 666 and opção != 4:
        print('\033[31mVOCÊ É FRACO!\033[m')
    else:
        print('\n\033[31mOpção inválida!\033[m')