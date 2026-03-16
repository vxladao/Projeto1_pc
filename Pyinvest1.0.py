import math
import random
import datetime
import statistics
import locale

locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")

#ENTRADAS
capital = float(input("Capital inicial:"))
aporte = float(input("Aporte mensal:"))
meses=int(input("Prazo (meses)"))
cdi_anual=float(input("CDI Anual (%)"))/100
percentual_cdb = float(input("Percentual do CDI (%)"))/100
percentual_lci=float(input("Percentual do LCI (%)")) /100
taxa_fii=float(input("Rentabilidade mensal FII (%)"))/100
meta=float(input("Meta financeira (R$)"))

#CONVERSÃO
cdi_mensal=math.pow((1+cdi_anual), 1/12)-1

#TOTAL INVESTIDO
total_investido=capital + (aporte * meses)

#CDB
taxa_cdb = cdi_mensal * percentual_cdb
montante_cdb = (capital*math.pow((1+taxa_cdb),meses)+(aporte*meses))
lucro_cdb = montante_cdb - total_investido
montante_cdb_liquido=total_investido+(lucro_cdb*0.85)

#LCI
taxa_lci=cdi_mensal*percentual_lci
montante_lci=(capital*math.pow((1+taxa_lci), meses) + (aporte*meses))

#POUPANÇA
taxa_poupança=0.005
montante_poupança=(capital*math.pow((1+taxa_poupança), meses)+(aporte*meses))

#FII - SIMULAÇÕES
Montante_fii = (capital * math.pow((1 + taxa_fii), meses) + (aporte * meses))
Sim_FII1 = Montante_fii * (1 + random.uniform (-0.03, 0.03))
Sim_FII2 = Montante_fii * (1 + random.uniform (-0.03, 0.03))
Sim_FII3 = Montante_fii * (1 + random.uniform (-0.03, 0.03))
Sim_FII4 = Montante_fii * (1 + random.uniform (-0.03, 0.03))
Sim_FII5 = Montante_fii * (1 + random.uniform (-0.03, 0.03))

Lista_FII = (Sim_FII1, Sim_FII2, Sim_FII3, Sim_FII4, Sim_FII5)

Media_fii = statistics.mean (Lista_FII)
Mediana_fii = statistics.median (Lista_FII)
Desvio_fii = statistics.stdev (Lista_FII)

#DATA DE RESGATE
Data_atual = datetime.datetime.now()
Data_final = Data_atual + datetime.timedelta(days = meses * 30)

#SE A META FOI ATINGIDA OU NÃO
Meta_atingida = Media_fii >= meta

#ESCALA PARA GERAR O GRAFICO ASCII
Escala = 1000

Barras_CDB = int(montante_cdb_liquido / Escala)
Barras_LCI = int(montante_lci / Escala)
Barras_poupanca = int(montante_poupança / Escala)
Barras_FII = int(Media_fii / Escala)

Grafico_CDB = "█" * Barras_CDB
Grafico_LCI = "█" * Barras_LCI
Grafico_poupanca = "█" * Barras_poupanca
Grafico_FII = "█" * Barras_FII

#ORGANIZAÇÃO DOS PRINTS PARA A SAIDA IGUAL O MODELO
print("\n========================================")
print("PyInvest - Simulador de Investimentos")
print("========================================")
print("Data da simulação:", Data_atual.strftime("%d/%m/%Y"))
print("Data estimada de resgate:", Data_final.strftime("%d/%m/%Y"))
print("\nTotal investido:", locale.currency(total_investido, grouping=True))
print("\n--- RESULTADOS FINANCEIROS ---")
print("CDB:", locale.currency(montante_cdb_liquido, grouping=True))
print(Grafico_CDB)
print("\nLCI/LCA:", locale.currency(montante_lci, grouping=True))
print(Grafico_LCI)
print("\nPoupança:", locale.currency(montante_poupança, grouping=True))
print(Grafico_poupanca)
print("\nFII (média):", locale.currency(Media_fii, grouping=True))
print(Grafico_FII)
print("\n--- ESTATÍSTICAS FII ---")
print("Mediana:", locale.currency(Mediana_fii, grouping=True))
print("Desvio padrão:", locale.currency(Desvio_fii, grouping=True))
print("\nMeta atingida:", Meta_atingida)
print("========================================")