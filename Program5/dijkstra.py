#! /usr/bin/env python
import argparse
import sys
from heapq import *

parser = argparse.ArgumentParser()
parser.add_argument("file")
parser.parse_args()
args = parser.parse_args()
file = open(args.file)

graph = dict()

for line in file.readlines():
  parts = line.split()
  if not parts[0] in graph:
    graph[parts[0]] = dict()
  for edge in parts[1:]:
    split = edge.split(',')
    graph[parts[0]][split[0]] = int(split[1])
    if not split[0] in graph:
      graph[split[0]] = dict()
      graph[split[0]][parts[0]] = int(split[1])

# print 'Graph:'
# for vertice in graph:
  # print vertice, ':', graph[vertice]

# print '\n'
paths = dict()
processed = []

start = '1'

heap = [];
heappush(heap, (0, '1', '1'))


while heap:
  # print '\n'
  # print heap
  # print paths
  
  current = heappop(heap)
  # print 'Popping: ', current[1]
  if not current[1] in processed:
    processed.append(current[1])
    paths[current[1]] = current[0]
    
    for edge in graph[current[1]]:      
      heappush(heap, (paths[current[1]] + graph[current[1]][edge], edge, current[1]))
      

      
# print '\n', 'Paths:'
# for vertice in sorted(paths.iterkeys()):
  # print vertice, ':', paths[vertice]
  
print '7', ':', paths['7']
print '37', ':', paths['37']
print '59', ':', paths['59']
print '82', ':', paths['82']
print '99', ':', paths['99']
print '115', ':', paths['115']
print '133', ':', paths['133']
print '165', ':', paths['165']
print '188', ':', paths['188']
print '197', ':', paths['197']