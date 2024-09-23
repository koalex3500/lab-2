#!/usr/bin/env python3

import sys

#check if correct number of arguments
if len(sys.argv) != 2:
 print("Usage: ./lab2f.py <number>")
 sys.exit(1)

#will use try to convert to interger
try:
 count = int(sys.argv[1])
except ValueError:
 print("Error: Argument must be a number")
 sys.exit(1)

#use similar from 2e for coutndown loop
while count > 0:
 print(count)
 count -= 1

#print 2f correct format
print("blast off!")

