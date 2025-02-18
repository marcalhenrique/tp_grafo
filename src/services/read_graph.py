import pandas as pd

class ReadGraph():
    def __init__(self, file_path):
        self.file_path = file_path
        if not self.file_path.endswith('.csv'):
            raise ValueError('File must be a .csv file')
        
    def read_csv(self) -> pd.DataFrame:
        return pd.read_csv(self.file_path)
    
    def build_graph(self):
        graph_df = self.read_csv()
        graph = {}

        for _, row in graph_df.iterrows():
            origem, destino, custo = int(row['origem']), int(row['destino']), int(row['custo'])
            
            if origem not in graph:
                graph[origem] = {}
            if destino not in graph:
                graph[destino] = {}

            graph[origem][destino] = custo  # Adiciona o caminho origem -> destino
            # Se for um grafo não-direcionado, adicione também o caminho destino -> origem
            graph[destino][origem] = custo 

        return graph