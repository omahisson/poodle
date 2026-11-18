import argparse
import json
from pathlib import Path


def classificar(resultado):
    codigo = str(resultado.get("reason_code", "")).upper()
    if "TIMEOUT" in codigo:
        return "TIMEOUT"
    if "ERROR" in codigo:
        return "ERRO"
    if resultado.get("found") is True:
        return "MORTO"
    if resultado.get("found") is False:
        return "SOBREVIVEU"
    return "INDEFINIDO"


def inspecionar(caminho, detalhes):
    dados = json.loads(caminho.read_text(encoding="utf-8"))
    resumo = dados.get("summary", {})
    mutantes = dados.get("mutant_trials", [])

    print(f"\nRELATORIO: {caminho}")
    print(f"Mutantes executados: {resumo.get('tested', 'nao informado')}")
    print(f"Mortos: {resumo.get('found', 'nao informado')}")
    print(f"Sobreviventes: {resumo.get('not_found', 'nao informado')}")
    print(f"Pontuacao: {resumo.get('coverage_display', 'nao informado')}")

    for numero, item in enumerate(mutantes, start=1):
        mutante = item.get("mutant", {})
        resultado = item.get("result", {})
        status = classificar(resultado)
        print(f"\n{numero}. {status} | {mutante.get('mutator_name', '?')} | "
              f"{mutante.get('source_file', '?')}:{mutante.get('lineno', '?')}")
        print(mutante.get("unified_diff", "sem diff disponivel"))

        if detalhes and resultado.get("reason_desc"):
            print("Saida do teste:")
            print(resultado["reason_desc"])


def executar():
    analisador = argparse.ArgumentParser()
    analisador.add_argument("arquivos", nargs="+", type=Path)
    analisador.add_argument("--detalhes", action="store_true")
    argumentos = analisador.parse_args()

    for caminho in argumentos.arquivos:
        inspecionar(caminho, argumentos.detalhes)


if __name__ == "__main__":
    executar()
