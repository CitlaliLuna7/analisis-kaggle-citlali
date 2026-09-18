import os
import pandas as pd

def ejecutar_analisis():
    data_path = os.path.join('data', 'datos_limpios.csv')
    if not os.path.exists(data_path):
        data_path = os.path.join('data', 'StudentsPerformance.csv')
        
    df = pd.read_csv(data_path)
    print("=== EXPLORACIÓN DE DATOS ===")
    print(f"Filas: {df.shape[0]} | Columnas: {df.shape[1]}")
    print("\nPrimeros registros:\n", df.head())

if __name__ == '__main__':
    ejecutar_analisis()
