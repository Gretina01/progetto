"""devo validare tutti i dati che fornisce l'utente come il formato del file, o tipo di dato inserito,
o se il dato inserito deve rientrare in qualche range..."""

def validate_latitude(lat: float | int) -> bool:
    """list function validated the lat"""
    if isinstance(lat, (float, int)):
        if abs(lat) <= 90.0:
            return True
    return False

def validate_longitude(lon: float | int) -> bool:
    """list function validated the lon"""
    if isinstance(lon, (float, int)):
        if abs(lon) <= 180.0:
            return True
    return False

        