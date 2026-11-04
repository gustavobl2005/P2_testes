import unittest
from unittest.mock import patch
from questao6 import atender_proximo_cliente


class TestFila(unittest.TestCase):

  
    @patch("questao6.registrar_atendimento")
    @patch("questao6.obter_proximo_cliente")
    def test_atendimento_sucesso(self, mock_cliente, mock_registro):
        mock_cliente.return_value = "João"
        mock_registro.return_value = True

        resultado = atender_proximo_cliente()

        self.assertEqual(resultado, "Atendimento realizado")

    @patch("questao6.registrar_atendimento")
    @patch("questao6.obter_proximo_cliente")
    def test_fila_vazia(self, mock_cliente, mock_registro):
        mock_cliente.return_value = None

        resultado = atender_proximo_cliente()

        self.assertEqual(resultado, "Fila vazia")

    @patch("questao6.registrar_atendimento")
    @patch("questao6.obter_proximo_cliente")
    def test_falha_atendimento(self, mock_cliente, mock_registro):
        mock_cliente.return_value = "Maria"
        mock_registro.return_value = False

        resultado = atender_proximo_cliente()

        self.assertEqual(resultado, "Falha no atendimento")

    @patch("questao6.obter_proximo_cliente")
    def test_obter_cliente_chamada(self, mock_cliente):
        mock_cliente.return_value = "João"

        atender_proximo_cliente()

        mock_cliente.assert_called_once()


    @patch("questao6.registrar_atendimento")
    @patch("questao6.obter_proximo_cliente")
    def test_registrar_cliente_correto(self, mock_cliente, mock_registro):
        mock_cliente.return_value = "Pedro"
        mock_registro.return_value = True

        atender_proximo_cliente()

        mock_registro.assert_called_once_with("Pedro")


    @patch("questao6.registrar_atendimento")
    @patch("questao6.obter_proximo_cliente")
    def test_registro_nao_chamado_fila_vazia(self, mock_cliente, mock_registro):
        mock_cliente.return_value = None

        atender_proximo_cliente()

        mock_registro.assert_not_called()


if __name__ == "__main__":
    unittest.main()