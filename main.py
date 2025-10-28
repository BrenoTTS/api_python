import requests
import pprint

api_key = "c00bfae10b1f4693a7a233311252710"
link_api = "https://api.weatherapi.com/v1/current.json"

parametros = {
    "key": api_key,
    "q": 'Ceara',
    "lang": 'pt'
}

try:
    response = requests.get(link_api, params=parametros)
    response.raise_for_status() # Lança um erro para status 4xx/5xx
    data = response.json()
    # pprint.pprint(data)
    temp = data['current']['temp_c']
    descricao = data['current']['condition']['text']
    localidade = data['location']['name']
    regiao = data['location']['region']
    print(f'Tempo: {temp}')
    print(f'Descrição do tempo: {descricao}')
    print(f'Qual cidade: {localidade}')
    print(f'Qual estado: {regiao}')

except requests.exceptions.RequestException as e:
    print(f"Erro na requisição: {e}")


