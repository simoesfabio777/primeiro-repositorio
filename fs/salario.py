salario = float(input('digite o seu salario:'))#float inserir numeros quebrados
if salario < 1500.00:#if se o salario for
    aumento = 0.25
if salario >= 1500.00 and salario <=1999.99:#and 'e' salario for esse e esse
    aumento = 0.20
if salario >= 2000.00 and salario <= 2999.99:#salario >= numero and salario 'entre'
    aumento = 0.15
if salario >= 3000.00 and salario <= 4999.99:
   aumento = 0.10
elif salario >=5000.00:#elif se nao dor if é isso
    aumento = 0.05
reajuste_total = salario*aumento
salario_novo = salario + reajuste_total

print(f'o seu salario é {salario}')
print(f'porcentagem de reajuste {aumento*100}')
print(f'seu aumento em {reajuste_total}')
print(f'salario novo {salario_novo}')