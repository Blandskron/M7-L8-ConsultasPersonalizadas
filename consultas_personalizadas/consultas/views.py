from django.db.models import F, Value
from django.db.models.functions import Concat
from django.db import connection
from django.http import JsonResponse
from .models import Person
from .custom_sql import execute_custom_sql, call_stored_procedure

def exclude_fields_view(request):
    # Excluyendo campos y concatenando con Concat
    people = Person.objects.annotate(
        full_name=Concat(F('first_name'), Value(' '), F('last_name'))
    ).values('full_name')
    return JsonResponse(list(people), safe=False)

def raw_query_view(request):
    # Consulta RAW parametrizada
    lname = 'Doe'
    people = Person.objects.raw('SELECT * FROM consultas_person WHERE last_name = %s', [lname])
    return JsonResponse([{'id': p.id, 'first_name': p.first_name, 'last_name': p.last_name} for p in people], safe=False)

def execute_sql_view(request):
    # Ejecutando SQL directo con connection.cursor()
    with connection.cursor() as cursor:
        cursor.execute("UPDATE consultas_person SET age = age + 1 WHERE age < %s", [30])
        cursor.execute("SELECT first_name, last_name FROM consultas_person WHERE age < %s", [30])
        rows = cursor.fetchall()
    return JsonResponse(rows, safe=False)

def execute_custom_sql_view(request):
    # Llamando a función SQL personalizada en custom_sql.py
    results = execute_custom_sql()
    return JsonResponse(results, safe=False)

def call_stored_procedure_view(request):
    # Llamando a procedimiento almacenado desde custom_sql.py
    results = call_stored_procedure()
    return JsonResponse(results, safe=False)
