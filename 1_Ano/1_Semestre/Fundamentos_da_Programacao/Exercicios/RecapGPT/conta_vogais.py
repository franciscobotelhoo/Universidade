def conta_vogais(texto):
    texto = texto.lower().replace(' ', '')
    vogais = 0
    for char in texto:
        if char in 'aeiou':
            vogais += 1
            
    return vogais

print(conta_vogais("AEIOU"))