from base import Grafo

def contar_triangulos(grafo: Grafo) -> int:
    total = 0

    for u in grafo.vertices():
        for v in grafo.vizinhos(u):
            if v <= u:
                continue

            for w in grafo.vizinhos(v):
                if w <= v:
                    continue

                if grafo.tem_aresta(u, w):
                    total += 1

    return total