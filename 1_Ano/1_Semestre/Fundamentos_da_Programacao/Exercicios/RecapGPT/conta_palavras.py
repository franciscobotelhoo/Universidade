def conta_palavras(texto):
    palavras = texto.lower().split()
    final = []
    for i in palavras:
        encontrada = False
        for t in range(0, len(final)):
            if final[t][0] == i:
                final[t] = (final[t][0], final[t][1]+1)
                encontrada = True
                break
        if encontrada == False:
            final.append((i, 1))
                
    return final


print(conta_palavras("gato cão gato peixe cão gato"))
                    