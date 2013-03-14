#! /usr/bin/env python
import argparse
import sys
import math
from heapq import *

parser = argparse.ArgumentParser()
parser.add_argument("file")
parser.parse_args()
args = parser.parse_args()
file = open(args.file)

numbers = map(int, file)

sum = 0

heap_min = []
heap_max = []

for number in numbers:
  if len(heap_max) == 0 or number < -heap_max[0]:
    heappush(heap_max, -number)
  else:
    heappush(heap_min, number)
  
  if math.fabs(len(heap_min)  - len(heap_max)) > 1:
    if len(heap_min)  > len(heap_max):
      heappush(heap_max, -heappop(heap_min))
    else:
      heappush(heap_min, -heappop(heap_max))
  median = 0
  # if len(heap_min)  == len(heap_max):
   # median = (heap_min[0] + -heap_max[0]) / 2
  # else:
  if len(heap_min)  > len(heap_max):
    median = heap_min[0] 
  else:
    median = -heap_max[0]
  sum += median
  #print median
  #print heap_max
  #print heap_min
  #print sum
print sum % 10000