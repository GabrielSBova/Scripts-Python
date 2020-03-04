from datetime import date
anoAtual = date.today().year
alistamento = 18 #Idade para se alistar
anoNasc = int(input('Digite o seu ano de nascimento: '))
idade = anoAtual - anoNasc
tempoQfalta = idade - 18

if idade < 18:
    print('Você deverá se alistar ao serviço militar daqui {} anos'.format(tempoQfalta))
elif idade == 18:
    print('Já é hora de você se alistar ao serviço militar')
elif idade > 18:
    print('Já passou {} anos do prazo de alistamento'.format(tempoQfalta))
