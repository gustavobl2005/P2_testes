from questao3 import validar_documento

def test_11_digitos():
    result = validar_documento("12345678910")
    assert result == True

def test_documento_formatado():
    result = validar_documento("123.456.789-10")
    assert result == True

def test_documento_menor_11():
    result = validar_documento("123")
    assert result == False

def test_documento_maior_11():
    result = validar_documento("123456789101")
    assert result == False

def test_documento_letra():
    result = validar_documento("1234567891a")
    assert result == "Tem letras"

def test_documento_vazio():
    result = validar_documento("")
    assert result == False