def validar_documento(documento: str):
    digitos = documento.replace('.', "").replace('-', '')
    if len(digitos) != 11:
        return False
    for char in digitos:
        if not char.isnumeric():
            return "Tem letras"
    return True

print(validar_documento(""))
