'''
O objetivo principal desse script é preparar o dataset para a visulazação dos dados e modelagem.
Passos:
- Separar os jogos por temporada em um arquivos diferentes.
Formatação: ano + '.csv' -> Ex: 2015.csv.
- Realizar a criação das novas colunas.
'''
import pandas as pd

def copiar_linha(data, i, ano, rodada, mandante, gols_m, gols_v, visitante, vencedor, valor_m, valor_v):
    data.loc[i, 'Ano'] = int(ano)
    data.loc[i, 'Rodada'] = rodada
    data.loc[i, 'Mandante'] = mandante
    data.loc[i, 'Gols_Mandante'] = gols_m
    data.loc[i, 'Gols_Visitante'] = gols_v
    data.loc[i, 'Visitante'] = visitante
    data.loc[i, 'Vencedor'] = vencedor
    data.loc[i, 'TC-Valor'] = valor_m
    data.loc[i, 'TV-Valor'] = valor_v

def escrever_datasets(data2015, data2016, data2017, data2018,data2019):
    data2015.to_csv('datasets/data_2015.csv')
    data2016.to_csv('datasets/data_2016.csv')
    data2017.to_csv('datasets/data_2017.csv')
    data2018.to_csv('datasets/data_2018.csv')
    data2019.to_csv('datasets/data_2019.csv')

def abrir_datasets(data2015, data2016, data2017, data2018,data2019):
    data2015 = pd.read_csv('datasets/data_2015.csv')
    data2016 = pd.read_csv('datasets/data_2016.csv')
    data2017 = pd.read_csv('datasets/data_2017.csv')
    data2018 = pd.read_csv('datasets/data_2018.csv')
    data2019 = pd.read_csv('datasets/data_2019.csv')

