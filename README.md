# Otimização por Colônia de Formigas para o Roteamento em Redes de Computadores

## Resumo do Artigo
O Problema do Caminho Mínimo em Roteamento de Redes de Computadores (PCMRRC) pode ser aplicado em diversas situações práticas, tal como na topologia de redes computacionais. Tal problema apresenta alta complexidade computacional, sendo a Computação Natural uma técnica alternativa interessante na solução deste tipo de problema. Este trabalho trata o PCMRRC através da Otimização por Colônia de Formigas, a qual é uma das técnicas de Computação Natural mais eficiente para problemas de roteamento. Os resultados encontrados são satisfatórios e motivam mais pesquisas e aprimoramentos do algoritmo.

## Alocando o Problema
Embora o artigo tenha utilizado técnicas de Ant Colony Optimization (ACO) para encontrar o menor caminho, este projeto traz uma abordagem alternativa, implementando os algoritmos **Dijkstra** e **Bellman-Ford** para a solução do problema proposto. Essa escolha visa explorar a eficiência e robustez desses algoritmos clássicos em diferentes cenários de redes.

## Algoritmos Implementados

### Dijkstra
- **Funcionamento**: Encontra o caminho mínimo em grafos com pesos **não negativos**.
- **Complexidade**: O((V + E) log V), onde V é o número de vértices e E é o número de arestas.
- **Vantagens**: Eficiente para grafos com pesos não negativos e de tamanho moderado.

### Bellman-Ford
- **Funcionamento**: Encontra o caminho mínimo em grafos com pesos **positivos ou negativos** e detecta ciclos negativos.
- **Complexidade**: O(V * E), onde V é o número de vértices e E é o número de arestas.
- **Vantagens**: Pode lidar com pesos negativos e detectar ciclos negativos.

## Objetivo
Repositório criado para expor o código-fonte de uma interface criada com a finalidade de:
1. **Implementar e comparar** os algoritmos de Dijkstra e Bellman-Ford para resolver o Problema do Caminho Mínimo em Roteamento de Redes de Computadores.
2. **Fornecer uma interface interativa** para visualização e análise dos resultados obtidos pelos algoritmos.
3. **Facilitar a compreensão** do funcionamento desses algoritmos por meio de exemplos práticos e explicações detalhadas.
