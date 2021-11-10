"""
    Como su  nombre lo dice, este archivo almacena las plantillas que se pueden utilizar
    en el programa, las plantillas se pueden modificar, y tambien se pueden agregar otras
    nuevas, con el fin de organizar mejor el codigo.
"""

def presentacion_programa():
    print('==================================================================================')
    print('==================================================================================')
    print('==================================================================================')
    print('==========================Software De Presupuesto Maestro=========================')
    print('==============================©Equipo 2 Contabilidad==============================')
    print('==================================================================================')
    print('==================================================================================')
    print('==================================================================================')
    input('Presione Enter Para Continuar... ')

# Plantillas de area
def plantilla_area(area):
    print(f'========================== {area} ==========================')

def plantilla_mediana(area):
    print(f'================================ {area} ================================')

def plantilla_area_grande(area):
    print(f'====================================================== {area} ======================================================')
# Fin plantillas de area

# Plantillas de finalizacion de area
def plantilla_finalizacion_area_grande():
    print("===================================================================================================================================")

def plantilla_finalizacion_ExtraGrande():
    print("======================================================================================================================================================================")

def plantilla_finalizacion_area():
    print("===================================================================================================")
# Fin plantillas de finalizacion de area
    
# Plantillas con salto de linea
def platillaArea_SaltoLinea(area):
    print(f"\n============================ {area} ============================\n")
    
def plantillas_Area_Msg_SL(msg,area):
    print(f"\n====================================== {msg} {area} ======================================\n")

def plantilla_Finalizacion_SaltoLinea():
    print("\n=================================================================================\n")
# Fin plantillas con salto de linea


# Menu de cedula 10.
def menu_cedula_10():
    print('\n================= Menu De Cedulas =================')
    print('1. Presupuesto De Requerimientos De Materiales.')
    print('2. Presupuesto De Compra De Materiales.')
    print('3. Presupuesto De Mano De Obra Directa.')
    print('4. Presupuesto De Gastos Indirectos de Fabricacion.')
    print('5. Limpiar La Pantalla.')
    print('X. No Mostrar Cedulas.')

  