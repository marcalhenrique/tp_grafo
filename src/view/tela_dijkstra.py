import streamlit as st
import time
from src.services.read_graph import ReadGraph
from src.services.dijkstra import Dijkstra
from src.services.graph_service import GraphService

class ViewDijkstra():
    def __init__(self):
        self.file_path = "data/grafo_roteadores.csv"
        self.graph_image = "data/images/grafo_roteadores.png"
        self.graph_data = ReadGraph(self.file_path).build_graph()
        self.graph_service = GraphService(self.graph_data)

    def dijkstra(self):
        st.title("Algoritmo de Dijkstra")
        st.subheader("Passo a Passo do Algoritmo")
        st.markdown("""
        1. **Inicialização:**
        - `distancia[origem] = 0`: A distância da origem para ela mesma é zero.
        - `nao_visitados`: Contém todos os nós do grafo.

        2. **Loop Principal:**
        - Enquanto houver nós não visitados:
            1. **Escolha do nó atual (`u`):**
                - Seleciona o nó não visitado com a menor distância conhecida (`min(nao_visitados, key=lambda v: distancia[v])`).
            2. **Remoção do nó atual:**
                - Remove o nó `u` da lista de nós não visitados.
            3. **Atualização das distâncias:**
                - Para cada vizinho `v` do nó `u`, calcula a distância total (`custo_total = distancia[u] + custo`).
                - Se `custo_total` for menor que a distância atual de `v`, atualiza `distancia[v]` e define `anterior[v] = u`.
        """)

        # Explicação da função `menor_caminho`
        st.header("2. Função `menor_caminho`")
        st.markdown("""
        A função `menor_caminho` reconstrói o caminho mais curto entre a **origem** e o **destino** usando o dicionário `anterior`.
        """)

        st.subheader("Passo a Passo da Função")
        st.markdown("""
        1. **Inicialização:**
        - `caminho`: Uma lista vazia para armazenar o caminho.
        - `atual`: Começa no nó de destino.

        2. **Reconstrução do caminho:**
        - Enquanto `atual` não for `None`, adiciona `atual` ao `caminho` e move para o nó anterior (`atual = anterior[atual]`).
        - No final, inverte a lista `caminho` para obter a ordem correta.

        3. **Verificação:**
        - Se o caminho começa na origem (`caminho[0] == origem`), retorna o caminho.
        - Caso contrário, retorna uma lista vazia, indicando que não há caminho possível.
        """)

        # Comparações e Operações
        st.header("3. Comparações e Operações")
        st.markdown("""
        - **Comparação de distâncias:**
        - O algoritmo compara constantemente as distâncias para determinar o nó com a menor distância atual (`min(nao_visitados, key=lambda v: distancia[v])`).
        - Também compara `custo_total` com `distancia[v]` para decidir se uma atualização é necessária.

        - **Atualizações:**
        - As distâncias e os nós anteriores são atualizados sempre que um caminho mais curto é encontrado.
        """)
        st.image(self.graph_image, caption="Algoritmo de Dijkstra", use_container_width=True)
        
        origem = st.number_input("Origem", min_value=1, max_value=10, step=1)
        destino = st.number_input("Destino", min_value=1, max_value=10, step=1)
        
        if st.button("Calcular Caminho"):
            start_time = time.time()
            dijkstra = Dijkstra(self.file_path)
            distancia, anterior = dijkstra.run(origem)
            caminho = dijkstra.menor_caminho(anterior, origem, destino)
            exec_time = time.time() - start_time
            
            if caminho:
                st.success(f"Caminho encontrado: {caminho}")
                st.info(f"Custo total: {distancia[destino]}")
                st.info(f"Tempo de execução: {exec_time:.6f} segundos")
                
                gif_filename = self.graph_service.generate_gif(caminho)
                st.image(gif_filename, caption="Execução do Algoritmo")
            else:
                st.error("Não há caminho entre os nós selecionados.")
