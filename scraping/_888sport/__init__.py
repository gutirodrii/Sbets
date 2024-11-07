from .api import get_data as res_data
from .data import Match
    
def get_data():
    res = []
    for v in res_data().values():
        if not Match(v).data:
            pass
        else:
            res.append(Match(v).data)
    return res