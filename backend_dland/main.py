from tkinter import messagebox
import webbrowser
import keyboard
import pyautogui as ubi
import time


# Registrar brave:
webbrowser.register('brave', None, webbrowser.BackgroundBrowser("C://Program Files/BraveSoftware/Brave-Browser/Application//brave.exe"))
webbrowser.get('brave')

def search_song():
    # Ingresa nombre de la cancion:
    song = ubi.prompt("Escriba la cancion:  ", "DOWNLANDER")
    str(song)
    # Abrir youtube:
    webbrowser.open('https://www.youtube.com')
    # Buscar cancion:
    time.sleep(20)
    ubi.click (x=659, y=130)
    ubi.doubleClick (x=659, y=130)
    ubi.typewrite (song + " audio")
    ubi.press("enter")
    # Click en la primera opcion:
    time.sleep(3)
    ubi.click (x=719, y=234)
    # Pausar el video:
    time.sleep(3)
    ubi.click (x=719, y=234)
    # Copiar url: 
    keyboard.press_and_release('ctrl + l')
    time.sleep(1)
    keyboard.press_and_release('ctrl + c')

def search_song_2():
    # Ingresa nombre de la cancion:
    song = ubi.prompt("Escriba la cancion:  ", "DOWNLANDER")
    str(song)
    # Buscar cancion:
    ubi.tripleClick (x=659, y=130)
    ubi.typewrite (song + " audio")
    ubi.press("enter")
    # Click en la primera opcion:
    time.sleep(3)
    ubi.click (x=719, y=234)
    # Pausar el video:
    time.sleep(3)
    ubi.click (x=719, y=234)
    # Copiar url: 
    keyboard.press_and_release('ctrl + l')
    time.sleep(1)
    keyboard.press_and_release('ctrl + c')

def dowland():
    # Abrir notube:
    webbrowser.open_new_tab('https://notube.site/es/youtube-app-v19')
    time.sleep(5)
    # Pegar url:
    ubi.doubleClick(x=542, y=514)
    keyboard.press_and_release('ctrl + v')
    time.sleep(2)
    ubi.doubleClick(x=1347, y=516)
    # Descargar audio:
    time.sleep(10)
    ubi.doubleClick(814, y=385) 
    # Cerrar pestaña actual:
    time.sleep(3)
    keyboard.press_and_release('ctrl + w')
    time.sleep(8)
    messagebox.showinfo(message="LISTO, DESCARGA COMPLETA", title="DOWNLANDER")

# Botones:
bot_si = "SI"
bot_no = "NO"

def ask_continue():
    # pregunta para continuar:
    caja_continue = ubi.confirm("¿Desea descargar otra musica?","DOWNLANDER", [bot_si,bot_no])

    # Tomar deciciones en base al boton seleccionado:
    if caja_continue == bot_si:
        search_song_2()
        dowland()
        ask_continue()

    elif caja_continue == bot_no:
        messagebox.showinfo(message="Que la fuerza te acompañe...Adios", title="DOWNLANDER")


# Run: 
search_song()
dowland()
ask_continue()
