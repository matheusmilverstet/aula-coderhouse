'''
4.	Calculadora de Consumo de Combustível: "Crie um aplicativo para calcular o consumo médio de combustível de um veículo. 
O usuário deve inserir o nome do motorista, a quantidade de quilômetros percorridos e a quantidade de combustível gasto em litros. 
O programa deve calcular o consumo médio (quilômetros por litro) e classificar a eficiência do veículo conforme a tabela:
•	Menos de 8 km/l: Venda o carro!
•	Entre 8 e 12 km/l: Econômico
•	Mais de 12 km/l: Super econômico 
Apresente o nome do motorista e a classificação de eficiência do veículo."
'''

nome = input("Digite o nome do(a) motorista:\n")
distancia = float(input("Digite a quilometragem percorrida:\n"))
gasto = float(input("Digite o combustível gasto em litros:\n"))
consumo = (distancia/gasto)

if consumo < 8 :
    print(f"O consumo médio do veículo foi de {consumo}km/l. {nome}, venda o carro!")
elif consumo >= 8 and consumo <= 12 :
    print(f"O consumo médio do veículo foi de {consumo}km/l. {nome}, o veículo é econômico!")
else :
    print(f"O consumo médio do veículo foi de {consumo}km/l. {nome}, o veículo é super econômico!")

    
