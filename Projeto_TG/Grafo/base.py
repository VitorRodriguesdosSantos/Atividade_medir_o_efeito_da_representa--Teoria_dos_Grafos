from abc import ABC, abstractmethod 
from typing import Iterable

class Grafo(ABC):
    @abstractmethod
    def ordem (self) -> int:
        pass

    @abstractmethod
    def tamanho(self) -> int:
        pass

    @abstractmethod
    def vizinhos(self, v: int) -> Iterable[int]:
        pass

    @abstractmethod
    def tem_aresta(self, u: int, v: int) -> bool:
        pass

    @abstractmethod
    def inserir_aresta(self, u: int, v: int):
        pass

    def vertices(self) -> Iterable[int]:
        return range(self.ordem())

    def grau(self, v: int) -> int:
        return sum(1 for _ in self.vizinhos(v))