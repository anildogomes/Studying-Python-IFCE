"""02.Escreva um programa que leia duas notas de um aluno e calcule a média. 
Se a média for maior ou igual a 7, imprima "Aprovado". 
Se a média for menor que 3, imprima "Reprovado". 
Se a média estiver entre 3 e 6,99, imprima "Avaliação Final" 
e peça o usuário para informar a nota que foi tirada na AF 
e calcule novamente a média, nesse caso, 
se a média for maior ou igual a 5, imprima "Aprovado", 
caso seja menor que 5, imprima "Reprovado"."""


nota1 = float(input('Primeira Nota: '))
nota2 = float(input('Segunda Nota: '))
media = (nota1 +nota2) / 2

print('A média do aluno é {}'.format(media))

if media >=7:
    print("APROVADO")

if media <3:
    print("REPROVADO")

else:
    print("Avaliação Final")
    nota_af = float(input("Digite a nota da Avaliação Final: "))
    media_af = (media + nota_af) / 2

        # Verifica se o aluno está aprovado ou reprovado após a Avaliação Final
    if media_af >= 5:
        print("Aprovado")
    else:
        print("Reprovado")




