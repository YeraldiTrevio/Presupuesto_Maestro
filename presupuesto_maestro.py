'''
    Este archivo contiene las funionalidad principal de todo el programa.
    Estas funciones son las que se utilizan para hacer el calculo del 
    presupuesto maestro, y que se encarga de guardar unica y exclusivamente
    los calculos del presupuesto maestro.
'''
# Area de importacion
import os
from plantillas import *
# Fin de area de importacion

# Variables y Lambas.
LimpiarPantalla = lambda: os.system('clear')

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

mtz_compra_materiales = [
    ['Material A', 42200.0, 34460.0, 5000, 3000, 47200.0, 37460.0,
     5000, 5000, 42200.0, 32460.0, 10.0, 12.0, 422000.0, 389520.0], 
    ['Material B', 21100.0, 17230.0, 3000, 2500, 24100.0, 19730.0,
     3000, 3000, 21100.0, 16730.0, 2.0, 3.0, 42200.0, 50190.0],
    ['Material C', 492500.0, 372500.0, 2000, 1800, 494500.0, 374300.0, 
     2000, 2000, 492500.0, 372300.0, 1.0, 2.0, 492500.0, 744600.0] 
]

mtz_total_compra_materiales = [
    [956700.0, 1184310.0, 2141010.0]
]

mtz_saldo_Proveedores_y_Flujo_Entradas = [
    [33500.0, 2141010.0, 2174510.0, 33500.0, 1070505.0, 1104005.0, 1070505.0]
]

mtz_mano_obra_directa =[
    ['CL', 12000, 6500, 18500, 2.0, 2.0, 2.0, 24000.0, 13000.0, 37000.0, 15.0, 18.0,
    360000.0, 234000.0, 594000.0],
    ['CE', 13500, 10800, 24300, 1.0, 1.0, 1.0, 13500.0, 10800.0, 24300.0, 15.0, 18.0,
    202500.0, 194400.0, 396900.0],
    ['CR', 7000, 7500, 14500, 1.5, 1.5, 1.5, 10500.0, 11250.0, 21750.0, 15.0, 18.0, 
    157500.0, 202500.0, 360000.0]
]

mtz_total_horas_y_MOD =[
    # Horas
    [48000.0, 35050.0, 83050.0],
    # MOD
    [720000.0, 630900.0, 1350900.0]
]

mtz_gastos_indirectos_fab = [
    [40000.0, 40000.0, 80000.0,
    12500.0, 12500.0, 25000.0,
    33000.0, 25000.0, 58000.0,
    40000.0, 35000.0, 75000.0,
    12500.0, 12500.0, 25000.0, 
    138000.0, 125000.0, 263000.0,
    83050.0,
    3.17]
]

