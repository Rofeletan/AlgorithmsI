#! /usr/bin/env python
import argparse
import sys


class Vertice:
  def __init__(self, label, edges):
    self.explored = False
    self.label = label
    self.edges = edges
    self.leader = None
    self.finish = None

def depth_first_search(graph, vertice, leader, finish):
  print '\nExploring Vertice: ', vertice.label, '\n'
  vertice.explored = True
  vertice.leader = leader
  for edge in vertice.edges:
    if not graph[edge].explored:
      depth_first_search(graph, graph[edge], leader, finish)
  finish += 1
  vertice.finish = finish
  
parser = argparse.ArgumentParser()
parser.add_argument("file")
parser.parse_args()
args = parser.parse_args()
file = open(args.file)


graph = dict()
reversegraph = dict()

for line in file.readlines():
  parts = line.split()
  if parts[0] in graph:
    graph[parts[0]].edges.append(parts[1])
  else:
    graph[parts[0]] = Vertice(parts[0], [parts[1]])

  if parts[1] in reversegraph:
    reversegraph[parts[1]].edges.append(parts[0])
  else:
    reversegraph[parts[1]] = Vertice(parts[1], [parts[0]])

# print 'Graph:\n'
# for vertice in graph:
  # print vertice, 'edges: ' , graph[vertice].edges
  
# print '\nReversed:\n'
# for vertice in reversegraph:
  # print vertice, 'edges: ' , reversegraph[vertice].edges
  
for vertice in graph:
  if not graph[vertice].explored:  
    depth_first_search(graph, graph[vertice], graph[vertice])

print 'Graph:\n'
for vertice in graph:
  print vertice, 'edges: ' , graph[vertice].edges, ' Leader: ', graph[vertice].leader.label, ' Finish: ' graph[vertice].leader.finish