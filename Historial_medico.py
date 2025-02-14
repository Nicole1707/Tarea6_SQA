import pytest
from unittest.mock import Mock

class HistorialMedico:
    def __init__(self):
        self.datos_locales = {}
        self.servidor = {}

    def descargar_historial(self, paciente_id):
        # Simula la descarga de datos desde el servidor
        if paciente_id in self.servidor:
            self.datos_locales[paciente_id] = self.servidor[paciente_id]
            return True
        return False

    def acceder_historial_offline(self, paciente_id):
        # Permite acceder al historial si está almacenado localmente
        return self.datos_locales.get(paciente_id, None)

    def sincronizar_historial(self, paciente_id):
        # Simula la sincronización con el servidor
        if paciente_id in self.datos_locales:
            self.servidor[paciente_id] = self.datos_locales[paciente_id]
            return True
        return False