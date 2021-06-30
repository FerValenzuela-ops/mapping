from sqlalchemy import create_engine
import pandas as pd
import mysql.connector
from mysql.connector import Error

archivocomunas = pd.read_csv('comunas.csv')
archivocomunas.head()

archivoregiones = pd.read_csv('regiones.csv')
archivoregiones.head()





con = mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin',
    database='establecimientos'

)
cursor = con.cursor()


codigocom = archivocomunas["codigo_comuna"]
nombrecom = archivocomunas["comuna_residencia"]
codregioncom = archivocomunas["codigo_region"]
regioncom = archivocomunas["region_residencia"]
fasecom = archivocomunas["Fase Comuna"]


codigoreg = archivoregiones["codigo_region"]
nombrereg = archivoregiones["region_residencia"]


for cod, nom, codreg,nomreg,comfase in zip(codigocom, nombrecom,codregioncom,regioncom,fasecom):
    query = cursor.execute("INSERT INTO establecimientos.comunas(id_comuna,nombre_comuna,codigo_region,region_comuna,fase_comuna) "
                           f"VALUES('{cod}','{nom}','{codreg}','{nomreg}', '{comfase}')")

# for cod, nom in zip(codigoreg, nombrereg):
#     query = cursor.execute("INSERT INTO establecimientos.regiones(id_region,nombre_region) "
#                            f"VALUES('{cod}','{nom}')")
con.commit()
