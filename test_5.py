import unittest
from unittest.mock import patch
from questao5 import acessar_sistema


class TestAcessoSistema(unittest.TestCase):


    @patch("questao5.verificar_permissao")
    def test_usuario_com_permissao(self, mock_permissao):
        mock_permissao.return_value = True

        resultado = acessar_sistema("admin")

        self.assertEqual(resultado, "Acesso autorizado")


    @patch("questao5.verificar_permissao")
    def test_usuario_sem_permissao(self, mock_permissao):
        mock_permissao.return_value = False

        resultado = acessar_sistema("visitante")

        self.assertEqual(resultado, "Acesso negado")


    @patch("questao5.verificar_permissao")
    def test_verificar_se_funcao_foi_chamada(self, mock_permissao):
        mock_permissao.return_value = True

        acessar_sistema("admin")

        mock_permissao.assert_called_once()


    @patch("questao5.verificar_permissao")
    def test_usuario_correto(self, mock_permissao):
        mock_permissao.return_value = True

        acessar_sistema("admin")

        mock_permissao.assert_called_once_with("admin")


if __name__ == "__main__":
    unittest.main()