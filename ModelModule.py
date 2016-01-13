class Model:
   
   def __init__(self):
      self.calculationValue = 0

   def addTwoNumbers(self,firstNumber, secondNumber):
      self.calculationValue = int(firstNumber) + int(secondNumber)

   def getCalculatorValue(self):
      return self.calculationValue
