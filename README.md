# Portfolio Django

Proyecto de la Unidad 4 - Desarrollo Backend Silabuz

## Installation
Para poder ejecutar el proyecto debe
- Crear un entorno virtual
```bash
  virtualenv env
```
- Activar la máquina virtual en Windows

```bash
    venv\Scripts\activate

```
```bash
    venv/Scripts/activate.ps1

```

- Instalar los requerimientos del proyecto

```bash
    pip install -r .\requirements.txt
```
## Migraciones a la base de datos
Ejecutar los siguientes comandos

```bash
    python manage.py makemigrations
```
```bash
    python manage.py migrate
```
## Usuario Admin

Creación de super Usuario

```bash
    python manage.py createsuperuser
```
## Arrancar el servidor

```bash
    python manage.py runserver
```

