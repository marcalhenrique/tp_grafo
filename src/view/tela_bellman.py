import streamlit as st
import time
from src.services.read_graph import ReadGraph
from src.services.bellman import BellmanFord
from src.services.graph_service import GraphService

class ViewBellmanFord():
    def __init__(self):
        self.file_path = "data/grafo_roteadores.csv"
        self.graph_image = "data/images/grafo_roteadores.png"
        self.graph_data = ReadGraph(self.file_path).build_graph()
        self.graph_service = GraphService(self.graph_data)

    def bellman_ford(self):
        st.title("Algoritmo de Bellman-Ford")
        
        st.subheader("Passo a Passo do Algoritmo")
        st.markdown("""
        1. **Inicialização:**
        - `distancia[origem] = 0`: A distância da origem para ela mesma é zero.
        - `anterior`: Todos os valores são inicializados como `None`.

        2. **Relaxamento das Arestas:**
        - O algoritmo realiza o relaxamento das arestas **|V| - 1** vezes, onde |V| é o número de nós no grafo.
        - Para cada aresta `(u, v)` com peso `custo`, ele verifica se a distância de `u` até `v` pode ser melhorada:
            ```python
            if distancia[u] + custo < distancia[v]:
                distancia[v] = distancia[u] + custo
                anterior[v] = u
            ```

        3. **Verificação de Ciclos Negativos:**
        - Após o relaxamento, o algoritmo verifica se ainda é possível melhorar alguma distância. Se sim, isso indica a presença de um **ciclo negativo**.
        - Se um ciclo negativo for detectado, o algoritmo retorna `None, None, True`.

        4. **Resultado:**
        - Se não houver ciclos negativos, o algoritmo retorna os dicionários `distancia` e `anterior`, além de `False` para indicar a ausência de ciclos negativos.
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
        - **Relaxamento:**
        - O algoritmo compara constantemente as distâncias para determinar se uma aresta pode ser relaxada (`distancia[u] + custo < distancia[v]`).
        - Essa operação é realizada **|V| - 1** vezes para garantir que todas as distâncias mínimas sejam encontradas.

        - **Detecção de Ciclos Negativos:**
        - Após o relaxamento, o algoritmo verifica se ainda é possível melhorar alguma distância. Se sim, isso indica a presença de um ciclo negativo.
        """)

        st.image(self.graph_image, caption="Algoritmo de Bellman-Ford", use_container_width=True)

        origem = st.number_input("Origem", min_value=1, max_value=10, step=1)
        destino = st.number_input("Destino", min_value=1, max_value=10, step=1)

        if st.button("Calcular Caminho"):
            start_time = time.time()
            bellman_ford = BellmanFord(self.graph_data)
            distancia, anterior, ciclo_negativo = bellman_ford.run(origem)
            exec_time = time.time() - start_time

            if ciclo_negativo:
                st.error("Ciclo negativo detectado! O algoritmo não pode calcular caminhos.")
            elif distancia and anterior:
                caminho = bellman_ford.menor_caminho(anterior, origem, destino)
                if caminho:
                    st.success(f"Caminho encontrado: {caminho}")
                    st.info(f"Custo total: {distancia[destino]}")
                    st.info(f"Tempo de execução: {exec_time:.6f} segundos")

                    gif_filename = self.graph_service.generate_gif(caminho)
                    st.image(gif_filename, caption="Execução do Algoritmo")
                else:
                    st.error("Não há caminho entre os nós selecionados.")