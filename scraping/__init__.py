## NORMALIZATION
import re

def get_match_id(name, name2):
    normalized_name = normalize_name(name)
    normalized_name2 = normalize_name(name2)
    strid = str(normalized_name) + str(normalized_name2)
    return get_id(strid)
    
def normalize_name(name=None):
    # Eliminar espacios adicionales, puntos, caracteres especiales y convertir a minúsculas
    if not name:
        return None
    name = name.replace('ñ','n')
    name = re.sub(r'\s+', ' ', name)  # Unificar espacios
    name = re.sub(r'[^a-zA-Z0-9-/\s]', ' ', name)  # Eliminar caracteres especiales
    name = re.sub(r'\s+', ' ', name) # Unificar espacios
    if not '/' in name:
        name = name.strip().lower()
        name = name.split(' ')
        return name[-1]
    else:
        name = name.split('/')
        name1 = normalize_name(name[0])
        name2 = normalize_name(name[1])
        return name1+name2
       
@staticmethod 
def get_id(name):
    return abs(hash(name)) % 10000000