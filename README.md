# Proyecto_UIOTEC_MVT_2025

# Modelo de proyecto final
se desarrrollo una aplicación web  programada en Python en Django. Esta web tendrá admin, perfiles, registro, páginas y formularios.

Este proyecto no utiliza Python puro sino Python con Django para desarrollo web. Y la magia de HTML5 Y CSS3 combinado  DJANGO HTML nos facilitan
el diseño FrontEnd de este proyecto.


# Comenzando🚀
Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu local para propósitos de desarrollo y pruebas.

git clone ()

# Descarga de instalación ZIP
Ir a “code” > download ZIP
Descomprimir el archivo
y luego elegir en que carpeta de tu equipo lo instalas y luego se abre con  VS CODE


# Pre-requisitos📋
Deberas tener instalado para correr este proyecto:

Visual Studio Code, Python 3.10 o superior, Django, DB SQLITE.


# instalacion🔧
Se instala en primer instancia VS Code se descarga de https://code.visualstudio.com/download 
se elige el sistema operativo que usas Windows, Mac o Linux se descarga y se siguen los pasos que nos indica hasta instalar VS CODE.

Luego se instala Python 3.10 se descarga de https://www.python.org/  en la primer pantalla selecionar la caja de path sera de utilidad para este proyecto y
luego seguir con la instalacion del mismo.

 DB SQLITE se instala cuando hacemos python manage.py migrate/ python manage.py makemigrations



# construido con🛠️
 VS CODE
 PYTHON 3.10
 DB SQLITE 
 Django
 HTML 5
 CSS 3


# Comandos usados en la consola de VS CODE para hacer funcionar el proyecto
python -m venv virtual (creamos el entorno virtual)

.\virtual\Scripts\activate (activación del entorno virtual)

django-admin startproject Proyecto (crea el proyecto)

cd .\Proyecto\   (nos posiciona en la carpeta del proyecto)

python manage.py startapp MiApp (crea la app)

python manage.py makemigrations (hace los cambios en la base de datos y los modelos) 

python manage.py migrate (Guarda los cambios de los modelos)( se crea la base de datos)

python manage.py runserver (activa el sitio web en localhost)

# Gestionando mi app

python manage.py startapp 

Creamos nuestro modelo dentro de models.py

En nuestro views.py, definimos la vista para mostrar nuestro modelo, importamos nuestro modelos!!

Creamos nuestra plantilla .html con las líneas de código necesarias para mostrar la información de nuestros modelos.

Creamos nuestro archivo urls.py (dentro de la app), creamos la url para la vista deseada, importamos nuestra vista!!

En nuestro archivo settings.py incluimos la app creada en INSTALLED_APPS, agregamos la dirección de la carpeta de nuestros templates en la sección DIRS, de templates. 
Listo!




## Autor✒️
IGNACIO GIORDANO
