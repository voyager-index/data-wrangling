import configparser
import csv
import googlemaps
import os


def main():
    config = configparser.ConfigParser()
    config.read('config.ini')
    key = config['DEFAULT']['key']
    gmaps = googlemaps.Client(key=key)
    delim = ','

    outfile = 'lat-lng.csv'
    if os.path.isfile(outfile) and os.stat(outfile).st_size != 0:
        overwrite = input(outfile + ' has data. Overwrite? [y/N] ')
        if overwrite == 'y':
            open(outfile, 'w').close()
        else:
            print("Ok, exiting now.")
            os.sys.exit(0)

    with open('intl-airports.csv', 'r', newline='') as csvfile:
        spamreader = csv.reader(csvfile)

        for row in spamreader:
            city = row[0]
            airport = row[1]
            print(city + delim + airport)

            # Geocoding an address
            geocode_result = gmaps.geocode(airport)
            y = geocode_result

            with open(outfile, 'a') as latLng:
                latLng.write(city + delim + airport + delim)
                try:
                    lat = y[0]['geometry']['location']['lat']
                    lng = y[0]['geometry']['location']['lng']
                    latLng.write(str(lat) + delim + str(lng) + '\n')
                except IndexError:
                    latLng.write('null' + delim + 'null' + '\n')
                    pass


if __name__ == '__main__':
    main()
