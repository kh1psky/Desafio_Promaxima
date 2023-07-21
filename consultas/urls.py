from django.urls import path
from .views import consulta_medicamentos, MedicamentoAPIView, exportar_medicamentos

app_name = 'consultas'

urlpatterns = [
    path('medicamentos/', MedicamentoAPIView.as_view(), name='medicamentos'),
    path('consulta/', consulta_medicamentos, name='consulta_medicamentos'),  # Adicionando esta linha
    path('', consulta_medicamentos, name='consultar_medicamentos'),
    path('exportar/', exportar_medicamentos, name='exportar_medicamentos'),
]
