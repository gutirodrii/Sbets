
import requests
import re
import json

url = 'https://www.winamax.es/apuestas-deportivas/sports/5'

headers = {
    'authority': 'www.winamax.es',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en;q=0.9',
    'cache-control': 'max-age=0',
    'cookie': 'PHPSESSID=tj0ev8h613fa6lu4n4jt3uv8ji; PHPSESSIONID=tj0ev8h613fa6lu4n4jt3uv8ji; _ga=GA1.2.16805930.1729624177; _gid=GA1.2.2001137865.1729624177; _tt_enable_cookie=1; _ttp=d81XltpPNS0fjhTfwEFB1FTfY-H; visit_language=ES; gang_installer=1; cappingshopvideo=1; winacookie=!winaads=true!winaanalytics=true!winasettings=true!winasocial=true',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
}

response = requests.get(url, headers=headers)

# Extract the PRELOADED_STATE JSON
match = re.search(r'PRELOADED_STATE = (\{.*?\});</script>', response.text, re.DOTALL)
if match:
    preloaded_state = match.group(1)
    data = json.loads(preloaded_state)
    
    # with open('data/data.json', 'w') as f:
    #     f.write(json.dumps(data, indent=2))
        
    # Extract "matches", "bets", and "odds" from the JSON
        
    matches = data.get('matches', {})
    bets = data.get('bets', {})
    odds = data.get('odds', {})
    
    # with open('data/matches.json', 'w') as f:
    #     f.write(json.dumps(matches, indent=2))
    
    # with open('data/bets.json', 'w') as f:
    #     f.write(json.dumps(bets, indent=2))

    # with open('data/odds.json', 'w') as f:
    #     f.write(json.dumps(odds, indent=2))
    
else:
    print('PRELOADED_STATE not found')

