"""
Module of weather-related functions.
"""

def comfort_level(temperature):
    """
    Given temperature in degrees Celsius, returns an indication of comfort
    level as a string ("COLD", "OK" or "HOT").
    """
    if temperature <= 15.0:
        return "COLD"
    elif temperature > 25.0:
        return "HOT"
    else:
        return "OK"

t = -5.0
while(t<=30):
    print(f"Tempo: {t} Returns: {comfort_level(t)}")
    t = t+1