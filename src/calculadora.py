def somar(a: int, b: int) -> int:
    return a + b


def atingiu_limite(valor: int, limite: int) -> bool:
    return valor >= limite


def somar_se_ativo(a: int, b: int, ativo: bool) -> int | None:
    if not ativo:
        return None
    return a + b
