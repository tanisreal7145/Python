from tkinter import *
f = Tk()

s1 = StringVar()
s2 = StringVar()
s3 = StringVar()
s4 = StringVar()

e3 = Entry(f,textvariable=s3)
e3.place(x=50,y=80)
e2 = Entry(f,textvariable=s4)
e2.place(x=250,y=80)

def xxxx():
    with open("b.csv",'w') as f:
        w = writer(f,lineterminator='\n')
        w.writerow( [s1.get(),s2.get()] )
        w.writerow( [s3.get(),s4.get()] )
d = Button(f,text="SAVE",command=xxxx)
d.place(x=100,y=150)

def yyyy():
    with open ("b.csv",'t')as f:
        r=reader(f)
        l=list(r)
        s1.set(1[0][0])
        s2.set(1[0][1])
        s3.set(1[1][0])
        s4.set(1[1][1])
d1 = Button(f,text="LOAD",command=yyyy)
d1.place(x=200,y=150)

f.mainloop
