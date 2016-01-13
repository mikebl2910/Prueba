from tkinter import *
from Controller import Controller


def main():
   root = Tk()
   root.title('Mi ventana')
   app = Controller(root)
   root.mainloop()

if __name__ == '__main__':
   main()