def criar_colunas(bd):
    for i, line in bd.iterrows():
        gm = gf = tpm = tgm = gsv = tpv = 0
        vc = ec = jf = dc = df = gc = gf = gs = 0
        gr = gfc = pts_c = pts_f = 0
        media_c = media_f = 0
        fora = bd.loc[i, 'Visitante']
        casa = bd.loc[i, 'Mandante']
        rodada = bd.loc[i,'Rodada']
        
        if rodada > 5:
            for j in range(i-50,i-1):
                if casa == bd.loc[j,'Mandante']:
                    media_c += bd.loc[j,'Gols_Mandante']
                elif casa == bd.loc[j,'Visitante']:
                    media_c += bd.loc[j,'Gols_Visitante']

                if fora == bd.loc[j,'Mandante']:
                    media_f += bd.loc[j,'Gols_Mandante']
                elif fora == bd.loc[j,'Visitante']:
                    media_f += bd.loc[j,'Gols_Visitante']
            
            bd.loc[i,'TC-Media_Gols'] = media_c/5.0
            bd.loc[i,'TV-Media_Gols'] = media_f/5.0
        else:
            for j in range(0,i-1):
                if casa == bd.loc[j,'Mandante']:
                    media_c += bd.loc[j,'Gols_Mandante']
                elif casa == bd.loc[j,'Visitante']:
                    media_c += bd.loc[j,'Gols_Visitante']

                if fora == bd.loc[j,'Mandante']:
                    media_f += bd.loc[j,'Gols_Mandante']
                elif fora == bd.loc[j,'Visitante']:
                    media_f += bd.loc[j,'Gols_Visitante']
                    
            if rodada > 1:
                bd.loc[i,'TC-Media_Gols'] = (float)(media_c)/(rodada-1)
                bd.loc[i,'TV-Media_Gols'] = float(media_f)/(rodada-1)
            else:
                bd.loc[i,'TC-Media_Gols'] = 0
                bd.loc[i,'TV-Media_Gols'] = 0

        for j in range(i-1):
            # Num empates
            if bd.loc[j, 'Mandante'] == casa and bd.loc[j, 'Vencedor'] == 0:
                ec += 1
            # Jogos fora
            if bd.loc[j, 'Visitante'] == casa:
                jf += 1
            # Derrotas fora
            if bd.loc[j, 'Visitante'] == casa and bd.loc[j, 'Vencedor'] == 1:
                df += 1
            # Pontos
            if bd.loc[j, 'Mandante'] == casa:
                if bd.loc[j, 'Vencedor'] == 1:  # Casa
                    pts_c += 3
                elif bd.loc[j, 'Vencedor'] == 0:
                    pts_c += 1
            if bd.loc[j, 'Visitante'] == casa:
                if bd.loc[j, 'Vencedor'] == 2:  # Fora
                    pts_c += 3
                elif bd.loc[j, 'Vencedor'] == 0:
                    pts_c += 1
            # Num vitorias
            if bd.loc[j, 'Mandante'] == fora and bd.loc[j, 'Vencedor'] == 1:
                vc += 1
            # Num derrotas
            if bd.loc[j, 'Mandante'] == fora and bd.loc[j, 'Vencedor'] == 2:
                dc += 1
            # Gols casa
            if bd.loc[j, 'Mandante'] == fora:
                gc += bd.loc[j, 'Gols_Mandante']
            # Gols fora
            if bd.loc[j, 'Visitante'] == fora:
                gf += bd.loc[j, 'Gols_Visitante']
            # Gols sofridos
            if bd.loc[j, 'Mandante'] == fora:
                gs += bd.loc[j, 'Gols_Visitante']
            if bd.loc[j, 'Visitante'] == fora:
                gs += bd.loc[j, 'Gols_Mandante']
            # Fator campo
            if bd.loc[j, 'Mandante'] == casa:
                ## Qtd de gols que o time mandante fez em casa
                gc += bd.loc[j, 'Gols_Mandante']
            if bd.loc[j, 'Visitante'] == casa:
                ## Qtd de gols que o time mandante fez fora
                gfc += bd.loc[j, 'Gols_Visitante']
            # Quantidade de gols de uma rodada k
            gr = gr + bd.loc[i, 'Gols_Mandante'] + bd.loc[i, 'Gols_Visitante']
            # Pontos
            if bd.loc[j, 'Mandante'] == fora:
                if bd.loc[j, 'Vencedor'] == 1:
                    pts_f += 3
                elif bd.loc[j, 'Vencedor'] == 0:
                    pts_f += 1
            if bd.loc[j, 'Visitante'] == fora:
                if bd.loc[j, 'Vencedor'] == 2:
                    pts_f += 3
                elif bd.loc[j, 'Vencedor'] == 0:
                    pts_f += 1

            # total de gols dos times mandantes
            tgm += bd.loc[j,'Gols_Mandante']
            # Total de gols sfridos pelos visitantes
            tgsv = tgm
            
            if casa == bd.loc[j,'Mandante']:
                #numero de gols cm mandante
                gm += bd.loc[j,'Gols_Mandante']
                # numero de partidas cm mandante
                tpm += 1

            #Gols sofridos
            if bd.loc[j,'Visitante'] == fora:
                #numero de gols sofridos cm visitante
                gsv += bd.loc[j,'Gols_Mandante']
                # numero de partidas cm visitante
                tpv += 1
                
        if bd.loc[i,'Rodada'] <= 5:
            bd.loc[i,'TC-Ofensivo'] = 0
            bd.loc[i,'TV-Defensivo'] = 0
        else:
            if tpm == 0 or tpv == 0:
                print(fora)
                print(tpm,tpv)
            tp = bd.loc[i,'Rodada'] - 1
            bd.loc[i,'TC-Ofensivo'] = round((gm/tpm)/(tgm/tp),4)
            bd.loc[i,'TV-Defensivo'] = round((gsv/tpv)/(tgsv/tp),4)

        bd.loc[i, 'TC-Empates_Casa'] = int(ec)
        bd.loc[i, 'TC-Jogos_Fora'] = jf
        bd.loc[i, 'TC-Derrotas_Fora'] = df
        bd.loc[i, 'TC-Pontos'] = pts_c
        if gfc+gc == 0:
            bd.loc[i, 'TC-Fator_Campo'] = 0
        else:
            bd.loc[i, 'TC-Fator_Campo'] = round(gc/(gc+float(gfc)),2)
        bd.loc[i, 'TV-Vitorias_Casa'] = vc
        bd.loc[i, 'TV-Derrotas_Casa'] = dc
        bd.loc[i, 'TV-Gols_Casa'] = gc
        bd.loc[i, 'TV-Gols_Fora'] = gf
        bd.loc[i, 'TV-Gols_Sofridos'] = gs
        bd.loc[i, 'TV-Pontos'] = pts_f 

