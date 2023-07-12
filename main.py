import csv
import time
import math
from datetime import datetime

# Función para leer el valor analógico del pin
def analogRead(pin):
    # Implementa aquí la lógica para leer el valor analógico del pin
    # y devuelve el valor leído.
    return 0

# Función para establecer el modo de un pin
def pinMode(pin, mode):
    # Implementa aquí la lógica para establecer el modo del pin.
    pass

# Función para leer la temperatura y la humedad
def readDHTSensor(port, sensor_type):
    # Implementa aquí la lógica para leer la temperatura y la humedad
    # utilizando el puerto y el tipo de sensor especificados.
    # Devuelve la temperatura y la humedad como una lista [temperatura, humedad].
    return [0, 0]

# Función para obtener la hora y la fecha actual
def obtener_hora_fecha_actual():
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

# Conexión y configuración del LDR
light_sensor = 2
pinMode(light_sensor, "INPUT")

# Valores de referencia para conversión a radiación lumínica
valorRef = 1000
valorMax = 763

# Conexión y configuración del Sensor de temperatura y humedad
dht_sensor_port = 3  # Puerto del sensor
dht_sensor_type = 0  # Identificador del sensor

# Conexión y configuración del potenciómetro
dhtpoten = 1

# Configuración del archivo de exportación de datos CSV
csv_file = "C:\Users\User\Desktop\Datos.csv"

# Abrir el archivo CSV en modo escritura
with open(csv_file, "w", newline="") as archivo:
    writer = csv.writer(archivo)
    writer.writerow(["Hora", "Fecha", "Temperatura", "Humedad", "Luz", "Tiempo Muestreo"])

    while True:
        try:
            # Obtener la hora y la fecha actual
            hora_fecha_actual = obtener_hora_fecha_actual()

            # Obtener el tiempo de muestreo
            timeM = analogRead(dhtpoten)
            mus = int((timeM / 255.75) + 1)
            tm = str(mus)

            # Lectura de la intensidad lumínica
            sensor_value = analogRead(light_sensor)

            # Conversión de valores del LDR a intensidad lumínica
            resistance = (float)(1023 - sensor_value) * 10 / (sensor_value + 0.3)
            svr = str((sensor_value / valorMax) * valorRef)
            time.sleep(0.5)

            # Lectura de temperatura y humedad
            [temp, hum] = readDHTSensor(dht_sensor_port, dht_sensor_type)
            print("temp =", temp, "C\thum =", hum, "%" "luz =", svr)

            if math.isnan(temp) or math.isnan(hum):
                raise TypeError('nan error')

            # Imprimir valores en la terminal
            t = str(temp)
            h = str(hum)
            print("Hora:", hora_fecha_actual)
            print("T:" + t + "  t:" + tm + "s\n" + "H:" + h + "% " + "L:" + svr)

            # Guardar los valores en el archivo CSV
            writer.writerow([hora_fecha_actual, temp, hum, svr, tm])

        except (IOError, TypeError) as e:
            print(str(e))

        except KeyboardInterrupt as e:
            print(str(e))
            break

        # Implementación del tiempo de muestreo
        time.sleep(mus)