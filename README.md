# Práctica: Arquitectura web con Docker

Este proyecto demuestra una arquitectura web básica con:
- Frontend: Servido por Nginx (HTML estático)
- Backend: Aplicación Python (Flask)
- Base de datos: PostgreSQL

## Comandos principales

- Iniciar todos los servicios: `docker-compose up --build`
- Detener todos los servicios: `docker-compose down`
- Acceder al frontend: http://localhost:8080
- Acceder al backend: http://localhost:5000

## Clonar el repo en el nuevo Ubuntu:
- git clone https://github.com/GitAlberto18/practica-docker.git
- cd practica-docker
  
## Ejecutar el despliegue con Docker Compose:
- docker compose up -d
