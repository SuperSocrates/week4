# Classifying things
# Classes vs. instances, data attributes, and methods.

import faa;

class Airport:
#when creating methods in a class, must always take at least one argument,
#even if you aren't going to use it in the method    

    def __init__(self, airport_code):
        self.code = airport_code

    def city(self):
        data = faa.get_weather(self.code)
        return data['city']

    def temp(self):
        data = faa.get_weather(self.code)
        return data['weather']['temp']

    def wind(self):
        data = faa.get_weather(self.code)
        return data['weather']['wind']
    
my_airport = Airport('ORD')

print("O'Hare Airport serves the city of", my_airport.city())
print("The temperature is:", my_airport.temp())
print("The wind is:", my_airport.wind())

