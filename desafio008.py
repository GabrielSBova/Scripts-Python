medida = float(input('Digite uma distância em metros: '))
km = medida/1000
hm = medida/100
dam = medida/10
m = medida
dm = medida*10
cm = medida*100
mm = medida*1000
print('O valor digitado corresponde a {} metros'. format(medida))
print('Em quilômetros equivale a: {:.0f}km'.format(km))
print('Em hectômetros equivale a: {:.0f}hm'.format(hm))
print('Em decâmetros equivale a: {:.0f}dam'.format(dam))
print('Em decímetros equivale a: {:.0f}dm'.format(dm))
print('Em centímetros equivale a: {:.0f}cm'.format(cm))
print('Em milímetros equivale a: {:.0f}mm'.format(mm))
