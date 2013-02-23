#! /usr/bin/env python
import argparse

def merge(array1, array2):	
  i = j = 0
  output = []
  
  for k in range (0, len(array1) + len(array2)):
    if i != len(array1) and (j == len(array2) or array1[i] < array2[j]):
      output.append(array1[i])
      i+=1
    else:
      output.append(array2[j])
      j+=1
  
  return output
  
def sort(array):
  if len(array) == 1:
    return array
  
  x = sort(array[:len(array) / 2])
  y = sort(array[len(array) / 2:])	
  z = merge(x,y)
  return z
  
def merge_and_count_split(array1, array2):	
  i = j = 0
  output = []
  count = 0
  for k in range (0, len(array1) + len(array2)):
    if i != len(array1) and (j == len(array2) or array1[i] < array2[j]):
      output.append(array1[i])
      i+=1
    else:
      output.append(array2[j])
      j+=1
      count += len(array1) - i
  
  return (output,count)
  
def sort_and_count(array):
  if len(array) == 1:
    return (array,0)
  
  x = sort_and_count(array[:len(array) / 2])
  y = sort_and_count(array[len(array) / 2:])	
  z = merge_and_count_split(x[0], y[0])
  return (z[0], x[1] + y[1] + z[1])

parser = argparse.ArgumentParser()
parser.add_argument("file")
parser.parse_args()
args = parser.parse_args()
file = open(args.file)

#Here was my original code for loading the file into an integer array
#After checking the forums I discovered the more concise way below

#lines = []
#for line in file.readlines():
#	line = line.rstrip()
#	lines.append(int(line))

lines = map(int, file)
file.close()

#Printed out the original array and just sorted array to check my logic originally
#print lines
#print sort(lines)

print sort_and_count(lines)[1]

