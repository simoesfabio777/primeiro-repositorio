ano = int(input('insira o ano:'))

if (ano % 400 == 0) or (ano % 4 ==0 and ano % 100 != 0):
    print('é bissexto')
else:
    print('não é bissexto')