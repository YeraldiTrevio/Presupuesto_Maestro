# Area de importacion.
import pandas as pd
import os
from plantillas import *
# Fin de area de importacion.

# Variables y lambdas.
LimpiarPantalla = lambda: os.system('clear')
# fin de variables y lambdas.

# Imprime la cedula 1.
def cedula_presupuesto_Ventas(mtz_presupuesto_ventas):
    plantilla_area_grande('Presupuesto De Ventas')

    # Creacion e impresion de data Frame
    mostrar_presupuesto_ventas = pd.DataFrame(mtz_presupuesto_ventas,\
        columns=['Nombre', 'Unidades Sem. 1','Unidades Sem. 2', 'Precio Sem. 1',
        'Precio Sem. 2', 'Importe Sem. 1','Importe Sem. 2', 'Total Por Producto'])
    print("\n",mostrar_presupuesto_ventas,"\n")
    # Fin de Creacion e impresion de data Frame
    plantilla_finalizacion_area_grande()
    input('\nPresiona Enter Para Continuar.')
    LimpiarPantalla()

# Imprime la cedula 2.
def cedula_Saldo_Cliente_y_Flujo_Entradas(periodo_actual, lista_saldo_Cliente_y_Flujo_Entradas):
    # Datos de Columnas
    saldo_Clientes_Anterior = f'Saldo De Clientes {periodo_actual-1}'
    ventas_Actual= f'Ventas {periodo_actual}'
    total_Clientes = f'Total Clientes {periodo_actual}'
    cobranza_anterior = f'Cobranza {periodo_actual-1}'
    cobranza_actual = f'Cobranza {periodo_actual}'
    totalEntradas = f'Total Entradas {periodo_actual}'
    saldo_Clientes_Actual = f'Saldo De Clientes {periodo_actual}'

    # Fin de Datos de Columnas
    plantilla_area_grande('Determinacion Del Saldo De Clientes y Flujo De Efectivo')
    # Creacion e impresion de data Frame
    mostrar_saldo_Cliente_y_Flujo_Entradas = pd.DataFrame(lista_saldo_Cliente_y_Flujo_Entradas,\
        columns=[saldo_Clientes_Anterior, ventas_Actual, total_Clientes, cobranza_anterior, 
        cobranza_actual, totalEntradas, saldo_Clientes_Actual])
    print("\n",mostrar_saldo_Cliente_y_Flujo_Entradas,"\n")
    # Fin de Creacion e impresion de data Frame

    plantilla_finalizacion_ExtraGrande()
    input('\nPresiona Enter Para Continuar.')
    LimpiarPantalla()

#Imprime la cedula 3 cambiar a algo similar que en la cedula 4.
def cedula_presupuesto_produccion(mtz_presupuesto_produccion):
    plantilla_area('Presupuesto De Produccion')
    # Creacion e Impresion de Data Frame
    mostrar_presupuesto_produccion = pd.DataFrame(mtz_presupuesto_produccion,\
        columns= ['Producto', 'Unidades Sem. 1', 'Unidades Sem. 2', 'Inventario Final Sem. 1',
        'Inventario Final Sem. 1', 'Total Unidades Sem. 1', 'Total Unidades Sem. 2',
         'Inventario Inicial Sem. 1', 'Inventario Inicial Sem. 2', 'Unidades Producir Sem. 1',
         'Unidades Producir Sem. 2', 'Total Unidades Producir'])
    # Fin de Creacion e Impresion de Data Frame
    print(mostrar_presupuesto_produccion)
    plantilla_finalizacion_area()
    input('\nPresiona Enter Para Continuar.')
    LimpiarPantalla()

# Imprime la cedula 4.
def cedula_requerimientos_materiales(mtz_requerimientos_materiales,mtz_total_requerimientos_materiales):
    # Funciones Locales
    def mtz(indice, elemento):
        return mtz_requerimientos_materiales[indice][elemento]

    def mtz1(indice, elemento):
        return mtz_total_requerimientos_materiales[indice][elemento]
    # Fin Funciones Locales

    # Recorrer mtz_requerimientos_materiales
    for requerimiento in mtz_requerimientos_materiales:
        i = mtz_requerimientos_materiales.index(requerimiento)
        for e in requerimiento:
            print(f"\n============================ Producto: {mtz(i,0)} ============================\n")
            print(f"                        1. Semestre                2. Semestre")
            print(f"Unidades a Producir\t    {mtz(i,1)}                  \t{mtz(i,2)}")
            print("\nMaterial A")
            print(f"Requerimiento Materal\t    {mtz(i,3)}                    \t{mtz(i,4)}")
            print(f"Total Material A Req.\t    {mtz(i,5)}                    \t{mtz(i,6)}")

            print("\nMaterial B")
            print(f"Requerimiento Materal\t    {mtz(i,7)}                    \t{mtz(i,8)}")
            print(f"Total Material B Req.\t    {mtz(i,8)}                    \t{mtz(i,10)}")

            print("\nMaterial C")
            print(f"Requerimiento Materal\t    {mtz(i,11)}                   \t{mtz(i,12)}")
            print(f"Total Material C Req.\t    {mtz(i,13)}                   \t{mtz(i,14)}")
            break
    # Fin del recorrido de mtz_requerimientos_materiales

    # Recorrer mtz_total_requerimientos_materiales
    platillaArea_SaltoLinea('Total De Requerimientos')
    print(f"                                  1. Semestre        2. Semestre")
    for materiales in mtz_total_requerimientos_materiales:
        i = mtz_total_requerimientos_materiales.index(materiales)
        for e in materiales:
            print(f"Total Material {mtz1(i,0)} Req.\t    {mtz1(i,1)}      \t{mtz1(i,2)}")
            break
    plantilla_Finalizacion_SaltoLinea()
    input('\nPresiona Enter Para Continuar.')
    LimpiarPantalla()
    # Fin Recorrido mtz_total_requerimientos_materiales