from django.urls import path
from .views import consulta_medicamentos, MedicamentoAPIView

app_name = 'consultas'

urlpatterns = [
    path('consulta/', consulta_medicamentos, name='consulta_medicamentos'),
    path('medicamentos/', MedicamentoAPIView.as_view(), name='medicamentos'),
]
