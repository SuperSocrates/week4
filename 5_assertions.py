import faa
data = faa.get_weather('ORD')

assert data['city'] == 'Chicago', "Should be Chicago" #customize error message
assert data['name'] == 'Chicago OHare International'
assert data['ICAO'] == 'KORD'
