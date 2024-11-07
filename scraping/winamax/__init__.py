from .api import matches
from .data import Match

def get_data():
    res = []
    for k,v in matches.items():
        if not Match(k, 5).data:
            pass
        else:
            res.append(Match(k, 5).data)
    return res