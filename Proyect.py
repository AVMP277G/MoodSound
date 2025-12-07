import tkinter as tk
import random
import winsound
import threading
import time


canciones = {
    "feliz": [
        "Can't Stop the Feeling – Justin Timberlake",
        "Dynamite – BTS",
        "Happy – Pharrell Williams",
        "Shake It Off – Taylor Swift"
    ],

    "triste": [
        "Someone Like You – Adele",
        "The Scientist – Coldplay",
        "Fix You – Coldplay",
        "Cry For Me – Twice"
    ],

    "poderosa": [
        "Run The World – Beyoncé",
        "Pretty Savage – BLACKPINK",
        "Believer – Imagine Dragons",
        "Therefore I Am – Billie Eilish"
    ],

    "cansada": [
        "Sweater Weather – The Neighbourhood",
        "Daydreaming – Radiohead",
        "Blue & Grey – BTS",
        "Lovely – Billie Eilish"
    ]
}


colores_por_mood = {
    "triste":    ["#A7C7E7", "white", "black"],
    "poderosa":  ["#ff00ff", "#6a0dad", "black"],
    "cansada":   ["#4b0082", "#0000ff", "black"],
    "feliz":     ["#00ff00", "#ffd700", "black", "white"]
}


fuentes = ["Courier", "Consolas", "Lucida Console", "Fixedsys"]
tamaños = [30, 38, 45, 55, 65]


def coro_mood(mood):
    if mood == "feliz":
        tonos = [880, 988, 1046, 1174, 1318]
        duracion = 150

    elif mood == "triste":
        tonos = [440, 392, 349, 330, 294]
        duracion = 250

    elif mood == "poderosa":
        tonos = [523, 659, 784, 1046]
        duracion = 180

    elif mood == "cansada":
        tonos = [220, 196, 174]
        duracion = 350

    for t in tonos:
        winsound.Beep(t, duracion)
        time.sleep(0.05)


def ventana_cancion(texto_cancion, mood):

   
    hilo = threading.Thread(target=coro_mood, args=(mood,))
    hilo.start()

    ventana2 = tk.Toplevel()
    ventana2.title("MoodSound")
    ventana2.geometry("600x400")
    ventana2.resizable(False, False)

    colores_fondo = colores_por_mood[mood]

    color_actual = random.choice(colores_fondo)
    letra_color = "white" if color_actual == "black" else "black"

    fuente = random.choice(fuentes)
    tamaño = random.choice(tamaños)

    ventana2.configure(bg=color_actual)

    etiqueta = tk.Label(
        ventana2,
        text=texto_cancion,
        font=(fuente, tamaño, "bold"),
        bg=color_actual,
        fg=letra_color,
        wraplength=550,
        justify="center"
    )

    etiqueta.pack(expand=True)

    def cambiar_estilo(event):
        nuevo_color = random.choice(colores_fondo)
        nueva_fuente = random.choice(fuentes)
        nuevo_tamaño = random.choice(tamaños)

        nuevo_color_letra = "white" if nuevo_color == "black" else "black"

        ventana2.configure(bg=nuevo_color)

        etiqueta.config(
            bg=nuevo_color,
            fg=nuevo_color_letra,
            font=(nueva_fuente, nuevo_tamaño, "bold")
        )

        
        mini = threading.Thread(target=coro_mood, args=(mood,))
        mini.start()

    ventana2.bind("<Button-1>", cambiar_estilo)

def recomendar():
    estado = entrada_estado.get().strip().lower()

    if estado in canciones:
        cancion = random.choice(canciones[estado])
        ventana_cancion(cancion, estado)
        resultado.config(text="")

    else:
        resultado.config(
            text="Usa solo: feliz, triste, poderosa, cansada"
        )


ventana = tk.Tk()
ventana.title("MoodSound")
ventana.geometry("500x300")
ventana.configure(bg="black")
ventana.resizable(False, False)

titulo = tk.Label(
    ventana,
    text="¿Cómo te sientes hoy?",
    font=("Courier", 18, "bold"),
    bg="black",
    fg="white"
)
titulo.pack(pady=20)

entrada_estado = tk.Entry(
    ventana,
    font=("Consolas", 16),
    justify="center"
)
entrada_estado.pack(pady=10)

boton = tk.Button(
    ventana,
    text="RECOMENDAR",
    command=recomendar,
    font=("Courier", 14, "bold"),
    bg="black",
    fg="white",
    activebackground="white",
    activeforeground="black"
)
boton.pack(pady=15)

resultado = tk.Label(
    ventana,
    text="",
    font=("Consolas", 12),
    bg="black",
    fg="red"
)
resultado.pack()

ventana.mainloop()