mtz_gastos_operacion = [
    [7500.0, 7500.0, 15000.0, 125000.0, 125000.0, 250000.0,
    86750.0, 85580.0, 172330.0, 10000.0, 8000.0, 18000.0, 2500.0,
    2500.0, 5000.0, 231750.0, 228580.0, 460330.0]
]
# Fin de variables y lambdas.

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
    porcentaje_cobranzaAnterior = float(input\
        (f'Ingresa el porcentaje de cobranza del {periodo_actual -1}: ')) /100
    cobranzaAnterior *= porcentaje_cobranzaAnterior

    porcetaje_cobranzaActual = float(input \
        (f'Ingresa el porcentaje de cobranza del {periodo_actual}: ')) / 100
    cobranzaActual = ventasImporte * porcetaje_cobranzaActual

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
def presupuesto_compra_materiales():
    # Creacion de contadores.
    compras_totales_1 = 0
    compras_totales_2 = 0
    compras_totales = 0
    # Extraccion de datos de la cedula 4.
    for material in mtz_total_requerimientos_materiales:
        i = mtz_total_requerimientos_materiales.index(material)
        for requerimiento in material:
            nombre_material = mtz_total_requerimientos_materiales[i][0]
            requerimiento_1 = mtz_total_requerimientos_materiales[i][1]
            requerimiento_2 = mtz_total_requerimientos_materiales[i][2]
            break
        # Fin de Extraccion de datos de la cedula 4.

    # Ingreso de datos del presupuesto de compra de materiales.
        platillaArea_SaltoLinea(nombre_material)

        inventario_final_1 = int(input('\nIngresa el inventario final del 1. Semestre: '))
        total_material_1 = requerimiento_1 + inventario_final_1
        inventario_final_2 = int(input('Ingresa el inventario final del 2. Semestre: '))
        total_material_2 = requerimiento_2 + inventario_final_2

        inventario_inicial_1 = int(input('\nIngresa el inventario inicial del 1. Semestre: '))
        material_comprar_1 = +(total_material_1 - inventario_inicial_1)
        inventario_inicial_2 = int(input('Ingresa el inventario inicial del 2. Semestre: '))
        material_comprar_2 = +(total_material_2 - inventario_inicial_2)

        precio_compra_1 = float(input('\nIngresa el precio de compra del 1. Semestre: '))
        total_material_dinero_1 = material_comprar_1 * precio_compra_1
        precio_compra_2 = float(input('Ingresa el precio de compra del 2. Semestre: '))
        total_material_dinero_2 = material_comprar_2 * precio_compra_2
    
        compras_totales_1 += total_material_dinero_1
        compras_totales_2 += total_material_dinero_2       

        # Almacenamiento de datos en matrices.
        mtz_compra_materiales.append([
            nombre_material,
            requerimiento_1, requerimiento_2,
            inventario_final_1, inventario_final_2,
            total_material_1, total_material_2,
            inventario_inicial_1, inventario_inicial_2,
            material_comprar_1, material_comprar_2,
            precio_compra_1, precio_compra_2, 
            total_material_dinero_1, total_material_dinero_2,
        ])
    
    compras_totales = compras_totales_1 + compras_totales_2
    mtz_total_compra_materiales.append([
        compras_totales_1,
        compras_totales_2,
        compras_totales])
    # Fin de ingreso de datos del presupuesto de compra de materiales.

# Cedula 6.
def determinacion_saldo_proveedores_flujo_salida(periodo_actual):
    # Ingreso del saldo pasado
    SaldoProveedoresPasado = float(input(f'\nIngresa el saldo de proveedores del periodo {periodo_actual-1}: $'))
    # Extraccion de datos de la cedula 5.
    compras_actuales = mtz_total_compra_materiales[0][-1]
    print(f'\nEl importe de las ventas del periodo {periodo_actual} es de: ${compras_actuales}')
    # Fin Extraccion de datos de la cedula 5.

    # Ingreso de datos de salidas actuales y pasadas.
    total_proveedores_actual = SaldoProveedoresPasado + compras_actuales

    salidaEfectivo_prov_pasado = SaldoProveedoresPasado
    porcentaje_prov_pasado = float(input\
    (f'\nIngresa el porcentaje de salida de proveedores del {periodo_actual -1}: ')) /100
    salidaEfectivo_prov_pasado *= porcentaje_prov_pasado


    salidaEfectivo_prov_actual = compras_actuales
    porcetaje_cobranzaActual = float(input \
        (f'\nIngresa el porcentaje de salida de proveedores del {periodo_actual}: ')) / 100
    salidaEfectivo_prov_actual *= porcetaje_cobranzaActual
    # fin de ingreso de datos de salidas actuales y pasadas.

    # Calculos para la cedula
    total_salidas = salidaEfectivo_prov_pasado + salidaEfectivo_prov_actual

    saldo_proveedores_actual = +(total_proveedores_actual) - total_salidas
    # Fin de calculos para la cedula.

    mtz_saldo_Proveedores_y_Flujo_Entradas.append([
        SaldoProveedoresPasado, compras_actuales, total_proveedores_actual,
        salidaEfectivo_prov_pasado, salidaEfectivo_prov_actual, total_salidas,
        saldo_proveedores_actual
    ])

