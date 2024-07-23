from tkinter import Tk,Label,Button,Entry

from Muller import MullerGraf


app=Tk()
app.geometry("512x320")
app.title("Metodo de Muller")

txt1=Entry(app,bg="silver")
txt1.place(relx=0.40,rely=0.25)
txt2=Entry(app,bg="silver")
txt2.place(relx=0.10,rely=0.4)
txt3=Entry(app,bg="silver")
txt3.place(relx=0.40,rely=0.4)
txt4=Entry(app,bg="silver")
txt4.place(relx=0.7,rely=0.4)
txt5=Entry(app,bg="yellow")
txt5.place(relx=0.28,rely=0.6,width=250,height=15)

lb0=Label(app,text="Metodo Iterativo de Muller")
lb0.place(relx=0.38,rely=0.05)

lb1=Label(app,text="f(x):")
lb1.place(relx=0.34,rely=0.25)
lb2=Label(app,text="X0:")
lb2.place(relx=0.05,rely=0.4)
lb3=Label(app,text="X1:")
lb3.place(relx=0.35,rely=0.4)
lb4=Label(app,text="X2:")
lb4.place(relx=0.65,rely=0.4)

def proceso():
    f=txt1.get()
    x0=float(txt2.get())
    x1=float(txt3.get())
    x2=float(txt4.get())
    txt5.delete(0,"end")
    txt5.insert(0,MullerGraf(f, x0, x1, x2))

btn=Button(app,text="Ejecutar",command=proceso)
btn.place(relx=0.44,rely=0.50,relwidth=0.17,relheight=0.06)


app.mainloop()