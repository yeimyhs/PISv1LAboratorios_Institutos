## Configuración Local

Para correr el proyecto en tu entorno local, sigue estos pasos:

1. **Entorno Virtual:**
   - Instala las dependencias del proyecto utilizando el archivo `requirements.txt`:
     ```sh
     pip install -r requirements.txt
     ```

2. **Base de Datos PostgreSQL:**
   - Crea una nueva base de datos en PostgreSQL.
   - Restaura la base de datos desde el backup proporcionado:
     ```sh
     pg_restore -U postgresuser -d PIS1706v1 PIS1706v1_migrations1706.backup
     ```
   - Asegúrate de que PostgreSQL esté corriendo en tu sistema.

3. **Configuración del Proyecto Django:**
   - En el archivo `settings.py` del proyecto, actualiza la configuración de la base de datos con tus credenciales:
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.postgresql',
             'NAME': 'PIS1706v1',  # Nombre de tu base de datos
             'USER': 'postgresuser',  # Tu usuario de PostgreSQL
             'PASSWORD': 'contrasenia',  # Tu contraseña de PostgreSQL
             'HOST': 'localhost',
             'PORT': '5432',
         }
     }
     ```

4. **Correr el Servidor:**
   - Inicia el servidor de desarrollo de Django:
     ```sh
     python manage.py runserver
     ```

Visita `http://localhost:8000` en tu navegador para ver el proyecto.

Asegúrate de reemplazar postgresuser y contrasenia con tu usuario y contraseña reales de PostgreSQL.
