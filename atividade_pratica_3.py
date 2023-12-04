'''
3.	Sistema de Bonificação de Funcionários: "Elabore um programa que calcule a bonificação anual de um funcionário. 
Peça o nome do funcionário, o salário e o tempo de serviço em anos na empresa. A bonificação é dada da seguinte forma:
•	Menos de 1 ano de serviço: sem bonificação
•	De 1 a 3 anos de serviço: 10% do salário
•	De 4 a 6 anos de serviço: 15% do salário
•	De 7 a 10 anos de serviço: 20% do salário
•	Mais de 10 anos de serviço: 25% do salário 
O programa deve mostrar o nome do funcionário e o valor da bonificação que ele receberá."
'''

nome =  input("Digite o nome do funcionário:\n")
salario = float(input("Digite o salário do funcionário:\n"))
tempo = int(input("Digite o tempo de serviço (em anos):\n"))

if tempo < 1 :
    print(f"O(A) funcionário(a) {nome} ainda não recebe bonificação")
elif tempo >= 1 and tempo <= 3 :
    print(f"A bonificação do(a) funcionário(a) {nome} é de {0.1*salario}")
elif tempo >= 4 and tempo <= 6 :
    print(f"A bonificação do(a) funcionário(a) {nome} é de {0.15*salario}")
elif tempo >= 7 and tempo <= 10 :
    print(f"A bonificação do(a) funcionário(a) {nome} é de {0.2*salario}")
else :
    print(f"A bonificação do(a) funcionário(a) {nome} é de {0.25*salario}")