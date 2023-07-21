from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Medicamento
import pandas as pd
from .serializers import MedicamentoSerializer
from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect

class MedicamentoAPIView(APIView):
    def get(self, request):
        medicamentos = Medicamento.objects.all()
        serializer = MedicamentoSerializer(medicamentos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MedicamentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_protect  # Adicione o decorator
def consulta_medicamentos(request):
    if request.method == 'POST':
        filtro_principio_ativo = request.POST.get('principio_ativo', '')
        filtro_laboratorio = request.POST.get('laboratorio', '')
        filtro_classe_terapeutica = request.POST.get('classe_terapeutica', '')

        medicamentos = Medicamento.objects.all()

        if filtro_principio_ativo:
            medicamentos = medicamentos.filter(principio_ativo__icontains=filtro_principio_ativo)
        if filtro_laboratorio:
            medicamentos = medicamentos.filter(laboratorio__icontains=filtro_laboratorio)
        if filtro_classe_terapeutica:
            medicamentos = medicamentos.filter(classe_terapeutica__icontains=filtro_classe_terapeutica)

        return render(request, 'consultas/resultado.html', {'medicamentos': medicamentos})

    return render(request, 'consultas/consulta.html')

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def exportar_medicamentos(request):
    if request.method == 'POST':
        selecionados_ids = request.POST.getlist('selecionado')  # Receive data as form data

        medicamentos_selecionados = Medicamento.objects.filter(id__in=selecionados_ids)

        df = pd.DataFrame(list(medicamentos_selecionados.values()))
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=medicamentos_selecionados.xlsx'
        df.to_excel(response, index=False)

        return response

    return HttpResponse()



def importar_dados_xls():
    df = pd.read_excel('C:\\Users\\Home\\Pictures\\consulta.xls')
    print(df.head())
    for _, row in df.iterrows():
        medicamento = Medicamento(
            principio_ativo=row['principio_ativo'],
            cnpj=row['cnpj'],
            laboratorio=row['laboratorio'],
            codigo_ggrem=row['codigo_ggrem'],
            registro=row['registro'],
            ean1=row['ean1'],
            produto=row['produto'],
            apresentacao=row['apresentacao'],
            classe_terapeutica=row['classe_terapeutica'],
            tipo_produto=row['tipo_produto'],
            regime_preco=row['regime_preco'],
            pf_sem_impostos=row['pf_sem_impostos'],
            pf_0_percent=row['pf_0_percent'],
            pf_12_percent=row['pf_12_percent'],
            pf_17_percent=row['pf_17_percent'],
            pf_17_alc=row['pf_17_alc'],
            pf_175_percent=row['pf_175_percent'],
            pf_175_alc=row['pf_175_alc'],
            pf_18_percent=row['pf_18_percent'],
            pf_18_alc=row['pf_18_alc'],
            pf_19_percent=row['pf_19_percent'],
            pf_20_percent=row['pf_20_percent'],
            pf_21_percent=row['pf_21_percent'],
            pf_22_percent=row['pf_22_percent'],
            pmvg_sem_impostos=row['pmvg_sem_impostos'],
            pmvg_0_percent=row['pmvg_0_percent'],
            pmvg_12_percent=row['pmvg_12_percent'],
            pmvg_17_percent=row['pmvg_17_percent'],
            pmvg_17_alc=row['pmvg_17_alc'],
            pmvg_175_percent=row['pmvg_175_percent'],
            pmvg_175_alc=row['pmvg_175_alc'],
            pmvg_18_percent=row['pmvg_18_percent'],
            pmvg_18_alc=row['pmvg_18_alc'],
            pmvg_19_percent=row['pmvg_19_percent'],
            pmvg_20_percent=row['pmvg_20_percent'],
            pmvg_21_percent=row['pmvg_21_percent'],
            pmvg_22_percent=row['pmvg_22_percent'],
            restricao_hospitalar=row['restricao_hospitalar'],
            cap=row['cap'],
            confaz_87=row['confaz_87'],
            icms_0_percent=row['icms_0_percent'],
            analise_recursal=row['analise_recursal'],
            lista_concessao_credito=row['lista_concessao_credito'],
            comercializacao_2022=row['comercializacao_2022'],
            tarja=row['tarja']
        )
        medicamento.save()
