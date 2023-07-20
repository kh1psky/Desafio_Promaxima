from django.urls import path
from .views import consulta_medicamentos


app_name = 'consultas'

urlpatterns = [
    path('consulta/', consulta_medicamentos, name='consulta_medicamentos'),
]
