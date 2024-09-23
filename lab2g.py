#!/usr/bin/env python3
import sys

#will have default countdown incase no input
def_count = 3

#check number of arguments
if len(sys.argv) == 1:
 count = def_count
#elseif if its not the first
elif len(sys.argv) == 2:
 try:
  count = int(sys.argv[1])
 except ValueError:
  print("Error: Argument must be a number")
  sys.exit(1)

else:
 print("Usage: ./lab2g.py [number]")
 sys.exit(1)

#countdown loop again
while count > 0:
 print(count)
 count -= 1

#print correct format for 2g
print("blast off!")

