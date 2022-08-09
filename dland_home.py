from distutils.cmd import Command
from re import search
from tkinter import _Padding, font, ttk
from tkinter import *
from turtle import color

from backend import dland_main


#Configuracion de atributos de la ventana home:
window_home = Tk() #crea ventana
window_home.title ("DLAND") #titulo de la ventana
window_home.geometry ("1000x500") #medidas de la ventana
window_home.config(bg = "#11223c") #fondo de la ventana
window_home.iconbitmap("img/dland_icono.ico") #icono de la ventana

#Botones:
continuar_boton = ttk.Style()
continuar_boton.configure(
    "continuar_boton.TButton",
    foreground= "11223c",
    background= "fef1db",
    padding=10,
)
continuar_boton = ttk.Button(text="Continuar", width=30, command=dland_main.search_song)
continuar_boton.place(x=220, y=300)


cancelar_boton = ttk.Button(text="Cancelar", width=30, command=dland_main.message_close)
cancelar_boton.place(x=520, y=300)



s = ttk.Style()
s.configure(
    "MyButton.TButton",
    foreground="#ff0000",
    background="#000000",
    padding=20,
    font=("Times", 12),
    anchor="w"
)
boton = ttk.Button(text="¡Hola, mundo!", style="MyButton.TButton")
boton.place(x=50, y=50)

window_home.mainloop()