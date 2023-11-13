#3.	Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.


valorhora = float(input('Quanto voce ganha por hora: '))
duracao = int(input('Quantidade de horas que trabalho neste mês: '))


salario = valorhora * duracao


print('Parabens! Seu salario será = R${}' .format(salario))
