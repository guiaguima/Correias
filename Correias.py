import streamlit as st
import pandas as pd
from math import sin, cos, pi, ceil

# --- Dados de Tabela (Do script original) ---
list_angulorep = [0, 5, 10, 15, 20, 25, 30]
list_largura = [16, 20, 24, 30, 36, 42, 48, 54, 60, 72, 84]

rolete_1_0 = {
    '16':[0,4,10,15,21,26,32],
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
rolete_2_20 = {
    '16':[35,40,45,51,56,62,68],
    '20':[47,55,63,70,78,86,95],
    '24':[0,0,0,0,0,0,0], '30':[0,0,0,0,0,0,0],
    '36':[0,0,0,0,0,0,0], '42':[0,0,0,0,0,0,0],
    '48':[0,0,0,0,0,0,0], '54':[0,0,0,0,0,0,0],
    '60':[0,0,0,0,0,0,0], '72':[0,0,0,0,0,0,0],
    '84':[0,0,0,0,0,0,0]
}
rolete_3_20 = {
    '16':[0,0,0,0,0,0,0], '20':[0,0,0,0,0,0,0],
    '24':[58,69,82,94,107,120,133],
    '30':[95,114,134,154,174,196,217],
    '36':[141,169,199,228,258,290,321],
    '42':[197,236,277,318,359,402,445],
    '48':[261,313,367,424,476,533,590],
    '54':[335,401,470,539,609,682,755],
    '60':[418,500,586,672,759,849,940],
    '72':[0,0,0,0,0,0,0], '84':[0,0,0,0,0,0,0]
}
rolete_3_35 = {
    '16':[0,0,0,0,0,0,0], '20':[0,0,0,0,0,0,0],
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
rolete_3_45 = {
    '16':[0,0,0,0,0,0,0], '20':[0,0,0,0,0,0,0],
    '24':[109,118,128,137,147,157,166],
    '30':[179,194,209,224,239,255,271],
    '36':[265,287,309,331,354,378,401],
    '42':[369,399,430,460,492,524,556],
    '48':[490,529,570,610,651,694,737],
    '54':[627,678,729,780,833,888,942],
    '60':[782,845,909,972,1038,1106,1173],
    '72':[1143,1233,1326,1419,1514,1613,1711],
    '84':[1572,1697,1822,1950,2079,2212,2349]
}

# Cria DataFrames para facilitar a consulta
df1 = pd.DataFrame(rolete_1_0)
df2 = pd.DataFrame(rolete_2_20)
df3 = pd.DataFrame(rolete_3_20)
df4 = pd.DataFrame(rolete_3_35)
df5 = pd.DataFrame(rolete_3_45)


def calcular_correia(velocidade, diam_tambor, angulo_repouso, largura, num_roletes, inc_roletes, comprimento, angulo, capacidade, densidade, espaco_roletes, num_tambores, num_raspadores):
    """Lógica de cálculo adaptada do script original."""
    
    # --- Verificações de Entrada ---
    if angulo_repouso not in list_angulorep:
        st.error(f"Erro: O ângulo de repouso deve ser um dos seguintes: {', '.join(map(str, list_angulorep))}°.")
        return
    if largura not in list_largura:
        st.error(f"Erro: A largura deve ser um dos seguintes valores em polegadas: {', '.join(map(str, list_largura))} in.")
        return

    # --- Cálculo de C_tabela ---
    Ctabela = 0
    idx_ang = angulo_repouso / 5
    larg_str = str(largura)
    
    try:
        if num_roletes == 1:
            if inc_roletes == 0:
                Ctabela = df1[larg_str][idx_ang]
        elif num_roletes == 2:
            if inc_roletes == 20:
                Ctabela = df2[larg_str][idx_ang]
        elif num_roletes == 3:
            if inc_roletes == 20:
                Ctabela = df3[larg_str][idx_ang]
            elif inc_roletes == 35:
                Ctabela = df4[larg_str][idx_ang]
            elif inc_roletes == 45:
                Ctabela = df5[larg_str][idx_ang]
        
        if Ctabela == 0 and num_roletes in [2, 3]:
            # Adiciona uma verificação para os casos em que a tabela tem '0' para certas configurações
            if (num_roletes == 2 and inc_roletes == 20 and largura not in [16, 20]) or \
               (num_roletes == 3 and inc_roletes == 20 and largura in [16, 20]) or \
               (num_roletes == 3 and inc_roletes in [35, 45] and largura in [16, 20]):
                st.error("Erro: A combinação de número de roletes, ângulo de inclinação e largura da correia não é válida para os dados da tabela.")
                return

    except KeyError:
        st.error("Erro: Combinação inválida de largura da correia e configuração de roletes. Verifique a tabela de dados.")
        return

    # --- Cálculos Principais ---
    
    # Rotação (RPM)
    n = 60 * velocidade / (3.1415 * diam_tambor)

    # Comprimento das guias laterais (m)
    Lg = comprimento * 0.9                  
    
    # Fator de correção do ângulo de inclinação (adimensional)
    Kangulo = -0.0006 * angulo**2 + 0.0017 * angulo + 0.9954
    
    # Conversão para radianos
    ang_rad = angulo * pi / 180
    ang_repouso_rad = angulo_repouso * pi / 180
    
    # Altura de elevação (m)
    H = comprimento * sin(ang_rad)             
    
    # Largura (pol)
    B = largura             
    
    # Capacidade volumétrica corrigida (m³/h)
    C = Ctabela * velocidade * Kangulo          
    
    # Capacidade de carga disponível (t/h)
    Qdisp = C * densidade                  

    if Qdisp < capacidade:
        st.error(f"Erro! A Capacidade disponível ({Qdisp:.2f} t/h) é menor que a necessária ({capacidade} t/h)!")
        return

    # Peso do material sobre a correia (kgf/m)
    Wm = 0.277 * (capacidade / velocidade)      
    
    # Peso da correia (kgf/m) - Fórmula simplificada do script original
    Wb = (largura + 4.9881) / 0.5602

    # Cálculo pelo método CEMA

    # Fatores de atrito e arrasto (adimensionais)
    Kx = 0.00068 * (Wm + Wb) + 0.9 / espaco_roletes
    Ky = 0.015

    # Fator de compensação (adimensional)
    Cs = (densidade / 2.3) * ((1 - sin(ang_repouso_rad)) / (1 + sin(ang_repouso_rad)))
    
    # Força para flexionar correia no tambor de retorno (kgf)
    Ft = 55.4 + (num_tambores - 2) * 18.1         
    
    # Forças adicionais (assumidas como zero no script original)
    Ftc = 0         
    Ftm = 0         
    Fd = 0          
    
    # Força para vencer o atrito dos raspadores (kgf)
    F1 = 1.15 * B * num_raspadores
    
    # Força de aceleração/desaceleração (kgf)
    Fa = (capacidade * (velocidade ** 2 - (velocidade * cos(ang_rad)) ** 2) / (36 * velocidade))
    
    # Força para arrastar a correia vazia (kgf)
    Fg = 0.01488 * Cs * Lg * B**2 + 8.92 * Lg
    
    # Forças diversas (kgf)
    Ta = Fg + Ft + Ftc + Ftm + Fd + F1 + Fa
    
    # Tensão efetiva (kgf)
    Te = comprimento * (Kx + Ky * (Wm + Wb) + 0.015 * Wb) + H * Wm + Ta
    
    # Potência necessária (CV) - real
    Ner = (Te * velocidade) / 75

    # Potência efetiva (CV) - arredondada para cima
    Ne = ceil(Ner)
    
    # Torque para acionamento (N*m)
    MT = 9.81 * Te * diam_tambor / 2
    
    # Torque disponível (N*m) - assumindo motor com rendimento 0.735
    MTdisp = (Ne * 0.735) * 9550 / n

    # Fator de segurança
    Fs = MTdisp / MT

    # Fator de correção de capacidade
    Kpacidade = 0.84

    # Tensão no esticador (kgf)
    T3 = Kpacidade * Te
    
    # Contrapeso (kgf)
    G = 2 * T3

    # Volume de concreto (m³) - Fator de 2800 kg/m³
    TB = G / 2800

    if Fs < 1:
        st.error(f"Erro! O fator de segurança (FS = {Fs:.2f}) está muito baixo!")
        return

    # --- Exibição dos Resultados ---
    st.success("✅ Cálculo da Correia Transportadora Concluído com Sucesso!")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Capacidade e Fluxo")
        st.metric(label="Capacidade Mássica Máxima", value=f"{Qdisp:.2f} t/h")
        st.metric(label="Capacidade Volumétrica Máxima", value=f"{C:.2f} m³/h")
        st.metric(label="Capacidade Necessária", value=f"{capacidade} t/h")
        st.metric(label="Grau de Enchimento", value=f"{100 * capacidade / Qdisp:.2f} %")
    
    with col2:
        st.subheader("⚙️ Acionamento e Segurança")
        st.metric(label="Tensão na Correia (Tensão Efetiva)", value=f"{Te:.2f} kgf")
        st.metric(label="Potência Necessária (Real)", value=f"{Ner:.2f} CV")
        st.metric(label="Potência Efetiva (Arred.)", value=f"{Ne} CV")
        st.metric(label="RPM de Saída", value=f"{n:.2f} RPM")
        st.metric(label="Fator de Segurança (FS)", value=f"{Fs:.2f}")

    st.subheader("🏗️ Tensão e Esticador")
    col3, col4, col5 = st.columns(3)
    col3.metric(label="Torque para Acionamento", value=f"{MT:.2f} N*m")
    col4.metric(label="Torque Disponível", value=f"{MTdisp:.2f} N*m")
    col5.metric(label="Tensão no Esticador (T3)", value=f"{T3:.2f} kgf")
    
    st.subheader("⚖️ Contrapeso (Esticador por Gravidade)")
    st.metric(label="Contrapeso Necessário", value=f"{G:.2f} kgf")
    st.metric(label="Volume de Concreto (Estimativa)", value=f"{TB:.4f} m³")

# --- Interface Streamlit ---

st.title("Correia Transportadora: Dimensionamento CEMA")
st.markdown("Use a barra lateral para inserir os parâmetros de projeto.")

# Sidebar para Entrada de Dados (Simulando ENTRADA.json)
st.sidebar.header("Dados de Entrada da Correia")

# Bloco 1: Geometria e Velocidade
st.sidebar.subheader("Geometria e Material")
velocidade = st.sidebar.number_input("Velocidade da Correia (m/s)", min_value=0.01, value=1.5, step=0.1)
diam_tambor = st.sidebar.number_input("Diâmetro do Tambor (m)", min_value=0.01, value=0.5, step=0.05)
comprimento = st.sidebar.number_input("Comprimento da Correia (m)", min_value=1.0, value=50.0, step=1.0)
angulo = st.sidebar.number_input("Ângulo de Inclinação (graus)", min_value=0.0, max_value=90.0, value=15.0, step=1.0)
largura = st.sidebar.selectbox("Largura da Correia (pol)", list_largura, index=list_largura.index(36))

# Bloco 2: Material e Capacidade
st.sidebar.subheader("Material e Requisitos")
densidade = st.sidebar.number_input("Densidade do Material (t/m³)", min_value=0.1, value=1.6, step=0.1)
capacidade = st.sidebar.number_input("Capacidade Necessária (t/h)", min_value=0.1, value=100.0, step=1.0)
angulo_repouso = st.sidebar.selectbox("Ângulo de Repouso (graus)", list_angulorep, index=list_angulorep.index(20))

# Bloco 3: Roletes e Acessórios
st.sidebar.subheader("Configuração dos Roletes")
num_roletes = st.sidebar.selectbox("Número de Roletes (2 ou 3)", [1, 2, 3], index=2)
inc_roletes = st.sidebar.selectbox("Inclinação dos Roletes (graus)", [0, 20, 35, 45], index=1 if num_roletes == 3 else 0)
espaco_roletes = st.sidebar.number_input("Espaço entre Roletes (m)", min_value=0.1, value=1.2, step=0.1)
num_tambores = st.sidebar.number_input("Número de Tambores de Retorno", min_value=2, value=4, step=1)
num_raspadores = st.sidebar.number_input("Número de Raspadores", min_value=0, value=2, step=1)


if st.button("Executar Cálculo"):
    calcular_correia(
        velocidade, diam_tambor, angulo_repouso, largura, num_roletes, 
        inc_roletes, comprimento, angulo, capacidade, densidade, 
        espaco_roletes, num_tambores, num_raspadores
    )

st.caption("Fórmulas baseadas no método CEMA. As entradas são feitas na barra lateral.")
st.write("---")
# Adiciona a exibição das tabelas de capacidade como um expander
with st.expander("Visualizar Tabelas de Capacidade Volumétrica (Ctabela)"):
    st.markdown("### Tabela 1: 1 Rolete (0°)")
    st.dataframe(df1.set_index(pd.Index(list_angulorep)))
    st.markdown("### Tabela 2: 2 Roletes (20°)")
    st.dataframe(df2.set_index(pd.Index(list_angulorep)))
    st.markdown("### Tabela 3: 3 Roletes (20°)")
    st.dataframe(df3.set_index(pd.Index(list_angulorep)))
    st.markdown("### Tabela 4: 3 Roletes (35°)")
    st.dataframe(df4.set_index(pd.Index(list_angulorep)))
    st.markdown("### Tabela 5: 3 Roletes (45°)")
    st.dataframe(df5.set_index(pd.Index(list_angulorep)))
