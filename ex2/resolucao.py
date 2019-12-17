def troca_vogais(frase):
    frase_separada = list(frase)
    frase_modificada = []

    for letra in frase_separada:
        print(letra)
        if letra == 'a':
            frase_modificada.append('@')
        elif letra == 'e':
            frase_modificada.append('&')
        elif letra == 'i':
            frase_modificada.append('!')
        elif letra == 'o':
            frase_modificada.append('#')
        elif letra == 'u':
            frase_modificada.append('*')
        else:
            frase_modificada.append(letra)
    return ''.join(map(str,frase_modificada))

print(troca_vogais('tranquilo'))   