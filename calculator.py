#!/usr/bin/env python
#-*-coding:utf-8-*-
from Tkinter import *
#-------------------------------------------------------------------
def summation():
        c=a.get()+b.get()
        func.delete(0,END)
        func.insert(0,c)
#-------------------------------------------------------------------
def multip():
        c1=a.get()*b.get()
        func.delete(0,END)
        func.insert(0,c1)
#-------------------------------------------------------------------
def division():
        c2=DoubleVar()
        c2=a.get()/b.get()
        func.delete(0,END)
        func.insert(0,c2)
#-------------------------------------------------------------------
def subt():
        c3=a.get()-b.get()
        func.delete(0,END)
        func.insert(0,c3)
#-------------------------------------------------------------------
mainwin=Tk()
mainwin.geometry("250x150+30+100")
mainwin.title("Basic Calculator")
mainwin.resizable(width=FALSE, height=FALSE)
#-------------------------------------------------------------------
a=DoubleVar()
a1=Entry(textvariable=a)
a1.pack()
#-------------------------------------------------------------------
b=DoubleVar()
b1=Entry(textvariable=b)
b1.pack()
#-------------------------------------------------------------------
func=Entry(width=10)
#-------------------------------------------------------------------
summation=Button(text="+",command=summation,cursor="hand2")
summation.place(relx = 0.17, rely = 0.34)
#-------------------------------------------------------------------
multip=Button(text="*",command=multip,cursor="hand2")
multip.place(relx = 0.32, rely = 0.34)
#-------------------------------------------------------------------
division=Button(text="/",command=division,cursor="hand2")
division.place(relx = 0.45, rely = 0.34)
#-------------------------------------------------------------------
subt=Button(text="-",command=subt,cursor="hand2")
subt.place(relx = 0.56, rely = 0.34)
#-------------------------------------------------------------------
func.place(relx = 0.75, rely = 0.36)

mainloop()
