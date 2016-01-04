#-----------------------------------------MVC Calculator -----------------------------
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
#---------------------------------------------Model------------------------------------
class Model:
   
   def __init__(self):
      self.calculationValue = 0

   def addTwoNumbers(self,firstNumber, secondNumber):
      self.calculationValue = int(firstNumber) + int(secondNumber)

   def getCalculatorValue(self):
      return self.calculationValue
  #-------------------------------------------View-------------------------------------
class View:
   def __init__ (self, root):
      self.root = root
      self.frame = Frame(self.root)
      self.frame.pack()
      self.firstNumber = Entry(self.frame)
      self.firstNumber.pack(side=LEFT)
      self.additionLabel = Label(self.frame,text='+')
      self.additionLabel.pack(side=LEFT)
      self.secondNumber = Entry(self.frame)
      self.secondNumber.pack(side=LEFT)
      self.calculateButton = Button(self.frame,text='Calculate')
      self.calculateButton.pack(side=LEFT)
      self.calcSolution = Entry(self.frame)
      self.calcSolution.pack(side=LEFT)

   def getFirstNumber(self):
      return self.firstNumber.get()

   def getSecondNumber(self):
      return self.secondNumber.get()
      
   def setCalcSolution(self,calculationValue):
      return self.calcSolution.insert(0,calculationValue)

   def clearCalcSolution(self):
      self.calcSolution.delete(0,END)
   
   def displayErroMessage(self):
      messagebox.showerror('Calculo imposible','Ingresa solo numeros')
#-----------------------------------------Controller-------------------------------------
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

def main():
   root = Tk()
   root.title('Mi ventana')
   app = Controller(root)
   root.mainloop()

if __name__ == '__main__':
   main()
