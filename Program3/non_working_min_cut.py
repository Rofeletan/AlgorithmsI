#! /usr/bin/env python
import argparse
import re
from random import randrange

parser = argparse.ArgumentParser()
parser.add_argument("file")
parser.parse_args()
args = parser.parse_args()
file = open(args.file)

vertices = []
edges = []
for line in file.readlines():
  parts = line.split()
  vertice = [parts[0], parts[1:]]
  vertices.append(vertice)
  for edge in parts[1:]:
    edges.append([parts[0],edge])
  

#for vertice in vertices:
#  print vertice
  
#print '\n'

#for edge in edges:
#  print edge
  
#print '\n'

  
while len(vertices) > 2:
  edge = edges[randrange(len(edges))]
  #print edge 
  #print '\n'
  
  vertice1 = None
  vertice2 = None
  for vertice in vertices:
    if vertice[0] == edge[0]:
      vertice1 = vertice
    if vertice[0] == edge[1]:
      vertice2 = vertice
  
  if vertice2[0] in vertice1[1]:
    vertice1[1].remove(vertice2[0])
  if vertice1[0] in vertice2[1]:
    vertice2[1].remove(vertice1[0])
  
  if [vertice1[0], vertice2[0]] in edges:
    edges.remove([vertice1[0], vertice2[0]])
  if [vertice2[0], vertice1[0]] in edges:
    edges.remove([vertice2[0], vertice1[0]])
	
  for edge in vertice2[1]:
    if edge not in vertice1[1]:
      vertice1[1].append(edge)
      if [vertice2[0], edge] in edges:
        edges.remove([vertice2[0], edge])
      edges.append([vertice1[0], edge])
  
  vertices.remove(vertice2)
  
  for vertice in vertices:
      vertice[1] = [x.replace(vertice2[0], vertice1[0]) for x in vertice[1]]
      if vertice[0] in vertice[1]:
        vertice[1].remove(vertice[0])
  
  for edge in edges:
    if (edge[0] == vertice2[0]):
      edge[0] = vertice1[0]
    if (edge[1] == vertice2[0]):
      edge[1] = vertice1[0]   
  
  edges = [value for value in edges if value[0] != value[1]]
  
for vertice in vertices:
  print vertice
  
print '\n'

for edge in edges:
  print edge  
  
print '\n'