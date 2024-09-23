#!/usr/bin/env python3

import sys

#check for the number of arguments
if len (sys.argv) != 3:
 print("Usage: ./lab2d.py name age")
 sys.exit(0) 
else:
#this will get arguments name and age
 name = sys.argv[1]
 age = sys.argv[2]

#will print for 2d format
print(f"Hi {name}, you are {age} years old.")
