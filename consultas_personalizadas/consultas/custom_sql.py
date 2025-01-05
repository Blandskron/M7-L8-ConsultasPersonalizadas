from django.db import connection

def execute_custom_sql():
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO consultas_person (first_name, last_name, age, email) VALUES (%s, %s, %s, %s)", 
                       ['John', 'Doe', 25, 'john.doe@example.com'])
        cursor.execute("SELECT * FROM consultas_person WHERE last_name = %s", ['Doe'])
        results = cursor.fetchall()
    return [{'id': row[0], 'first_name': row[1], 'last_name': row[2], 'age': row[3], 'email': row[4]} for row in results]
