'''
    Este arhivo es el encargado de imprimir las cedulas.
    Utilizando las matrices, y los datos que se van guardando
    en las mismas.
'''
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

#Imprime la cedula 3.
def cedula_presupuesto_produccion(mtz_presupuesto_produccion):
    plantilla_mediana('Presupuesto De Produccion')
    
    # Funciones locales
    def mtz(i,elemento):
        return mtz_presupuesto_produccion[i][elemento]
    # Fin de funciones locales

    # Impresion de la cedula
    for producto in mtz_presupuesto_produccion:
        i = mtz_presupuesto_produccion.index(producto)
        for e in producto:
            plantillas_Area_Msg_SL('Producto: ',mtz(i,0))
            print(f"                        1. Semestre                2. Semestre               Total\n")
            print(f"Unidades a Vender\t    {mtz(i,1)}                  \t{mtz(i,2)}")
            print(f"Inventario Final \t    {mtz(i,3)}                  \t{mtz(i,4)}")
            print(f"Total de Unidades\t    {mtz(i,5)}                  \t{mtz(i,6)}")
            print(f"Inventario Incial\t    {mtz(i,7)}                  \t{mtz(i,8)}")
            print(f"Unidades Producir\t    {mtz(i,9)}                  \t{mtz(i,10)}\t\t     {mtz(i,11)}")
            break
    # Fin de Impresion de la cedula
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
    plantilla_area('Presupuesto De Requerimiento De Materiales')
    # Recorrer mtz_requerimientos_materiales
    for requerimiento in mtz_requerimientos_materiales:
        i = mtz_requerimientos_materiales.index(requerimiento)
        for e in requerimiento:
            plantillas_Area_Msg_SL('Producto: ',mtz(i,0))
            print(f"                        1. Semestre                2. Semestre\n")
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

# Imprime la cedula 5.
def cedula_compras_materiales(mtz_compra_materiales, mtz_total_compra_materiales):
    # Funciones Locales
    def mtz(indice, elemento):
        return mtz_compra_materiales[indice][elemento]

    def mtz1(indice, elemento):
        return mtz_total_compra_materiales[indice][elemento]
    # Fin Funciones Locales
    plantilla_area('Presupuesto De Compras De Materiales')
    # Recorrer mtz_requerimientos_materiales
    for requerimiento in mtz_compra_materiales:
        i = mtz_compra_materiales.index(requerimiento)
        for e in requerimiento:
            plantillas_Area_Msg_SL('Producto: ',mtz(i,0))
            print(f"                           \t 1. Semestre                2. Semestre\n")
            print(f"Requerimiento de materiales\t    {mtz(i,1)}                  \t{mtz(i,2)}")
            print(f"(+)Inventario final        \t    {mtz(i,3)}                  \t{mtz(i,4)}")
            print(f"Total de Materiales        \t    {mtz(i,5)}                  \t{mtz(i,6)}")
            print(f"(-)inventario inicial      \t    {mtz(i,7)}                  \t{mtz(i,8)}")
            print(f"Material a comprar         \t    {mtz(i,9)}                  \t{mtz(i,10)}")
            print(f"Precio de compra           \t    {mtz(i,11)}                 \t{mtz(i,12)}")
            print(f"Total Material A en $.     \t    {mtz(i,13)}                 \t{mtz(i,14)}")
            break
    # Fin del recorrido de mtz_requerimientos_materiales
    for total in mtz_total_compra_materiales:
        i = mtz_total_compra_materiales.index(total)
        for e in total:
            plantilla_finalizacion_area()
            print(f"                           \t 1. Semestre                2. Semestre           Total")
            print(f"\nCompras Totales          \t    {mtz1(i,0)}              \t{mtz1(i,1)}   \t{mtz1(i,2)}\n")
            break
    
    plantilla_finalizacion_area()
    input('\nPresiona Enter Para Continuar.')
    LimpiarPantalla()

