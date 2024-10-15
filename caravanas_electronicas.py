import streamlit as st
import pandas as pd
import mysql.connector
import chardet
from mysql.connector import Error
import traceback


st.title("Proyecto: Caravanas electronicas - Gestiones Ganaderas Individuales GGI")

DB_CONFIG = {
    'host': '200.58.127.65',
    'port': 33066,
    'database': 'caravanas',
    'user': 'root',
    'password': 'Tr0pema44cr34'
}

def conectar_bd():
    try:
        conexion = mysql.connector.connect(**DB_CONFIG)
        if conexion.is_connected():
            return conexion
    except Error as e:
        st.error(f"Error al conectar a MySQL: {e}")
        st.error(f"Detalles del error: {traceback.format_exc()}")
    return None

def insertar_datos(conexion, df):
    cursor = conexion.cursor()
    
    insert_tabla1 = """
    INSERT INTO z_animales (sexo, raza, origen, idv)
    VALUES (%s, %s, %s, %s)
    """
    
    insert_tabla2 = """
    INSERT INTO z_caravanas (ide, animal)
    VALUES (%s, %s)
    """
    
    insert_tabla3 = """
    INSERT INTO z_pesadas (caravana, fecha, peso, gdm, gpv)
    VALUES (%s, %s, %s, %s, %s)
    """
    
    try:
        datos_tabla1 = df[['sexo', 'raza', 'origen', 'idv']].values.tolist()
        cursor.executemany(insert_tabla1, datos_tabla1)
        
        #datos_tabla2 = df[['ide', 'animal']].values.tolist()
        #cursor.executemany(insert_tabla2, datos_tabla2)
        #
        #datos_tabla3 = df[['caravana', 'fecha', 'peso', 'gdm', 'gpv']].values.tolist()
        #cursor.executemany(insert_tabla3, datos_tabla3)
        
        conexion.commit()
    except Error as e:
        st.error(f"Error al insertar datos: {e}")
        st.error(f"Detalles del error: {traceback.format_exc()}")
        conexion.rollback()

    finally:
        cursor.close()

uploaded_file = st.file_uploader("Subir tu Caravana", type=['csv', 'xlsx', 'xls'])

if uploaded_file is not None:
    try:
        if uploaded_file.name.endswith('.csv'):
            raw_data = uploaded_file.read()
            result = chardet.detect(raw_data)
            encoding = result['encoding']
            df = pd.read_csv(uploaded_file, encoding=encoding)
        elif uploaded_file.name.endswith(('.xlsx', '.xls')):
            df = pd.read_excel(uploaded_file)
        else:
            st.error("Formato de archivo no soportado. Por favor, sube un archivo CSV o Excel.")
            st.stop()
        
        st.write(df)
        
        columnas_con_nulos = df.columns[df.isnull().any()].tolist()
        
        if columnas_con_nulos:
            st.warning(f"Las siguientes columnas contienen valores nulos: {', '.join(columnas_con_nulos)}")
        else:
            st.success("Todas las columnas están completas y no contienen valores nulos.")
        
        if st.button("Subir a la base de datos"):
            st.info("Iniciando proceso de subida a la base de datos...")
            conexion = conectar_bd()
            if conexion:
                insertar_datos(conexion, df)
                conexion.close()
                st.success("Conexión a la base de datos cerrada.")
    
    except Exception as e:
        st.error(f"Error al procesar el archivo: {str(e)}")
        st.error(f"Detalles del error: {traceback.format_exc()}")
        st.write("Por favor, asegúrate de que el archivo esté en el formato correcto y no esté dañado.")

st.info("Fin del script. Si no ves errores arriba, el script se ejecutó completamente.")