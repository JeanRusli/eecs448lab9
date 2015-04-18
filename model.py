class Model:
	def __init__(self, sol)
		self.sol == 0.0
	
	def validateNumber(self, num): #Checks for valid number input
		try:
			returnNum = float(num)
			return True
		except ValueError: #Input was not a number so requests the number again
			return False
	
	def validateOperator(self, op): #Checks for valid operator input (+,-,*,/)
		if op == "+" or op == "-" or op == "*" or op == "/":
			return True
		else:
			return False
	
	def isZero(self, num): #Checks for divide by zero
		if num == 0:
			return True
		else:
			return False
	
	def performOperation(self, num1, num2, op) #Returns solution to operation
		if op == "+":
			self.sol = float(num1) + float(num2)
		elif op == "-":
			self.sol = float(num1) - float(num2)
		elif op == "*":
			self.sol = float(num1) * float(num2)
		else:
			self.sol = float(num1) / float(num2)
		return sol
