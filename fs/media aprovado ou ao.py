nota1 = float(input('digite a primeira nota:'))
nota2 = float(input('digite a segunda nota:'))
media = (nota1+nota2)/2
print('sua media ' + str(media))
if media >7:
    print('aprovado')
elif media <5:
    print('reprovado')
else:
    print('recuperacao')