
def obter_proximo_cliente():
    fila = ["João", "Maria", "Pedro"]

    if fila:
        return fila[0]

    return None


def registrar_atendimento(cliente):
    print(f"Atendimento registrado para {cliente}")
    return True


def atender_proximo_cliente():
    cliente = obter_proximo_cliente()

    if cliente is None:
        return "Fila vazia"

    if registrar_atendimento(cliente):
        return "Atendimento realizado"

    return "Falha no atendimento"