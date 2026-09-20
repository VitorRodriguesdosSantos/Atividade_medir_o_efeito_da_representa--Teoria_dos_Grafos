# **Teoria dos Grafos — Atividade: Medir o efeito da representação**

## **Sobre a atividade**

Esta atividade tem como objetivo analisar, na prática, como a **representação computacional de um grafo** influencia o custo das operações realizadas sobre ele.

Serão implementadas duas representações para grafos simples não orientados:

* **Matriz de adjacência**  
* **Lista de adjacência**

As duas implementações devem seguir a mesma interface `Grafo`, permitindo executar o mesmo algoritmo sobre ambas e comparar seus resultados.

A atividade é baseada na seção **3.15 — Atividade: medir o efeito da representação**, do material de Teoria dos Grafos.

## **Objetivos**

* Implementar um tipo abstrato de grafo.  
* Implementar `GrafoMatriz` e `GrafoLista`.  
* Validar as duas implementações usando um grafo conhecido.  
* Comparar o tempo de execução de `contar_triangulos`.  
* Comparar o espaço ocupado pelas duas representações.  
* Observar como a densidade do grafo influencia o desempenho.  
* Relacionar os resultados experimentais aos custos teóricos das operações.
