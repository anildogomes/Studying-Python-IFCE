#6.	Escreva um programa que peça ao usuário para digitar a temperatura em Fahrenheit e converta para Celsius e Kelvin, imprimindo o resultado na tela.


fahr = float(input('Insira a temperatura em FAHRENHEIT: '))
cel = (fahr - 32 )/1.8
kel = (cel + 273)



print('A temperatura informada convertida em Celsius: {} e Kelvin: {}' .format(cel, kel))
