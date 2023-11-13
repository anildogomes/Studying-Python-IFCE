"01.Escreva um programa que leia um número inteiro e verifique se ele é par ou ímpar. Caso seja par, imprima O número é par. Caso seja ímpar, imprima O número é ímpar. "

num = int(input('Digite qualquer número: '))
resultado = num % 2

if resultado ==0:
    print('O número {} é PAR'.format(num))
else:
    print('O número {} é IMPAR'.format(num))


