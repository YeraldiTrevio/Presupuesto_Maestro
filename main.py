# region importacion
import os
from presupuesto_maestro import *
from cedulas_presupuesto import *
# endregion

# region definicion.
LimpiarPantalla = lambda: os.system('cls')
# endregion

LimpiarPantalla()
def main():
    # Desplegar menu de bienvendia
    print('==================================================================================')
    print('==================================================================================')
    print('==================================================================================')
    print('==========================Software De Presupuesto Maestro=========================')
    print('==============================©Equipo 2 Contabilidad==============================')
    print('==================================================================================')
    print('==================================================================================')
    print('==================================================================================')
    input('Presione Enter Para Continuar... ')
    LimpiarPantalla()
    print('========================== Registro Datos De La Empresa y Periodo A Trabajar ==========================')
    nombre_empresa = input('Ingresa el nombre de la empresa: ')
    periodo_actual = int(input('Ingresa el año del periodo a realizar: '))
    LimpiarPantalla()
    print('==========================Presupuesto De Ventas==========================')
    presupuesto_ventas()
    LimpiarPantalla()
    cedula_presupuesto_Ventas(mtz_presupuesto_ventas)
    
    print('==========================Determinacion Del Saldo De Clientes y Flujo De Efectivo ==========================')
    determinacion_Saldo_Cliente_y_Flujo_Entradas(periodo_actual)
    LimpiarPantalla()
    cedula_Saldo_Cliente_y_Flujo_Entradas(periodo_actual, lista_saldo_Cliente_y_Flujo_Entradas)

    # print('==========================Presupuesto De Produccion==========================')
    # presupuesto_produccion()
    
if __name__ == '__main__':
    main()
