from grovepi import *
from grove_rgb_lcd import *
from time import sleep
from math import isnan
import pickle

# Conexión y configuración del LDR 
light_sensor = 2
pinMode(light_sensor,"INPUT")

# Valores de referencia para conversion a radiación lumínica 
valorRef = 1000
valorMax = 763

# Conexión y configuración del Sensor de temperatura y humedad 
dht_sensor_port = 3 # Puerto del sensor
dht_sensor_type = 0 # Identificador del sensor 

# Conexión y configuración del potenciometro
dhtpoten = 1

# Configuración del archivo de exportación de datos
log_file ="/home/pi/Desktop/Lista.pkl"

# Configuración del color de la pantalla LCD
setRGB(0,255,0)

#Inicio del programa
while True:
    try:
        
        u = 5
        # Determinación del tiempo de muestreo mediante un potenciometro
        timeM = analogRead(dhtpoten)
        mus= int((timeM / 255.75) +1)
        tm=str(mus)
        
        # Lectura de la intensidad lumínica
        sensor_value = analogRead(light_sensor)
        
        # conversion de valores del LDR a valores de intensidad luminica
        resistance = (float)(1023 - sensor_value) * 10 / (sensor_value+0.3)
        
        # mostrar en la pantalla LCD
        svr= str((sensor_value / valorMax) * valorRef)
        time.sleep(.5)
        
        # lectura de temperatura y humedad
        [ temp,hum ] = dht(dht_sensor_port,dht_sensor_type)
        print("temp =", temp, "C\thum =", hum,"%"  "luz =", svr )

        if isnan(temp) is True or isnan(hum) is True:
            raise TypeError('nan error')
        
        # Imprimir mensajes en el terminal y en la pantalla LCD    
        t = str(temp)
        h = str(hum)
        setText_norefresh("T:" + t + "  t:" + tm +"s\n" + "H:" + h + "% " + "L:" + svr)

        lista=[t,h,svr,tm]
        with open(log_file,"wb") as archivo:
            pickle.dump(lista,archivo)

    except (IOError, TypeError) as e:
        print(str(e))
        setText("")

    except KeyboardInterrupt as e:
        print(str(e))
        setText("")
        break
    
    # Implementación del tiempo de muestreo
    sleep(mus)