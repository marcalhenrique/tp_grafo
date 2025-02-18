import networkx as nx
import matplotlib.pyplot as plt
from PIL import Image
import os

class GraphService:
    def __init__(self, graph_data):
        self.graph = self._build_graph(graph_data)
        self.pos = nx.circular_layout(self.graph)

    def _build_graph(self, graph_data):
        G = nx.DiGraph()
        for node, edges in graph_data.items():
            for neighbor, weight in edges.items():
                G.add_edge(node, neighbor, weight=weight)
        return G

    def plot_graph(self, path=None, filename='data/graph.png'):
        labels = nx.get_edge_attributes(self.graph, 'weight')
        plt.clf()
        plt.figure(figsize=(8, 6))
        nx.draw(self.graph, self.pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=10)
        nx.draw_networkx_edge_labels(self.graph, self.pos, edge_labels=labels)

        if path:
            edges = list(zip(path, path[1:]))
            nx.draw_networkx_edges(self.graph, self.pos, edgelist=edges, edge_color='red', width=2, arrowstyle='->', arrowsize=15)

        plt.savefig(filename)
        plt.close()
        return filename

    def generate_gif(self, path, filename='data/images/caminho_dijkstra.gif'):
        frames = []
        for i in range(len(path)):
            img_filename = f'frame_{i}.png'
            self.plot_graph(path[:i+1], img_filename)
            frames.append(Image.open(img_filename))

        frames[0].save(
            filename,
            save_all=True,
            append_images=frames[1:],
            duration=1000,
            loop=0
        )

        for i in range(len(path)):
            os.remove(f'frame_{i}.png')

        return filename
