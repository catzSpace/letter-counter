from tkinter import *

w = Tk()
w.title("letter counter")
w.geometry("500x400")

t1 = Label(w, text="ingresa una frase")
t1.place(x=10, y=10)
e1 = Entry()
e1.place(x=10, y=30)

t2 = Label(w, text="¿Qué letra quieres buscar?")
t2.place(x=10, y=60)
e2 = Entry()
e2.place(x=10, y=90)

num = Label(w, text="waiting for...")
num.place(x=10, y=180)


def cont():
    v1 = str(e1.get())
    v2 = str(e2.get())

    n = v1.count(v2) #este metodo cuenta el numero de veces que se repite 
    #el parametro indicado entre los (), devuelve un int.
    res = "la letra se repite "
    if n <= 1:
        num["text"] = res + str(n) + " vez"
    else:
        num["text"] = res + str(n) + " veces"
        #lo concatené de esta manera ya que antes
        #me aparecia lo siguiente
        #{la letra se repite} 1 vez
        #esto ya que intentaba juntar numeros y letras.


b = Button(text="procesar", command=lambda: cont())
b.pack(padx=50, pady=120)


w.mainloop()





