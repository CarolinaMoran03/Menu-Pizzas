print(''' *** EJERCICIO UNO
REALIZAR UN PROGRAMA QUE EMITA 
EL PRECIO DE UNA PIZZA DEPENDIENDO 
DE SU TAMAÑO, INGREDIENTES ADICIONALES, PORCIONES.
CON EL COSTO DEL IVA SEGUN EL PEDIDO ***

''')

def operacion_precio(tipo, tamano, extra, porcion, adicional ):
	precio_porciones = porcion * tamano
	precio_adicionales = adicional * extra
	precio_sin_iva = precio_porciones + precio_adicionales

	if precio_sin_iva > 0 and precio_porciones < 51:
		porcentaje_iva = eval("precio_sin_iva * 0 / 100")
		iva = 0

	elif precio_sin_iva > 50 and precio_porciones < 71:
		porcentaje_iva = eval("precio_sin_iva * 5 / 100")
		iva = 5

	elif precio_sin_iva > 70 and precio_porciones < 91:
		porcentaje_iva = eval("precio_sin_iva * 7 / 100")
		iva = 7

	elif precio_sin_iva > 90 and precio_porciones <= 120:
		porcentaje_iva = eval("precio_sin_iva * 9 / 100")
		iva = 9

	elif precio_sin_iva > 120:
		porcentaje_iva = eval("precio_sin_iva * 11 / 100")
		iva = 11

	resultado_total = precio_sin_iva + porcentaje_iva
	print('''
{p} Unidades {t} - {pt} c/u          $ {pp}
{a} Ingredientes     - {e} c/u          $ {pa}
                                     --------
Precio sin iva                        $ {psi}
IVA {iva} %                               $ {pi}
Precio Final                          $ {rt}
'''.format(p = porcion, t = tipo, pt = tamano, pp = precio_porciones, a = adicional,
	e = extra, pa = precio_adicionales, psi = precio_sin_iva, pi = porcentaje_iva, rt = resultado_total, iva = iva))


print('    *PROGRAMA PIZZA*')

print('''
*	      CARTA	        *
* Tamaño    |    Precio *
* Pequeña   |     6.50  *
* Mediana   |    12.35  *
* Familiar  |    22.50  *

''')

extra = 0.99
seleccion = input('Selecciona el tamaño de la pizza: ')


while True:
	try:
		porciones = int(input('Cuantas porciones de pizza deceas: '))
		if not(0 <  porciones <= 30):
			print('*Solo se pueden de 1 a 30 porciones de pizza*')
			continue
		break
	except ValueError:
		print('*Error!. Introduce valores numericos*') 
while True:
	try:
		adicionales = int(input('Cuantas ingredientes adicionales deceas: '))
		if not(0 < adicionales <= 8):
			print('*Solo se pueden de 1 a 8 ingrediente adicionales*')
			continue
		break
	except ValueError:
		print('*Error!. Introduce valores numericos*')


if (seleccion.lower() == 'pequeña'):
	tipo = 'Pequeña'
	pequena = 6.50
	operacion_precio(tipo, pequena, extra, porciones, adicionales)

elif (seleccion.lower() == 'mediana'):
	tipo = 'Mediana'
	mediana = 12.35
	operacion_precio(tipo, mediana, extra, porciones, adicionales)


elif (seleccion.lower() == 'familiar'):
	tipo = 'Familiar'
	familiar = 22.50
	operacion_precio(tipo, familiar, extra, porciones, adicionales)

else:
	print('La opcion no existe')
	
	
	
