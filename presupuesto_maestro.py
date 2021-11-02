'''
    Este archivo contiene las funionalidad principal de todo el programa.
    Estas funciones son las que se utilizan para hacer el calculo del 
    presupuesto maestro, y que se encarga de guardar unica y exclusivamente
    los calculos del presupuesto maestro.
'''
# region importacion
import os
from plantillas import *
LimpiarPantalla = lambda: os.system('clear')
# endregion

# region definicion.
mtz_presupuesto_ventas = [
    ['CL', 12000, 10000, 300.00, 320.00, 3600000, 3200000, 6800000],
    ['CE', 13500, 11800, 280.00, 310.00, 3780000, 3658000, 7438000],
    ['CR', 7000, 8500, 185.00, 200.00, 1295000, 1700000, 2995000]              
]

lista_saldo_Cliente_y_Flujo_Entradas = [
    [80000, 17233000, 17313000, 80000, 13786400, 13866400, 3446600] 
]

mtz_presupuesto_produccion = [
    ['CL', 12000, 10000, 10000, 6500, 22000, 16500, 10000, 10000, 12000, 6500, 18500],
    ['CE', 13500, 11800, 8500, 7500, 22000, 7500, 8500, 8500, 13500, 10800, 24300],
    ['CR', 7000, 8500, 6000, 5000, 13000, 13500, 6000, 6000, 7000, 7500, 14500]
]

mtz_requerimientos_materiales = [
    ['CL', 12000, 6500, 1.0, 1.0, 12000.0, 6500.0, 0.5, 0.5, 6000.0, 
    3250.0, 10.0, 10.0, 120000.0, 65000.0],
    ['CE', 13500, 10800, 1.2, 1.2, 16200.0, 12960.0, 0.6, 0.6, 8100.0
    , 6480.0, 25.0, 25.0, 337500.0, 270000.0],
    ['CR', 7000, 7500, 2.0, 2.0, 14000.0, 15000.0, 1.0, 1.0, 7000.0
    , 7500.0, 5.0, 5.0, 35000.0, 37500.0]
]

mtz_total_requerimientos_materiales = [
    ['Material A', 42200.0, 34460.0], 
    ['Material B', 21100.0, 17230.0], 
    ['Material C', 492500.0, 372500.0]
]

# Funciones del presupuesto de venta
# Cedula 1
def presupuesto_ventas():
    # Ingreso de productos a vender
    while True:
        productos = input('Ingresa la cantidad de productos a vender: ')
        try:
            productos = int(productos)
            LimpiarPantalla()
            break
        except:
            print('\nPor Favor, ingrese solo un numero entero.')
            input('Presiona Enter para continuar ')
            LimpiarPantalla()
    # Fin de ingreso de productos a vender

    # Ingreso de los datos del presupuesto de ventas.
    plantilla_area('Presupuesto De Ventas')
    for producto in range(productos):
        print(f"\n============== Producto {producto + 1} ==============")
        nombre = input('Ingresa el nombre del producto: ')

        unidades_vender_1 = int(input('\nIngresa las unidades del 1. Semestre: '))
        unidades_vender_2 = int(input('Ingresa las unidades del 2. Semestre: '))
        
        precio_venta_1 = float(input('\nIngresa el precio de venta del 1. Semestre: '))
        precio_venta_2 = float(input('Ingresa el precio de venta del 2. Semestre: '))

        importe_venta_1 = unidades_vender_1 * precio_venta_1
        importe_venta_2 = unidades_vender_2 * precio_venta_2

        importe_venta_total = importe_venta_1 + importe_venta_2

        mtz_presupuesto_ventas.append([
            nombre,
            unidades_vender_1, unidades_vender_2,
            precio_venta_1, precio_venta_2,
            importe_venta_1, importe_venta_2,
            importe_venta_total,
            ])
    # Fin de ingreso de los datos del presupuesto de ventas.
    plantilla_Finalizacion_SaltoLinea()
    input('\nPresiona Enter Para Continuar.')
    LimpiarPantalla()

# Cedula 2
def determinacion_Saldo_Cliente_y_Flujo_Entradas(periodo_actual):
    # Extraccion e ingreso de datos de la cedula 1
    saldoClientesPasado = float(input(f'Ingresa el saldo de clientes del periodo {periodo_actual-1}: $'))
    ventasImporte = 0 
    for elementos in mtz_presupuesto_ventas:
        indice = mtz_presupuesto_ventas.index(elementos)
        for i in elementos:
            ventasImporte += mtz_presupuesto_ventas[indice][-1]
            break
    print(f'El importe de las ventas del periodo {periodo_actual} es de: ${ventasImporte}')

    totalClientesActual = saldoClientesPasado + ventasImporte

    cobranzaAnterior = saldoClientesPasado
    cobranzaActual = ventasImporte * 0.80
    entradasActual = cobranzaAnterior + cobranzaActual

    saldoClientesActual = +(totalClientesActual) - entradasActual

    lista_saldo_Cliente_y_Flujo_Entradas.append([
        saldoClientesPasado, ventasImporte,
        totalClientesActual,
        cobranzaAnterior, cobranzaActual,
        entradasActual,
        saldoClientesActual
    ])
     # Fin de Extraccion e ingreso de datos de la cedula 1

    plantilla_Finalizacion_SaltoLinea()
    input('Presiona Enter Para Continuar.')
    LimpiarPantalla()

