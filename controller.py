import model
import view

class controller:
	def __init__(self):
		self.m = model.Model()
		self.v = view.View()
	def program(self):
		
		self.v.welcomeMessage()
		
		while 1:
			Exit = False
			while Exit == False: #Loops until valid 1st number input
				num1 = self.v.inputNumber("1st")
				Exit = self.m.validateNumber(num1)
				if Exit == False: #If input number is not valid
					self.v.invalidNumber()
					continue
			
			Exit = False
			while Exit == False: #Loops until valid operator input
				op = self.v.inputOperator()
				Exit = self.m.validateOperator(op)
				if Exit == False: #If input operator is not valid
					self.v.invalidOperator()
					continue
			
			Exit = False
			while Exit == False: #Loops until valid 2nd number input
				num2 = self.v.inputNumber("2nd")
				Exit = self.m.validateNumber(num2)
				if Exit == False: #If input number is not valid
					self.v.invalidOperator()
					continue
				if self.m.divByZero(num2, op) == True: #Checks for divide by zero error
					self.v.outputError("Error! Divide By Zero!")
					Exit = False
					continue
			
			result = self.m.performOperation(num1, num2, op)
			self.v.printSolution(result[0], result[1], result[2], result[3])
			
			goAgain = self.v.userContinue()
			if goAgain != "Y" and goAgain != "y" and goAgain != "Yes" and goAgain != "yes": #If user wants to exit
				break
		self.v.endMessage()
		
c = controller()

c.program()