from logging import root
from tkinter import ttk
from tkinter import *

#Configuracion de atributos de la ventana home:
window_home = Tk() #crea ventana
window_home.title ("DLAND") #titulo de la ventana
window_home.geometry ("1000x500") #medidas de la ventana
window_home.config(bg = "#11223c") #fondo de la ventana
window_home.iconbitmap("img/dland_icono.ico") #icono de la ventana

#Botones:
cancelar_boton = ttk.Button(text="Continuar")
cancelar_boton.place(x=100, y=250)

window_home.mainloop()