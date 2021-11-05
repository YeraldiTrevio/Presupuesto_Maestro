'''
    Este archivo es el principal de todo. Aqui es donde se ejecutan
    todas las funciones necesarias para el correcto funcionamiento
    del programa.

    Aqui se mandan a llamar todas aquellas funciones y variables
    que estan guardados en otros archivos.
'''

# Area de importacion.
import os
from presupuesto_maestro import *
from cedulas_presupuesto import *
from plantillas import *
# fin de area de importacion.

# Area de vriables y lambdas.
LimpiarPantalla = lambda: os.system('clear')
# fin de area de variables y lambdas.

LimpiarPantalla()
def main():
    # Desplegar menu de bienvendia
    presentacion_programa()
    LimpiarPantalla()

    # Registro de la empresa y periodo.
    plantilla_area('Registro Datos De La Empresa y Periodo A Trabajar')
    nombre_empresa = input('Ingresa el nombre de la empresa: ')
    periodo_actual = int(input('Ingresa el año del periodo a realizar: '))
    LimpiarPantalla()

    # Presupuesto de ventas
    plantilla_area('Presupuesto De Ventas')
    # presupuesto_ventas()
    LimpiarPantalla()
    cedula_presupuesto_Ventas(mtz_presupuesto_ventas)
    
    # Determinacion Del Saldo De Clientes y Flujo De Efectivo
    plantilla_area('Determinacion Del Saldo De Clientes y Flujo De Efectivo')
    # determinacion_Saldo_Cliente_y_Flujo_Entradas(periodo_actual)
    LimpiarPantalla()
    cedula_Saldo_Cliente_y_Flujo_Entradas(periodo_actual, lista_saldo_Cliente_y_Flujo_Entradas)

    # Presupuesto de produccion
    plantilla_mediana('Presupuesto De Produccion')
    # presupuesto_produccion()
    LimpiarPantalla()
    cedula_presupuesto_produccion(mtz_presupuesto_produccion)

    # Presupuesto de requerimiento de materiales
    plantilla_area('Presupuesto De Requerimiento De Materiales')
    # requerimientos_materiales()
    LimpiarPantalla()
    cedula_requerimientos_materiales(mtz_requerimientos_materiales,mtz_total_requerimientos_materiales)

    # Presupuesto de compras de materiales
    plantilla_area('Presupuesto De Compras De Materiales')
    # presupuesto_compra_materiales()
    LimpiarPantalla()

    # Determinacion Del Saldo De Proveedores y Flujo De Efectivo
    plantilla_area('Determinacion Del Saldo De Proveedores y Flujo De Efectivo')
    #determinacion_saldo_proveedores_flujo_salida(periodo_actual)
    LimpiarPantalla()


if __name__ == '__main__':
    main()
