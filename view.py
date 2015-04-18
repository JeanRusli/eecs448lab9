class View:
	def welcomeMessage(self): #Outputs a welcome message
		print "\n\n         Welcome to the Python Calculator!\n"
		print "I can add, subtract, multiply, and divide 2 numbers.\n\n"
		print "You can always enter \'ans\' to use the previous solution as your input."
	
	def inputNumber(self, text): #Prompts user to input a number
		return raw_input("\nInput %s Number: " % text)
	
	def inputOperator(self): #Prompts user to input an operator
		return raw_input("\nInput Operator (+,-,*,/): ")
	
	def invalidNumber(self): #Invalid Number Input Error
		print "Either input a valid number or input \'ans\' without the quotes."
	
	def invalidOperator(self): #Invalid Operator Input Error
		print "Must enter either +, -, *, or /."
	
	def outputError(self, text): #Outputs the error message 'text'
		print text
	
	def printSolution(self, number1, number2, operator, solution): #Outputs the Solution
		print "%s %s %s =\n\t%s\n" % (float(number1), operator, float(number2), solution)
	
	def userContinue(self): #Asks if user would like to continue
		return raw_input("Would you like to continue? (y/N): ")
	
	def endMessage(self): #Outputs an end of program message
		print "\nThank you for using our program. Have a great day!\n"
		print "This program written by Jake Suddock and Jeanette Rusli\n\n"