import json
import requests

def convertir_tiempo (dt_a_convertir):
    from datetime import datetime, timezone, timedelta
    # Convertir el Unix timestamp a una fecha y hora legible en UTC
    converted_time = datetime.fromtimestamp(dt_a_convertir, tz=timezone.utc)
    # Restar 3 horas a la hora convertida
    adjusted_time = converted_time - timedelta(hours=3)
    # Convertir a una cadena de texto
    hora = adjusted_time.hour 
    minuto = adjusted_time.minute
    return hora, minuto



def extraer_sunrise_sunset(cadena_json):
    try:
        datos = json.loads(cadena_json)  # Parsea la cadena JSON
        sunrise = datos["current"]["sunrise"]
        sunset = datos["current"]["sunset"]
        return {"sunrise": sunrise, "sunset": sunset}
    except (json.JSONDecodeError, KeyError, TypeError):
        return None  # Retorna None si hay un error al parsear o acceder a los datos


InfoClima = requests.post('https://openweathermap.org/data/2.5/onecall?lat=-32.952&lon=-68.862&units=metric&appid=439d4b804bc8187953eb36d2a8c26a02')
resultado = extraer_sunrise_sunset(InfoClima.text)

if resultado:
    print(f"Sunrise: {resultado['sunrise']}")
    print(f"Sunset: {resultado['sunset']}")
else:
    print("No se encontraron los valores de sunrise y sunset en la cadena JSON.")

hora, minuto = convertir_tiempo(resultado['sunrise'])
print("La hora convertida para Amanecer es: " + str(hora) + ":" + str(minuto)+ " hs")

hora, minuto = convertir_tiempo(resultado['sunset'])
print("La hora convertida para Anochecer es: " + str(hora) + ":" + str(minuto)+ " hs")


