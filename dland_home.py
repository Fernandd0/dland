from tkinter import Tk, font, ttk, messagebox, Label, Button


color_1="#11223c" # color principal

# Creacion de la ventana principal:
window_home = Tk() #crea ventana principal.
window_home.title ("DLAND") #titulo de la ventana.
window_home.resizable(width=False,height=False) #evita redimencionar la ventana.
window_home.iconbitmap("img/dland_icono.ico") #icono de la ventana.
window_home.config(bg=color_1) #color de fondo de la ventana
# Proceso para obtener medidas de la pantalla y siempre posicionar la ventana al centro:
ancho_ventana = 1000 #medida seleccionada de ancho.
alto_ventana = 500  #medida seleccionada de altura.
x_ventana = window_home.winfo_screenwidth() // 2 - ancho_ventana // 2 #obtener posicion de ancho al centro.
y_ventana = window_home.winfo_screenheight() // 2 - alto_ventana // 2 #obtener posicion de altura al centro.
posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana) #concatenacion de los valores para pantalla.
window_home.geometry (posicion) #posicionamiento de la ventana.


#Titulo y texto de blienvenida:
welcome = Label(
    window_home,
    text ="\nHey, type a song to downland: ",
    font = ("Mono", 20, "bold"),
    bg=color_1, fg="white"
).place(x=300,y=10)

text_or = Label(
    window_home,
    text ="or",
    font = ("Mono", 12, "bold"),
    bg=color_1, fg="gray"
).place(x=470,y=270)

#Input text
input_song = ttk.Entry(
    window_home,
    font=font.Font(family="Mono", size=20)
).place(x=250, y=120,width=500, height=35,)

#Botones:
continuar_boton = Button(
    window_home,
    text="CONTINUE",
    height=3,width=20,
    cursor="hand2",
    bg="white", fg=color_1,
    font=("Mono",10,"bold"),
    command=()
).place(x=300, y=200)

def close_windows ():
    window_home.destroy() #Cerrar la ventana

cancelar_boton = Button(
    window_home,
    text="EXIT",
    height=3,width=20,
    cursor="hand2",
    bg="white", fg=color_1,
    font=("Mono",10,"bold"),
    command=()
).place(x=500, y=200)

open_doc_boton = Button(
    window_home,
    text="MAKE A LIST",
    cursor="hand2",
    bg="white", fg=color_1,
    font=("Mono",10,"bold"),
    height=3,width=20,
).place(x=400, y=300)


# Robot animado:

#Run:
window_home.mainloop()