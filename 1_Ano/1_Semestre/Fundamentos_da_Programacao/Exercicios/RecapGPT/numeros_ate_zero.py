numero = int(input())
contador = 0
soma = 0
positivos = 0
while numero != 0:
    contador += 1
    soma += numero
    if numero > 0:
        positivos += 1
    numero = int(input())
    
print(f'Quantidade de números: {contador}')
print(f'Soma: {soma}')
print(f'Positivos: {positivos}')    