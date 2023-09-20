# Program to convert input to
# phonenumber format
  
import phonenumbers
from phonenumbers import geocoder

# Parsing String to Phone number
# Phone number format: (+Countrycode)xxxxxxxxxx
phoneNumber1 = phonenumbers.parse("+919876543210")
phoneNumber2 = phonenumbers.parse("+919891939215")
phoneNumber3 = phonenumbers.parse("+447575710251")
  
# This will print the phone number and 
# it's basic details.
print(phoneNumber1)
print(phoneNumber2)
print(phoneNumber3)

# Phone number location
print(geocoder.description_for_number(phoneNumber1,"en"))
print(geocoder.description_for_number(phoneNumber2,"en"))
print(geocoder.description_for_number(phoneNumber3,"en"))

print(phonenumbers.region_code_for_number(phoneNumber1))