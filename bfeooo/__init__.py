import itertools
import networkx as nx #Agregamos import networkx as nx ya que nos aparecía un error de que no se encontraba el módulo networkx en "nx", línea 32, y es necesario para trabajar con grafos.
def is_proper_coloring(graph, coloring):
    for edge in graph.edges():
        if coloring[edge[0]] == coloring[edge[1]]:
            return False
    return True

def is_3_colorable(graph):
  n = graph.order() #numero de vertices
  colorings = itertools.product([0,1,2],repeat = n) #Agregamos itertools. a product
  for coloring in colorings:
    if is_proper_coloring(graph,coloring):
      return coloring
  return False

def is_hamiltonian_cycle(graph, cycle):
  """Check if cycle is a hamiltonian cycle in graph.
      graph is a NetworkX Graph, and cycle is list if vertices"""
  n = len(set(cycle))
  if n != graph.order():
    return False
  for i in range(n-1):
    if not graph.has_edge(cycle[i], cycle[i+1]):
      return False
    if not graph.has_edge(cycle[n-1], cycle[0]):
      return False
  return True


def is_hamiltonian(graph):
  if not nx.is_connected(graph):
    return False
  vertices = list(graph.nodes())
  if len(vertices) < 3:
    return False
  perms = itertools.permutations(vertices)
  for perm in perms:
    if is_hamiltonian_cycle(graph, perm):
      return perm
  return False