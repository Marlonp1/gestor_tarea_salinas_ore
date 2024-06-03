import unittest
from src.logica.gestor_tareas import GestorTareas

class TestGestorTareas(unittest.TestCase):
    def setUp(self):
        self.gestor = GestorTareas()

    def test_agregar_tarea(self):
        self.gestor.agregar_tarea("Tarea 1", "Descripción de la tarea 1")
        self.assertEqual(len(self.gestor.tareas), 1)
        self.assertEqual(self.gestor.tareas[0].titulo, "Tarea 1")
        self.assertEqual(self.gestor.tareas[0].descripcion, "Descripción de la tarea 1")

    def test_agregar_tarea_sin_titulo(self):
        with self.assertRaises(ValueError):
            self.gestor.agregar_tarea("", "Descripción")

    def test_ver_tareas(self):
        # Agregar algunas tareas
        self.gestor.agregar_tarea("Tarea 1", "Descripción de la tarea 1")
        self.gestor.agregar_tarea("Tarea 2", "Descripción de la tarea 2")

        # Imprimir las tareas en la consola
        print("Lista de tareas:")
        for i, tarea in enumerate(self.gestor.tareas, start=1):
            print(f"{i}. {tarea.titulo}: {tarea.descripcion} - {'Completada' if tarea.completada else 'Pendiente'}")

    def test_marcar_completada(self):
        self.gestor.agregar_tarea("Tarea 1", "Descripción de la tarea 1")
        self.gestor.marcar_completada(0)
        self.assertTrue(self.gestor.tareas[0].completada)
if __name__ == "__main__":
    unittest.main()
