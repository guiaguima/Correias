import json
import sys
from math import sin, cos, pi, ceil
import pandas as pd

root = tkinter.Tk()
root.withdraw()

f = open('ENTRADA.json')
data = json.load(f)
correia = data['correia']

locals().update(correia)

list_angulorep = [0,5,10,15,20,25,30]
list_largura = [16,20,24,30,36,42,48,54,60,72,84]

rolete_1_0 = {'16':[0,4,10,15,21,26,32],
            '20':[0,7,16,26,35,44,53],
            '24':[0,10,25,39,52,66,80],
            '30':[0,17,40,63,85,107,130],
            '36':[0,25,59,93,125,158,192],
            '42':[0,35,82,129,173,219,265],
            '48':[0,44,100,163,218,266,334],
            '54':[0,59,140,219,293,371,449],
            '60':[0,74,174,272,365,461,559],
            '72':[0,108,254,397,532,673,815],
            '84':[0,153,369,569,777,948,1021]
            }
rolete_2_20 = {'16':[35,40,45,51,56,62,68],
            '20':[47,55,63,70,78,86,95],
            '24':[0,0,0,0,0,0,0],
            '30':[0,0,0,0,0,0,0],
            '36':[0,0,0,0,0,0,0],
            '42':[0,0,0,0,0,0,0],
            '48':[0,0,0,0,0,0,0],
            '54':[0,0,0,0,0,0,0],
            '60':[0,0,0,0,0,0,0],
            '72':[0,0,0,0,0,0,0],
            '84':[0,0,0,0,0,0,0]
               }
rolete_3_20 = {'16':[0,0,0,0,0,0,0],
            '20':[0,0,0,0,0,0,0],
            '24':[58,69,82,94,107,120,133],
            '30':[95,114,134,154,174,196,217],
            '36':[141,169,199,228,258,290,321],
            '42':[197,236,277,318,359,402,445],
            '48':[261,313,367,424,476,533,590],
            '54':[335,401,470,539,609,682,755],
            '60':[418,500,586,672,759,849,940],
            '72':[0,0,0,0,0,0,0],
            '84':[0,0,0,0,0,0,0]
               }
rolete_3_35 = {'16':[0,0,0,0,0,0,0],
            '20':[0,0,0,0,0,0,0],
            '24':[93,103,114,125,135,147,158],
            '30':[152,169,186,204,221,240,258],
            '36':[226,250,276,302,328,355,382],
            '42':[314,348,384,419,455,492,530],
            '48':[417,462,509,556,603,652,702],
            '54':[535,592,652,711,772,835,898],
            '60':[666,738,812,885,961,1040,1118],
            '72':[977,1078,1186,1296,1403,1517,1631],
            '84':[1341,1486,1631,1779,1929,2083,2242]
               }
rolete_3_45 = {'16':[0,0,0,0,0,0,0],
            '20':[0,0,0,0,0,0,0],
            '24':[109,118,128,137,147,157,166],
            '30':[179,194,209,224,239,255,271],
            '36':[265,287,309,331,354,378,401],
            '42':[369,399,430,460,492,524,556],
            '48':[490,529,570,610,651,694,737],
            '54':[627,678,729,780,833,888,942],
            '60':[782,845,909,792,1038,1106,1173],
            '72':[1143,1233,1326,1419,1514,1613,1711],
            '84':[1572,1697,1822,1950,2079,2212,2349]
               }

df1 = pd.DataFrame(rolete_1_0)
df2 = pd.DataFrame(rolete_2_20)
df3 = pd.DataFrame(rolete_3_20)
df4 = pd.DataFrame(rolete_3_35)
df5 = pd.DataFrame(rolete_3_45)



n = 60*velocidade/(3.1415 * diam_tambor)      #RPM

if (angulo_repouso not in list_angulorep):
    messagebox.showerror("Erro!", "O ângulo de repouso deve ser 0°, 5°, 10°, 15°, 20°, 25° ou 30°!")
    sys.exit("O ângulo de repouso deve ser 0°, 5°, 10°, 15°, 20°, 25° ou 30°!")

if (largura not in list_largura):
    messagebox.showerror("Erro!", "A largura deve ser de 16, 20, 24, 30, 36, 42, 48, 54, 60, 72 ou 84 pol!")
    sys.exit("A largura deve ser de 16, 20, 24, 30, 36, 42, 48, 54, 60, 72 ou 84 pol!")

