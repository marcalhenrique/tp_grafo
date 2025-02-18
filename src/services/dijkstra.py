from src.services import ReadGraph

class Dijkstra():
    def __init__(self, file_path):
        self.read_graph = ReadGraph(file_path=file_path)
        self.graph = self.read_graph.build_graph()
    
    def run(self, origem: int):
        """
        Executa o algoritmo de Dijkstra para encontrar o menor caminho a partir de um nó de origem.
        Retorna um dicionário de distâncias e um dicionário de predecessores.
        """
        distancia = {v: float('inf') for v in self.graph}
        anterior = {v: None for v in self.graph}
        distancia[origem] = 0
        
        nao_visitados = list(self.graph.keys())
        
        while nao_visitados:
            u = min(nao_visitados, key=lambda v: distancia[v])
            nao_visitados.remove(u)

            for v, custo in self.graph[u].items():
                custo_total = distancia[u] + custo
                if custo_total < distancia[v]:
                    distancia[v] = custo_total
                    anterior[v] = u
        
        return distancia, anterior
    
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

        # Se o caminho não começar pela origem, significa que não há caminho viável
        if caminho and caminho[0] == origem:
            return caminho
        else:
            return []  # Retorna lista vazia se não há caminho possível
    

        
        