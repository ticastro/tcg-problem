# TCG PROGRAMMING CHALLENGE

## Introducción

El objetivo de este repositorio es almacenar la aplicación que contiene la solución del desafío propuesto por TCG LATAM. El programa fue desarrollado en lenguaje Python utilizando el framework para aplicaciones Django. Además, se utiliza Heroku como host para levantar el servicio.

![Default Home View](__screenshots/home.png?raw=true "Title")

## Principales Features
* Traducción de strings a los números romanos correspondientes.
* Manejo de errores de input 
* Respuestas al input correspondiente
* Vista que permite ingresar el input y ver la respuesta
* Procfile para deploy a Heroku

## Uso

La aplicación se encuentra en el link https://tcgchallenge.herokuapp.com/. En caso de querer probar la aplicación en local, es necesario seguir los siguientes pasos:

### Clonar el repositorio en una carpeta
```
git clone https://github.com/ticastro/tcg-problem.git
```
### (OPCIONAL) Crear un entorno virtual
Para windows:
Instalar la librería
```
pip install virtualenv
```
Crear el virtualenv
```
virtualenv environment
```
Activar el virtualenv
```
environment/Scripts/activate
```
Para Mac seguir el tutorial en el siguiente [link](https://sourabhbajaj.com/mac-setup/Python/virtualenv.html)

### Instalar las dependencias necesarias para el proyecto:
```
pip install -r requirements.txt
```

### Instalar las migraciones
```
python manage.py migrate
```

### Correr la aplicación:
```
python manage.py runserver
```
