import requests

def obter_dados():
    url = "http://127.0.0.1:8000/v1/forecast"

    parametros = {
        "latitude": -26.4851,
        "longitude": -49.0713
    }

    resposta = requests.get(url, params=parametros, timeout=15)

    if resposta.status_code == 200:
        dados = resposta.json()
        temperatura = dados["current"]["temperature_2m"]
        umidade = dados["current"]["relative_humidity_2m"]
        sensacao = dados["current"]["apparent_temperature"]
        precipitacao = dados["current"]["precipitation"]
        vento = dados["current"]["wind_speed_10m"]
        data = dados["current"]["time"]

        print(f"A temperatura é: {temperatura}°C")
        print(f"A umidade é: {umidade}%")
        print(f"A sensação térmica é: {sensacao}°C")
        print(f"A precipitação de chuva é: {precipitacao}mm")
        print(f"O vento está a: {vento}km/h")
        print(f"Data/Hora: {data}")
        return dados

    else: 
        print("Algo deu errado! Tente novamente.")

obter_dados()