def verificar_permissao(usuario):
    usuarios_autorizados = ["admin", "professor"]

    return usuario in usuarios_autorizados


def acessar_sistema(usuario):
    if verificar_permissao(usuario):
        return "Acesso autorizado"
    else:
        return "Acesso negado"