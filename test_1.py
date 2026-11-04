from questao1 import classificar_produto
def test_sem_estoque():
    result = classificar_produto(0)
    assert result == "Sem estoque"

def test_estoque_baixo():
    result = classificar_produto(5)
    assert result == "Estoque baixo"

def test_estoque_normal():
    result = classificar_produto(18)
    assert result == "Estoque normal"

def test_estoque_alto():
      result = classificar_produto(50)
      assert result == "Estoque alto"

def test_estoque_invalido():
      result = classificar_produto(-5)
      assert result == "Quantidade inválida"