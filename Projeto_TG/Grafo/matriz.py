from typing import Iterable
from base import Grafo

class GrafoMatriz(Grafo):
    def __init__(self, qtd_vertices: int):
        self.qtd_vertices = qtd_vertices
        self.qtd_aresta = 0
        self.matriz = [[0] * qtd_vertices for _ in range(qtd_vertices)]

    def ordem (self) -> int:
        return self.qtd_vertices

    def tamanho(self) -> int:
        return self.qtd_aresta

    def vizinhos(self, v: int) -> Iterable[int]:
        return (u for u in range(self.qtd_vertices) if self.matriz[v][u] == 1)

    def tem_aresta(self, u: int, v: int) -> bool:
        return self.matriz[u][v] == 1

    def inserir_aresta(self, u: int, v: int) -> None:
        if u == v:
            raise ValueError("laço não é permitido em grafo simples")
        if self.matriz[u][v] == 1:
            return
        self.matriz[u][v] = 1
        self.matriz[v][u] = 1
        self.qtd_aresta += 1

g = GrafoMatriz(4)
print(g.qtd_aresta)        # 0
print(g.qtd_vertices)      # 4
g.inserir_aresta(1, 2)
print(g.qtd_aresta)        # 1
print(list(g.vizinhos(1))) # [2]
print(g.grau(1)) 