# Imprime la Cedula 6.
def cedula_saldo_proveedores_y_flujo_salida(periodo_actual, lista_saldo_proveedores_y_Flujo_Salida):
    #Datos de columnas
    SaldoProveedoresPasado = f'Saldo de Proveedores { periodo_actual - 1} '
    compras_actuales = f'Compras { periodo_actual }'
    total_proveedores_actual = f'Total Proveedores { periodo_actual }'
    salidaEfectivo_prov_pasado = f'Proveedores { periodo_actual - 1}'
    salidaEfectivo_prov_actual = f'Proveedores { periodo_actual }'
    total_salidas = f'Total Salidas { periodo_actual }'
    saldo_proveedores_actual = f'Saldo de Proveedores { periodo_actual }'

    #Fin de datos de columnas
    plantilla_area_grande ( 'Determinación del Saldo de Proveedores y Flujo de Efectivo ')
    #Datos
    mostrar_saldo_proveedores_y_flujo_salida = pd.DataFrame( lista_saldo_proveedores_y_Flujo_Salida,
        columns=[ SaldoProveedoresPasado, compras_actuales, total_proveedores_actual, salidaEfectivo_prov_pasado,
        salidaEfectivo_prov_actual, total_salidas, saldo_proveedores_actual])
    print ( "\n" , mostrar_saldo_proveedores_y_flujo_salida , "\n" )
    # Fin de Creación e impresión de marco de datos

    plantilla_finalizacion_ExtraGrande ()
    input ( '\n Presiona Enter Para Continuar.' )
    LimpiarPantalla ()

# Imprimir la cedula 7.
def cedula_mano_obra_directa(mtz_mano_obra_directa,mtz_total_horas_y_MOD):
    # Funciones Locales
    def mtz(indice, elemento):
        return mtz_mano_obra_directa[indice][elemento]

    def mtz1(indice, elemento):
        return mtz_total_horas_y_MOD[indice][elemento]
    # Fin Funciones Locales
    plantilla_area('Presupuesto De Mano De Obra Directa')
    # Recorrer mtz_mano_obra_directa
    for requerimiento in mtz_mano_obra_directa:
        i = mtz_mano_obra_directa.index(requerimiento)
        for e in requerimiento:
            print(f"\n============================ Producto: {mtz(i,0)} ============================\n")
            print(f"                                1. Semestre                    2. Semestre")
            print(f"Unidades a Producir\t            {mtz(i,1)}                    \t{mtz(i,2)}")
            print(f"Horas requeridas por unidad\t    {mtz(i,3)}                    \t{mtz(i,4)}")
            print(f"Total de horas requeridas\t      {mtz(i,5)}                    \t{mtz(i,6)}")
            print(f"Cuota por hora\t                   {mtz(i,7)}                    \t{mtz(i,8)}")
            print(f"Importe de M.O.D\t           {mtz(i,9)}                    \t{mtz(i,10)}")
            break
        # Fin del recorrido de mtz_requerimientos_materiales
    plantilla_finalizacion_area()
    print(f"                           \t 1. Semestre                2. Semestre           Total")
    print(f"\nTotal Horas              \t    {mtz1(0,0)}              \t{mtz1(0,1)}   \t{mtz1(0,2)}\n")
    print(f"Total M.O.D                \t    {mtz1(1,0)}              \t{mtz1(1,1)}   \t{mtz1(1,2)}\n")
    
    plantilla_finalizacion_area()
    input('\nPresiona Enter Para Continuar.')
    LimpiarPantalla()

# Imprimir la cedula 8.
def cedula_gastos_fabricacion(mtz_gastos_fabricacion):
    # Funciones locales
    def mtz(i,e):
        return mtz_gastos_fabricacion[i][e]
    # Fin Funciones locales
    plantilla_area('Presupuesto Gastos Indirectos De Fabricacion')
    # Impresion de la cedula
    for e in mtz_gastos_fabricacion:
        i = mtz_gastos_fabricacion.index(e)
        for iterador in mtz_gastos_fabricacion:
            print(f"                     1. Semestre               2. Semestre               Total\n")
            print(f"Depreciación         \t${mtz(i,0)}               \t${mtz(i,1)}               \t${mtz(i,2)}")
            print(f"Seguros              \t${mtz(i,3)}               \t${mtz(i,4)}               \t${mtz(i,5)}")
            print(f"Mantenimiento        \t${mtz(i,6)}               \t${mtz(i,7)}               \t${mtz(i,8)}")
            print(f"Energéticos          \t${mtz(i,9)}               \t${mtz(i,10)}              \t${mtz(i,11)}")
            print(f"Varios               \t${mtz(i,12)}              \t${mtz(i,13)}              \t${mtz(i,14)}")
            print(f"Total por semestre   \t${mtz(i,15)}              \t${mtz(i,16)}              \t${mtz(i,17)}")
            print(f"Total de G.I.F.                                                        \t${mtz(i,17)}")
            print(f"Total horas M.O.D. anual                                               \t${mtz(i,18)}")
            print(f"Costo Hora G.I.F.                                                      \t${mtz(i,19)}")
            break

    plantilla_finalizacion_area()
    input('\nPresiona Enter Para Continuar.')
    LimpiarPantalla()

