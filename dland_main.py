from tkinter import Tk, font, ttk, Button, PhotoImage, Canvas, messagebox
import webbrowser
import keyboard
import pyautogui as ubi
import time

# Funcion para obtener data del entry; buscar la musica y obtener enlace:
def search_song(): #funcion para obtener data del entry.
    song_data= str(input_song.get()) #obtener data del entry y guardarla.
    webbrowser.open('https://www.youtube.com') #abrir youtube.
    time.sleep(20)
    ubi.click (x=659, y=130) #click en el buscador de youtube
    ubi.doubleClick (x=659, y=130) #clicks para confirmar el espacio de busqueda.
    ubi.typewrite (song_data) #type la data de song.
    ubi.press("enter") #presionar tecla enter para buscar.
    time.sleep(3)
    ubi.click (x=719, y=234) #click en la primera opcion.
    time.sleep(3)
    ubi.click (x=719, y=234) #pausar el video.
    keyboard.press_and_release('ctrl + l') #hotkeys para seleccionar el url de la busqueda.
    time.sleep(1)
    keyboard.press_and_release('ctrl + c') #hotkeys para copiar la url.

# Funcion para descargar la musica don ayuda del url:
def dowland():
    keyboard.press_and_release('ctrl + w') #hotkeys para cerrar la ventana de youtube.
    webbrowser.open_new_tab('https://notube.site/es/youtube-app-v19') #abrir notube.
    time.sleep(5)
    ubi.doubleClick(x=542, y=514) #click en el input de notube
    keyboard.press_and_release('ctrl + v') #hotkeys para pegar url.
    time.sleep(2)
    ubi.doubleClick(x=1347, y=516) #clicks para confirmar la solicirud de descarga.
    time.sleep(15)
    ubi.doubleClick(814, y=385) #clicks para iniciar la descarga.
    time.sleep(3)
    keyboard.press_and_release('ctrl + w') #hotkeys para cerrar la ventana
    time.sleep(8)
    messagebox.showinfo(message="LISTO, DESCARGA COMPLETA", title="DLAND") #mensaje de confirmacion de la descarga.

# Funcion de adios y fin del programa:
def close_windows ():
    window_home.destroy() #cerrar la ventana
    messagebox.showinfo(message="Que la fuerza te acompañe...", title="DLAND") #mensaje de adios.

color_1="#11223c" # color principal

# Creacion de la ventana principal:
window_home = Tk() #crea ventana principal.
window_home.title ("DLAND") #titulo de la ventana.
window_home.resizable(width=False,height=False) #evita redimencionar la ventana.
window_home.iconbitmap("img/dland_icono.ico") #icono de la ventana.

# Proceso para obtener medidas de la pantalla y siempre posicionar la ventana al centro:
ancho_ventana = 1000 #medida seleccionada de ancho.
alto_ventana = 500  #medida seleccionada de altura.
x_ventana = window_home.winfo_screenwidth() // 2 - ancho_ventana // 2 #obtener posicion de ancho al centro.
y_ventana = window_home.winfo_screenheight() // 2 - alto_ventana // 2 #obtener posicion de altura al centro.
posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana) #concatenacion de los valores para pantalla.
window_home.geometry (posicion) #posicionamiento de la ventana.
space=Canvas(width=1000,height=500,bg='white') #widget que crea area de trabajo.

# Imagen de fondo:
fondo=PhotoImage(file='img/dland_fondo.gif') #variable que almacena la imagen.
space.create_image(500,500,image=fondo) #coloca la imagen.

# Textos:
space.create_text(500,50, text="Hey, type a song to downland: ",font=('mononoki NF',18, 'bold'),fill='white') #texto de bienvenida.
space.create_text(480,250, text="or",font=('mononoki NF',15),fill='gray') #texto opcional.

# Input texto:
input_song = ttk.Entry(
    space,
    font=font.Font(family="mononoki NF", size=15)
)
input_song.place(x=250, y=90,width=500, height=30,)

# Botones:
continuar_boton = Button(
    space,
    text="CONTINUE",
    height=3,width=20,
    cursor="hand2",
    bg="white", fg=color_1,
    font=("mononoki NF",10,"bold"),
    command=lambda:[search_song(), dowland()] #llama a la funcion de obtner data del entry
).place(x=300, y=170)

exit_boton = Button(
    space,
    text="EXIT",
    height=3,width=20,
    cursor="hand2",
    bg="white", fg=color_1,
    font=("mononoki NF",10,"bold"),
    command=lambda:[close_windows()]
).place(x=500, y=170)

open_doc_boton = Button(
    space,
    text="MAKE A LIST",
    cursor="hand2",
    bg="white", fg=color_1,
    font=("mononoki NF",10,"bold"),
    height=3,width=20,
).place(x=400, y=270)

# Robot animado:

#Run:
space.pack()
window_home.mainloop()