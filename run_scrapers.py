import pandas as pd
from scraping.bwin import get_data as bwin
from scraping.winamax import get_data as wina
from scraping._888sport import get_data as _888

import json
def run_scrapers():
    bwin_data = pd.DataFrame(bwin())
    wina_data = pd.DataFrame(wina())
    _888data = pd.DataFrame(_888())
    # with open('wina.csv', 'w') as f:
    #     f.write(wina_data.to_csv(index=False))
    
    # with open('bwin.csv', 'w') as f:
    #     f.write(bwin_data.to_csv(index=False))

    # print(merge_tuples(wina_tuples_list, bwin_tuples_list))
    # print(NameList(wina_tuples_list,bwin_tuples_list).compare())
    # print(NameList(choices, choices1).compare())
    

if __name__ == '__main__':
    run_scrapers()