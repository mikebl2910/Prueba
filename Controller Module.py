from Model import Model
from View import View

class Controller:
   def __init__(self,root):
      self.root = root
      self.model = Model()
      self.view = View(self.root)
      self.view.calculateButton.bind('<Button>',self.calculate)
      
   def calculate(self,event):
      
      self.view.clearCalcSolution()

      try:
         firstNumber = self.view.getFirstNumber()
         secondNumber = self.view.getSecondNumber()
         self.model.addTwoNumbers(firstNumber,secondNumber )
         solution = self.model.getCalculatorValue()
         self.view.setCalcSolution(solution)
      except:
         self.view.displayErroMessage()