data = pd.read_csv('datasets/dataset.csv')
anos = list(data['Ano'].unique())

# Criação dos datasets
for i in anos:
    nome_data = 'data_' + str(i) + '.csv'
    aux_data = pd.DataFrame()
    aux_data.to_csv('datasets/' + nome_data)

# Abrindo os datasets
data2015 = pd.DataFrame()
data2016 = pd.DataFrame()
data2017 = pd.DataFrame()
data2018 = pd.DataFrame()
data2019 = pd.DataFrame()

abrir_datasets(data2015, data2016, data2017, data2018,data2019)

# Separando por temporada
print('Separando por temporada...')
for i, linha in data.iterrows():
    aux = 'data_' + str(data.loc[i, 'Ano'])
    ano = data.loc[i, 'Ano']
    rodada = data.loc[i, 'Rodada']
    mandante = data.loc[i, 'Mandante']
    gols_m = data.loc[i, 'Gols_Mandante']
    gols_v = data.loc[i, 'Gols_Visitante']
    visitante = data.loc[i, 'Visitante']
    vencedor = data.loc[i, 'Vencedor']
    valor_m = data.loc[i, 'TC-Valor']
    valor_v = data.loc[i, 'TV-Valor']

    if ano == 2015:
        copiar_linha(data2015, i, ano, rodada, mandante, gols_m,
                     gols_v, visitante, vencedor, valor_m, valor_v)
    elif ano == 2016:
        copiar_linha(data2016, i-380, ano, rodada, mandante, gols_m,
                     gols_v, visitante, vencedor, valor_m, valor_v)
    elif ano == 2017:
        copiar_linha(data2017, i-(380*2), ano, rodada, mandante, gols_m,
                     gols_v, visitante, vencedor, valor_m, valor_v)
    elif ano == 2018:
        copiar_linha(data2018, i-(380*3), ano, rodada, mandante, gols_m,
                     gols_v, visitante, vencedor, valor_m, valor_v)
    elif ano == 2019:
        copiar_linha(data2019, i-(380*4), ano, rodada, mandante, gols_m,
                     gols_v, visitante, vencedor, valor_m, valor_v)

escrever_datasets(data2015, data2016, data2017, data2018,data2019)

'''
Passo 2 - Criar as colunas em cada dataset

Vamos preparar o dataset para a modelagem com base nos seguintes artigos:
- Previsão de Resultados de Jogos do Campeonato Brasileiro: Uma Abordagem de Mineração de Dados - Carlos Bezerra
- 1X2 – Previsão De Resultados De Jogos De Futebol - Luís Duarte
- Uso de Técnicas de Aprendizado de Máquina no Auxílio em Previsão de Resultados de Partidas de Futebol - Henrique Schmidt

Criaremos as seguintes colunas:
- TC-Empates_Casa
- TC-Jogos_Fora
- TC-Derrotas_Fora
- TC-Pontos
- TC-Ofensivo
- TV-Vitorias_Casa
- TV-Derrotas_Casa
- TV-Gols_Casa
- TV-Gols_Fora
- TV-Gols_Sofridos
- TV-Pontos
- TV-Defensivo
'''

abrir_datasets(data2015, data2016, data2017, data2018,data2019)

# Criando as colunas
print('Criando colunas dos datasets...')
criar_colunas(data2015)
criar_colunas(data2016)
criar_colunas(data2017)
criar_colunas(data2018)
criar_colunas(data2019)

print('Escrevendo os datasets...')
escrever_datasets(data2015, data2016, data2017, data2018,data2019)

print('Unindo datasets...')
df = pd.concat([data2015,data2016,data2017,data2018,data2019],ignore_index=True)

print('Informações do dataset final...')
print(df.info())
print('Head do dataset final...')
print(df.head())
df.to_csv('datasets/dataset_completo.csv')
print('Pronto!')
### Criar colunas count encoder, media das colocações ultimos 5, 3, 2 anos