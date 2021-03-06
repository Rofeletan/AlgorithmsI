#! /usr/bin/env python
import argparse
import math

def partition_begin(array, start, end):
  
  partition_element = array[start]
  i = start + 1
  for j in range (start + 1, end):
    if array[j] < partition_element: 
      array[i], array[j] = array[j], array[i]        
      i += 1  
  array[start], array[i-1] = array[i-1], array[start]
  
  return i
  
def quick_sort_begin(array, start, end):
  if end - start <= 0:
    return (array,0)
  comparisions = 0  
  pivot = partition_begin(array, start, end)  
  comparisions += (pivot - 1 - start)
  comparisions += quick_sort_begin(array, start, pivot - 1)[1]
   
  comparisions += (end - pivot)
  comparisions += quick_sort_begin(array, pivot, end)[1]
  return (array, comparisions)
  
def partition_end(array, start, end):
  array[start], array[end-1] = array[end-1], array[start]
  
  partition_element = array[start]
  i = start + 1
  for j in range (start + 1, end):
    if array[j] < partition_element: 
      array[i], array[j] = array[j], array[i]        
      i += 1  
  array[start], array[i-1] = array[i-1], array[start]
  
  return i
  
def quick_sort_end(array, start, end):
  if end - start <= 0:
    return (array,0)
  comparisions = 0  
  
  pivot = partition_end(array, start, end)  
  comparisions += (pivot - 1 - start)
  comparisions += quick_sort_end(array, start, pivot - 1)[1]
   
  comparisions += (end - pivot)
  comparisions += quick_sort_end(array, pivot, end)[1]
  return (array, comparisions)
  
def partition_median_of_three(array, start, end):
  if end - start > 2:
    mid = int(math.ceil(((end - start) - 1) / 2))     
      
    x,y,z = array[start], array[start + mid], array[end-1]
    if x <= y and x <= z:
      if y <= z:
        array[start], array[start + mid] = array[start + mid], array[start]
      else:
        array[start], array[end-1] = array[end-1], array[start]
    elif y <= x and y <= z:
      if z <= x:      
        array[start], array[end-1] = array[end-1], array[start]
      #if x is less than z do nothing since x is at the start already
    elif z <= x and z <= y:
      if y <= x:      
        array[start], array[start + mid] = array[start + mid], array[start]
      #if x is less than y do nothing since x is at the start already
  
  else:
    if array[start] > array[end-1]:
      array[start], array[end-1] = array[end-1], array[start ]
  
  partition_element = array[start]
 
  
  i = start + 1
  for j in range (start + 1, end):
    if array[j] < partition_element: 
      array[i], array[j] = array[j], array[i]        
      i += 1  
  array[start], array[i-1] = array[i-1], array[start]
  
  return i
  
def quick_sort_median_of_three(array, start, end):
  if end - start <= 0:
    return (array,0)
  comparisions = 0  
  
  pivot = partition_median_of_three(array, start, end)  
  comparisions += (pivot - 1 - start)
  comparisions += quick_sort_median_of_three(array, start, pivot - 1)[1]
   
  comparisions += (end - pivot)
  comparisions += quick_sort_median_of_three(array, pivot, end)[1]
  return (array, comparisions)
  
parser = argparse.ArgumentParser()
parser.add_argument("file")
parser.parse_args()
args = parser.parse_args()
file = open(args.file)

lines = map(int, file)
file.close()

#print lines
#print '\n'
print quick_sort_begin(list(lines), 0, len(lines))[1]
print quick_sort_end(list(lines), 0, len(lines))[1]
print quick_sort_median_of_three(list(lines), 0, len(lines))[1]