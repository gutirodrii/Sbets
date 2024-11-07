import scraping

class Match:
    def __init__(self,lib):
        self.data = {}
        self.lib = lib
        self.get_data()
    
    def get_data(self):
        self.data['status'] = 'PREMATCH' if self.lib.get('event_status') == 'PENDING' else 'LIVE'
        self.data['url'] = f"https://www.888sport.es/en-vivo/mercados_partido/{self.lib.get('id')}-ipe-{self.lib.get('id')}" if self.data['status'] == 'LIVE' else f"https://www.888sport.es/{self.lib.get('sport_l10n_slug')}/{self.lib.get('category_l10n_slug')}/{self.lib.get('tournament_slug')}/{self.lib.get('event_l10n_slug')}-e-{self.lib.get('id')}"
        self.data['sportId'] = self.lib.get('sport_id')
        selections = self.lib.get('markets', {}).get('11904', {}).get('selections', {})
        if len(selections) < 2:
            self.data['competitor1Name'] = list(self.lib.get('competitors',{}).values())[0].get('name')
            self.data['competitor2Name'] = list(self.lib.get('competitors',{}).values())[1].get('name')
            self.data['competitor1Cuote'] = float(list(selections.values())[0].get('decimal_price')) if list(selections.values())[0].get('name') == self.data['competitor1Name'] else 0
            self.data['competitor2Cuote'] = float(list(selections.values())[0].get('decimal_price')) if list(selections.values())[0].get('name') == self.data['competitor2Name'] else 0
        if len(selections) == 2:
            self.data['competitor1Name'] = list(selections.values())[0].get('name')
            self.data['competitor2Name'] = list(selections.values())[1].get('name')
            self.data['competitor1Cuote'] = float(list(selections.values())[0].get('decimal_price'))
            self.data['competitor2Cuote'] = float(list(selections.values())[1].get('decimal_price'))
        if len(selections) == 3:
            self.data['competitor1Name'] = list(selections.values())[0].get('name')
            self.data['competitor2Name'] = list(selections.values())[1].get('name')
            self.data['draftCuote'] = float(list(selections.values())[2].get('decimal_price'))
            self.data['competitor1Cuote'] = float(list(selections.values())[0].get('decimal_price'))
            self.data['competitor2Cuote'] = float(list(selections.values())[1].get('decimal_price'))
        if len(selections) > 3:
            self.data['cuotes'] = [x.get('decimal_price') for x in selections.values()]
            
        self.data['matchId'] = scraping.get_match_id(self.data['competitor1Name'], self.data['competitor2Name'])
    
    def __repr__(self):
        return str(self.data)