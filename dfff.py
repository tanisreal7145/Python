from tkinter import*
f=Tk()
x1 = StringVar()
x1.set("GUN")

x2=StringVar()
x2.set("GUNYOU")

def input_change():
    x2.set("KAK")

f.minsize(500,200)
f.maxsize(200,200)

l=Label(f,textvariable=x1)
l.pack()

e=Entry(f,textvariable=x2)
e.pack()

b1=Button(f,text='Change',command=input_change,width=20,height=3)
b1.pack()


f.mainloop()
