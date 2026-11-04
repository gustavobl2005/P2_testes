from questao2 import inverte_palavra
def test_varias_palavras():
    result = inverte_palavra("Macaco louco biruta")
    assert result == "biruta louco Macaco"

def test_uma_palavra():
    result = inverte_palavra("Pão")
    assert result == "Pão"

def test_frase_vazia():
    result = inverte_palavra("")
    assert result == ""

def test_frase_com_espacos_extras():
    result = inverte_palavra("Chapolin      Colorado")
    assert result == "Colorado Chapolin"

def test_letras_numeros():
    result = inverte_palavra("Vou tirar 10")
    assert result == "10 tirar Vou"