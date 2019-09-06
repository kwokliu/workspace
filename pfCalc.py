#!/usr/bin/python

import sys

f = sys.stdin
l = f.readline()
while l:
	done = 1
	l = l.strip (' \t\n')
	operand= []
	result = 0.0
	if(len(l.split()) < 3 ) or (len(l.split()) % 2 == 0):
		print '-E-'
		done = 0
	else:
		for x in l.split():
			if (x != '+') and (x != '-') and (x != '*') and (x != '/') and (x != '^'):
				operand.append(float(x))
			else:
				y = operand.pop()
				if ( len(operand) == 0 ):
					print '-E'
					done = 0
				else:
					if (x == '+'):
						x = operand.pop()
						result = x + y
					elif (x == '-'):
						x = operand.pop()
						result = x - y
					elif (x == '*'):
						x = operand.pop()
						result = x * y
					elif (x == '^'):
						x = operand.pop()
						result = x ** y
					else:
						x = operand.pop()
						if (y != 0):
							result = x / y
						else:
							print '-E-'
							done = 0
					operand.append(result)
		if (done == 1):
			if (len(operand) == 1 ):
				print operand.pop()
			else:
				print '-E-'
	l = f.readline()
