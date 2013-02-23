#! /usr/bin/env python
import argparse
import sys
from random import randrange

def create_edge_list(vertices):
	edges = []
	for vertice in vertices:
		for edge in vertice[1]:
			edges.append([vertice[0],edge])
			
	return edges
	
def min_cut(vertices):
	while len(vertices) > 2:	
		#Print Vertices
		# for vertice in vertices:
			# print vertice  
		# print '\n'
		
		#Create the list of edges fresh
		edges = create_edge_list(vertices)
		
		#Print Edges
		# for edge in edges:
		  # print edge		  
		# print '\n'
		
		#Pick edge at random to contract
		edge = edges[randrange(len(edges))]
		# print edge 
		# print '\n'
		
		#Create new vertice list
		new_vertices = []
		
		
		#Pull out the vertices to contract and add the others to the new list
		vertice1 = None
		vertice2 = None
		for vertice in vertices:
			if vertice[0] == edge[0]:
				vertice1 = vertice
			elif vertice[0] == edge[1]:
				vertice2 = vertice
			else:
				new_vertices.append(vertice)
		
		#Print vertices to contract
		# print vertice1
		# print vertice2
		# print '\n'
		
		#Combine edge list
		vertice1[1] = vertice1[1] + vertice2[1]
		
		#Remove any self edges
		for edge in vertice1[1][:]:
			if edge == vertice1[0]:
				vertice1[1].remove(edge)
			if edge == vertice2[0]:
				vertice1[1].remove(edge)
		
		
		#Create a new vertex label
		new_vertice_label = vertice1[0] + vertice2[0]
		
		#Update existing vertice edges to point to new vertex
		for vertice in new_vertices:
			vertice[1] = [new_vertice_label if x == vertice1[0] else x for x in vertice[1]]
			vertice[1] = [new_vertice_label if x == vertice2[0] else x for x in vertice[1]]
			
		vertice1[0] = new_vertice_label
		
		#Add contracted vertex to list
		new_vertices.append(vertice1)	
		
		#Set vertice list to the new list
		vertices = new_vertices
		
	#Print Vertices
	# for vertice in vertices:
		# print vertice  
	# print '\n'
	
	#Create the list of edges fresh
	edges = create_edge_list(vertices)
	
	#Print Edges
	# for edge in edges:
	  # print edge		  
	# print '\n'
	
	print "Minimum Cut: " + str(len(edges))
	return len(edges)

parser = argparse.ArgumentParser()
parser.add_argument("file")
parser.parse_args()
args = parser.parse_args()
file = open(args.file)

vertices = []
for line in file.readlines():
  parts = line.split()
  vertice = [parts[0], parts[1:]]
  vertices.append(vertice)  

min_cut_value = min_cut(vertices)
