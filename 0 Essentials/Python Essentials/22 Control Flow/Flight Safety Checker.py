altitude = 90
airspeed = 125

def safe_or_unsafe(altitude, airspeed):
    if altitude <= 100 or altitude >= 50000 or airspeed <= 60 or airspeed >= 500:
        safety = False
    else:
        safety = True

    return safety

print(safe_or_unsafe(altitude, airspeed))