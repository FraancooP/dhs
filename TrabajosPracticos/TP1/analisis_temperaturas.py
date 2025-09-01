# TP1 - Lectura y organización de datos de temperaturas SMN
# Lee el archivo de temperaturas y organiza los datos en el diccionario solicitado

datos = {}
with open('registro_temperatura365d_smn.txt', encoding='latin1') as f:
    next(f)  # Salta la primera línea (encabezado)
    next(f)  # Salta la segunda línea (guiones)
    for linea in f:
        # Extrae los campos por posición fija
        fecha = linea[0:8].strip()
        tmax = linea[9:15].strip()
        tmin = linea[15:21].strip()
        nombre = linea[21:].strip()
        # Convierte tmax y tmin a float o None si falta
        tmax = float(tmax) if tmax and tmax != '-----' else None
        tmin = float(tmin) if tmin and tmin != '-----' else None
        # Si la estación no está en el diccionario, la agrega
        if nombre not in datos:
            datos[nombre] = {'tmax': [], 'tmin': []}
        # Agrega las temperaturas a las listas correspondientes
        datos[nombre]['tmax'].append(tmax)
        datos[nombre]['tmin'].append(tmin)


# --- Análisis y reporte ---
reporte = []

# 1. Reporte por estación: temperatura máxima y mínima del año
reporte.append('Reporte de temperaturas máximas y mínimas por estación:')
for estacion, temps in datos.items():
    tmax_validas = [t for t in temps['tmax'] if t is not None]
    tmin_validas = [t for t in temps['tmin'] if t is not None]
    max_tmax = max(tmax_validas) if tmax_validas else 'Sin datos'
    min_tmin = min(tmin_validas) if tmin_validas else 'Sin datos'
    reporte.append(f"{estacion}: Máxima = {max_tmax}, Mínima = {min_tmin}")

# 2 y 3. Mayor y menor amplitud térmica en un mismo día por estación
mayor_amplitud = {'estacion': None, 'dia': None, 'amplitud': float('-inf')}
menor_amplitud = {'estacion': None, 'dia': None, 'amplitud': float('inf')}
for estacion, temps in datos.items():
    for i, (tmax, tmin) in enumerate(zip(temps['tmax'], temps['tmin'])):
        if tmax is not None and tmin is not None:
            amplitud = tmax - tmin
            if amplitud > mayor_amplitud['amplitud']:
                mayor_amplitud = {'estacion': estacion, 'dia': i+1, 'amplitud': amplitud}
            if amplitud < menor_amplitud['amplitud']:
                menor_amplitud = {'estacion': estacion, 'dia': i+1, 'amplitud': amplitud}
reporte.append('')
reporte.append(f"Mayor amplitud térmica: {mayor_amplitud['amplitud']}°C en {mayor_amplitud['estacion']} (día {mayor_amplitud['dia']})")
reporte.append(f"Menor amplitud térmica: {menor_amplitud['amplitud']}°C en {menor_amplitud['estacion']} (día {menor_amplitud['dia']})")

# 4 y 5. Máxima y mínima diferencia de temperatura entre dos estaciones en un mismo día
max_dif = {'dia': None, 'est1': None, 't1': None, 'est2': None, 't2': None, 'dif': float('-inf')}
min_dif = {'dia': None, 'est1': None, 't1': None, 'est2': None, 't2': None, 'dif': float('inf')}
estaciones = list(datos.keys())
num_dias = max(len(temps['tmax']) for temps in datos.values())
for dia in range(num_dias):
    temps_dia = []
    for estacion in estaciones:
        tmax = datos[estacion]['tmax'][dia] if dia < len(datos[estacion]['tmax']) else None
        tmin = datos[estacion]['tmin'][dia] if dia < len(datos[estacion]['tmin']) else None
        if tmax is not None:
            temps_dia.append((estacion, 'tmax', tmax))
        if tmin is not None:
            temps_dia.append((estacion, 'tmin', tmin))
    for i in range(len(temps_dia)):
        for j in range(i+1, len(temps_dia)):
            est1, tipo1, t1 = temps_dia[i]
            est2, tipo2, t2 = temps_dia[j]
            dif = abs(t1 - t2)
            if dif > max_dif['dif']:
                max_dif = {'dia': dia+1, 'est1': f"{est1} ({tipo1})", 't1': t1, 'est2': f"{est2} ({tipo2})", 't2': t2, 'dif': dif}
            if dif < min_dif['dif'] and dif != 0:
                min_dif = {'dia': dia+1, 'est1': f"{est1} ({tipo1})", 't1': t1, 'est2': f"{est2} ({tipo2})", 't2': t2, 'dif': dif}
reporte.append('')
reporte.append(f"Máxima diferencia de temperatura entre dos estaciones en un mismo día: {max_dif['dif']}°C entre {max_dif['est1']} ({max_dif['t1']}°C) y {max_dif['est2']} ({max_dif['t2']}°C) en el día {max_dif['dia']}")
reporte.append(f"Mínima diferencia de temperatura entre dos estaciones en un mismo día: {min_dif['dif']}°C entre {min_dif['est1']} ({min_dif['t1']}°C) y {min_dif['est2']} ({min_dif['t2']}°C) en el día {min_dif['dia']}")

# Guardar el reporte en un archivo de texto
with open('reporte_temperaturas.txt', 'w', encoding='utf-8') as f:
    for linea in reporte:
        f.write(linea + '\n')
