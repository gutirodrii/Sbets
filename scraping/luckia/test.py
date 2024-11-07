""""
**1. Entendiendo el Problema
a. Página de Verificación de Cloudflare
El HTML que proporcionaste es característico de las páginas de desafío de Cloudflare. Cloudflare utiliza este tipo de desafíos para proteger los sitios web contra ataques DDoS, bots y actividades maliciosas. Cuando detecta una solicitud sospechosa (por ejemplo, demasiadas solicitudes en poco tiempo, patrones de tráfico inusuales, o falta de ciertas cabeceras que un navegador real enviaría), presenta un desafío que típicamente requiere la ejecución de JavaScript para verificar que la solicitud proviene de un usuario real y no de un bot.

b. Inconsistencias en las Respuestas
Intermitencia en curl: A veces, tu solicitud curl puede pasar las verificaciones de Cloudflare si la solicitud parece legítima y no se realiza con demasiada frecuencia. Otras veces, Cloudflare detecta la solicitud como sospechosa y despliega el desafío.

Errores en Python: Al intentar replicar la solicitud en Python, es probable que estés enfrentando el mismo desafío de Cloudflare, y dado que las bibliotecas estándar como requests no pueden manejar estos desafíos automáticamente, la solicitud falla.

**2. Soluciones Potenciales
a. Utilizar Bibliotecas que Manejen Desafíos de Cloudflare
Hay bibliotecas diseñadas específicamente para manejar las protecciones de Cloudflare, como cloudscraper. Estas bibliotecas simulan un navegador real, ejecutan JavaScript y manejan cookies y desafíos automáticamente.
"""
import cloudscraper
import requests
# Crear una instancia de cloudscraper
scraper = cloudscraper.create_scraper()

# Definir la URL y los parámetros
url = 'https://livedataproviderv2.luckia.es/api/BetOffer/live/data'
params = {
    'sportId': '53',
    'languageId': 'es'
}

# Definir los encabezados (headers)
headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8,es;q=0.7',
    'Origin': 'https://apuestas.luckia.es',
    'Priority': 'u=1, i',
    'Referer': 'https://apuestas.luckia.es/',
    'Sec-CH-UA': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'Sec-CH-UA-Mobile': '?0',
    'Sec-CH-UA-Platform': '"macOS"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/130.0.0.0 Safari/537.36'
}

try:
    # Realizar la solicitud GET
    response = scraper.get(url, headers=headers, params=params, timeout=15)
    response.raise_for_status()  # Lanzar excepción para códigos 4xx/5xx

    # Intentar parsear la respuesta como JSON
    data = response.json()
    print(data)

except cloudscraper.exceptions.CloudflareChallengeError as cf_err:
    print(f'Error de desafío de Cloudflare: {cf_err}')
except requests.exceptions.HTTPError as http_err:
    print(f'Error HTTP: {http_err}')
except requests.exceptions.ConnectionError as conn_err:
    print(f'Error de conexión: {conn_err}')
except requests.exceptions.Timeout as timeout_err:
    print(f'Error de timeout: {timeout_err}')
except requests.exceptions.RequestException as req_err:
    print(f'Error en la solicitud: {req_err}')
except ValueError:
    print('Error al decodificar JSON')
