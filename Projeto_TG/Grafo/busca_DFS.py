from lista import GrafoLista
from matriz import GrafoMatriz
from buscas import dfs, componentes, encontrar_ciclo

ARESTAS = [(0, 1), (0, 2), (1, 3), (2, 3), (2, 4), (3, 5), (4, 5), (5, 6)]

def construir(classe, n=8, arestas=ARESTAS):
    g = classe(n)
    for u, v in arestas:
        g.inserir_aresta(u, v)
    return g

def eh_ancestral(a, b, pai):
    while b is not None:
        if b == a:
            return True
        b = pai[b]
    return False

def testar(g):
    n = g.ordem()
    pai, ent, sai, raiz = dfs(g)

    assert sorted(ent + sai) == list(range(1, 2 * n + 1))
    assert all(ent[v] < sai[v] for v in g.vertices())

    for v in g.vertices():
        if pai[v] is not None:
            assert ent[pai[v]] < ent[v] < sai[v] < sai[pai[v]]

    for u in g.vertices():
        for v in g.vizinhos(u):
            if pai[u] == v or pai[v] == u:
                continue
            assert eh_ancestral(u, v, pai) or eh_ancestral(v, u, pai)

    c = len(set(raiz))
    assert sum(p is not None for p in pai) == n - c

    comps = sorted(sorted(x) for x in componentes(g))
    assert comps == [[0, 1, 2, 3, 4, 5, 6], [7]]
    ciclo = encontrar_ciclo(g)
    assert ciclo is not None and ciclo[0] == ciclo[-1]
    assert all(g.tem_aresta(a, b) for a, b in zip(ciclo, ciclo[1:]))

def testar_casos_pequenos(classe):
    assert dfs(classe(0)) == ([], [], [], [])               
    assert encontrar_ciclo(construir(classe, 1, [])) is None  # isolado
    assert encontrar_ciclo(construir(classe, 2, [(0, 1)])) is None  # uma aresta
    assert encontrar_ciclo(construir(classe, 4, [(0, 1), (1, 2), (2, 3)])) is None  # caminho
    assert encontrar_ciclo(construir(classe, 3, [(0, 1), (1, 2), (0, 2)])) is not None  # triângulo

def main():
    for classe in (GrafoLista, GrafoMatriz):
        testar(construir(classe))
        testar_casos_pequenos(classe)
        print(f"{classe.__name__}: todos os testes da DFS passaram.")

    g = construir(GrafoLista, 5000, [(i, i + 1) for i in range(4999)])
    pai, ent, sai, _ = dfs(g)
    assert ent[4999] == 5000 and sai[0] == 10000
    print("Caminho com 5000 vértices: OK (sem RecursionError).")

if __name__ == "__main__":
    main()