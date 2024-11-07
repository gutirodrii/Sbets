from .api import fixtures
from .data import Match

def get_data():
    res = []
    for v in fixtures:
        if not Match(v).data:
            pass
        else:
            res.append(Match(v).data)
    return res