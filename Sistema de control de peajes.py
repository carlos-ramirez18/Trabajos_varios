#Control de peajes mercosur


#Archivo de txt
m = open("peajes.txt")
line = m.readline()
idioma = 0
if "PT" in line:
    idioma = "Portugués"
else:
    idioma = "Español"



# Carga de datos...
carg = 0
cbol = 0
cbra = 0
cchi = 0
cpar = 0
curu = 0
cotr = 0
imp_acu_total = 0
primera = 0
cpp = 0
mayimp = 0
maypat = 0
porc = 0
prom = 0
paispatente = str()
promedio = float()
bandera_promedio = False
pri_patente = False
paten_ = 0
vuelta1 = True
cont_vuel = 0
cont_dis = 0
carg1 = 0

while True:
    line = m.readline()
    if line == "":
        break

    #Contador Vueltas
    cont_vuel += 1
    #Datos
    patente = line[0:7].lstrip()
    tipo = int(line[7])
    pago = int(line[8])
    cabina = int(line[9])
    distancia = int(line[10:13])

    #Tuplas
    num = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
    letras = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")

    #Primera patente
    # Montos
    monto = 300
    if cabina == 2:
        monto = 400
    elif cabina == 1:
        monto = 200

    # Clasificacion vehiculos
    if tipo == 0:
        monto = monto - (monto * 0.50)
    elif tipo == 2:
        monto = monto + (monto * 0.60)

    # Medio pago
    if pago == 2:
        monto = monto - (monto * 0.10)
    #Importe total acumulado
    imp_acu_total += monto

    #Patente mismo formato
    if len(patente) == 7:
        a1, a2, a3, a4, a5, a6, a7 = patente
    #Patente Argentina
        if (a1 in letras and a2 in letras and a3 in num and a4 in num and a5 in num and a6 in letras and a7 in letras):
            a3, a4, a5 = int(a3), int(a4), int(a5)
            carg += 1
            #paispatente = "Su patente es Argentina"
            # Distancia promedio de Arg en Br
            if distancia != 0:
                if cabina == 2:
                    carg1 += 1
                    cont_dis += distancia
    #Patente Brasil
        elif (a1 in letras and a2 in letras and a3 in letras and a4 in num and a5 in letras and a6 in num and a7 in num):
            a4, a6, a7 = int(a4), int(a6), int(a7)
            cbra += 1
            #paispatente = "Su patente es Brasilera"
    #Patente Bolivia
        elif (a1 in letras and a2 in letras and a3 in num and a4 in num and a5 in num and a6 in num and a7 in num):
            a3, a4, a5, a6, a7 = int(a3), int(a4), int(a5), int(a6), int(a7)
            cbol += 1
            #paispatente = "Su patente es Boliviana"
    #Patente Paraguay
        elif (a1 in letras and a2 in letras and a3 in letras and a4 in letras and a5 in num and a6 in num and a7 in num):
            a5, a6, a7 = int(a5), int(a6), int(a7)
            cpar += 1
            #paispatente = "Su patente es Paraguaya"
    # Patente Uruguay
        elif (a1 in letras and a2 in letras and a3 in letras and a4 in num and a5 in num and a6 in num and a7 in num):
            a4, a5, a6, a7 = int(a4), int(a5), int(a6), int(a7)
            curu += 1
            #paispatente = "Su patente es Uruguaya"
        else:
            cotr += 1

    if len(patente) == 6:
        a1, a2, a3, a4, a5, a6, = patente
        # Patente Chile
        if (a1 in letras and a2 in letras and a3 in letras and a4 in letras and a5 in num and a6 in num):
            a5, a6 = int(a6), int(a6)
            cchi += 1
            # paispatente = "Su patente es Chilena"
        else:
            cotr += 1
    #Primera patente + contador
    paten_ = patente
    if pri_patente == False:
        primera = patente
        pri_patente = True
    if paten_ == primera:
        cpp += 1

    #Importe mas caro
    if vuelta1:
        mayimp = monto
        vuelta1 = False
    if mayimp < monto:
        mayimp = monto
        maypat = patente

#Porcentaje otros
porc = (cotr * 100) / cont_vuel
porc = round(porc, 2)

#Promedio distancia de vh arg en br
if carg1 != 0:
    prom = cont_dis / carg1
else:
    prom = 0

# Visualización de resultados...
print('(r1) - Idioma a usar en los informes:', idioma)

print()
print('(r2) - Cantidad de patentes de Argentina:', carg)
print('(r2) - Cantidad de patentes de Bolivia:', cbol)
print('(r2) - Cantidad de patentes de Brasil:', cbra)
print('(r2) - Cantidad de patentes de Chile:', cchi)
print('(r2) - Cantidad de patentes de Paraguay:', cpar)
print('(r2) - Cantidad de patentes de Uruguay:', curu)
print('(r2) - Cantidad de patentes de otro país:', cotr)

print()
print('(r3) - Importe acumulado total de importes finales:', imp_acu_total)

print()
print('(r4) - Primera patente del archivo:', primera, '- Frecuencia de aparición:', cpp)

print()
print('(r5) - Mayor importe final cobrado:', mayimp, '- Patente a la que se cobró ese importe:', maypat)

print()
print('(r6) - Porcentaje de patentes de otros países:', porc, '\b%')

print()
print('(r7) - Distancia promedio recorrida por vehículos argentinos pasando por cabinas brasileñas:', prom, '\bkm')

m.close()