from tkinter import *

root=Tk()

"""" 
Creating the function to change the colour after hovering below
"""


def clear():
    textbox.delete(0,END)


def equalTo():
    o=textbox.get()
    if(op=="Addition"):
        answer = int(o) + int(var)
        answer = str(answer)
        textbox.delete(0, END)
        textbox.insert(0, answer)
    if (op == "sub"):
        answer = int(var) - int(o);
        textbox.delete(0, END)
        textbox.insert(0, answer)
    if (op == "Multiplication"):
        answer = int(var) * int(o);
        answer = str(answer)
        textbox.delete(0, END)
        textbox.insert(0, answer)
    if (op == "Division"):
        answer = int(var) / int(o);
        answer = str(answer)
        textbox.delete(0, END)
        textbox.insert(0, answer)


def add():
    global var;
    var=textbox.get()
    global op;
    op = "Addition"
    textbox.delete(0,END)




def subtraction():
    global var;
    var=textbox.get()
    global op;
    op = "sub"
    textbox.delete(0,END)



def Multiplication():
    global var;
    var=textbox.get()
    global op
    op ="Multiplication"
    textbox.delete(0,END)

def Division():
    global var;
    var=textbox.get()
    textbox.delete(0, END)
    global op
    op = "Division"





def clickme(number):
    currnt=textbox.get()
    textbox.delete(0,END)
    textbox.insert(0,str(currnt)+str(number))



textbox=Entry(root,width=40,borderwidth=5,font=("arial",15))
textbox.grid(columnspan=4)

#creating the button

botton_1=Button(root,text="1",width=18,height=4 ,font=("arial",10,"bold"),command=lambda:clickme(1))
botton_2=Button(root,text="2",width=18,height=4 ,font=("arial",10,"bold"),command=lambda:clickme(2))
botton_3=Button(root,text="3",width=18,height=4 ,font=("arial",10,"bold"),command=lambda:clickme(3))
botton_4=Button(root,text="4",width=18,height=4 ,font=("arial",10,"bold"),command=lambda:clickme(4))
botton_5=Button(root,text="5",width=18,height=4 ,font=("arial",10,"bold"),command=lambda:clickme(5))
botton_6=Button(root,text="6",width=18,height=4 ,font=("arial",10,"bold"),command=lambda:clickme(6))
botton_7=Button(root,text="7",width=18,height=4 ,font=("arial",10,"bold"),command=lambda:clickme(7))
botton_8=Button(root,text="8",width=18,height=4 ,font=("arial",10,"bold"),command=lambda:clickme(8))
botton_9=Button(root,text="9",width=18,height=4 ,font=("arial",10,"bold"),command=lambda:clickme(9))
botton_0=Button(root,text="0",width=18,height=4 ,font=("arial",10,"bold"),command=lambda:clickme(0))

# Button for the diffrent operations
add=Button(root,text="+",width=18,height=4 ,font=("arial",10,"bold"),command=add)
Substraction=Button(root,text="-",width=18,height=4 ,font=("arial",10,"bold"),command=subtraction)
multiply=Button(root,text="x",width=18,height=4 ,font=("arial",10,"bold"),command=Multiplication)
Division=Button(root,text="/",width=18,height=4 ,font=("arial",10,"bold"),command=Division)


Equal=Button(root,text="=",width=18,height=4 ,font=("arial",10,"bold"),command=equalTo)
Clear=Button(root,text="C",width=18,height=4 ,font=("arial",10,"bold"),command=clear)





# shvoing the button
botton_1.grid(row=3,column=0)
botton_2.grid(row=3,column=1)
botton_3.grid(row=3,column=2)
add.grid(row=3,column=3)

botton_4.grid(row=2,column=0)
botton_5.grid(row=2,column=1)
botton_6.grid(row=2,column=2)
Substraction.grid(row=2,column=3)


botton_7.grid(row=1,column=0)
botton_8.grid(row=1,column=1)
botton_9.grid(row=1,column=2)
multiply.grid(row=1,column=3)

botton_0.grid(row=4,column=0)
Division.grid(row=4,column=3)
Clear.grid(row=4,column=2)
Equal.grid(row=4,column=1)












root.mainloop()
