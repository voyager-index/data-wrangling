import googlemaps
from datetime import datetime
import csv
import configparser
import json

config = configparser.ConfigParser()
config.read('config.ini')
key = config['DEFAULT']['key']

gmaps = googlemaps.Client(key=key)
f = open('lat-lng.txt', 'w').close()

def main():
    with open('intl-airports.csv', 'r', newline='') as csvfile:
        spamreader = csv.reader(csvfile)

        for row in spamreader:
            city = row[0]
            airport = row[1]
            print(city + ", " + airport)
            # Geocoding an address
            geocode_result = gmaps.geocode(airport)
            y = geocode_result

            try:
                lat = y[0]['geometry']['location']['lat']
                lng = y[0]['geometry']['location']['lng']
                with open('lat-lng.txt', 'a') as latLng:
                    latLng.write(airport + "," + str(lat) + "," + str(lng) + '\n')
            except IndexError:
                with open('lat-lng.txt', 'a') as latLng:
                    latLng.write(airport + ",null" + '\n')
                pass


if __name__ == '__main__':
    main()
