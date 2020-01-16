from typing import Hashable, List
import networkx as nx


def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
	"""
	Do an depth-first search and returns list of nodes in the visited order

	:param g: input graph
	:param start_node: starting node of search
	:return: list of nodes in the visited order
	"""
	print(g, start_node)
	return list(g.nodes)

def dfs_find( graph,src,dst,visited):
	visited[src] = True
	if src == dst: #src -откуда мы начинаем dst -куда мы хотим доити
		return True


	for node in graph.adj[src]:
		if not visited[node]:
			if dfs_find(graph,node,dst,visited):
				return True
	return False



if __name__=="__main__":
	graph = nx.Graph()
	graph.add_nodes_from("ABCDEFG")
	graph.add_edges_from(
		[("A", "B"),
		 ("A", "C"),
		 ("B", "D"),
		 ("B", "E"),
		 ("C", "F"),
		 ("E", "G"),]
	)
	graph.add_node("Z")
	src = "A"
	dst = "Z"

	visited = {node: False for node in graph.nodes()}
	print(dfs_find(graph,src,dst,visited))