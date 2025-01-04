# Proyecto Django: Consultas Personalizadas y Procedimientos Almacenados

Este proyecto es un ejemplo práctico de cómo implementar consultas personalizadas, anotaciones, procedimientos almacenados y SQL crudo en Django. Incluye configuraciones, vistas, y ejemplos de uso para diferentes bases de datos.

---

## Características

1. **Modelos Personalizados**:
   - Modelo `Person` con los campos `first_name`, `last_name`, `age`, y `email`.
   - Gestión completa de la tabla mediante el ORM de Django.

2. **Consultas Avanzadas**:
   - Uso de anotaciones para excluir y combinar campos.
   - Consultas SQL personalizadas utilizando `connection.cursor()`.
   - Consultas RAW utilizando `Person.objects.raw()`.

3. **Procedimientos Almacenados**:
   - Ejemplo de integración con procedimientos almacenados para bases de datos compatibles.
   - Solución alternativa para bases de datos SQLite.

4. **Datos de Población**:
   - Script para poblar la tabla `Person` con datos de ejemplo.

---

## Estructura del Proyecto

```
myproject/
├── myapp/
│   ├── models.py        # Definición de modelos
│   ├── views.py         # Vistas del proyecto
│   ├── custom_sql.py    # Consultas SQL personalizadas
│   ├── urls.py          # Rutas del proyecto
│   ├── populate_persons.py  # Script para poblar la base de datos
│   ├── __init__.py
└── manage.py
```

---

## Instalación y Configuración

### 1. Clonar el Repositorio
```bash
git clone <url-del-repositorio>
cd myproject
```

### 2. Configurar el Entorno Virtual
```bash
python -m venv venv
source venv/bin/activate   # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configurar la Base de Datos
#### Para PostgreSQL:
1. Instala PostgreSQL y crea una base de datos:
   ```sql
   CREATE DATABASE mydatabase;
   CREATE USER myuser WITH PASSWORD 'mypassword';
   GRANT ALL PRIVILEGES ON DATABASE mydatabase TO myuser;
   ```
2. Actualiza `settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'mydatabase',
           'USER': 'myuser',
           'PASSWORD': 'mypassword',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```
3. Realiza las migraciones:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

#### Para SQLite:
La configuración predeterminada utiliza SQLite y no requiere configuraciones adicionales.

---

## Uso del Proyecto

### 1. Poblar la Base de Datos
Ejecuta el siguiente comando para poblar la tabla `Person` con datos de ejemplo:
```bash
python populate_persons.py
```

### 2. Iniciar el Servidor de Desarrollo
```bash
python manage.py runserver
```

### 3. Endpoints Disponibles

#### Consultas Personalizadas:
- **Excluir Campos**:
  ```
  GET /consultas/exclude-fields/
  ```
  Devuelve los nombres completos de las personas excluyendo otros campos.

- **Consulta RAW**:
  ```
  GET /consultas/raw-query/
  ```
  Realiza una consulta RAW para filtrar personas por apellido.

- **SQL Personalizado**:
  ```
  GET /consultas/execute-sql/
  ```
  Ejecuta una consulta SQL personalizada para actualizar y seleccionar datos.

- **Procedimiento Almacenado**:
  ```
  GET /consultas/call-stored-procedure/
  ```
  Llama a un procedimiento almacenado (requiere PostgreSQL o MySQL).

---

## Solución de Problemas

### Error: `'SQLiteCursorWrapper' object has no attribute 'callproc'`
- Causa: SQLite no soporta procedimientos almacenados.
- Solución:
  - Cambiar la base de datos a PostgreSQL o MySQL.
  - Simular la lógica del procedimiento almacenado directamente en `views.py`.

### Error: `FieldError: Cannot infer type of '+' expression`
- Causa: Django no puede inferir el tipo de datos de una concatenación.
- Solución: Especificar el `output_field` en las anotaciones o usar `Concat`.

---

## Recursos
- [Documentación de Django](https://docs.djangoproject.com/en/stable/)
- [PostgreSQL](https://www.postgresql.org/)
- [MySQL](https://www.mysql.com/)

---
