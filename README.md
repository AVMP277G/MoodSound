# Proyecto: Módulo MoodSound 🎧

## Descripción

MoodSound es un módulo interactivo que analiza el estado de ánimo del usuario y lo transforma en una experiencia multisensorial: sonido, color, atmósfera y música sugerida.

No utiliza archivos MP3.
Toda la experiencia sonora se genera a través de secuencias **Beep** programadas en código, donde las frecuencias y duraciones replican de forma simbólica el *coro* de cada canción recomendada.

Cada estado de ánimo tiene su propia identidad cromática, energética y sonora.
MoodSound no reproduce música… **traduce emociones en código**.

---

## Estados de ánimo y paletas oficiales

| Estado         | Paleta de colores                              | Significado                        |
| -------------- | ---------------------------------------------- | ---------------------------------- |
| **Triste**     | Azul hielo + Blanco + Negro                    | Soledad, introspección, calma fría |
| **Empoderada** | Rosa neón + Morado + Negro                     | Fuerza, seguridad, dominio         |
| **Cansada**    | Morado + Azul + Negro                          | Desgaste, lentitud, vacío suave    |
| **Feliz**      | Verde cyber o Amarillo + Negro + Glitch blanco | Energía, luz, euforia, caos bonito |

---

## Objetivo del proyecto

* Analizar el estado emocional del usuario
* Recomendar canciones según el mood
* Generar colores y ambiente visual únicos
* Reproducir un patrón de sonido tipo **coro digital**
* Simular una experiencia emocional interactiva
* Unir psicología + programación + música + arte

---

## División del módulo – MoodSound

Este módulo se encarga de:

* Detectar el estado de ánimo ingresado
* Asignar una paleta de colores específica
* Seleccionar una canción al azar del mood
* Generar una secuencia sonora (Beep) inspirada en el coro
* Mostrar resultados en una interfaz visual (Tkinter)
* Cambiar atmósfera al hacer clic (sin modo fullscreen)

---

## Canciones asociadas por estado

**Mood feliz**

* Can’t Stop the Feeling – Justin Timberlake
* Dynamite – BTS
* Happy – Pharrell Williams
* Shake It Off – Taylor Swift

**Mood triste**

* Someone Like You – Adele
* The Scientist – Coldplay
* Fix You – Coldplay
* Cry For Me – TWICE

**Mood empoderada**

* Run the World – Beyoncé
* Pretty Savage – BLACKPINK
* Believer – Imagine Dragons
* Therefore I Am – Billie Eilish

**Mood cansada**

* Sweater Weather – The Neighbourhood
* Daydreaming – Radiohead
* Blue & Grey – BTS
* Lovely – Billie Eilish

---

## Operaciones del sistema

El módulo permite:

* Ingresar estado de ánimo
* Seleccionar canción automáticamente
* Cambiar colores de interfaz
* Generar sonido de fondo (Bit tipo coro)
* Cambiar energía visual con clic
* Activar modo glitch (feliz)
* Variar patrón sonoro en cada ejecución
* Registrar historial de estados (opcional)

Cada interacción es diferente.
Cada emoción crea su propio sonido.

---

## Datos (Entradas del sistema)

* Estado de ánimo (texto)
* Paleta de color
* Canción asociada
* Patrón de frecuencias
* Duración del sonido
* Intensidad de energía
* Reacción visual programada

---

## Ejemplo de estructura de datos

| Estado     | Colores                     | Frecuencia Base | Energía  |
| ---------- | --------------------------- | --------------- | -------- |
| Feliz      | Verde / Amarillo / Negro    | 900 – 1200 Hz   | Alta     |
| Triste     | Azul hielo / Blanco / Negro | 300 – 500 Hz    | Baja     |
| Empoderada | Rosa neón / Morado / Negro  | 700 – 900 Hz    | Muy alta |
| Cansada    | Morado / Azul / Negro       | 200 – 350 Hz    | Suave    |

---

## Tecnologías utilizadas

* Lenguaje: **Python 3**
* Librerías:

  * Tkinter (interfaz)
  * Winsound (sonido Beep)
  * Random (variaciones)
  * Threading (multitarea)
* Paradigma: POO + estructuras de datos
* Entorno: VS Code / GitHub
* No se usan audios externos

---

## Estructura del proyecto (GitHub)

│ moodsound.py
│ README.md
│ /assets (opcional)
│ /docs

Todo contenido sonoro es generado desde código.

---

## Funcionalidades principales

* Sistema de recomendación musical
* Generación de sonido tipo coro (Beep)
* Estética según emoción
* Interfaz cambiante
* Historial opcional
* Modo glitch
* No pantalla completa
* No MP3

---

## Limitaciones

* No se reproduce música real
* No incluye IA (todavía)
* No hay conexión externa
* No almacena datos en la nube
* No analiza expresiones faciales

---

## Cronograma

| Semana | Actividad                      |
| ------ | ------------------------------ |
| 1      | Construcción base del módulo   |
| 2      | Integración UI + sonidos       |
| 3      | Estética + GitHub + README     |
| 4      | Pruebas, correcciones, entrega |

---

## Posibles mejoras futuras

* App móvil
* Lectura de rostro
* Exportar a Spotify
* Modo sueño / zen
* Animaciones suaves
* Versión web
* Historial gráfico emocional

---

## Autora

**Angie Valentina Martínez Poveda**
Ingeniería de Sistemas – UNISANGIL

MoodSound es la prueba de que una mente puede cantar en binario.
Que la emoción también sabe programar.
Y que tú… programaste el alma de una máquina.
