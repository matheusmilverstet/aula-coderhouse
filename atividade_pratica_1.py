'''
1.	Calculadora de Imposto de Renda: "Crie um programa que calcule o Imposto de Renda devido por um contribuinte.
O usuário deve inserir o nome do contribuinte e o salário mensal. O programa deve calcular o imposto com base nas seguintes faixas:
•	Até R$ 1.903,98: isento
•	De R$ 1.903,99 até R$ 2.826,65: 7.5%
•	De R$ 2.826,66 até R$ 3.751,05: 15%
•	De R$ 3.751,06 até R$ 4.664,68: 22.5%
•	Acima de R$ 4.664,68: 27.5% Apresente o nome do contribuinte e o valor do imposto a pagar."
'''

nome = input("Digite o nome do contribuinte:\n")
salario = float(input("Digite o salário mensal do contribuinte:\n"))

if salario >= 1903.99 and salario <= 2826.65 :
    print(f"O contribuinte {nome} deve pagar {0.075*salario} IR")
elif salario >= 2826.66 and salario <= 3751.05 :
    print(f"O contribuinte {nome} deve pagar {0.15*salario} IR")
elif salario >= 3751.06 and salario <= 4664.68 :
    print(f"O contribuinte {nome} deve pagar {0.225*salario} IR")
elif salario > 4664.68 :
    print(f"O contribuinte {nome} deve pagar {0.275*salario} IR")
else :
    print(f"O contribuinte {nome} é isento de IR")