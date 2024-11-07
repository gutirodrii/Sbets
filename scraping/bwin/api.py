import json
import requests

url = 'https://sports.bwin.es/cds-api/bettingoffer/fixtures'

headers = {
    'sec-ch-ua-platform': '"Android"',
    'X-App-Context': 'default',
    'Referer': 'https://sports.bwin.es/es/sports/tenis-5/hoy',
    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'x-bwin-browser-url': 'https://sports.bwin.es/es/sports/tenis-5/hoy',
    'sec-ch-ua-mobile': '?1',
    'X-From-Product': 'sports',
    'X-Device-Type': 'phone',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Mobile Safari/537.36',
    'Accept': 'application/json, text/plain, */*'
}

params = {
    'x-bwin-accessid': 'OTdhMjU3MWQtYzI5Yi00NWQ5LWFmOGEtNmFhOTJjMWVhNmRl',
    'lang': 'es',
    'country': 'ES',
    'userCountry': 'ES',
    'fixtureTypes': 'Standard',
    'state': 'Latest',
    'offerMapping': 'Filtered',
    'offerCategories': 'Gridable',
    'fixtureCategories': 'Gridable,NonGridable,Other,Specials,Outrights',
    'sportIds': '5',
    'tournamentIds': '',
    'competitionIds': '',
    'conferenceIds': '',
    'isPriceBoost': 'false',
    'statisticsModes': 'None',
    'skip': '0',
    'take': '999',
    'sortBy': 'StartDate',
    'from': '2024-11-04T00:00:00.000Z',
    'to': '2024-11-30T00:00:00.000Z'
}

response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    data = response.json()
        # Extraer datos específicos de los fixtures
    fixtures = data.get('fixtures', [])
    # json.dump(fixtures, open('bwin.json', 'w'),indent=4)
            
else:
    print(f"Error: {response.status_code}")
