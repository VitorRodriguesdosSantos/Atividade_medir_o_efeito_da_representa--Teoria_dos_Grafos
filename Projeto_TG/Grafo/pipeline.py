from pathlib import Path

from leitura import ler_pares, indexar
from construcao import construir
from conferencia import conferir
from lista import GrafoLista

def main():
    caminho = Path("Dados/karate.edgelist")

    pares, relatorio = ler_pares(caminho)

    indice = indexar(pares)

    grafo, repetidas = construir(
        pares,
        indice,
        GrafoLista
    )

    conferencia = conferir(grafo)

    print("Relatório da leitura:")
    print(relatorio)

    print("\nRótulos distintos:")
    print(len(indice))

    print("\nArestas repetidas:")
    print(repetidas)

    print("\nConferência:")
    print(conferencia)


if __name__ == "__main__":
    main()