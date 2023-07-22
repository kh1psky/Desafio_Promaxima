from django.db import models
import pandas as pd


class Medicamento(models.Model):
    principio_ativo = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=100)
    laboratorio = models.CharField(max_length=100)
    codigo_ggrem = models.CharField(max_length=100)
    registro = models.CharField(max_length=100)
    ean1 = models.CharField(max_length=100)
    produto = models.CharField(max_length=100)
    apresentacao = models.CharField(max_length=100)
    classe_terapeutica = models.CharField(max_length=100)
    tipo_produto = models.CharField(max_length=100)
    regime_preco = models.CharField(max_length=100)
    pf_sem_impostos = models.CharField(max_length=100)
    pf_0_percent = models.CharField(max_length=100)
    pf_12_percent = models.CharField(max_length=100)
    pf_17_percent = models.CharField(max_length=100)
    pf_17_alc = models.CharField(max_length=100)
    pf_175_percent = models.CharField(max_length=100)
    pf_175_alc = models.CharField(max_length=100)
    pf_18_percent = models.CharField(max_length=100)
    pf_18_alc = models.CharField(max_length=100)
    pf_19_percent = models.CharField(max_length=100)
    pf_20_percent = models.CharField(max_length=100)
    pf_21_percent = models.CharField(max_length=100)
    pf_22_percent = models.CharField(max_length=100)
    pmvg_sem_impostos = models.CharField(max_length=100)
    pmvg_0_percent = models.CharField(max_length=100)
    pmvg_12_percent = models.CharField(max_length=100)
    pmvg_17_percent = models.CharField(max_length=100)
    pmvg_17_alc = models.CharField(max_length=100)
    pmvg_175_percent = models.CharField(max_length=100)
    pmvg_175_alc = models.CharField(max_length=100)
    pmvg_18_percent = models.CharField(max_length=100)
    pmvg_18_alc = models.CharField(max_length=100)
    pmvg_19_percent = models.CharField(max_length=100)
    pmvg_20_percent = models.CharField(max_length=100)
    pmvg_21_percent = models.CharField(max_length=100)
    pmvg_22_percent = models.CharField(max_length=100)
    restricao_hospitalar = models.CharField(max_length=100)
    cap = models.CharField(max_length=100)
    confaz_87 = models.CharField(max_length=100)
    icms_0_percent = models.CharField(max_length=100)
    analise_recursal = models.CharField(max_length=100)
    lista_concessao_credito = models.CharField(max_length=100)
    comercializacao_2022 = models.CharField(max_length=100)
    tarja = models.CharField(max_length=100)
    objects = models.Manager()


    def __str__(self):
        return f"Princípio Ativo: {self.principio_ativo}, CNPJ: {self.cnpj}, Laboratório: {self.laboratorio}, Código GGREM: {self.codigo_ggrem}, Registro: {self.registro}, EAN1: {self.ean1}, Produto: {self.produto}, Apresentação: {self.apresentacao}, Classe Terapêutica: {self.classe_terapeutica}, Tipo de Produto: {self.tipo_produto}, Regime de Preço: {self.regime_preco}, PF sem Impostos: {self.pf_sem_impostos}, PF 0%: {self.pf_0_percent}, PF 12%: {self.pf_12_percent}, PF 17%: {self.pf_17_percent}, PF 17 ALC: {self.pf_17_alc}, PF 17.5%: {self.pf_175_percent}, PF 17.5 ALC: {self.pf_175_alc}, PF 18%: {self.pf_18_percent}, PF 18 ALC: {self.pf_18_alc}, PF 19%: {self.pf_19_percent}, PF 20%: {self.pf_20_percent}, PF 21%: {self.pf_21_percent}, PF 22%: {self.pf_22_percent}, PMVG sem Impostos: {self.pmvg_sem_impostos}, PMVG 0%: {self.pmvg_0_percent}, PMVG 12%: {self.pmvg_12_percent}, PMVG 17%: {self.pmvg_17_percent}, PMVG 17 ALC: {self.pmvg_17_alc}, PMVG 17.5%: {self.pmvg_175_percent}, PMVG 17.5 ALC: {self.pmvg_175_alc}, PMVG 18%: {self.pmvg_18_percent}, PMVG 18 ALC: {self.pmvg_18_alc}, PMVG 19%: {self.pmvg_19_percent}, PMVG 20%: {self.pmvg_20_percent}, PMVG 21%: {self.pmvg_21_percent}, PMVG 22%: {self.pmvg_22_percent}, Restrição Hospitalar: {self.restricao_hospitalar}, CAP: {self.cap}, Confaz 87: {self.confaz_87}, ICMS 0%: {self.icms_0_percent}, Análise Recursal: {self.analise_recursal}, Lista Concessão Crédito: {self.lista_concessao_credito}, Comercialização 2022: {self.comercializacao_2022}, Tarja: {self.tarja}"

def importar_dados_xls():
    df = pd.read_excel('C:\\Users\\Home\\Pictures\\consulta.xls') 
    print(df.head()) 
    for _, row in df.iterrows():
        medicamento = Medicamento(
            principio_ativo=row['Princípio Ativo'],
            cnpj=row['CNPJ'],
            laboratorio=row['Laboratório'],
            codigo_ggrem=row['Código GGREM'],
            registro=row['Registro'],
            ean1=row['EAN1'],
            produto=row['Produto'],
            apresentacao=row['Apresentação'],
            classe_terapeutica=row['Classe Terapêutica'],
            tipo_produto=row['Tipo de Produto'],
            regime_preco=row['Regime de Preço'],
            pf_sem_impostos=row['PF sem Impostos'],
            pf_0_percent=row['PF 0%'],
            pf_12_percent=row['PF 12%'],
            pf_17_percent=row['PF 17%'],
            pf_17_alc=row['PF 17 ALC'],
            pf_175_percent=row['PF 17.5%'],
            pf_175_alc=row['PF 17.5 ALC'],
            pf_18_percent=row['PF 18%'],
            pf_18_alc=row['PF 18 ALC'],
            pf_19_percent=row['PF 19%'],
            pf_20_percent=row['PF 20%'],
            pf_21_percent=row['PF 21%'],
            pf_22_percent=row['PF 22%'],
            pmvg_sem_impostos=row['PMVG sem Impostos'],
            pmvg_0_percent=row['PMVG 0%'],
            pmvg_12_percent=row['PMVG 12%'],
            pmvg_17_percent=row['PMVG 17%'],
            pmvg_17_alc=row['PMVG 17 ALC'],
            pmvg_175_percent=row['PMVG 17.5%'],
            pmvg_175_alc=row['PMVG 17.5 ALC'],
            pmvg_18_percent=row['PMVG 18%'],
            pmvg_18_alc=row['PMVG 18 ALC'],
            pmvg_19_percent=row['PMVG 19%'],
            pmvg_20_percent=row['PMVG 20%'],
            pmvg_21_percent=row['PMVG 21%'],
            pmvg_22_percent=row['PMVG 22%'],
            restricao_hospitalar=row['Restrição Hospitalar'],
            cap=row['CAP'],
            confaz_87=row['Confaz 87'],
            icms_0_percent=row['ICMS 0%'],
            analise_recursal=row['Análise Recursal'],
            lista_concessao_credito=row['Lista Concessão Crédito'],
            comercializacao_2022=row['Comercialização 2022'],
            tarja=row['Tarja']
        )
        medicamento.save()