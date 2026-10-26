def analisa_notas(notas):
    if len(notas) == 0:
        return 
    else:
        positivas = 0
        soma = 0
        alta = notas[0]
        for i in notas:
            if i >= 10:
                positivas += 1
            soma += i
            if i > alta:
                alta = i
        
        return (positivas, soma/len(notas), alta)
    
    
print(analisa_notas([12, 8, 17, 10]))