if num_roletes == 1:
    if inc_roletes == 0:
        Ctabela = (df1[str(largura)][angulo_repouso / 5])
if num_roletes == 2:
    if inc_roletes == 20:
        Ctabela = (df2[str(largura)][angulo_repouso / 5])
if num_roletes == 3:
    if inc_roletes == 20:
        Ctabela = (df3[str(largura)][angulo_repouso / 5])
    elif inc_roletes == 35:
        Ctabela = (df4[str(largura)][angulo_repouso / 5])
    elif inc_roletes == 45:
        Ctabela = (df5[str(largura)][angulo_repouso / 5])

Lg = comprimento*0.9                  #comprimento das guias laterais (m)

Kangulo = -0.0006*angulo**2+0.0017*angulo+0.9954

angulo = angulo*pi/180
angulo_repouso = angulo_repouso * pi / 180
H = comprimento * sin(angulo)             #altura de elevação

B = largura             #largura (pol)
dp = 0.055*B + 0.9           #distância padrão do material à borda (pol)

C = Ctabela * velocidade * Kangulo          #Capacidade volumétrica corrigida
Qdisp = C * densidade                   #capacidade de carga (t/h)

if Qdisp < capacidade:
    messagebox.showerror("Erro !", "A Capacidade disponível é menor que a necessária!")
    sys.exit("A Capacidade disponível é menor que a necessária!")

Wm = 0.277 * (capacidade / velocidade)      #Peso do material sobre a correia (kgf/m)
Wb = (largura+4.9881)/0.5602

#cálculo pelo método CEMA

Kx = 0.00068 * (Wm + Wb) + 0.9 / espaco_roletes
Ky = 0.015

Cs = (densidade / 2.3) * ((1 - sin(angulo_repouso)) / (1 + sin(angulo_repouso)))
Ft = 55.4+(num_tambores-2)*18.1         #força para flexionar correia no tambor de retorno (kgf)
Ftc = 0         #força para movimentar trippers acionados pela correia (kgf)
Ftm = 0         #força para movimentar trippers motorizados (kgf)
Fd = 0          #força para vencer atrito dos desviadores (kgf)
F1 = 1.15 * B * num_raspadores
Fa = (capacidade * (velocidade ** 2 - (velocidade * cos(angulo)) ** 2) / (36 * velocidade))
Fg = 0.01488 * Cs * Lg * B**2 + 8.92 * Lg
Ta = Fg + Ft + Ftc + Ftm + Fd + F1 + Fa
Te = comprimento*(Kx + Ky*(Wm + Wb) + 0.015*Wb)+ H * Wm + Ta
Ner = (Te * velocidade) / 75

Ne = ceil((Te * velocidade) / 75)
MT = 9.81 * Te * diam_tambor / 2
MTdisp = (Ne*0.735)*9550/n

Fs = MTdisp/MT

Kpacidade = 0.84

T3 = Kpacidade * Te
G = 2 * T3

if Fs < 1 :
    messagebox.showerror("Erro !", "O fator de segurança está muito baixo!")
    sys.exit("O fator de segurança está muito baixo!")

TB = G/2800

f = open ('SAÍDA.txt', 'w')

f.write("Cálculo de correia transportadora:\n\n")
f.write("Capacidade mássica máxima: "+str(Qdisp)+"t/h\n")
f.write('Capacidade volumétrica máxima: '+str(C)+'m³/h\n')
f.write("Capacidade necessária: " + str(capacidade) + "t/h\n")
f.write("Grau de enchimento: " + str(100 * capacidade / Qdisp) + "%\n\n")
f.write("RPM de saída: "+str(n)+"RPM\n")
f.write("Tensão na correia: "+str(Te)+"kgf\n")
f.write("Potência necessária :"+str(Ner)+"CV\n")
f.write("Potência efetiva :"+str(Ne)+"CV\n")
f.write("Torque para acionamento: "+str(MT)+"N*m\n")
f.write("Torque disponível: "+str(MTdisp)+"N*m\n")
f.write("FS: "+str(Fs)+"\n\n")
f.write("Contrapeso para esticador por gravidade (kgf): "+str(G)+"\n")
f.write("volume de concreto para esticador (m³): "+str(TB))
