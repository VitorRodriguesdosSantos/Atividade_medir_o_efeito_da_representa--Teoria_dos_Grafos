import random
import time
from statistics import median

from matriz import GrafoMatriz
from lista import GrafoLista
from triangulos import contar_triangulos

def gerar_arestas(n, densidade, seed=42):
    random.seed(seed)

    arestas = []

    for u in range(n):
        for v in range(u + 1, n):
            if random.random() < densidade:
                arestas.append((u, v))

    return arestas

def construir_grafo(GrafoClasse, n, arestas):
    grafo = GrafoClasse(n)

    for u, v in arestas:
        grafo.inserir_aresta(u, v)

    return grafo

def medir_tempo(grafo, repeticoes=3):
    tempos = []
    resultado = None

    for _ in range(repeticoes):
        inicio = time.perf_counter()

        resultado_atual = contar_triangulos(grafo)

        fim = time.perf_counter()

        tempos.append(fim - inicio)

        if resultado is None:
            resultado = resultado_atual
        elif resultado_atual != resultado:
            raise ValueError("O resultado de contar_triangulos mudou entre execuções.")

    return median(tempos), resultado

def densidade_real(grafo):
    n = grafo.ordem()
    m = grafo.tamanho()

    return (2 * m) / (n * (n - 1))

def main():
    n = 2000
    densidades = [0.001, 0.05, 0.5]

    print(
        f"{'Densidade':<12}"
        f"{'Real':<12}"
        f"{'Representação':<18}"
        f"{'Triângulos':<15}"
        f"{'Tempo (s)':<15}"
        f"{'Espaço':<15}"
    )

    print("-" * 87)

    for densidade in densidades:

        arestas = gerar_arestas(n, densidade, seed=42)

        matriz = construir_grafo(GrafoMatriz, n, arestas)
        lista = construir_grafo(GrafoLista, n, arestas)

        if matriz.tamanho() != lista.tamanho():
            raise ValueError("Matriz e lista possuem quantidades diferentes de arestas.")

        densidade_observada = densidade_real(matriz)

        tempo_matriz, triangulos_matriz = medir_tempo(matriz)

        espaco_matriz = n ** 2

        print(
            f"{densidade:<12.3f}"
            f"{densidade_observada:<12.6f}"
            f"{'Matriz':<18}"
            f"{triangulos_matriz:<15}"
            f"{tempo_matriz:<15.6f}"
            f"{espaco_matriz:<15}"
        )

        tempo_lista, triangulos_lista = medir_tempo(lista)

        espaco_lista = n + 2 * lista.tamanho()

        print(
            f"{densidade:<12.3f}"
            f"{densidade_observada:<12.6f}"
            f"{'Lista':<18}"
            f"{triangulos_lista:<15}"
            f"{tempo_lista:<15.6f}"
            f"{espaco_lista:<15}"
        )

        if triangulos_matriz != triangulos_lista:
            raise ValueError("Matriz e lista produziram quantidades diferentes de triângulos.")

if __name__ == "__main__":
    main()