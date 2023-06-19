# implementation of an undirected graph using Adjacency Listsi
from doublelinked import *
from BinarySearchTree import Tree


class Vertex:
	def __init__(self, n):
		self.name = n
		self.neighbors = DoublyLinkedList()

		self.distance = 9999
		self.color = 'black'

	def add_neighbor(self, v, weight):
		if v not in self.neighbors:
			self.neighbors.insert_to_end((v, weight))
			#self.neighbors.sort()

class Graph:
	vertices = Tree()

	def __init__(self):
		self.start_node = None

	def add_vertex(self, vertex):
		if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
			self.vertices[vertex.name] = vertex
			return True
		else:
			return False


	def add_edge(self, u, v, weight=0):
		print(f"adding neighbor {u} to {v}")
		print(f"contains is: {u in self.vertices}")
		if u in self.vertices and v in self.vertices:
			for key, value in self.vertices.neighbors():
				if key == u:
					self.vertices[u].add_neighbor(v, weight)
				if key == v:
					self.vertices[v].add_neighbor(u, weight)
			return True
		else:
			return False

	def print_graph(self):
		for vertex in self.vertices.inorder():
			print(vertex.name + str(vertex.neighbors))

	
	def bfs(self, vert):
		q = DoublyLinkedList()
		vert.distance = 0
		vert.color = 'red'
		for v in vert.neighbors:
			self.vertices[v].distance = vert.distance + 1
			q.append(v)

		while len(q) > 0:
			u = q.pop(0)
			node_u = self.vertices[u]
			node_u.color = 'red'

			for v in node_u.neighbors:
				node_v = self.vertices[v]
				if node_v.color == 'black':
					q.append(v)
					if node_v.distsance > node.u.distance + 1:
						node_v.distance = node_u.distance + 1


if __name__ == "__main__":
	g = Graph()
	# print(str(len(g.vertices)))
	a = Vertex('A')
	g.add_vertex(a)
	g.add_vertex(Vertex('B'))
	for i in range(ord('A'), ord('K')):
		g.add_vertex(Vertex(chr(i)))
	edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
	for edge in edges:
		g.add_edge(edge[:1], edge[1:])
	g.bfs(a)
	g.print_graph()


#addVertex(label)   ###
#addEdge(labe1, label2)   ###
#hasVertex(label):boolean
#getVertexCOunt():int
#getEdgeCount():int
#isAdjacent(label, label2):boolean
#getAdjacent(label):vertexList
#displayAsList()
#displayAsMatrix()
