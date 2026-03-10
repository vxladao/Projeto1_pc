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
montante_poupança=(capital * math.pow((1+taxa_poupança), meses)(aporte+meses))

#FII - SIMULAÇÕES

