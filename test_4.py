from unittest.mock import patch
from questao4 import criar_identificacao

def test_obter_nome():
    with patch("questao4.criar_identificacao") as mock_criar_identificacao:
        mock_criar_identificacao.return_value = {
            "nome":"Carlos"
        }
        frase = criar_identificacao("Carlos")

        assert frase == "Usuário Carlos cadastrado com código USR-1234"


