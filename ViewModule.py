from tkinter import *
from tkinter import ttk
from tkinter import messagebox

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
