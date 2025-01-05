# Gestor de Tareas - Fullstack con Flask

Este es un proyecto de gestión de tareas, donde los usuarios pueden agregar, editar, eliminar y visualizar tareas con fecha y hora límite. Las notificaciones automáticas avisan cuando una tarea está por vencerse. El proyecto está construido con **Flask** (backend) y **SQLite** (base de datos), y se utiliza **Bootstrap** para el diseño front-end.

## Características

- **Agregar tareas**: Permite crear nuevas tareas con un título, descripción, fecha y hora límite.
- **Editar tareas**: Los usuarios pueden actualizar tareas existentes.
- **Eliminar tareas**: Elimina tareas que ya no son necesarias.
- **Notificaciones**: Las tareas con fecha y hora límite reciben notificaciones cuando llega el momento.
- **Interfaz estética**: Se utiliza Bootstrap para proporcionar un diseño limpio, moderno y atractivo.

## Tecnologías Utilizadas

- **Flask**: Framework web ligero para Python.
- **SQLite**: Base de datos ligera para almacenar las tareas.
- **Bootstrap**: Framework de CSS para crear una interfaz de usuario atractiva y responsiva.
- **Plyer**: Biblioteca para enviar notificaciones de escritorio.

## Requisitos

Para ejecutar este proyecto, necesitarás tener **Python 3.x** instalado. También necesitarás instalar las siguientes dependencias:

- **Flask**: Para el desarrollo web.
- **SQLite**: Ya está integrado con Python, no es necesario instalarlo.
- **Plyer**: Para las notificaciones de escritorio.

## Instalación

1. **Clona este repositorio**:

   ```bash
   git clone https://github.com/tu_usuario/gestor-de-tareas.git
   cd gestor-de-tareas
