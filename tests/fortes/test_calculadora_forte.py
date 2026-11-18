import pytest

from calculadora import atingiu_limite, somar, somar_se_ativo


@pytest.mark.parametrize(
    "primeiro, segundo, esperado",
    [(2, 2, 4), (3, 4, 7), (-2, 5, 3)],
)
def test_soma_confere_resultado_exato(primeiro, segundo, esperado):
    assert somar(primeiro, segundo) == esperado


@pytest.mark.parametrize(
    "valor, limite, esperado",
    [(10, 5, True), (5, 5, True), (4, 5, False)],
)
def test_limite_confere_casos_de_fronteira(valor, limite, esperado):
    assert atingiu_limite(valor, limite) is esperado


def test_soma_com_calculadora_ativa():
    assert somar_se_ativo(2, 3, True) == 5


def test_calculadora_inativa_nao_calcula():
    assert somar_se_ativo(2, 3, False) is None
