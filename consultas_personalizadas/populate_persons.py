import os
import django

# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'consultas_personalizadas.settings')
django.setup()

from consultas.models import Person

def populate_person_table():
    # Datos a insertar
    people_data = [
        {'first_name': 'John', 'last_name': 'Doe', 'age': 25, 'email': 'john.doe@example.com'},
        {'first_name': 'Jane', 'last_name': 'Smith', 'age': 30, 'email': 'jane.smith@example.com'},
        {'first_name': 'Alice', 'last_name': 'Johnson', 'age': 28, 'email': 'alice.johnson@example.com'},
        {'first_name': 'Bob', 'last_name': 'Brown', 'age': 35, 'email': 'bob.brown@example.com'},
        {'first_name': 'Charlie', 'last_name': 'Davis', 'age': 22, 'email': 'charlie.davis@example.com'},
    ]

    # Insertar los datos
    for person_data in people_data:
        Person.objects.create(**person_data)
        print(f"Inserted: {person_data}")

    print("Población de la tabla 'Person' completada.")

if __name__ == "__main__":
    populate_person_table()
