from .api import matches, bets, odds
import scraping
"""
    OPTIMIZED AND CLEAN CODE
"""
class Odds:
    def __init__(self, ids):
        self.values = [v for k, v in odds.items() if int(k) in ids]
                
class Bet:
    def __init__(self, id):
        self.values = []
        items = bets.get(str(id))
        if items:
            outcomes = items.get('outcomes', [])
            self.values = Odds(outcomes).values

class Match:
    def __init__(self, id, sportId):
        match_data = matches.get(str(id))
        if not match_data or int(match_data.get('sportId')) != int(sportId) or not match_data.get('competitor1Name') or not match_data.get('mainBetId'):
            self.data = {}
        else:
            self.data = {
                'url' : f"https://www.winamax.es/apuestas-deportivas/match/{id}",
                'status': match_data.get('status'),
                'sportId': match_data.get('sportId'),
                'competitor1Name': match_data.get('competitor1Name'),
                'competitor2Name': match_data.get('competitor2Name'),
                'matchId': scraping.get_match_id(match_data.get('competitor1Name'), match_data.get('competitor2Name'))
            }
            bet = Bet(match_data.get('mainBetId'))
            if len(bet.values) == 2:
                self.data['competitor1Cuote'] = bet.values[0]
                self.data['competitor2Cuote'] = bet.values[1]
            if len(bet.values) == 3:
                self.data['competitor1Cuote'] = bet.values[0]
                self.data['draftCuote'] = bet.values[1]
                self.data['competitor2Cuote'] = bet.values[2]
            if len(bet.values) > 3:
                self.data['cuotes'] = bet.values

    def __repr__(self):
        return str(self.data)



# {'status': 'PREMATCH', 'mainBetId': 366315806, 'sportId': 1, 'competitor1Id': 2817, 'competitor1Name': 'FC Barcelona', 'competitor2Id': 2672, 'competitor2Name': 'Bayern Múnich', 'competitor1Cuote': 2.6, 'draftCuote': 3.85, 'competitor2Cuote': 2.45}

    