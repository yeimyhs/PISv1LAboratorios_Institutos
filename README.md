Para correr el proyecto en local se tiene:
Entorno virtual - requeriments.txt
Base de Datos Postgresql 
Crean una BD 
Hay backup de la BD hasta el momento PIS1706v1_migrations1706.backup deben restaurarla en la bd creada 
Cambiar en el proyecto settings.py por su usuario y contrasenia si quieren pueden cambiar el nombre de la bd

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'PIS1706v1',
        'USER': 'postgresuser',
        'PASSWORD': 'contrasenia',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

