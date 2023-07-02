#pip install phonenumbers
#pip install geopy
import phonenumbers
from phonenumbers import timezone, geocoder, carrier
from geopy.geocoders import Nominatim

number = input("Enter your phone number with country code: ")
phone = phonenumbers.parse(number)
time = timezone.time_zones_for_number(phone)
car = carrier.name_for_number(phone, "en")
reg = geocoder.description_for_number(phone, "en")

# Useing Nominatim geocoder to get latitude and longitude
geolocator = Nominatim(user_agent="phone_locator")
location = geolocator.geocode(reg)

print(phone)
print(car)
print(reg)
print("Time Zone:", time)
print("Latitude:", location.latitude)
print("Longitude:", location.longitude)

