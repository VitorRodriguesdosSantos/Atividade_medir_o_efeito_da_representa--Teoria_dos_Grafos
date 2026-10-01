from typing import Iterable
from base import Grafo

class GrafoLista(Grafo):
    def __init__(self, qtd_vertices: int) -> None:
        self.qtd_vertices = qtd_vertices
        self.qtd_arestas = 0
        self.lista_adj: list[set[int]] = [set() for _ in range(qtd_vertices)]

    def ordem(self) -> int:
        return self.qtd_vertices

    def tamanho(self) -> int:
        return self.qtd_arestas

    def vizinhos(self, v: int) -> Iterable[int]:
        return iter(self.lista_adj[v])

    def grau(self, v: int) -> int:
        return len(self.lista_adj[v])

    def tem_aresta(self, u: int, v: int) -> bool:
        return v in self.lista_adj[u]

    def inserir_aresta(self, u: int, v: int) -> None:
        if u == v:
            raise ValueError("laço não é permitido em grafo simples")
        if v in self.lista_adj[u]:
            return
        self.lista_adj[u].add(v)
        self.lista_adj[v].add(u)
        self.qtd_arestas += 1