# Cedula 3
def presupuesto_produccion():
    # Extraccionde datos de la cedula 2
    for elementos in mtz_presupuesto_ventas:
        indice = mtz_presupuesto_ventas.index(elementos)
        for i in elementos:
            nombre = mtz_presupuesto_ventas[indice][0]
            unidades_vender_1 = mtz_presupuesto_ventas[indice][1]
            unidades_vender_2 = mtz_presupuesto_ventas[indice][2]
            break
            # Fin de Extraccionde datos de la cedula 2

        # Ingreso de datos del presupuesto de produccion.
        print(f"\n============== Producto: {nombre} ==============")
        inventario_final_1 = int(input('Ingresa el inventario final del 1. semestre: '))
        inventario_final_2 = int(input('Ingresa el inventario final del 2. semestre: '))

        total_unidades_1 = unidades_vender_1 + inventario_final_1
        total_unidades_2 = unidades_vender_2 + inventario_final_2

        inventario_incial_1 = inventario_final_1
        inventario_incial_2 = inventario_final_1

        unidades_producir_1 = total_unidades_1 - inventario_incial_1
        unidades_producir_2 = total_unidades_2 - inventario_incial_2
        total_unidades_producir = unidades_producir_1 + unidades_producir_2

        mtz_presupuesto_produccion.append([
            nombre,
            unidades_vender_1, unidades_vender_2,
            inventario_final_1, inventario_final_2,
            total_unidades_1, total_unidades_2,
            inventario_incial_1, inventario_incial_2,
            unidades_producir_1, unidades_producir_2, total_unidades_producir
        ])
    # Fin de ingreso de datos del presupuesto de produccion.
    plantilla_Finalizacion_SaltoLinea()
    input('Presiona Enter Para Continuar.')
    LimpiarPantalla()

# Cedula 4
def requerimientos_materiales():
    # Creacion de contadores.
    total_rquerimiento_material_A_1 = 0
    total_rquerimiento_material_A_2 = 0
    total_rquerimiento_material_B_1 = 0
    total_rquerimiento_material_B_2 = 0
    total_rquerimiento_material_C_1 = 0
    total_rquerimiento_material_C_2 = 0
    # Fin de Creacion de contadores.

    # Extraccion de datos de la cedula 3
    for elementos in mtz_presupuesto_produccion:
        indice = mtz_presupuesto_produccion.index(elementos)
        for i in elementos:
            nombre = mtz_presupuesto_produccion[indice][0]
            unidades_producir_1 = mtz_presupuesto_produccion[indice][-3]
            unidades_producir_2 = mtz_presupuesto_produccion[indice][-2]
            total_unidades_producir = mtz_presupuesto_produccion[indice][-1]
            break
            # Fin de Extraccion de datos de la cedula 3
        # Ingreso de datos de requerimientos de materiales.
        print(f"\n============== Producto: {nombre} ==============\n")
        print(f'Unidades a producir del 1. Semestre: {unidades_producir_1}')
        print(f'Unidades a producir del 2. Semestre: {unidades_producir_2}')
        print(f'Unidades a producir: {total_unidades_producir}')

        material_A1 = float(input('\nIngresa el requerimiento de material A del smestre 1: '))
        material_A2 = float(input('Ingresa el requerimiento de material A del semestre 2: '))
        total_material_A1 = unidades_producir_1 * material_A1
        total_material_A2 = unidades_producir_2 * material_A2


        material_B1 = float(input('\nIngresa el requerimiento de material B del smestre 1: '))
        material_B2 = float(input('Ingresa el requerimiento de material B del semestre 2: '))
        total_material_B1 = unidades_producir_1 * material_B1
        total_material_B2 = unidades_producir_2 * material_B2

        material_C1 = float(input('\nIngresa el requerimiento de material C del smestre 1: '))
        material_C2 = float(input('Ingresa el requerimiento de material C del semestre 2: '))
        total_material_C1 = unidades_producir_1 * material_C1
        total_material_C2 = unidades_producir_2 * material_C2

        total_rquerimiento_material_A_1 += total_material_A1
        total_rquerimiento_material_A_2 += total_material_A2

        total_rquerimiento_material_B_1 += total_material_B1
        total_rquerimiento_material_B_2 += total_material_B2

        total_rquerimiento_material_C_1 += total_material_C1
        total_rquerimiento_material_C_2 += total_material_C2
        
        mtz_requerimientos_materiales.append([
            nombre,
            unidades_producir_1, unidades_producir_2,
            material_A1, material_A2, total_material_A1, total_material_A2,
            material_B1, material_B2, total_material_B1, total_material_B2,
            material_C1, material_C2, total_material_C1, total_material_C2,
        ])

    mtz_total_requerimientos_materiales.append(['Material A',
        total_rquerimiento_material_A_1, total_rquerimiento_material_A_2,])

    mtz_total_requerimientos_materiales.append(['Material B',
        total_rquerimiento_material_B_1, total_rquerimiento_material_B_2,])
    
    mtz_total_requerimientos_materiales.append(['Material C',
        total_rquerimiento_material_C_1, total_rquerimiento_material_C_2,])
    # Fin de ingreso de datos de requerimientos de materiales.
    
    plantilla_Finalizacion_SaltoLinea()
    input('Presiona Enter Para Continuar.')
    LimpiarPantalla()

# Cedula 5