from poly import Polynomials
from tkinter import *

window = Tk()
window.title("Polynomial Calculator - Base")
window.geometry('400x250')
window.config(padx=20,pady=20)

#Label(Polynomial) = for num in range(len(polynomial)): text += str(polynomial[num]) + str(x^num)

firstpoly = [0]
x = 0
y = 0
secondpoly = [0]

def display(poly):
  units = [str(round(poly[y], 5)) + f'x^{y}' for y in range(len(poly)) if poly[y] !=0]
  if units != []:
    if units[0][-1] == '0':
      units[0] = units[0][0:-3]
    elif units[0][-1] == '1':
      units[0] = units[0][0:-2]
  if len(units) > 1:
    if units[1][-1] == '1':
      units[1] = units[1][0:-2]
  for x in range(len(units)):
    if units[x][0] != '-' and x != 0:
      units[x] = '+' + units[x]
  text = (''.join(units))
  return text
  
  

def getpolya():
  top = Toplevel(window)
  top.title("First Polynomial")
  top.config(padx=20,pady=20)
  global firstpoly
  global x
  firstpoly = []
  x = 0
  firstlabel = Label(top, text=f"Now at degree {x} for x, enter value: ")
  firstlabel.grid(row=0,column=1)
  firstentry = Entry(top)
  firstentry.grid(row=1,column=1)
  def next():
    firstpoly.append(float(firstentry.get()))
    global x
    x = x + 1
    firstlabel.config(text=f"Now at degree {x} for x, enter value: ")
    firstentry.delete(0, END)
    polydisplay.config(text=display(firstpoly))
  keepfirst = Button(top, text="Next degree", command=next)
  def end():
    polyone.config(text=display(firstpoly))
    top.destroy()
  stopfirst = Button(top, text="End polynomial", command=end)
  keepfirst.grid(row=3,column=0)
  stopfirst.grid(row=3,column=2)
  polydisplay = Label(top, text=display(firstpoly))
  polydisplay.grid(row=4,column=0, columnspan=3)
  
def getpolyb():
  topb = Toplevel(window)
  topb.title("Second Polynomial")
  topb.config(padx=20,pady=20)
  global secondpoly
  global y
  secondpoly = []
  y = 0
  secondlabel = Label(topb, text=f"Now at degree {y} for x, enter value: ")
  secondlabel.grid(row=0,column=1)
  secondentry = Entry(topb)
  secondentry.grid(row=1,column=1)
  def next():
    secondpoly.append(float(secondentry.get()))
    global y
    y = y + 1
    secondlabel.config(text=f"Now at degree {y} for x, enter value: ")
    secondentry.delete(0, END)
    polydisplay.config(text=display(secondpoly))
  keepsecond = Button(topb, text="Next degree", command=next)
  def end():
    polytwo.config(text=display(secondpoly))
    topb.destroy()
  stopsecond = Button(topb, text="End polynomial", command=end)
  keepsecond.grid(row=3,column=0)
  stopsecond.grid(row=3,column=2)
  polydisplay = Label(topb, text=display(secondpoly))
  polydisplay.grid(row=4,column=0, columnspan=3)
  
def ops():
  global A
  global B
  global C
  oper = Toplevel(window)
  oper.title("Operations Menu")
  oper.config(padx=20,pady=20)
  result = []
  arg = Label(oper, text="Arguments: ", justify='center')
  arg.config(padx=250)
  arg.grid(row=0,column=2)
  a = Label(oper, text=display(firstpoly))
  b = Label(oper, text=display(secondpoly))
  res = Label(oper, text="Result: ")
  c = Label(oper, text=display(result))
  A = Polynomials(firstpoly)
  B = Polynomials(secondpoly)
  a.grid(row=1,column=1,columnspan=3)
  b.grid(row=2,column=1,columnspan=3)
  res.grid(row=3,column=2)
  c.grid(row=4,column=1,columnspan=3)
  def sum():
    global C
    C = A.sum(B)
    c.config(text=display(C.base))
  sum = Button(oper,text="Add", command=sum)
  sum.grid(row=0, column=0)
  def subtract():
    global C
    C = A.subtract(B)
    c.config(text=display(C.base))
  subtract = Button(oper, text="Subtract", command=subtract)
  subtract.grid(row=1,column=0)
  def multiply():
    global C
    C = A.mult(B)
    c.config(text=display(C.base))
  multiply = Button(oper, text="Multiply", command=multiply)
  multiply.grid(row=2,column=0)
  def quotient():
    global C
    C = A.div(B)['q']
    c.config(text=display(C.base))
  div = Button(oper, text="Quotient", command=quotient)
  div.grid(row=3,column=0)
  def remainder():
    global C
    C = A.remain(B)
    c.config(text=display(C.base))
  remainder = Button(oper, text="Remainder", command=remainder)
  remainder.grid(row=4,column=0)
  def gcd():
    global C
    C = A.gcd(B)
    c.config(text=display(C.base))
  gcd = Button(oper, text="GCD", command=gcd)
  gcd.grid(row=5, column=0)
  def invert():
    global A
    global B
    D = A
    A = B
    B = D
    a.config(text=display(A.base))
    b.config(text=display(B.base))
  inverse = Button(oper, text="Invert", command=invert)
  inverse.grid(row=6,column=0)
  def result_as_two():
    global B
    global C
    global secondpoly
    B = C
    secondpoly = B
    text = display(B.base)
    polytwo.config(text=text)
    b.config(text=text)
  result_as_two = Button(oper, text="Result in B", command=result_as_two)
  result_as_two.grid(row=7,column=0)

one = Button(text="First Polynomial", command=getpolya)
one.pack()
polyone = Label(text='')
polyone.config(pady=20)
polyone.pack()

two = Button(text="Second Polynomial", command=getpolyb)
two.pack()
polytwo = Label(text='')
polytwo.config(pady=20)
polytwo.pack()

operations = Button(text="Go to operations", command=ops)
operations.pack()


window.mainloop()