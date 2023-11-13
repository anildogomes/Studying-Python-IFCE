#1.	Escreva um algoritmo que receba dois números e retorne a soma, a subtração, a multiplicação e a divisão entre eles.


n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))


soma = n1 + n2
subtracao = n1 - n2
mult = n1 * n2
div = n1 / n2

print('A Soma entre {} e mais {} é igual = {}' .format(n1,n2,soma))
print('A Subtração entre {} e mais {} é igual = {}' .format(n1,n2,subtracao))
print('A Multiplicação entre {} e mais {} é igual = {}' .format(n1,n2,mult))
print('A Divisão entre {} e mais {} é igual = {}' .format(n1,n2,div))
