import streamlit as st
from src.view.tela_dijkstra import ViewDijkstra
from src.view.tela_bellman import ViewBellmanFord
from src.view.tela_sobre import ViewSobre

class ViewHome():
    def __init__(self) -> None:
        self.view_dijkstra = ViewDijkstra()
        self.view_bellman = ViewBellmanFord()
        self.view_sobre = ViewSobre()
    
    
    def home(self)-> None:
        
        st.sidebar.title("Menu")
        pagina = st.sidebar.selectbox("Selecione a página", ["Home", "Dijkstra", "Bellman-Ford", "Sobre"])
        
        if pagina == "Home":
            st.title("Algoritmos de Caminho Mínimo")
            st.write("Escolha um algoritmo no menu laterla para visualizar seu funcionamento.")
        elif pagina == "Dijkstra":
            self.view_dijkstra.dijkstra()
        elif pagina == "Bellman-Ford":
            self.view_bellman.bellman_ford()
        elif pagina == "Sobre":
            self.view_sobre.sobre()
            
                

        