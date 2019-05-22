from pprint import pprint
import configparser
import csv
import googlemaps
import os
import requests
import signal
import sys
import timing


def signal_handler(sig, frame):
    print()
    sys.exit(0)


def main():
    signal.signal(signal.SIGINT, signal_handler)
    config = configparser.ConfigParser()
    config.read('config.ini')
    key = config['DEFAULT']['key']
    gmaps = googlemaps.Client(key=key)
    delim = ','

    outfile = 'city-src.csv'
    if os.path.isfile(outfile) and os.stat(outfile).st_size != 0:
        overwrite = input(outfile + ' has data. Overwrite? [y/N] ')
        if overwrite == 'y':
            open(outfile, 'w').close()
        else:
            print("Ok, exiting now.")
            sys.exit(0)

    with open('pop.csv', 'r', newline='') as csvfile:
        spamreader = csv.reader(csvfile)
        next(csvfile)
        url = 'https://maps.googleapis.com/maps/api/place/photo'

        for row in spamreader:
            id = row[0]
            city = row[1]
            print(city)
            query_result = gmaps.places(city)

            try:
                ref = query_result.get('results')[0].get('photos')[0].get('photo_reference')
                payload = {'key': key, 'photoreference': ref, 'maxwidth': 400}
                r = requests.get(url, params=payload)
                #pprint(vars(r))
                result = r.url

            except:
                result = 'null'

            print(result)
            with open(outfile, 'a') as out:
                out.write(id + ',' + result + '\n')


if __name__ == '__main__':
    main()
