## Substituindo caractere repetido
# Escreva um programa Python para obter uma string de uma determinada string em que todas as 
# ocorrências de seu primeiro caractere foram alteradas para '$', exceto o próprio primeiro caractere

# Ex:
# fifa 23 → **fi#a 23**
# restart→ resta#t

nome = input("Digite uma palavra\n").lower()
primeira = nome[0:1]
resto = nome[1:]

for i in range(len(resto)):
    if(resto[i] == primeira):
        print(f"{primeira}{resto.replace(resto[i], "#")}")
        break

## Substituindo caractere repetido
# Escreva um programa Python para obter uma única string de duas strings fornecidas, separadas 
# por um espaço e troque os dois primeiros caracteres de cada string.

# Ex:
# abc xyz → **xyc abz**

ex1 = "xyz"
ex2 = "abc"

print(f"\n{ex1.replace(ex1[2], ex2[2])}")
print(f"\n{ex2.replace(ex2[2], ex1[2])}")