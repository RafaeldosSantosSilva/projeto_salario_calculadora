''' Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
 Calcule e mostre o total do seu salário no referido mês, 
sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato,
 e mostre as informações no final.'''

print(f'PROGRAMA QUE CALCULA INFORMAÇÕES DO SALÁRIO')

salario_hora = float(input('Digite quanto você recebe por hora: '))
horas_trabalhadas = float(input('Digite a quantidade de horas trabalhadas: '))

sal_bruto = salario_hora * horas_trabalhadas

ir = 0.11*sal_bruto
inss = 0.08*sal_bruto 
sindicato = 0.05*sal_bruto
sal_liquido = sal_bruto - ir - inss - sindicato

print(f'         Salário Bruto: R${sal_bruto:.2f} \n \
        Salário Líquido: R${sal_liquido:.2f} \n \
        Imposto de Renda = R${ir:.2f} \n \
        INSS = R${inss:.2f} \n \
        Sindicato = R${sindicato:.2f}' )