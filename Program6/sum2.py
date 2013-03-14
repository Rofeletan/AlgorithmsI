#! /usr/bin/env python
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("file")
parser.parse_args()
args = parser.parse_args()
file = open(args.file)

numbers = map(int, file)
num_dict = dict(zip(numbers, numbers) ) 

matches = []

for target in range(60, 101):
  for key in num_dict:
    if  target - num_dict[key]  != num_dict[key]  and target - num_dict[key] in num_dict:    
      matches.append((target, num_dict[key], target - num_dict[key]))
      break
  
      

print len(matches)