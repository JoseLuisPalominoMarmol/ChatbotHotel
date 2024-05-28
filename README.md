# Assistant Bot

## Descripción
Este proyecto configura un bot asistente utilizando varios componentes para gestionar y procesar tareas específicas como reservaciones de habitaciones, cancelaciones y retroalimentación de servicios.

## Configuración
- **Lenguaje:** Español

## Archivos en el proyecto
- `config.yml`: Contiene configuraciones básicas del bot como el idioma y el ID del asistente.
- `credentials.yml`: Configura las credenciales para los servicios externos.
- `domain.yml`: Define intenciones, entidades, y slots utilizados por el bot.
- `endpoints.yml`: Configura los endpoints para integrar servicios externos.
- `actions.py`: Contiene las acciones personalizadas escritas en Python para procesar la lógica del negocio.

## Endpoints
Se configuró el endpoint de Rasa en `http://localhost:5002/api`.

## Entidades y slots
- **Entidades:** room_type, check_in_date, check_out_date, customer_email, reservation_id, feedback_content.
- **Slots:** room_type, check_in_date, check_out_date, number_of_guests, customer_email, reservation_id.

## Acciones personalizadas
El archivo `actions.py` incluye validaciones y acciones detalladas que el bot puede realizar, como validar fechas y la cantidad de huéspedes.

## Uso
1. Asegúrese de tener todas las dependencias instaladas.
2. Configure los endpoints y credenciales necesarios.
3. Ejecute el bot utilizando su método preferido.
