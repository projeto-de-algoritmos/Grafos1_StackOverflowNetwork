import pandas as pd
import sys


class Graph():
  def instance_graph(self, list_neighbor):
    for i in list_neighbor:
      self.edges.append(i)

  def  __init__(self, name, list_neighbor):
    self.name = name
    self.list_neighbor = [a for a in list_neighbor]



def graph_gps(file_name):
  graphs = []
  file_data = read_file(file_name)

  keys = file_data.keys()
  for i in range(len(file_data[keys[1]])):
    graphs.append(Graph(file_data[keys[0]][i], 
                        eval(file_data[keys[1]][i])))

  for i in graphs:
    print(i.name)
    print(i.list_neighbor)


def read_file(file_name):
  return pd.read_csv(file_name, delimiter=';')

if __name__ == '__main__':
  graph_gps(sys.argv[1])
