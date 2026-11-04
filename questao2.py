def inverte_palavra(frase: str):
    palavras = frase.split()
    palavra_invertida = palavras[::-1]
    resultado = " ".join(palavra_invertida)

    return resultado

print(inverte_palavra("Vou tirar 10"))