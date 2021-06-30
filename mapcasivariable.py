import geopy
from geopy.geocoders import ArcGIS
import pandas as pd
import folium
import mysql.connector

nom = ArcGIS()

con = mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin',
    database='establecimientos'

)

cursor = con.cursor(buffered=True)

print('Hola, porfavor ingresa los datos de tu negocio. ')
nombre_establecimiento = input('Ingresa el nombre: ').capitalize()
direccion_establecimiento = input('Ingresa la direccion: ').capitalize()
comuna_establecimiento = input('Ingresa la comuna: ').capitalize()
horario_establecimiento = input('Ingresa el horario atencion: ').capitalize()


coordenadas = nom.geocode(f'{direccion_establecimiento}, {comuna_establecimiento}')
latitud = coordenadas.latitude
longitud = coordenadas.longitude


query1 = cursor.execute(f"select comunas.fase_comuna from establecimientos.comunas where nombre_comuna = '{comuna_establecimiento}';")
fasecomuna = list(*cursor.fetchall())


query = cursor.execute("INSERT INTO establecimientos.negocios(nombre,direccion,comuna,horario,latitud,longitud,fasecomuna)"
            f"VALUES('{nombre_establecimiento}','{direccion_establecimiento}','{comuna_establecimiento}' , '{horario_establecimiento}' ,  '{latitud}' , '{longitud}', '{fasecomuna[0]}' )")

con.commit()


df = pd.read_sql('SELECT * FROM negocios', con=con)
df_lat = list(df["latitud"])
df_lon = list(df["longitud"])
df_nombre_negocio = list(df["nombre"])
df_direccion_negocio = list(df['direccion'])
df_comuna_negocio = list(df['comuna'])
df_fase_comuna_negocio = list(df['fasecomuna'])

df2 = pd.read_sql(
    'SELECT nombre_comuna, fase_comuna FROM comunas where codigo_region = 13', con=con)
df2_nombre_comuna = list(df2["nombre_comuna"])
df2_fase_comuna = list(df2["fase_comuna"])

my_santiago_info = pd.read_sql(
    'SELECT * FROM comunas where codigo_region = 13', con=con)
my_santiago_info.to_csv('my_santiago_info.csv', index=False)

my_info = r'csvs/my_santiago_info.csv'
my_info = pd.read_csv(my_info)


mymap = folium.Map(location=[-33.40, -70.60],
                   zoom_start=12,)


def color_marcador(fase):
    if fase == '1':
        return 'red'
    elif fase == '2':
        return 'orange'
    elif fase == '3':
        return 'green'
    else:
        return 'blue'


mymap = folium.Map(location=[-33.40, -70.60],
                   zoom_start=12, tiles='Stamen Terrain')





fg = folium.FeatureGroup(name='Establecimientos')
for (lt, ln, nom, direccionegocio, com_negocio, fase_neg) in zip(df_lat, df_lon, df_nombre_negocio, df_direccion_negocio, df_comuna_negocio, df_fase_comuna_negocio):
    fg.add_child(folium.Marker(location=[lt, ln], popup=(nom + '\nDireccion: ' + direccionegocio + '\nComuna: ' +
                 com_negocio + '\nFase: ' + fase_neg), icon=folium.Icon(icon='info-sign', color=color_marcador(fase_neg))))

folium.Choropleth(geo_data='jsons/all.json',
                    name="Fases",
                    data=my_info,
                    columns=['nombre_comuna', 'fase_comuna'],
                    key_on="feature.properties.NOM_COM",
                    fill_color= 'RdYlGn',  # YlOrRd  RdYlGn YlGn
                    fill_opacity=0.7,
                    line_opacity=0.2,
                    legend_name="Fases en Santiago",
                    
                    reset=True).add_to(mymap)

mymap.add_child(fg)
mymap.add_child(folium.LayerControl())
mymap.save('MapaConDb.html')
