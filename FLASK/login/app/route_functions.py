import json
from flask import Flask,flash, render_template, request, redirect, url_for, session, jsonify
from app import utils
import pandas as pd

selected_period = None
status_selected = None

def functions(app):
    interval_df=None
    @app.route('/update-period', methods=['POST'])
    def update_period():
        global selected_period
        data = request.get_json()
        periodo = data.get('periodo')
        start_date = data.get('start_date')
        end_date = data.get('end_date')

        selected_period=periodo
        
        if periodo == "intervalo personalizado":
            selected_period+=f": {start_date} | {end_date}"

        print(f"Período selecionado: {selected_period}")

        return jsonify({"message": "Período atualizado com sucesso!"})
    
    @app.route('/get_period_label', methods=['GET'])
    def get_period_label():
        return jsonify({"periodo_selecionado": f"Periodo Selecionado: {selected_period}"})

    @app.route('/get_name_label', methods=['GET'])
    def get_name_label():
        name = session['user']
        return jsonify({"name": f"{name}"})

    
    @app.route('/data_table_att', methods=['GET'])
    def data_table_att():
        global status_selected

        try:
            df = utils.get_data()
            df = utils.treat_df(df)
            interval_df = utils.get_interval(df, selected_period)
            status_df = utils.get_status_df(interval_df, int(status_selected))

            # Verificar se status_df existe e não é None
            if status_df is not None:
                # Obter os cabeçalhos (colunas) do DataFrame
                columns = status_df.columns.tolist()

                # Obter as linhas do DataFrame
                rows = status_df.values.tolist()

                # Definindo a cor do cabeçalho (por exemplo, cor em hex)
                colors = [
                    '#ffffff',
                    '#00ff00',
                    '#ff0000',
                    '#ffff00',
                ]
                header_color = colors[int(status_selected)]  # Altere para a cor desejada

                # Combinando o cabeçalho com as linhas de dados
                table_data = {
                    'header_color': header_color,  # Inclui a cor do cabeçalho
                    'columns': columns,  # Colunas
                    'rows': rows  # Linhas
                }

                # Retornando como JSON
                return jsonify(table_data)
            else:
                # Criar um DataFrame vazio e retornar
                empty_df = pd.DataFrame()
                return jsonify({'header_color': "", 'columns': [], 'rows': empty_df.values.tolist()})

        except Exception as e:
            # Caso haja algum erro, cria um DataFrame vazio e retorna
            empty_df = pd.DataFrame()
            return jsonify({'header_color': "", 'columns': [], 'rows': empty_df.values.tolist()})
        

    @app.route('/get-squares-data', methods=['GET'])
    def get_squares_data():
        df = utils.get_data()
        df = utils.treat_df(df)
        interval_df = utils.get_interval(df, selected_period)
        status = interval_df['status']

        # Criar a lista squares_data com base nas contagens dos status
        squares_data = [
        {"color": "#cccccc", "label": "TOTAL", "number": int(len(status))},
        {"color": "#00ff00", "label": "ATENDIDA", "number": int(status[status == 'ATENDIDA'].count())},
        {"color": "#ff0000", "label": "NA", "number": int(status[status == 'NA'].count())},
        {"color": "#ffff00", "label": "ENDCALL", "number": int(status[status == 'ENDCALL'].count())}
        ]
        # Retorna os dados dos quadrados como JSON
        return jsonify({"squares": squares_data})
    
    @app.route('/bt_pressed', methods=['GET'])
    def bt_pressed():
        global status_selected
        status_selected = request.args.get('button')

        print(f"Botão {status_selected} foi pressionado!")
        
        return f"Botão {status_selected} foi pressionado!", 200
