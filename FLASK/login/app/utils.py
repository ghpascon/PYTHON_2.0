import pandas as pd
import pytz
import json
from datetime import datetime, date

def get_df(cdr_log):
    df_data = []

    for line in cdr_log:
        data_features = line.split(',')
        df_data.append(data_features)

    return pd.DataFrame(df_data)

def get_data():
    try:
        # Abrindo e carregando o arquivo JSON
        with open('config/config.json', 'r') as file:
            config = json.load(file)
            file_path = config["cdr_path"]
            with open(file_path, "r", encoding="utf-8") as arquivo:
                cdr_log = []
                for linha in arquivo:
                    if linha != '\n': cdr_log.append(linha)
            return get_df(cdr_log)
    except:
        return None


def treat_df(df_raw):
    #DATE
    date = pd.to_datetime(df_raw[3])
    original_timezone = pytz.utc
    br_timezone = pytz.timezone('America/Sao_Paulo')
    date_br = [dat.replace(tzinfo=original_timezone).astimezone(br_timezone) for dat in date]

    #DURACAO
    duracao = df_raw[2].copy().replace('','NULL')

    #CHAIN
    chain = []
    for call in df_raw[20]:
        if call is None: 
            chain.append('-')
            continue
        call = call.replace('Chain:','')
        chain.append(call)

    #CHAIN_END
    chain_end = [call.split(';')[-2 if len(call) > 1 else -1] for call in chain]

    #TERMINATED
    terminated = df_raw[7].copy()

    #STATUS
    status = []
    for sts in chain_end:
        if sts == '-':
            status.append('ERRO')
        elif sts.startswith('Ext.8'):
            status.append('NA')
        elif sts == 'EndCall': 
            status.append('ENDCALL')
        else:
            status.append('ATENDIDA')

    #DF
    df = pd.DataFrame()
    df['date'] = date_br
    df['duration'] = duracao
    df['chain'] = chain
    df['chain_end'] = chain_end
    df['terminated'] = terminated
    df['status'] = status
    return df

def get_interval_data(period):
    if period is None:
        return None
    
    if period == 'todo o periodo':
        return None
    if period == 'hoje':
        return ((date.today().strftime('%Y-%m-%d'), date.today().strftime('%Y-%m-%d')))
    
    if period == 'este mes':
        return (date(date.today().year, date.today().month, 1).strftime('%Y-%m-%d'), date.today().strftime('%Y-%m-%d'))
    
    if period == 'este ano':
        return (date(date.today().year, 1, 1).strftime('%Y-%m-%d'), date.today().strftime('%Y-%m-%d'))
    
    if period.startswith('intervalo personalizado'):
        parts = period.split('|')
        data_inicial = parts[0].split(':')[1].strip()
        data_final = parts[1].strip()
        return (str(data_inicial), str(data_final))
    
    return None


def get_interval(df, period=None):
    interval = get_interval_data(period)
    print('data',interval)
    if interval is None:
        return df
    return df[(df['date'] >= interval[0]) & (df['date'] <= interval[1])]

def get_status_df(df, status):
    if status == 0 or status is None:
        return df
    
    if status == 1:
        return df[(df['status'] == 'ATENDIDA')]
    
    if status == 2:
        return df[(df['status'] == 'NA')]
    
    if status == 3:
        return df[(df['status'] == 'ENDCALL')]
    
    # Caso o status não seja nenhum dos acima, retornar o DataFrame original
    return df