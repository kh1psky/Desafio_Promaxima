from django.shortcuts import render
from .models import Medicamento
import pandas as pd

def consulta_medicamentos(request):
    if request.method == 'POST':
        filtro_principio_ativo = request.POST.get('principio_ativo', '')
        filtro_laboratorio = request.POST.get('laboratorio', '')
        filtro_produto = request.POST.get('produto', '')

        medicamentos = Medicamento.objects.all()

        if filtro_principio_ativo:
            medicamentos = medicamentos.filter(principio_ativo__icontains=filtro_principio_ativo)
        if filtro_laboratorio:
            medicamentos = medicamentos.filter(laboratorio__icontains=filtro_laboratorio)
        if filtro_produto:
            medicamentos = medicamentos.filter(produto__icontains=filtro_produto)

        return render(request, 'consultas/resultado.html', {'medicamentos': medicamentos})

    return render(request, 'consultas/consulta.html')

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
