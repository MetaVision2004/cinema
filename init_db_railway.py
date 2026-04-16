import os
import mysql.connector

# Por favor, reemplaza estos valores con los datos de "Public Connection" de Railway
# Los encuentras haciendo clic en el botón morado "Connect" en el panel de Railway > pestaña TCP Proxy
HOST = input("Ingresa el host público de Railway (ej. viaduct.proxy.rlwy.net): ")
PORT = int(input("Ingresa el puerto público de Railway (ej. 12345): "))
USER = 'root'
PASSWORD = input("Ingresa el password de la base de datos: ")
DATABASE = 'cinema'

def run_sql_file():
    print(f"Conectando a la base de datos en {HOST}:{PORT}...")
    try:
        conn = mysql.connector.connect(
            host=HOST,
            port=PORT,
            user=USER,
            password=PASSWORD,
            database=DATABASE
        )
        cursor = conn.cursor()
        
        with open('cinema.sql', 'r', encoding='utf-8') as f:
            sql_file = f.read()
            
        print("Leyendo el archivo cinema.sql...")
        
        # Separar las sentencias SQL
        sql_commands = sql_file.split(';')
        
        print("Ejecutando sentencias...")
        for command in sql_commands:
            try:
                if command.strip() != '':
                    cursor.execute(command)
            except Exception as e:
                print(f"Error en instruccion: {e}")
                
        conn.commit()
        cursor.close()
        conn.close()
        
        print("✅ ¡La base de datos se ha importado exitosamente en Railway!")
    except Exception as e:
        print(f"❌ Error al conectar o importar: {e}")

if __name__ == "__main__":
    run_sql_file()
