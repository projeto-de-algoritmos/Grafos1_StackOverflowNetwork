class Graph():
  def  init(self, name, list_neighbor):
    self.name = name
    self.list_neighbor = [a for a in list_neighbor]

  def bfs(self, verticie, graph):
    visited = {}
    for a in graph:
      visited[a.name] = False

    queue = []

    queue.append(verticie)
    visited[verticie] = True
    while queue:
      verticie = queue.pop()
      print (verticie, end = " ")
      for i in find_graph(graph, verticie):
        if visited[i] == False:
          queue.append(i)
          visited[i] == True

def find_graph(graphs, verticie):
  for i in graphs:
    if i.name == verticie:
      return i.list_neighbor

