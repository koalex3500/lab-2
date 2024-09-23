#!/usr/bin/env python3

import sys

# this part will help me check if correct number of arguments is given
if len(sys.argv) != 3:
 print("Usage: ./lab2c.py name age")
 sys.exit(1)
# these are my arguments so it will get the name and age
name = sys.argv[1]
age = sys.argv[2]
#this will check if age is a valid number.
try:
 age = int(age)
except ValueError:
 print("Age must be a number.")
 sys.exit(1)
#will print out required format for check.py lab2c
print(f"Hi {name}, you are {age} years old.")


