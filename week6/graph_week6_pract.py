# implementation of an undirected graph using Adjacency Listsi
from doublelinked import *
from BinarySearchTree import Tree
from queue import Queue
from stack import Stack

class Vertex:
	def __init__(self, n):
		self.name = n
		self.neighbors = DoublyLinkedList()



	def add_neighbor(self, v, weight):
		if v not in self.neighbors:
			self.neighbors.insert_to_end((v, weight))
			print('hello')
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


	def add_edge(self, u, v, weight):
	#	print(f'Adding "{u}" to "{v}"')
		if u in self.vertices and v in self.vertices:
			print('='*80)
			print(u)
			print(v)
			self.vertices[u].add_neighbor(v, weight)
			self.vertices[v].add_neighbor(u, weight)
			return True
		else:
			return False



	def print_graph(self):
		for vertex in self.vertices.inorder():
			print(vertex.name + ': [' + str(vertex.neighbors) + ']')




	def read_file(self, filename):
		with open(filename, 'r') as f:
			for line in f:
				items = line.strip().split(' ')
				node_a = items[0]
				node_b = items[1]
				node_c = items[2]
				self.add_edge(node_a, node_b, node_c)




	def bfs(self, vert):
		q = Queue() #adjacency vertex or place to go next
		#visited = Tree()
		T = DoublyLinkedList()
		T.insert_to_end(vert.name)
		q.append(vert)
#		visited[vert.name] = True


		while not q.is_empty():
			u = q.pop()
			
			for v in u.neighbors:
				v_node = self.vertices[v[0]]
		#		if not v_node.name in visited:  #doublelinked
				if not v_node.name in T:
					T.insert_to_end(v_node.name)
					q.append(v_node)
				#	visited[v_node.name] = True

		return T

	def dfs(self, vert):

	#	print("first line of dfs and neighbors is \n")
	#	print(vert.neighbors)
		s = Stack() #adjacency vertex or place to go next
	#	visited = Tree()
		T = DoublyLinkedList()
		T.insert_to_end(vert.name)
		s.append(vert)
		u = vert
		v = vert
		while not s.is_empty():
	#		print(f'1.the u name is {u.name} & neighbors is {u.neighbors}')

			while v:	
				v = None

				for current in u.neighbors:
					if current[0] not in T:
						v = current
				#		print('this is v')
				#		print(v)

				if v:
					v_node = self.vertices[v[0]]
				#	print(';aslfkjsa;flksaj')
				#	print(v_node)
					T.insert_to_end(v_node.name)
					s.append(v_node)
					u = v_node

			u = s.pop()
			v = u
			#print('back tracking u')
			#print(u.name)

		return T






if __name__ == "__main__":
	g = Graph()
	a = Vertex('A')
	print(g.add_vertex(a))
	print(g.add_vertex(Vertex('B')))
	for i in range(ord('A'), ord('K')):
		print(g.add_vertex(Vertex(chr(i))))

	g.read_file('first.txt')

	print("Breadth-First-Search")
	print(g.bfs(a))
	print("\n")
	print("Depth-First-Search")
	print(g.dfs(a))
	print("\n")

	print("Graph!")
	g.print_graph()

#	print(type(a.neighbors))





#addVertex(label)   ###
#addEdge(labe1, label2)   ###
#hasVertex(label):boolean
#getVertexCOunt():int
#getEdgeCount():int
#isAdjacent(label, label2):boolean
#getAdjacent(label):vertexList
#displayAsList()
#displayAsMatrix()
