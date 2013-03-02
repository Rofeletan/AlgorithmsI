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

def depth_first_search(graph, vertice, leader, do_finish):
  global finish
  global orderedvertices
  
  stack = []  
  stack.append(vertice)
  
  while stack:
    # print 'Stack: '
    # for vertice in stack:
      # print vertice.label
    # print '\n' 
    current_vertice = stack.pop()
    # print 'Popping Vertice: ', current_vertice.label, '\n'    
    
    current_vertice.explored = True
    current_vertice.leader = leader
    
    unexplored_edges = []
    for edge in current_vertice.edges:        
      if not graph[edge].explored:
        unexplored_edges.append(graph[edge])
    
    #print 'Unexplored: ', len(unexplored_edges), " ", unexplored_edges, '\n'
    
    if unexplored_edges:
      stack.append(current_vertice)
      stack += unexplored_edges
      
    elif do_finish and current_vertice.finish == None :
      finish += 1
      current_vertice.finish = finish
      # print 'Finish', finish
      orderedvertices[finish - 1] = current_vertice
      
  
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
    if not parts[1] in graph:
      graph[parts[1]] = Vertice(parts[1], [])
  else:
    graph[parts[0]] = Vertice(parts[0], [parts[1]])
    if not parts[1] in graph:
      graph[parts[1]] = Vertice(parts[1], [])

  if parts[1] in reversegraph:
    reversegraph[parts[1]].edges.append(parts[0])
    if not parts[0] in reversegraph:
      reversegraph[parts[0]] = Vertice(parts[0], [])
  else:
    reversegraph[parts[1]] = Vertice(parts[1], [parts[0]])
    if not parts[0] in reversegraph:
      reversegraph[parts[0]] = Vertice(parts[0], [])

# print 'Graph:\n'
# for vertice in graph:
  # print vertice, 'edges: ' , graph[vertice].edges
  
# print '\nReversed:\n'
# for vertice in reversegraph:
  # print vertice, 'edges: ' , reversegraph[vertice].edges
  
finish = 0
orderedvertices = [None] * len(graph)

for vertice in reversegraph:
  if not reversegraph[vertice].explored:  
    depth_first_search(reversegraph, reversegraph[vertice], reversegraph[vertice], True)

# print 'Graph:\n'
# for vertice in orderedvertices:
  # print vertice.label, 'edges: ' , vertice.edges, ' Leader: ', vertice.leader.label, ' Finish: ', vertice.finish

for rev_vertice in orderedvertices[::-1]:
  vertice = graph[rev_vertice.label]
  if not vertice.explored:
    depth_first_search(graph, vertice, vertice, False)

    
# print 'Graph:\n'
# for vertice in graph:
  # print vertice, 'edges: ' , graph[vertice].edges, ' Leader: ', graph[vertice].leader.label

  
scc = dict() 
for vertice in graph:
  if graph[vertice].leader.label in scc:
    scc[graph[vertice].leader.label] = scc[graph[vertice].leader.label] + 1
  else:
    scc[graph[vertice].leader.label] = 1
    
# for leader in scc:
  # print leader, 'Count: ' , scc[leader]

counts = scc.values()
counts.sort()

print counts[-5:]