# Cedula 7
def mano_obra_directa():
    # Creacion de contadores.
    total_mod_1 = 0
    total_mod_2 = 0
    total_mod = 0

    CONT_total_horas_requerias_1 = 0
    CONT_total_horas_requerias_2 = 0
    CONT_total_horas_requerias = 0
    # Fin de creacion de contadores.

    # Extraccion de datos de la cedula 3.
    for producto in mtz_presupuesto_produccion:
        i = mtz_presupuesto_produccion.index(producto)
        for e in producto:
            nombre_producto = mtz_presupuesto_produccion[i][0]
            unidades_producir_1 = mtz_presupuesto_produccion[i][-3]
            unidades_producir_2 = mtz_presupuesto_produccion[i][-2]
            unidades_producir = mtz_presupuesto_produccion[i][-1]
            break
        # Fin de extraccion de datos de la cedula 3.
        plantillas_Area_Msg_SL('Producto:', nombre_producto)
        # Ingreso de datos de mano de obra directa.
        horas_requeridas_1 = float(input('\nIngresa las horas requeridas del 1. Semestre: '))
        horas_requeridas_2 = float(input('Ingresa las horas requeridas del 2. Semestre: '))
        horas_requeridas = horas_requeridas_1
        total_horas_requeridas_1 = +(horas_requeridas_1)*(unidades_producir_1)
        total_horas_requeridas_2 = +(horas_requeridas_2)*(unidades_producir_2)
        total_horas_requeridas = +(horas_requeridas)*(unidades_producir)

        cuota_hora_1 = float(input('\nIngresa la cuota por hora del 1. Semestre: $'))
        cuota_hora_2 = float(input('Ingresa la cuota por hora del 2. Semestre: $'))
        importe_MOD_1 = +(total_horas_requeridas_1)*(cuota_hora_1)
        importe_MOD_2 = +(total_horas_requeridas_2)*(cuota_hora_2)
        importe_MOD = +(importe_MOD_1) + (importe_MOD_2)
        # Fin de ingreso de datos de mano de obra directa.

        # Incremento de contadores.
        total_mod_1 += importe_MOD_1
        total_mod_2 += importe_MOD_2
        total_mod += importe_MOD

        CONT_total_horas_requerias_1 += total_horas_requeridas_1
        CONT_total_horas_requerias_2 += total_horas_requeridas_2
        CONT_total_horas_requerias += total_horas_requeridas
        # Fin de incremento de contadores.

        # Ingreso de datos de mano de obra directa.
        mtz_mano_obra_directa.append([
            nombre_producto,
            unidades_producir_1, unidades_producir_2, unidades_producir,
            horas_requeridas_1, horas_requeridas_2, horas_requeridas,
            total_horas_requeridas_1, total_horas_requeridas_2, total_horas_requeridas,
            cuota_hora_1, cuota_hora_2,
            importe_MOD_1, importe_MOD_2, importe_MOD
        ])
        # Fin de ingreso de datos de mano de obra directa.

    # Ingreso de datos totales de mano de obra directa.
    mtz_total_horas_y_MOD.append([
        CONT_total_horas_requerias_1, CONT_total_horas_requerias_2,
        CONT_total_horas_requerias
    ])

    mtz_total_horas_y_MOD.append([
        total_mod_1, total_mod_2, total_mod
    ])
    # Fin de ingreso de datos totales de mano de obra directa.

