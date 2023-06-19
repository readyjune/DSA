
from doublelinked import *
from BinarySearchTree import Tree


class Graph:
	def __init__(self, Nodes):
		self.nodes = Nodes
		self.adj_list = Tree()

		for node in self.nodes:
			self.adj_list[node] = []

	def add_edge(self, u, v):
		self.adj_list[u].append(v)
		self.adj_list[v].append(u)


		#how many adjaceny node
	def degree(self,node):
		deg = len(self.adj_list[node])
		return deg

	def print_adj_list(self):
		for node in self.nodes:
			print(node, "->", self.adj_list[node])

if __name__ == "__main__":
	#List = DoublyLinkedList()
	#List.insert_in_emptylist("A")
	#List.insert_to_end("B")
	#List.insert_to_end("C")

	#n = List.start_node	
	#while n is not None:
	#	print(n.item)

	#	n= n.next

	#print("\n")


	nodes = ["A", "B", "C", "D", "E"]
	graph = Graph(nodes)

	all_edges = [("A","B"),("A","C"),("B","D"),("C","D"),("C","E"),("D","E")]
	for u,v in all_edges:
		graph.add_edge(u,v)

	graph.print_adj_list()

	print("Degree of C", graph.degree("C"))
