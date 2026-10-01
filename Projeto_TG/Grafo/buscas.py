from base import Grafo

def dfs(g: Grafo):
    n = g.ordem()
    entrada = [0] * n
    saida = [0] * n
    pai: list[int | None] = [None] * n
    raiz: list[int | None] = [None] * n
    tempo = 0

    for r in g.vertices():
        if entrada[r] != 0:
            continue

        tempo += 1
        entrada[r] = tempo
        raiz[r] = r
        pilha = [(r, iter(g.vizinhos(r)))]

        while pilha:
            u, vizinhos = pilha[-1]
            try:
                v = next(vizinhos)
            except StopIteration:

                tempo += 1
                saida[u] = tempo
                pilha.pop()
                continue

            if entrada[v] == 0:
                pai[v] = u
                raiz[v] = r
                tempo += 1
                entrada[v] = tempo
                pilha.append((v, iter(g.vizinhos(v))))

    return pai, entrada, saida, raiz

def componentes(g: Grafo) -> list[list[int]]:
    _, _, _, raiz = dfs(g)
    grupos: dict[int, list[int]] = {}
    for v in g.vertices():
        grupos.setdefault(raiz[v], []).append(v)
    return list(grupos.values())

def encontrar_ciclo(g: Grafo) -> list[int] | None:
    pai, entrada, _, _ = dfs(g)
    for u in g.vertices():
        for v in g.vizinhos(u):
            if u >= v:
                continue
            if pai[u] == v or pai[v] == u:  
                continue
            a, b = (u, v) if entrada[u] < entrada[v] else (v, u)  
            ciclo = [b]
            while ciclo[-1] != a:
                ciclo.append(pai[ciclo[-1]])
            ciclo.append(b)
            return ciclo
    return None