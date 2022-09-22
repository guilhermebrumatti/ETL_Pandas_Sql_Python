import pandas as pd
import sqlite3

#Abro o arquivo world_population.csv
df = pd.read_csv('world_population.csv')

#removendo colunas indesejadas
del df['2015 Population']
del df["2010 Population"]
del df["2000 Population"]
del df["1990 Population"]
del df["1980 Population"]
del df["1970 Population"]

#Conectando ao banco de dados no sqlite3
database = "world_population.sqlite"
conn = sqlite3.connect(database)

#O 'to_sql' exporta o conteúdo da tabela csv para o banco Sqlite3, de maneira automática
df.to_sql(name='tabela', con=conn, if_exists="replace", index=True)

sql = ('SELECT \
    "Rank", \
        "CCA3", \
            "Country", \
                "Capital", \
                    "Continent", \
                        "2022 Population", \
                            "2020 Population", \
                                "Area (km²)", \
                                    "Density (per km²)", \
                                        "Growth Rate", \
                                            "World Population Percentage" \
                                                FROM \
                                                    tabela \
                                                        ORDER BY \
                                                            Rank ASC')

#O read_sql cria um DataFrame através da QUERY acima.
df2 = pd.read_sql(sql, conn)

#Exporto o DataFrame gerado a partir da consulta a tabela no Sqlite, em arquivo .xlsx
df2.to_excel("conteudo_do_bd.xlsx", encoding="UTF-8")
conn.close()