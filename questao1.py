def classificar_produto(quantidade):
    if quantidade == 0:
        return "Sem estoque"
    elif quantidade <= 5 and quantidade > 0:
        return "Estoque baixo"
    elif quantidade <= 20 and quantidade > 5:
        return "Estoque normal"
    elif quantidade > 20:
        return "Estoque alto"
    elif quantidade < 0:
        return "Quantidade inválida"

