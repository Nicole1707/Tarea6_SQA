import pytest
from Historial_medico import HistorialMedico
@pytest.fixture
def historial():
    return HistorialMedico()

# Prueba 1: Descargar historial médico
def test_descargar_historial(historial):
    historial.servidor["paciente_123"] = {"nombre": "Juan", "edad": 30, "diagnóstico": "Gripe"}
    resultado = historial.descargar_historial("paciente_123")
    assert resultado is True, "El historial no se descargó correctamente"
    assert "paciente_123" in historial.datos_locales, "El historial no se almacenó localmente"

# Prueba 2: Acceder al historial offline
def test_acceder_historial_offline(historial):
    historial.datos_locales["paciente_123"] = {"nombre": "Juan", "edad": 30, "diagnóstico": "Gripe"}
    resultado = historial.acceder_historial_offline("paciente_123")
    assert resultado is not None, "No se pudo acceder al historial offline"
    assert resultado["nombre"] == "Juan", "El nombre del paciente no coincide"

# Prueba 3: Sincronización tras reconexión
def test_sincronizar_historial(historial):
    historial.datos_locales["paciente_123"] = {"nombre": "Juan", "edad": 30, "diagnóstico": "Gripe"}
    resultado = historial.sincronizar_historial("paciente_123")
    assert resultado is True, "El historial no se sincronizó correctamente"
    assert "paciente_123" in historial.servidor, "El historial no se envió al servidor"
