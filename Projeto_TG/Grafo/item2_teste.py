from matriz import GrafoMatriz
from lista import GrafoLista

ARESTAS = [
    (0, 1),  
    (0, 2),  
    (1, 2),  
    (1, 3),  
    (2, 3),  
    (2, 4), 
    (3, 4),  
    (4, 5),  
]

def construir_grafo(GrafoClasse):
    grafo = GrafoClasse(6)

    for u, v in ARESTAS:
        grafo.inserir_aresta(u, v)

    return grafo

def testar_grafo(grafo):
    assert grafo.ordem() == 6

    assert grafo.tamanho() == 8

    graus = [grafo.grau(v) for v in grafo.vertices()]

    assert sorted(graus, reverse=True) == [4, 3, 3, 3, 2, 1]

    assert sum(graus) == 2 * grafo.tamanho()

def main():
    grafo_matriz = construir_grafo(GrafoMatriz)
    testar_grafo(grafo_matriz)
    print("GrafoMatriz: todos os testes passaram.")

    grafo_lista = construir_grafo(GrafoLista)
    testar_grafo(grafo_lista)
    print("GrafoLista: todos os testes passaram.")

if __name__ == "__main__":
    main()