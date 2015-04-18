class View:
	def welcomeMessage(self):
		print "Welcome to the Python Calculator!\n"
		print "I can add, subtract, multiply, and divide 2 numbers.\n\n"
		print "Please enter your two numbers (enter \'ans\' to use the previous solution):"
	
	def inputNumber(self, text):
		return raw_input("Input %s Number: " % text)
	
	def inputOperator(self):
		return raw_input("Input Operator (+,-,*,/): ")
	
	def invalidNumber(self):
		print "Either input a valid number or input \'ans\' without the quotes.\n"
	
	def invalidOperator(self):
		print "Must enter either +, -, *, or /.\n"
	
	def printSolution(self, number1, number2, operator, solution)
		print "%d %s %d =\n\t%d" % (number1, operator, number2, solution)
	
	def userContinue(self):
		return raw_input("Would you like to continue? (y/N): ")