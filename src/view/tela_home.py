import streamlit as st
from src.view.tela_dijkstra import ViewDijkstra
from src.view.tela_bellman import ViewBellmanFord
from src.view.tela_sobre import ViewSobre


class ViewHome():
    def __init__(self) -> None:
        self.view_dijkstra = ViewDijkstra()
        self.view_bellman = ViewBellmanFord()
        self.view_sobre = ViewSobre()

    def home(self) -> None:
        st.sidebar.title("Menu")
        pagina = st.sidebar.selectbox("Selecione a página", ["Home", "Dijkstra", "Bellman-Ford", "Sobre"])

        if pagina == "Home":
            st.title("Algoritmos de Roteamento em Redes de Computadores")

            st.header("Contexto e Motivação")
            st.write("""
            De acordo com o artigo "Otimização por Colônia de Formigas para o Roteamento em Redes de Computadores", foram realizados estudos para calcular a minimização de caminhos em uma rede de roteadores. 
            Embora o artigo tenha utilizado técnicas de Ant Colony Optimization (ACO) para encontrar o menor caminho, este projeto traz uma abordagem alternativa, implementando os algoritmos Dijkstra e Bellman-Ford para a solução do problema proposto. 
            Essa escolha visa explorar a eficiência e robustez desses algoritmos clássicos em diferentes cenários de redes.
            """)

            st.header("Metodologia")
            with st.expander("Algoritmo de Dijkstra"):
                st.write("""
                O algoritmo de Djikstra é um método eficiente para encontrar o caminho mais curto entre um nó de origem e todos os outros nós em um grafo, desde que as arestas tenham 
                pesos não negativos. Ele é amplamente utilizado em redes de computadores, sistemas de navegação e problemas de otimização.
                """)
                st.title("Passos do Algoritmo")

                st.write("""
                Inicialização:
                                    
                Defina a distância do nó de origem como 0 e a de todos os outros nós como infinita (∞).
                Crie um conjunto de nós não visitados.
                Seleção do Nó Atual:

                Escolha o nó com a menor distância provisória do conjunto de não visitados. Inicialmente, esse será o nó de origem.
                Atualização das Distâncias:

                Para cada nó vizinho do nó atual:
                Calcule a distância total até esse vizinho passando pelo nó atual.
                Se essa distância calculada for menor que a distância atualmente registrada, atualize-a.
                Marcação do Nó como Visitado:

                Depois de considerar todos os vizinhos do nó atual, marque-o como visitado. Um nó visitado não será verificado novamente.
                Repetição:

                Repita os passos 2 a 4 até que todos os nós tenham sido visitados ou que o caminho mais curto para o destino tenha sido determinado.""")

            with st.expander("Algoritmo de Bellman-Ford"):
                st.write("""
                O algoritmo de Bellman-Ford é utilizado para encontrar o caminho mais curto de um nó de origem para todos os outros nós em um grafo.
                 Diferente do algoritmo de Dijkstra, ele pode lidar com pesos negativos nas arestas e ainda pode detectar ciclos de peso negativo, que são ciclos cujo custo total diminui indefinidamente.
                """)
                st.title("Passos do Algoritmo")

                st.write("""
                    Inicialização:

                    Defina a distância do nó de origem como 0 e de todos os outros nós como infinita (∞).
                    Relaxamento das Arestas (Repetição):

                    Para cada nó do grafo, repita (V-1) vezes (V = número de vértices):
                         

                    Para cada aresta (u, v) com peso w, atualize a distância para o nó v se:
                         

                    [Distância(v) > Distância(u) + w]
                         

                    Se for verdadeiro, defina:
                         

                    [Distância(v) = Distância(u) + w]
                         

                    Verificação de Ciclos Negativos:

                    Faça uma última varredura em todas as arestas.
                    Se ainda for possível atualizar alguma distância, o grafo contém um ciclo negativo, e o algoritmo indicará a sua existência.
                    .""")

            st.header("Resultados Obtidos")
            st.write("""
            Os testes demonstraram eficácia na identificação da rota ótima:
            - **Dijkstra:** Maior eficiência sem pesos negativos.
            - **Bellman-Ford:** Robusto em cenários complexos.
            """)

            st.write("-" * 120)
            st.write("Escolha um algoritmo no menu lateral para visualizar seu funcionamento.")

        elif pagina == "Dijkstra":
            self.view_dijkstra.dijkstra()

        elif pagina == "Bellman-Ford":
            self.view_bellman.bellman_ford()

        elif pagina == "Sobre":
            self.view_sobre.sobre()
