#Ex03. Escreva um programa que leia uma sequência de números inteiros informados pelo usuário e imprima os números primos dessa sequência.

print('************NÚMEROS PRIMOS**************')



num = int(input('Digite um número: '))
tot = 0
          
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m' , end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(c), end='')

print('\n \033[m 0 número {} foi divisível {} vezes'. format(num, tot))
                  
if tot == 2:
    print('E por isso, ele é PRIMO!')
else:
    print("Não é PRIMO!")
                  

print('*************************')