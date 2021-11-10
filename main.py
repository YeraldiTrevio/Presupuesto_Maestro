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
# Funcion Main.
def main():
    # Desplegar menu de bienvendia
    presentacion_programa()
    LimpiarPantalla()

    # Registro de la empresa y periodo.
    plantilla_area('Registro Datos De La Empresa y Periodo A Trabajar')
    nombre_empresa = input('Ingresa el nombre de la empresa: ')
    periodo_actual = int(input('Ingresa el año del periodo a realizar: '))
    LimpiarPantalla()
    # Cedula 1.
    # Presupuesto de ventas
    plantilla_area('Presupuesto De Ventas')
    #presupuesto_ventas()
    LimpiarPantalla()
    cedula_presupuesto_Ventas(mtz_presupuesto_ventas)

    # Cedula 2.
    # Determinacion Del Saldo De Clientes y Flujo De Efectivo
    plantilla_area('Determinacion Del Saldo De Clientes y Flujo De Efectivo')
    #determinacion_Saldo_Cliente_y_Flujo_Entradas(periodo_actual)
    LimpiarPantalla()
    cedula_Saldo_Cliente_y_Flujo_Entradas(periodo_actual, lista_saldo_Cliente_y_Flujo_Entradas)

    # Cedula 3.
    # Presupuesto de produccion
    plantilla_mediana('Presupuesto De Produccion')
    #presupuesto_produccion()
    LimpiarPantalla()
    cedula_presupuesto_produccion(mtz_presupuesto_produccion)

    # Cedula 4.
    # Presupuesto de requerimiento de materiales
    plantilla_area('Presupuesto De Requerimiento De Materiales')
    #requerimientos_materiales()
    LimpiarPantalla()
    cedula_requerimientos_materiales(mtz_requerimientos_materiales,mtz_total_requerimientos_materiales)

    # Cedula 5.
    # Presupuesto de compras de materiales
    plantilla_area('Presupuesto De Compras De Materiales')
    #presupuesto_compra_materiales()
    LimpiarPantalla()
    cedula_compras_materiales(mtz_compra_materiales, mtz_total_compra_materiales)

    # Cedula 6.
    # Determinacion Del Saldo De Proveedores y Flujo De Efectivo
    plantilla_area('Determinacion Del Saldo De Proveedores y Flujo De Efectivo')
    #determinacion_saldo_proveedores_flujo_salida(periodo_actual)
    LimpiarPantalla()
    cedula_saldo_proveedores_y_flujo_salida(periodo_actual, mtz_saldo_Proveedores_y_Flujo_Entradas)

    # Cedula 7.
    # Presupuesto de Mano de Obra Directa
    plantilla_area('Presupuesto De Mano De Obra Directa')
    #mano_obra_directa()
    LimpiarPantalla()
    cedula_mano_obra_directa(mtz_mano_obra_directa,mtz_total_horas_y_MOD)

    # Cedula 8.
    # Presupuesto Gastos Indirectos De Fabricacion
    plantilla_area('Presupuesto Gastos Indirectos De Fabricacion')
    #gastos_indirectos_fabricacion()
    LimpiarPantalla()
    cedula_gastos_fabricacion(mtz_gastos_indirectos_fab)

    # Cedula 9.
    # Presupuesto De Gastos De Operacion.
    plantilla_area('Presupuesto De Gastos De Operacion')
    #presupuesto_gastos_operacion()
    LimpiarPantalla()
    cedula_gastos_operacion(mtz_gastos_operacion)

    # Cedula 10.
    # Determinacion Del Costo Unitario De Productos Terminados.
    plantilla_area('Determinacion Del Costo Unitario De Productos Terminados')
    #determinacion_costoUnitario_productosTerminados()
    LimpiarPantalla()
    cedula_costoUnitario_productosTerminados(mtz_costoUnitario_productosTerminados)

    # Cedula 11.
    # Validacion De Inventarios Finales.
    plantilla_area('Validacion De Inventarios Finales')
    print('\n')
    #validacion_inventarios_finales()
    LimpiarPantalla()
    cedula_validacion_inventarios_finales(mtz_validacion_inventarios_finales)

    #* Estados Financieros
    # Estado  De Costos De Produccion Y Ventas.
    plantilla_area('Estado  De Costos De Produccion Y Ventas')
    #estado_costo_produccion_ventas(periodo_actual)
    LimpiarPantalla()

    # Estado De Resultados.
    plantilla_area('Estado De Resultados')
    #estado_resultados(periodo_actual)
    LimpiarPantalla()

    # Estado De Flujo De Efectivo.
    plantilla_area('Estado De Flujo De Efectivo')
    estado_flujo_efectivo(periodo_actual)
    LimpiarPantalla()
# Fin de la funcion Main.

# Ejecucion del programa.
if __name__ == '__main__':
    main()