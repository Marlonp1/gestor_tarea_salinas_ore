import tkinter as tk
from tkinter import ttk, messagebox

class Tarea:
    def __init__(self, titulo, descripcion):
        self.titulo = titulo
        self.descripcion = descripcion
        self.completada = False

class GestorTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, titulo, descripcion):
        if not titulo:
            raise ValueError("El título no puede estar vacío")
        tarea = Tarea(titulo, descripcion)
        self.tareas.append(tarea)

    def ver_tareas(self):
        if self.tareas:
            print("Lista de tareas:")
            for i, tarea in enumerate(self.tareas, start=1):
                print(f"{i}. {tarea.titulo}: {tarea.descripcion} - {'Completada' if tarea.completada else 'Pendiente'}")
        else:
            print("No hay tareas en la lista.")

    def obtener_tareas(self):
        return self.tareas

    def marcar_completada(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas[indice].completada = True
        else:
            raise IndexError("Índice fuera de rango")

    def eliminar_tarea(self, indice):
        if 0 <= indice < len(self.tareas):
            del self.tareas[indice]
        else:
            raise IndexError("Índice fuera de rango")

if __name__ == "__main__":
    gestor = GestorTareas()
    gestor.agregar_tarea("Tarea 1", "Descripción de la tarea 1")
    gestor.agregar_tarea("Tarea 2", "Descripción de la tarea 2")
    gestor.ver_tareas()
