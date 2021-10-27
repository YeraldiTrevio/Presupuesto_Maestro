import pandas as pd

# Imprime la cedula del presupuesto de ventas.
def cedula_presupuesto_Ventas(mtz_presupuesto_ventas):
    print('==========================Presupuesto De Ventas==========================')
    mostrar_presupuesto_ventas = pd.DataFrame(mtz_presupuesto_ventas,\
        columns=['Nombre', 'Unidades 1','Unidades 2', 'Precio 1',
        'Precio 2', 'Importe 1','Importe 2', 'Total'])
    print(mostrar_presupuesto_ventas)
    input('Presiona Enter Para Continuar.') 