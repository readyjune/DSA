from doublelinked import *
from BinarySearchTree import Tree

class Vertex:
	def __init__(self, n):
		self.name = n
		self.neighbors = DoublyLinkedList()
		
		self.discovery = 0
		self.finish = 0
		self.color = 'black'
	
	def add_neighbor(self, v):
		if v not in self.neighbors:
			self.neighbors.insert_to_end(v)
		#	self.neighbors.sort()

class Graph:
	vertices = Tree()
	time = 0
	
	def add_vertex(self, vertex):
		if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
			self.vertices[vertex.name] = vertex
			return True
		else:
			return False
	
	def add_edge(self, u, v):
		if u in self.vertices and v in self.vertices:
			self.vertices[u].add_neighbor(v)
			self.vertices[v].add_neighbor(u)
			return True
		else:
			return False
			
	def print_graph(self):
		for vertex in self.vertices.inorder():
			print(vertex.name + str(vertex.neighbors))


	def _dfs(self, vertex):
		global time
		vertex.color = 'red'
		vertex.discovery = time
		time += 1
		for v in vertex.neighbors:
			if self.vertices[v].color == 'black':
				self._dfs(self.vertices[v])
		vertex.color = 'blue'
		vertex.finish = time
		time += 1
		
	def dfs(self, vertex):
		global time
		time = 1
		self._dfs(vertex)

if __name__=="__main__":
			
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
		
	g.dfs(a)
	g.print_graph()

