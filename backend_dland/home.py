import tkinter
from tkinter.ttk import Button, Label
from turtle import title
from unittest import TestCase

# Ventana principal:
window = tkinter.Tk()
window.title("DOWNLANDER")
window.geometry("400x300")

# Etiquetas: 
etiqueta = tkinter.Label(window, text= "Type a message", font="Bahnschrift 20")
etiqueta.pack(fill = tkinter.X)

# Caja de texto:
cajaTexto = tkinter.Entry(window, font="Bahnschrift 15")
cajaTexto.pack()

# Botones:
def boton_ok():
    message = cajaTexto.get()
    print(message)

botonOK = tkinter.Button(window, text= "OK", font="Bahnschrift 20", command=boton_ok)
botonOK.pack()
'''botonOK.grid(row = 3, column = 3)'''


window.mainloop()
