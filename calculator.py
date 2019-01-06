from tkinter import * 
root =Tk()
#root.minsize(width=300,height=300)

equation=StringVar()
lab=Label(root,textvariable=equation,height=3)
equation.set('enter equation')
lab.grid(columnspan=8)

equal=''

def calculate():
    global equal
    total=str(eval(equal))
    equal=""
    equal=total
    equation.set(equal)
def clear():
    global equal
    equal=''
    equation.set('')
def onpress(num):
    global equal
    equal=equal + str(num)
    equation.set(equal)

button1=Button(root,text='1',command=lambda:onpress(1),height=2,width=3)
button1.grid(row=1,column=2)
button2=Button(root,text='2',command=lambda:onpress(2),height=2,width=3)
button2.grid(row=1,column=4)
button3=Button(root,text='3',command=lambda:onpress(3),height=2,width=3)
button3.grid(row=1,column=6)
buttonplus=Button(root,text='+',command=lambda:onpress('+'),height=2,width=3)
buttonplus.grid(row=1,column=8)
button4=Button(root,text='4',command=lambda:onpress(4),height=2,width=3)
button4.grid(row=3,column=2)
button5=Button(root,text='5',command=lambda:onpress(5),height=2,width=3)
button5.grid(row=3,column=4)
button6=Button(root,text='6',command=lambda:onpress(6),height=2,width=3)
button6.grid(row=3,column=6)
buttonminus=Button(root,text='-',command=lambda:onpress('-'),height=2,width=3)
buttonminus.grid(row=3,column=8)
button7=Button(root,text='7',command=lambda:onpress(7),height=2,width=3)
button7.grid(row=5,column=2)
button8=Button(root,text='8',command=lambda:onpress(8),height=2,width=3)
button8.grid(row=5,column=4)
button9=Button(root,text='9',command=lambda:onpress(9),height=2,width=3)
button9.grid(row=5,column=6)
buttonmultiply=Button(root,text='*',command=lambda:onpress('*'),height=2,width=3)
buttonmultiply.grid(row=5,column=8)
buttonc=Button(root,text='C',command=clear,height=2,width=3)
buttonc.grid(row=7,column=2)
button0=Button(root,text='0',command=lambda:onpress(0),height=2,width=3)
button0.grid(row=7,column=4)
buttoneq=Button(root,text='=',command=calculate,height=2,width=3)
buttoneq.grid(row=7,column=6)
buttondiv=Button(root,text='/',command=lambda:onpress('/'),height=2,width=3)
buttondiv.grid(row=7,column=8)


root.mainloop()
