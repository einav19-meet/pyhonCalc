#importing the liberary that allows us to do graphics
from tkinter import *
  
root = Tk()
root.title("einav is calculating some numbers")
expression = "" 

 #input holder

inp = Entry(root,width=20)
inp.grid(row=1, column=1)

equation = StringVar() 
current=inp.get()


def button_n(str): #once you click a button, this is the function that runs, with the numer
	inp.insert(0,str) #insert the number that was inside the button to the input holder


def calc(): # using the "eval" calculating python function once = button is pressed
	try: 
		current=inp.get()
		print(current)
		a = str(eval(current)) 
		inp.delete(0,END) #deletes what is inside the input
		inp.insert(0,a) 
		print(a)
	
	except: 
		inp.insert(0,"error")  
		inp.delete(0,END) #deletes what is inside the input
	return



def button_clear(): #once you click the clear button this func will run
	inp.delete(0,END) #deletes what is inside the input
	return


 # buttons

ButtonNum1 = Button(root, text="1", fg='black', bg='yellow', command = lambda: button_n("1"))
ButtonNum1.grid(row=2, column=0) 


ButtonNum2 = Button(root, text="2", fg='black', bg='yellow', command = lambda: button_n("2"))
ButtonNum2.grid(row=2, column=1) 


ButtonNum3 = Button(root, text="3", fg='black', bg='yellow', command = lambda: button_n("3"))
ButtonNum3.grid(row=2, column=2) 


ButtonNum4 = Button(root, text="4", fg='black', bg='yellow', command = lambda: button_n("4"))
ButtonNum4.grid(row=3, column=0) 


ButtonNum5 = Button(root, text="5", fg='black', bg='yellow', command = lambda: button_n("5"))
ButtonNum5.grid(row=3, column=1) 


ButtonNum6 = Button(root, text="6", fg='black', bg='yellow', command = lambda: button_n("6"))
ButtonNum6.grid(row=3, column=2) 

ButtonNum7 = Button(root, text="7", fg='black', bg='yellow', command = lambda: button_n("7"))
ButtonNum7.grid(row=4, column=0) 


ButtonNum8 = Button(root, text="8", fg='black', bg='yellow', command = lambda: button_n("8"))
ButtonNum8.grid(row=4, column=1) 


ButtonNum9 = Button(root, text="9", fg='black', bg='yellow', command = lambda: button_n("9"))
ButtonNum9.grid(row=4, column=2) 

ButtonNum0 = Button(root, text="0", fg='black', bg='yellow', command = lambda: button_n("0"))
ButtonNum0.grid(row=5, column=0) 

ButtonPlus = Button(root, text="+", fg='black', bg='red', command = lambda: button_n("+"))
ButtonPlus.grid(row=2, column=3) 


ButtonMinus = Button(root, text="-", fg='black', bg='green', command = lambda: button_n("-"))
ButtonMinus.grid(row=3, column=3) 


ButtonMultip = Button(root, text="*", fg='black', bg='blue', command = lambda: button_n("*"))
ButtonMultip.grid(row=4, column=3) 

ButtonDivide = Button(root, text="/", fg='black', bg='pink', command = lambda: button_n("/"))
ButtonDivide.grid(row=5, column=3) 

Buttonclear = Button(root, text="Clear", fg='black', bg='light blue', command = lambda: button_clear())
Buttonclear.grid(row=5, column=1) 

Button = Button(root, text="=", fg='black', bg='orange', command =  calc)
Button.grid(row=5, column=4) 

root.mainloop()
