from data import descargar_mp4, descargar_mp4_clip, descargar_mp3_2, descargar_mp3_clip_2
import pygame
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image


nombre_sonido = ["saringansasuke", "Chidorisasuke", "itachimangekio", "itachiamateratsu"]


def reproducir_sonido(nombre_sonido=""):
    ruta_sonido = f"./assets/{nombre_sonido}.mp3"
    sonido = pygame.mixer.Sound(ruta_sonido)
    sonido.set_volume(0.20)
    sonido.play()


def reproducir_musica():
    pygame.mixer.init()
    pygame.mixer.music.load("./assets/itachimenu.mp3")
    pygame.mixer.music.play(loops=-1)


def cambiar_volumen(valor):
    volumen = float(valor) / 100.0
    pygame.mixer.music.set_volume(volumen)


def salir_app():
    ventana.quit()


ventana = tk.Tk()
ventana.title("MagicMP3")
ventana.geometry("749x467+467+100")

style = ttk.Style()
style.configure("TButton", font=("Segoe UI", 12), padding=10)

imagen_fondo = Image.open("./assets/nubes.jpg")
imagen_fondo = imagen_fondo.resize((749, 467), Image.LANCZOS)
imagen_fondo = ImageTk.PhotoImage(imagen_fondo)

fondo = tk.Label(ventana, image=imagen_fondo)
fondo.place(x=0, y=0, relwidth=1, relheight=1)

label_url = ttk.Label(ventana, text="Introduce el enlace de youtube", font=("Arial", 16))
label_url.pack(pady=10)
label_url.place(x=240, y=85)

entry_url = ttk.Entry(ventana, font=("Arial", 14))
entry_url.pack(pady=5)
entry_url.place(x=275, y=125)

label_inicio = ttk.Label(ventana, text="Para clip introduce en segundos el inicio", font=("Arial", 16))
label_inicio.pack(pady=10)
label_inicio.place(x=205, y=165)

entry_inicio = ttk.Entry(ventana, font=("Arial", 14))
entry_inicio.pack(pady=5)
entry_inicio.place(x=275, y=205)

label_final = ttk.Label(ventana, text="Para clip introduce en segundos el final", font=("Arial", 16))
label_final.pack(pady=10)
label_final.place(x=215, y=245)

entry_final = ttk.Entry(ventana, font=("Arial", 14))
entry_final.pack(pady=5)
entry_final.place(x=275, y=285)

boton_exit = ttk.Button(ventana, text="Exit", command=salir_app)
boton_exit.pack(pady=10)
boton_exit.place(x=610, y=10)

boton_mp4 = ttk.Button(ventana, text="MP4", command=lambda: (descargar_mp4(url=entry_url.get()), reproducir_sonido(nombre_sonido[0])), width=10)
boton_mp4.pack(pady=10)
boton_mp4.place(x=10, y=410)

boton_mp3 = ttk.Button(ventana, text="MP3", command=lambda: (descargar_mp3_2(url=entry_url.get()), reproducir_sonido(nombre_sonido[1])), width=10)
boton_mp3.pack(pady=10)
boton_mp3.place(x=140, y=410)

boton_mp4_clip = ttk.Button(ventana, text="MP4_clip", command=lambda: (descargar_mp4_clip(url=entry_url.get(),
start_time=entry_inicio.get(), end_time=entry_final.get()), reproducir_sonido(nombre_sonido[2])), width=10)
boton_mp4_clip.pack(pady=10)
boton_mp4_clip.place(x=490, y=410)

boton_mp3_clip = ttk.Button(ventana, text="MP3_clip", command=lambda: (descargar_mp3_clip_2(url=entry_url.get(),
start_time=entry_inicio.get(), end_time=entry_final.get()), reproducir_sonido(nombre_sonido[3])), width=10)
boton_mp3_clip.pack(pady=10)
boton_mp3_clip.place(x=620, y=410)

scale = ttk.Scale(ventana, from_=100, to=0, orient=tk.VERTICAL, command=cambiar_volumen)
scale.set(25)
scale.pack()
scale.place(x=10, y=10)

reproducir_musica()

ventana.mainloop()
