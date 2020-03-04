print('-=' * 20)
print('Analisador de Triângulos')
print('-=' * 20)
retaA = float(input('Digite o comprimento da reta A: '))
retaB = float(input('Digite o comprimento da reta B: '))
retaC = float(input('Digite o comprimento da reta C: '))
if retaA < (retaB + retaC) and retaB < (retaA + retaC) and retaC < (retaA + retaB):
    print('Essas retas PODEM FORMAR um triângulo')
else:
    print('Essas retas NÃO FORMAM um triângulo')
