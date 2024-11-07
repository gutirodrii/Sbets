import scraping

class Match:
    def __init__(self,lib):
        self.data = {}
        self.lib = lib
        self.get_data()
        
        
    def get_data(self):
        games = self.lib.get('games', [])
        results = games[0].get('results', []) if games else []
        if not results:
            self.data = {}
        else:
            self.data['url'] = f"https://sports.bwin.es/es/sports/eventos/{self.lib.get('id')}"
            self.data['status'] = self.lib.get('stage').upper()
            self.data['sportId'] = self.lib.get('sport').get('id')
            if len(results) == 2:
                self.name = games[0].get('name', {}).get('value')
                self.data['competitor1Name'] = results[0]['name']['value']
                self.data['competitor2Name'] = results[1]['name']['value']
                self.data['competitor1Cuote'] = results[0]['odds']
                self.data['competitor2Cuote'] = results[1]['odds']
            if len(results) == 3:
                self.name = games[0].get('name', {}).get('value')
                self.data['competitor1Name'] = results[0]['name']['value']
                self.data['competitor2Name'] = results[1]['name']['value']
                self.data['draftCuote'] = results[2]['odds']
                self.data['competitor1Cuote'] = results[0]['odds']
                self.data['competitor2Cuote'] = results[1]['odds']
            if len(results) > 3:
                self.data['cuotes'] = [x['odds'] for x in results]
                
            self.data['matchId'] = scraping.get_match_id(self.data['competitor1Name'], self.data['competitor2Name'])

    def __repr__(self):
        return str(self.data)