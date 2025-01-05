from django.urls import path
from . import views

urlpatterns = [
    path('exclude-fields/', views.exclude_fields_view, name='exclude_fields'),
    path('raw-query/', views.raw_query_view, name='raw_query'),
    path('execute-sql/', views.execute_sql_view, name='execute_sql'),
    path('execute-custom-sql/', views.execute_custom_sql_view, name='execute_custom_sql'),
]
