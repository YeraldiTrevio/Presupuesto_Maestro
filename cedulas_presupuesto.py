import pandas as pd
from presupuesto_maestro import LimpiarPantalla

# Imprime la cedula del presupuesto de ventas.
def cedula_presupuesto_Ventas(mtz_presupuesto_ventas):
    print('==========================Presupuesto De Ventas==========================')
    mostrar_presupuesto_ventas = pd.DataFrame(mtz_presupuesto_ventas,\
        columns=['Nombre', 'Unidades Sem. 1','Unidades Sem. 2', 'Precio Sem. 1',
        'Precio Sem. 2', 'Importe Sem. 1','Importe Sem. 2', 'Total Por Producto'])
    print(mostrar_presupuesto_ventas)
    input('Presiona Enter Para Continuar.')
    LimpiarPantalla()


def cedula_Saldo_Cliente_y_Flujo_Entradas(periodo_actual, lista_saldo_Cliente_y_Flujo_Entradas):
    # Datos de Columnas
    saldo_Clientes_Anterior = f'Saldo De Clientes {periodo_actual-1}'
    ventas_Actual= f'Ventas {periodo_actual}'
    total_Clientes = f'Total Clientes {periodo_actual}'
    cobranza_anterior = f'Cobranza {periodo_actual-1}'
    cobranza_actual = f'Cobranza {periodo_actual}'
    totalEntradas = f'Total Entradas {periodo_actual}'
    saldo_Clientes_Actual = f'Saldo De Clientes {periodo_actual}'

    print('==========================Presupuesto De Ventas==========================')
    mostrar_saldo_Cliente_y_Flujo_Entradas = pd.DataFrame(lista_saldo_Cliente_y_Flujo_Entradas,\
        columns=[saldo_Clientes_Anterior, ventas_Actual, total_Clientes, cobranza_anterior, 
        cobranza_actual, totalEntradas, saldo_Clientes_Actual])

    print(mostrar_saldo_Cliente_y_Flujo_Entradas)
    input('Presiona Enter Para Continuar.')
    LimpiarPantalla()