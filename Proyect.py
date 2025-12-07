import tkinter as tk
import random
import webbrowser

# 💬 Canciones por estado de ánimo (diccionarios + listas)
canciones = {
    "feliz": [
        "Happy - Pharrell Williams",
        "Good as Hell - Lizzo",
        "Can't Stop the Feeling - Justin Timberlake"
    ],
    "triste": [
        "Someone Like You - Adele",
        "Fix You - Coldplay",
        "All I Want - Kodaline"
    ],
    "poderosa": [
        "Run the World - Beyoncé",
        "Titanium - David Guetta",
        "Confident - Demi Lovato"
    ],
    "cansada": [
        "Let Her Go - Passenger",
        "Lovely - Billie Eilish",
        "Breathe Me - Sia"
    ]
}

# 🎨 Colores y fuentes que cambian
colores = ["#FF6F61", "#FFB347", "#FFD700", "#FF1493", "#9370DB", "#1E90FF"]
fuentes = ["Helvetica", "Courier", "Times New Roman", "Arial", "Comic Sans MS"]

def recomendar():
    estado = entrada.get().lower()
    
    if estado in canciones:
        cancion = random.choice(canciones[estado])

        # Cambios visuales mágicos
        color_fondo = random.choice(colores)
        color_texto = random.choice(colores)
        fuente = random.choice(fuentes)
        tamaño = random.randint(14, 26)

        ventana.config(bg=color_fondo)
        resultado.config(
            text=f"Tu canción para un estado '{estado}' es:\n\n{cancion}",
            bg=color_fondo,
            fg=color_texto,
            font=(fuente, tamaño, "bold")
        )

        # Abrir en Google
        webbrowser.open(f"https://www.google.com/search?q={cancion.replace(' ', '+')}")

    else:
        resultado.config(
            text="Estado no válido. Usa: feliz, triste, poderosa o cansada",
            fg="red",
            bg=ventana["bg"],
            font=("Arial", 14)
        )

# 🪟 Ventana principal
ventana = tk.Tk()
ventana.title("MoodSound 🎵")
ventana.geometry("520x420")
ventana.config(bg=random.choice(colores))

# 🖋️ Título
titulo = tk.Label(
    ventana,
    text="🎧 MOODSOUND 🎧\nLa música según tu estado de ánimo",
    bg=ventana["bg"],
    fg="white",
    font=("Helvetica", 16, "bold")
)
titulo.pack(pady=20)

# 🧩 Entrada
entrada = tk.Entry(ventana, font=("Arial", 14), justify="center")
entrada.pack(pady=10)

# 🔘 Botón
boton = tk.Button(
    ventana,
    text="Recomendar canción",
    command=recomendar,
    font=("Arial", 13, "bold"),
    bg="#222",
    fg="white",
    padx=10,
    pady=5
)
boton.pack(pady=10)

# 🎤 Resultado
resultado = tk.Label(
    ventana,
    text="",
    bg=ventana["bg"],
    wraplength=420,
    justify="center"
)
resultado.pack(pady=20)

# ❤️ Click en el fondo también cambia todo
ventana.bind("<Button-1>", lambda e: recomendar())

ventana.mainloop()
