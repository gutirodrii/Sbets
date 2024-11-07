import json
import requests
import datetime

endpoint = ['today','tomorrow']

for i in range(7):
    res = datetime.datetime.today() + datetime.timedelta(days=2+i)
    endpoint.append(res.strftime('%Y-%m-%d'))

# url = f'https://spectate-web.888sport.es/spectate/sportsbook-req/getUpcomingEvents/tennis/{endpoint}'

headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8,es;q=0.7',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryyAMLKQhEPgNrI9NJ',
    'Cookie': '888Cookie=lang%3Des%26OSR%3D1911954; 888TestData=%7B%22referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22last-referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22orig-lp%22%3A%22https%3A%2F%2Fwww.888sport.es%2F%22%2C%22currentvisittype%22%3A%22SEO%22%2C%22strategy%22%3A%22SeoStrategy%22%2C%22strategysource%22%3A%22previousvisit%22%2C%22publisher%22%3A%22SearchEngine%22%7D; 888TestDataLocal=%7B%22datecreated%22%3A%222024-10-29T18%3A45%3A29.701Z%22%2C%22expiredat%22%3A%22Tue%2C%2005%20Nov%202024%2018%3A45%3A00%20GMT%22%7D; anon_hash=2212c47f74366e29b0bc434d0672686b; spectate_session=d831173a-c19b-4800-8735-ce25d9348961%3Aanon; odds_format=DECIMAL; spectate_client_ver=2.96; bbsess=ZUwDbKUud7x7NmVY32ViQdsviAu; lang=esp; OptanonAlertBoxClosed=2024-10-29T18:57:36.402Z; _ga=GA1.1.354214537.1730228252; _gcl_au=1.1.403478172.1730228256; OptanonConsent=isGpcEnabled=0&datestamp=Tue+Oct+29+2024+19%3A57%3A36+GMT%2B0100+(Central+European+Standard+Time)&version=202303.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=78b27fc6-922a-4745-9513-95ac908e2e37&interactionCount=2&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1; FPID=FPID2.2.7npWpNc15D92zTMY49JdJvVKfXLqaz%2B1r21MUoh8gBw%3D.1730228252; FPAU=1.2.1552381046.1730228257; _fbp=fb.1.1730228256570.297353173567568567; blueID=d1ba79db-3137-4b8e-a61c-ca1ae2a9abad; FPLC=VFDqj1H%2BZsD4i6VS0spNQRXvLAXMcY3gTxoNiac5MTJoEy8tTCIe%2FCk9yeaB2dHOol2cPEY%2BgIOHRFmEigR%2F8Hfzq0Hl6mFX7UGlurGkwn6GJtiuWHVpZWu6fdZwpw%3D%3D; _tguatd=eyJzYyI6Ind3dy5nb29nbGUuY29tIn0=; _tgpc=31f94a81-1703-5941-9b7e-fcc29103b09e; _tgidts=eyJzaCI6ImQ0MWQ4Y2Q5OGYwMGIyMDRlOTgwMDk5OGVjZjg0MjdlIiwiY2kiOiIyMjM3Zjc3ZC1iNTAyLTUzYTAtYWYwMC02MzdkNjZiYmJlZmQiLCJzaSI6IjI0OWEzYjkwLWU1MmItNTEyMS1iZjRlLTkyZTlkZmY3OWYyZSJ9; _tglksd=eyJzIjoiMjQ5YTNiOTAtZTUyYi01MTIxLWJmNGUtOTJlOWRmZjc5ZjJlIiwic3QiOjE3MzAyMjgyNjU5OTYsInNvZCI6Ind3dy5nb29nbGUuY29tIiwic29kdCI6MTczMDIyODI2NTk5Niwic29kcyI6InIiLCJzb2RzdCI6MTczMDIyODI2NTk5Nn0=; _uetsid=af486820962711ef8d4dab535c6d24f9; _uetvid=af488e80962711efa7421b04eecdb469; _cs_c=0; _ga_G49FQKZWH3=GS1.1.1730228251.1.1.1730228361.0.0.1445969054; FPGSID=1.1730228256.1730228361.G-G49FQKZWH3.PC3gG-9Xm-sB2ZS4AYAXYw; _tgsid=eyJscGQiOiJ7XCJscHVcIjpcImh0dHBzOi8vd3d3Ljg4OHNwb3J0LmVzJTJGXCIsXCJscHRcIjpcIkFwdWVzdGFzJTIwRGVwb3J0aXZhcyUyMCU3QyUyMENhc2ElMjBkZSUyMEFwdWVzdGFzJTIwJTdDJTIwODg4JTIwU3BvcnRcIixcImxwclwiOlwiaHR0cHM6Ly93d3cuZ29vZ2xlLmNvbVwifSIsInBzIjoiNmZjMzBmMDEtYTRkYi00ZWYxLTgyNjMtNmEzNmUzM2FhYTYxIiwicHZjIjoiMSIsInNjIjoiMjQ5YTNiOTAtZTUyYi01MTIxLWJmNGUtOTJlOWRmZjc5ZjJlOi0xIiwiZWMiOiI3IiwicHYiOiIxIiwidGltIjoiMjQ5YTNiOTAtZTUyYi01MTIxLWJmNGUtOTJlOWRmZjc5ZjJlOjE3MzAyMjgyNjkxODE6LTEifQ==; _cs_id=3781e4be-497b-a41d-f64e-1782529b2113.1730228266.1.1730228460.1730228266.1716998419.1764392266309.1; _cs_s=11.0.0.9.1730230260541',
    'Origin': 'https://www.888sport.es',
    'Priority': 'u=1, i',
    'Referer': 'https://www.888sport.es/',
    'Sec-CH-UA': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'Sec-CH-UA-Mobile': '?0',
    'Sec-CH-UA-Platform': '"macOS"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
}

# # Datos en formato multipart/form-data
data = '------WebKitFormBoundaryyAMLKQhEPgNrI9NJ--\r\n'

def get_data():
    res_data = {}
    for i in endpoint:
        url = f'https://spectate-web.888sport.es/spectate/sportsbook-req/getUpcomingEvents/tennis/{i}'
        response = requests.post(url, headers=headers, data=data, timeout=15) 
        if response.status_code == 200:
            res_data.update(response.json().get('events'))
        else:
            print(f"Error: {response.status_code}")
            break
    return res_data

# json.dump(get_data(), open('888sport.json', 'w'),indent=4)