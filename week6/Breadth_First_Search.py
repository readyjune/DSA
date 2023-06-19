from doublelinked import *
from BinarySearchTree import Tree
from queue import Queue
class Vertex:
	def __init__(self, n):
		self.name = n
		self.neighbors = DoublyLinkedList()
		

	
	def add_neighbor(self, v):
		if v not in self.neighbors:
			self.neighbors.insert_to_end(v)
			#self.neighbors.sort()

class Graph:

	def __init__(self):
		self.vertices = Tree()
	
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
			print(vertex.name + ': [' + str(vertex.neighbors) + ']')

#		for key in sorted(list(self.vertices.keys())):
#			print(key + str(self.vertices[key].neighbors) + "  " + str(self.vertices[key].distance))
		
	def bfs(self, vert):
		q = Queue() #adjacency vertex or place to go next
		visited = Tree()
		T = DoublyLinkedList()
		T.insert_to_end(vert.name)
		q.append(vert)
		visited[vert.name] = True

		while not q.is_empty():
			u = q.pop()
			
			for v in u.neighbors:
				v_node = self.vertices[v]
#				if not v_node.name in visited:  doublelinked
				if not v_node.name in T:
					T.insert_to_end(v_node.name)
					q.append(v_node)
#					visited[v_node.name] = True

		return T

if __name__== "__main__":
					
	g = Graph()
	a = Vertex('A')
	g.add_vertex(a)
	g.add_vertex(Vertex('B'))
	for i in range(ord('A'), ord('K')):
		g.add_vertex(Vertex(chr(i)))

	edges = ['AB', 'AD', 'BC', 'DE', 'DF', 'EG', 'FH', 'GH']
	for edge in edges:
		g.add_edge(edge[:1], edge[1:])
	
	print(g.bfs(a))
	print("Graph:")
	g.print_graph()
