# region importacion
import os
import pandas as pd
# endregion

# Variables Globales

# region definicion.
LimpiarPantalla = lambda: os.system('cls')
mtz_presupuesto_ventas = [
    # [
    # 'Teclado',
    # [100,150],
    # [350, 250],
    # [234, 567],
    # 150.10
    # ],
    # [
    # 'ratones',
    # [100,150],
    # [350, 250],
    # [234, 567],
    # 150.10
    # ]
]
mtz_presupuesto_produccion = [
    # [
    # nombre,
    # [unidades_vender_1,unidades_vender_2],
    # [inventario_final_1, inventario_final_2],
    # [total_unidades_1, total_unidades_2],
    # [inventario_inicial_1, inventario_incial_2]
    # [unidades_producir_1, unidades_producir_2, total_unidades_producir]
    # ]
]
lista_saldo_Cliente_y_Flujo_Entradas = []



def presupuesto_ventas():
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

    print('==========================Presupuesto De Ventas==========================\n')
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
    LimpiarPantalla()


def determinacion_Saldo_Cliente_y_Flujo_Entradas(periodo_actual):
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


def presupuesto_produccion():
    for elementos in mtz_presupuesto_ventas:
        indice = mtz_presupuesto_ventas.index(elementos)
        for i in elementos:
            nombre = mtz_presupuesto_ventas[indice][0]
            unidades_vender_1 = mtz_presupuesto_ventas[indice][1][0]
            unidades_vender_2 = mtz_presupuesto_ventas[indice][1][1]
            break
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
            [unidades_vender_1, unidades_vender_2],
            [inventario_final_1, inventario_final_2],
            [total_unidades_1, total_unidades_2],
            [inventario_incial_1, inventario_incial_2],
            [unidades_producir_1, unidades_producir_2, total_unidades_producir]
        ])
        
        LimpiarPantalla()
    print()
    print('='*80)
    for i in mtz_presupuesto_produccion:
        print(i)
        print()
        print('='*80)

