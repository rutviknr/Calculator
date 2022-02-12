from tkinter import*

tk=Tk()
tk.geometry("300x400")
tk.title("CALCULATOR")
tk.config(background='green')

textin=StringVar()
operator=""

def clickbut(number):   #lambda:clickbut(1)
     global operator
     operator=operator+str(number)
     textin.set(operator)

def equlbut():
     global operator
     add=str(eval(operator))
     textin.set(add)
     operator=''
def equlbut():
     global operator
     sub=str(eval(operator))
     textin.set(sub)
     operator=''     
def equlbut():
     global operator
     mul=str(eval(operator))
     textin.set(mul)
     operator=''
def equlbut():
     global operator
     div=str(eval(operator))
     textin.set(div)
     operator=''    

def clrbut():
     textin.set('')

     
tktext=Entry(tk,font=("Courier New",12,'bold'),textvar=textin,width=20,bd=30,bg='yellow')
tktext.pack()

butclr=Button(tk,padx=14,pady=14,bd=4,bg='orange',command=clrbut,text="C",font=("Courier New",16,'bold'))
butclr.place(x=10,y=100)

butad=Button(tk,padx=14,pady=14,bd=4,bg='pink',command=lambda:clickbut("+"),text="+",font=("Courier New",16,'bold'))
butad.place(x=10,y=170)

butmn=Button(tk,padx=14,pady=14,bd=4,bg='pink',command=lambda:clickbut("-"),text="-",font=("Courier New",16,'bold'))
butmn.place(x=10,y=240)

but7=Button(tk,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(7),text="7",font=("Courier New",16,'bold'))
but7.place(x=75,y=100)

but4=Button(tk,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(4),text="4",font=("Courier New",16,'bold'))
but4.place(x=75,y=170)

but1=Button(tk,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(1),text="1",font=("Courier New",16,'bold'))
but1.place(x=75,y=240)

but8=Button(tk,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(8),text="8",font=("Courier New",16,'bold'))
but8.place(x=140,y=100)

but5=Button(tk,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(5),text="5",font=("Courier New",16,'bold'))
but5.place(x=140,y=170)

but2=Button(tk,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(2),text="2",font=("Courier New",16,'bold'))
but2.place(x=140,y=240)

butml=Button(tk,padx=14,pady=14,bd=4,bg='pink',command=lambda:clickbut("*"),text="*",font=("Courier New",16,'bold'))
butml.place(x=10,y=310)

butdiv=Button(tk,padx=14,pady=14,bd=4,bg='pink',command=lambda:clickbut("/"),text="/",font=("Courier New",16,'bold'))
butdiv.place(x=75,y=310)

but0=Button(tk,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(0),text="0",font=("Courier New",16,'bold'))
but0.place(x=140,y=310)

but9=Button(tk,padx=14,pady=14,bd=4,bg='white',text="9",command=lambda:clickbut(9),font=("Courier New",16,'bold'))
but9.place(x=205,y=100)

but6=Button(tk,padx=14,pady=14,bd=4,bg='white',text="6",command=lambda:clickbut(6),font=("Courier New",16,'bold'))
but6.place(x=205,y=170)

but3=Button(tk,padx=14,pady=14,bd=4,bg='white',text="3",command=lambda:clickbut(3),font=("Courier New",16,'bold'))
but3.place(x=205,y=240)

buteql=Button(tk,padx=14,pady=14,bd=4,bg='red',text="=",command=equlbut,font=("Courier New",16,'bold'))
buteql.place(x=205,y=310)

