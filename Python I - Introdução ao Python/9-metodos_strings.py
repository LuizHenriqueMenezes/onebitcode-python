gameName = "FIFONA"

gameDescription = """
joguinho de futebol, pra ganhar
várias champions league com 
o real madrid
"""

print("Maiúsculo / Minúsculo")
print(gameName.upper()) #Maiúsculo
print(f"{gameName.lower()}\n") # Minúsculo

print("Apenas primeira letra maiúscula")
print(gameName.capitalize()) 
print(f"{gameName.title()}\n") 

print("Retorna a string centralizada")
print(f"{gameName.center(10, '-')}\n")

print("Retorna a posição que o caractere foi encontrado ")
print(f"{gameDescription.find('o')}\n") 

print("Conta quantos caracteres ")
print(gameDescription.count('a')) 
print(f"{gameDescription.count('A')}\n")  

print("Altera elementos")
print(f"{gameDescription.replace("joguinho", "Jogão")}\n") 

print("quebra a string (no exemplo na virgula)")
print(gameDescription.split(','))