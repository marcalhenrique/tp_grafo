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
        st.write("O algoritmo de Dijkstra é um algoritmo de caminho mínimo que encontra o caminho mais curto entre dois nós em um grafo ponderado.")
        st.write("Alguma coisa")
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
