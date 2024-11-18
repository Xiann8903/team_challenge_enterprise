import tkinter as tk #Importante siempre importar los graficos chicos
from funciones import *
import random as ran

def abrir_nueva_ventana(): #Funcion para crear una segunda ventana
    ventana_inicio.destroy()  # Cierra la ventana principal
    ventana_menu = tk.Tk()  # Crear la nueva ventana principal
    ventana_menu.title("Menu juego")
    ventana_menu.geometry("300x200")
    ### Le añadimos la personalización
    etiqueta = tk.Label(ventana_menu, text="Menu",fg="black")
    etiqueta.pack(pady=20)
    facil = tk.Button(ventana_menu, text="Fácil", fg="green")
    normal = tk.Button(ventana_menu ,text="Normal", fg="blue")
    dificil = tk.Button(ventana_menu, text="Imposible", fg="red")
    # Los añadimos
    facil.pack(pady=10)
    normal.pack(pady=10)
    dificil.pack(pady=10)

    ventana_menu.mainloop()

def crear_tablero():
    tamaño=5
    return [[" " for _ in range(tamaño)] for _ in range(tamaño)]

#### Voy a crear la ventana del menú
ventana_inicio = tk.Tk()
ventana_inicio.title("Menu de inicio") #Le asigno el nombre q del menu ya directamente

### Le damos tamaño
ventana_inicio.geometry("300x200")

### Vamos a ponerle texto
texto_inicio = tk.Label(ventana_inicio, text="Hundir la flota", font=("Arial", 14), fg="red")
texto_inicio.pack(pady=20)

jugar = tk.Button(ventana_inicio, text="Jugar", command=abrir_nueva_ventana)
jugar.pack(pady=20)


ventana_inicio.mainloop()

