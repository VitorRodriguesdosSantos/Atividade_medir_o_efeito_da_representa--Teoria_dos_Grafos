import random
from lista import GrafoLista

def gerar_grafo(GrafoClasse, n, densidade, seed=42):
    random.seed(seed)

    grafo = GrafoClasse(n)

    for u in range(n):
        for v in range(u + 1, n):
            if random.random() < densidade:
                grafo.inserir_aresta(u, v)

    return grafo

def main():
    n = 2000
    densidades = [0.001, 0.05, 0.5]

    for densidade in densidades:
        grafo = gerar_grafo(GrafoLista, n, densidade, seed=42)

        print(f"Densidade alvo: {densidade}")
        print(f"n = {grafo.ordem()}")
        print(f"m = {grafo.tamanho()}")
        print()

if __name__ == "__main__":
    main()