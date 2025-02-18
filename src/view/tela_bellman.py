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
        st.write("O algoritmo de Bellman-Ford encontra o caminho mais curto de um vértice para todos os outros em um grafo ponderado, mesmo com pesos negativos. Ele também detecta ciclos negativos.")

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