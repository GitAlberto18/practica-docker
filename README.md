# Práctica: Arquitectura web con Docker

Este proyecto es una demostración de una arquitectura web básica usando contenedores Docker.  
Consta de tres servicios principales:

- **Frontend**: Servido con Nginx, que despliega una página HTML estática.  
- **Backend**: Aplicación escrita en Python con Flask, que ofrece una API REST simple.  
- **Base de datos**: PostgreSQL para almacenar datos persistentes.

La idea es practicar la orquestación de múltiples servicios con Docker Compose, manteniendo la persistencia de datos y facilitando la ejecución en cualquier entorno.

## Composición de los servicios

- **frontend**: Contenedor con Nginx que sirve la interfaz web estática.  
- **backend**: Contenedor con Flask que proporciona la lógica de negocio y API REST.  
- **db**: Contenedor PostgreSQL que almacena la base de datos con persistencia a disco mediante volúmenes Docker.

## Comandos principales

- Construir e iniciar los servicios en segundo plano:  
  ```bash
  docker compose up -d --build
## Detener y eliminar los servicios y la red creada:
- docker compose down
## Ver contenedores en ejecución:
- docker ps
## Acceder al frontend en:
- http://localhost:8080
## Acceder al backend en:
- http://localhost:5000

## Despliegue en una nueva máquina Ubuntu
- Clonar el repositorio:
  - git clone https://github.com/GitAlberto18/practica-docker.git
  - cd practica-docker
- Ejecutar los servicios:
  - docker compose up -d --build
