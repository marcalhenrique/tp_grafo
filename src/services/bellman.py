class BellmanFord():
    def __init__(self, graph):
        self.graph = graph

    def run(self, origem):
        """
        Executa o algoritmo de Bellman-Ford para encontrar o menor caminho a partir de um nó de origem.
        Retorna um dicionário de distâncias, um dicionário de predecessores e um indicador de ciclo negativo.
        """
        distancia = {v: float('inf') for v in self.graph}
        distancia[origem] = 0
        anterior = {v: None for v in self.graph}

        # Relaxamento das arestas |V| - 1 vezes
        for _ in range(len(self.graph) - 1):
            for u in self.graph:
                for v, custo in self.graph[u].items():
                    if distancia[u] + custo < distancia[v]:
                        distancia[v] = distancia[u] + custo
                        anterior[v] = u

        # Verificação de ciclos negativos
        for u in self.graph:
            for v, custo in self.graph[u].items():
                if distancia[u] + custo < distancia[v]:
                    return None, None, True  # Ciclo negativo encontrado

        return distancia, anterior, False  # Retorna as distâncias, os predecessores e False (sem ciclo negativo)

    def menor_caminho(self, anterior, origem, destino):
        """
        Retorna a sequência de nós que formam o menor caminho entre a origem e o destino.
        """
        caminho = []
        atual = destino

        while atual is not None:
            caminho.append(atual)
            atual = anterior[atual]

        caminho.reverse()
        return caminho if caminho and caminho[0] == origem else []
