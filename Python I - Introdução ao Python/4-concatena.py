name = input("Digite o nome do game menzinho: \n")
yearLaunch = int(input("Qual a data de lançamento menzinho?\n"))
gamePrice = float(input("e qual o preço?\n"))
planIncluded = input("está incluso no serviço mensal?\n")

#FORMAS DE CONCATENAS: 
# 1 
# print("game name: ", name)
# print("year launch: ", yearLaunch)
# print("price: ", gamePrice)
# print("plan included? ", planIncluded)

# 2
print(f"Nome do Jogo: {name} \nAno Lançamento: {yearLaunch} \nPreço do Jogo: {gamePrice} \nEstá incluso no serviço? {planIncluded}")

