from zepotscha_slow import generate_context_chain_string
from obrabotka_texts import normalize_text, extract_keyparola
import random

def zapros(promt):
    promt = normalize_text(promt)
    tschislo_paroli = promt.split()
    if promt:
        range_parola = random.randint(1,10)
        tschislo_parolia = len(tschislo_paroli)
        suma = tschislo_parolia + range_parola
        return generate_context_chain_string(promt, 40)
    else:
        return "я не знаю"