#Cedula 8 
def gastos_indirectos_fabricacion():
    deprec1er = float(input(f'\nIngrese los gastos de depreciación del primer semestre: ')) 
    deprec2do = float(input(f'Ingrese los gastos de depreciacion del segundo semestre: '))   
    total_deprec = deprec2do + deprec2do

    segur1er = float(input(f'\nIngrese los gastos de los seguros del primer semestre: '))
    segur2do = float(input(f'Ingrese los gastos de los seguros del segundo semestre: '))
    total_segur = segur1er + segur2do

    manten1er = float(input(f'\nIngrese los gastos de mantenimiento del primer semestre: '))
    manten2do = float(input(f'Ingrese los gastos mantenimiento del segundo semestre: '))
    total_manten = manten1er + manten2do

    energ1er = float(input(f'\nIngrese los gastos de energéticos de primer semestre: '))
    energ2do = float(input(f'Ingrese los gastos de energéticos de segundo semestre: '))
    total_energ = energ1er + energ2do

    var1er = float(input(f'\nIngrese los gastos de varios del primer semestre: '))
    var2do = float(input(f'Ingrese los gastos de varios del segundo semestre: '))
    total_var = var1er + var2do

    total_gif_semestre1 = deprec1er + segur1er + manten1er + energ1er + var1er
    total_gif_semestre2 = deprec2do + segur2do + manten2do + energ2do + var2do

    total_gif_semestres = total_gif_semestre1 + total_gif_semestre2
    total_horas_mod_anual = mtz_total_horas_y_MOD[0][-1]
    costo_hora_gif = round((total_gif_semestres / total_horas_mod_anual),2)

    print(f'\nEl costo por hora de gif es: {costo_hora_gif}')

    mtz_gastos_indirectos_fab.append([
        deprec1er, deprec2do, total_deprec,
        segur1er, segur2do, total_segur,
        manten1er, manten2do, total_manten,
        energ1er, energ2do, total_energ,
        var1er, var2do, total_var,
        total_gif_semestre1, total_gif_semestre2,
        total_gif_semestres, 
        total_horas_mod_anual,
        costo_hora_gif
    ])

#Cédula 9
def presupuesto_gastos_operacion():
    print("Presupuesto de gastos de operación\n")
    Depr1er = float(input("\nEscribe la cantidad de depreciación del 1er semestre: "))
    Depr2do = float(input("Escribe la cantidad de depreciación del 2do semestre: "))
    TotalDepr=(Depr1er+Depr2do)
    print("Total de Depreciación: ", TotalDepr)

    SueldoySal1er = float(input("\nEscribe la cantidad de sueldos y salarios del 1er semestre: "))
    SueldoySal2do = float(input("Escribe la cantidad de sueldos y salarios del 1er semestre: "))
    TotalSuelySal=(SueldoySal1er+SueldoySal2do)
    print("Total de Sueldos y Salarios: ", TotalSuelySal)

    Comisiones1er = float(input("\nEscribe la cantidad de Comisiones del 1er semestre: "))
    Comisiones2do=float(input("Escribe la cantidad de Comisiones del 2do semestre: "))
    TotalComisiones=(Comisiones1er+Comisiones2do)
    print("Total de Comisiones: ", TotalComisiones) 

    Gastosvar1er = float(input("\nEscribe la cantidad de gastos Varios del 1er semestre: "))
    Gastosvar2do = float(input("Escribe la cantidad de gastos Varios del 2do semestre: "))
    TotalVarios=(Gastosvar1er+Gastosvar2do)
    print("Total de gastos Varios: ", TotalVarios) 

    Intereses1ero = float(input("\nEscribe la cantidad de intereses por obligaciones del 1er semestre: "))
    Intereses2do = float(input("Escribe la cantidad de intereses por obligaciones del 2do semestre: "))
    TotalIntereses=(Intereses1ero+Intereses2do)
    print("Total de intereses por obligaciones", TotalIntereses)

    Total_gastos_operacion_1 = Depr1er + SueldoySal1er + Comisiones1er + Gastosvar1er + Intereses1ero
    Total_gastos_operacion_2 = Depr2do + SueldoySal2do + Comisiones2do + Gastosvar2do + Intereses2do
    Total_gastos_operacion=(TotalDepr + TotalSuelySal + TotalComisiones + TotalVarios + TotalIntereses)

    mtz_gastos_operacion.append([
        Depr1er, Depr2do, TotalDepr,
        SueldoySal1er, SueldoySal2do, TotalSuelySal,
        Comisiones1er, Comisiones2do, TotalComisiones,
        Gastosvar1er, Gastosvar2do, TotalVarios,
        Intereses1ero, Intereses2do, TotalIntereses,
        Total_gastos_operacion_1, Total_gastos_operacion_2, Total_gastos_operacion
    ])

#Cédula 10