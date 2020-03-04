from datetime import date
anoNasc = int(input('Atleta, digite seu ano de nascimento: '))
anoAtual = date.today().year
idade = anoAtual - anoNasc
if idade > 0 and idade <= 9:
    print('Você tem {} anos e pertencia a categoria MIRIM'.format(idade))
elif idade > 9 and idade <= 14:
    print('Você tem {} anos e pertence a categoria INFANTIL'.format(idade))
elif idade > 14 and idade <= 19:
    print('Você tem {} anos e pertence a categoria JUNIOR'.format(idade))
elif idade > 19 and idade <= 20:
    print('Você tem {} anos e pertence a categoria SÊNIOR'.format(idade))
else:
    print('Você tem {} anos e pertence a categoria MASTER'.format(idade))


