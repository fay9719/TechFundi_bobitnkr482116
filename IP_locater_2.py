
'''imports'''
from geolite2 import geolite2
import requests


def my_ip_location(my_ip):
    reader = geolite2.reader()
    location = reader.get(my_ip)

    #geolite database dict values and fine tunning
    1=(location['city']['names']['en'])
    2=(location['continent']['names']['en'])
    3=(location['country']['names']['en'])
    4=(location['location'])
    5=(location['postal'])
    6=(location['registered_country']['names']['en'])
    7=(location['subdivisions'][0]['names']['en'])

    print('''city: %s\ncontinent: %s\ncountry: %s\nlocation: %s\npostal: %s\nregistered_country: %s\nsubdivisions: %s\n'''
     % (1,2,,4,5,6,7))


my_ip = requests.get('https://api.ipify.org').text

my_ip_location(my_ip)
