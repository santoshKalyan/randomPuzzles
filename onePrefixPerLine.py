
""" 
You are given a prefix expression. Write a program to evaluate it. Your program should accept as its first argument a path to a filename. The file contains one prefix expression per line. 

INPUT SAMPLE:

	1
	* + 2 3 4

	Your program has to read this and insert it into any data structure you like. Traverse that data structure and evaluate the prefix expression. Each token is delimited by a whitespace. You may assume that the only valid operators appearing in test data are '+','*' and '/'(floating-point division).

	OUTPUT SAMPLE:

		Print to stdout, the output of the prefix expression, one per line. E.g.

		1
		20

		Constraints: 
			The evaluation result will always be an integer >= 0. 
			The number of the test cases is <= 40.

Run the code using 

python onePrefixPerLine.py inputdata

This code uses stack datastructure to evaluate the expression.

"""

import sys
import operator

# reading the Input file provided as first argument

with open(sys.argv[1], 'r') as myInput :
	rawExpression = myInput.read().strip().splitlines()

	
	""" 
 	You may assume that the only valid operators
  	appearing in test data are '+','*' and '/'(floating-point division).
	
	"""

for evaluate in rawExpression:
	expression = evaluate.split()
	validOperators = {		 
		 '*' : operator.mul,
		 '+' : operator.add,
		 '/' : operator.truediv
	}

	stack = []
	
	"""

	Traverse that data structure and evaluate the prefix expression. Each token is
	delimited by a whitespace.

	"""

	for i in expression[::-1]:
		if i not in  validOperators:
			stack.append(int(i))
		else:
			symbolA , symbolB = stack.pop(), stack.pop() 
			expressionResult = validOperators[i](symbolA, symbolB)
			stack.append(expressionResult)
	
	#Print to stdout, the output of the prefix expression, one per line.
	print int(round(stack.pop()))
