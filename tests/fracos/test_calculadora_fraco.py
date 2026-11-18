from calculadora import atingiu_limite, somar, somar_se_ativo


def test_soma_com_valores_iguais():
    assert somar(2, 2) == 4


def test_limite_sem_verificar_fronteira():
    assert atingiu_limite(10, 5) is True


def test_atividade_sem_verificar_resultado_exato():
    assert somar_se_ativo(2, 3, True) != 0
