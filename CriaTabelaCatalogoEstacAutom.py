# -*- coding: utf-8 -*-
"""
Created on Fri May 31 19:41:50 2024

@author: celre
"""

import mysql.connector
import csv

# Conexão com o banco de dados MySQL
conn = mysql.connector.connect(
    host='108.167.188.170',
    user='mectsu42_lakare',
    password='Fiap@2024',
    database='mectsu42_chuvaseguraSP'
)
cursor = conn.cursor()

# Comando para criar a tabela
create_table_query = """
CREATE TABLE estacoes_metereologicas (
    DC_NOME VARCHAR(255),
    SG_ESTADO VARCHAR(2),
    CD_SITUACAO VARCHAR(10),
    VL_LATITUDE FLOAT,
    VL_LONGITUDE FLOAT,
    VL_ALTITUDE FLOAT,
    DT_INICIO_OPERACAO DATE,
    CD_ESTACAO VARCHAR(10)
)
"""
cursor.execute(create_table_query)

# Carregar dados do arquivo CSV para a tabela
with open('CatalogoEstaçõesAutomáticas.csv', 'r') as file:
    data = csv.reader(file, delimiter=';')
    next(data)  # Pular o cabeçalho do CSV
    for row in data:
        insert_query = "INSERT INTO estacoes_metereologicas VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(insert_query, row)

conn.commit()

# Fechar a conexão
conn.close()