# Imprimir la cedula 9.
def cedula_gastos_operacion(mtz_gastos_operacion):
    plantilla_mediana('Presupuesto de gastos de operación')
    
    # Funciones locales
    def mtz(i,e):
        return mtz_gastos_operacion[i][e]
    # Fin de funciones locales

    # Impresion de la cedula
    print(f"                          \t 1. Semestre                  2. Semestre               Total\n")
    print(f"Depreciación              \t   {mtz(0,0)}                 \t{mtz(0,1)}           \t{mtz(0,2)}")  
    print(f"Sueldos y salarios        \t   {mtz(0,3)}                 \t{mtz(0,4)}           \t{mtz(0,5)}")
    print(f"Comisiones                \t   {mtz(0,6)}                 \t{mtz(0,7)}           \t{mtz(0,8)}")
    print(f"Varios                    \t   {mtz(0,9)}                 \t{mtz(0,10)}          \t{mtz(0,11)}")
    print(f"Intereses por obligaciones\t   {mtz(0,12)}                \t{mtz(0,13)}          \t{mtz(0,14)}")
    print(f"Total                     \t   {mtz(0,15)}                \t{mtz(0,16)}          \t{mtz(0,17)}")

    plantilla_finalizacion_area()
    input('\nPresiona Enter Para Continuar.')
    LimpiarPantalla()

# Imprimir la cedula 10.
def cedula_costoUnitario_productosTerminados(mtz_costoUnitario_productosTerminados):
    # Funciones Locales
    def mtz(indice, elemento):
        return mtz_costoUnitario_productosTerminados[indice][elemento]
    # Fin Funciones Locales
    # Recorrer mtz_costoUnitario_productosTerminados
    plantilla_area('Determinacion Del Costo Unitario De Productos Terminados')
    for requerimiento in mtz_costoUnitario_productosTerminados:
        i = mtz_costoUnitario_productosTerminados.index(requerimiento)
        for e in requerimiento:
            print(f"\n===================================== Producto: {mtz(i,0)} ====================================\n")
            print(f"                                \t1. Costo     2. Cantidad\tCosto Unitario\n")
            print(f"Material A                      \t ${round(mtz(i,1),2)}        \t{round(mtz(i,2),2)}           \t    ${round(mtz(i,3),2)}")
            print(f"Material B                      \t ${round(mtz(i,4),2)}        \t{round(mtz(i,5),2)}           \t    ${round(mtz(i,6),2)}")
            print(f"Material C                      \t ${round(mtz(i,7),2)}        \t{round(mtz(i,8),2)}           \t    ${round(mtz(i,9),2)}")
            print(f"Mano de obra                    \t ${round(mtz(i,10),2)}       \t{round(mtz(i,11),2)}          \t    ${round(mtz(i,12),2)}")
            print(f"Gastos indirectos de fabricacion\t ${round(mtz(i,13),2)}       \t{round(mtz(i,11),2)}          \t    ${round(mtz(i,14),2)}")
            print(f"Costo unitario                                                         \t    ${round(mtz(i,15),2)}")
            break   
    plantilla_finalizacion_area()
    input('\nPresiona Enter Para Continuar.')
    LimpiarPantalla()

# Impresion de la cedula 11.
def cedula_validacion_inventarios_finales(mtz_validacion_inventarios_finales):
    pass