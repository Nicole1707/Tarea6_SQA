Introducción
Este documento describe las pruebas unitarias implementadas para el módulo de Historial Médico Digital. Se detallan los propósitos de cada prueba y los casos cubiertos.

Pruebas Implementadas
1. test_descargar_historial
Propósito: Verificar que el historial médico de un paciente pueda descargarse correctamente desde el servidor y almacenarse localmente. Casos cubiertos:

Descarga exitosa cuando el paciente tiene historial en el servidor.

Manejo de errores cuando el paciente no tiene historial disponible.

2. test_acceder_historial_offline
Propósito: Asegurar que el historial médico pueda ser accedido sin conexión, si previamente se almacenó localmente. Casos cubiertos:

Acceso exitoso a un historial previamente descargado.

Manejo de errores cuando no hay historial almacenado localmente.

3. test_sincronizar_historial
Propósito: Comprobar que los datos almacenados localmente puedan sincronizarse correctamente con el servidor. Casos cubiertos:
Sincronización exitosa cuando hay conexión a internet.
Manejo de errores si el paciente no tiene historial local para sincronizar.