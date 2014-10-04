=============
Team roulette
=============

Boostraping
-----------

0. Clonar repo

   .. code::

       git clone git@github.com:migonzalvar/teamroulette.git
       cd teamroulette

1. Crear entorno virtual

   .. code::
   
       python3.4 -m venv .venv

2. Activar entorno

   Linux/Mac OS:

   .. code::

       source .venv/bin/activate

   Windows:

   .. code::

       .venv\Scripts\activate.bat

3. Instalar requisitos

   .. code::

       pip install django djangorestframework


Comandos Django
---------------

.. code::

    python manage.py <comando>

Comandos:

migrate
    Aplica cambios en la base de datos

createsuperuser
    Crea un usuario administrador
    
runserver
    Lanza servidor de desarollo

shell
    Lanza un intérprete interactivo con Django configurado

startapp *<app>*
    Inicializa archivos de una aplicación Django nueva

makemigrations *<app>*
    Genera código para migración de modelos

.. note:: Inicializar proyecto

      .. code::
      
          django-admin startproject teamroulette .

Heroku
------

.. code::

    heroku create
    git push heroku master
    heroku run python manage.py migrate
    heroku open

