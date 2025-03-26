import tkinter as tk
from tkinter import messagebox

# Lista de tareas
tareas = []

def agregar_tarea():
    tarea = entrada.get()
    if tarea:
        tareas.append(tarea)
        actualizar_lista()
        entrada.delete(0, tk.END)
    else:
        messagebox.showwarning("Aviso", "No puedes agregar una tarea vacía.")

def eliminar_tarea():
    try:
        seleccion = lista_tareas.curselection()[0]
        tareas.pop(seleccion)
        actualizar_lista()
    except IndexError:
        messagebox.showwarning("Aviso", "Selecciona una tarea para eliminar.")

def actualizar_lista():
    lista_tareas.delete(0, tk.END)
    for tarea in tareas:
        lista_tareas.insert(tk.END, tarea)

# Configuración de la ventana
ventana = tk.Tk()
ventana.title("Gestor de Tareas")
ventana.geometry("300x400")

# Widgets
etiqueta = tk.Label(ventana, text="Ingrese una tarea:", font=("Arial", 12))
etiqueta.pack(pady=5)

entrada = tk.Entry(ventana, width=30)
entrada.pack(pady=5)

boton_agregar = tk.Button(ventana, text="Agregar Tarea", command=agregar_tarea)
boton_agregar.pack(pady=5)

lista_tareas = tk.Listbox(ventana, width=40, height=10)
lista_tareas.pack(pady=5)

boton_eliminar = tk.Button(ventana, text="Eliminar Tarea", command=eliminar_tarea)
boton_eliminar.pack(pady=5)

# Ejecutar la aplicación
ventana.mainloop()
