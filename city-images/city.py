from pprint import pprint
import configparser
import csv
import googlemaps
import os
import requests
import signal
import sys
import timing
import json


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
    i = 1
    inputs_dir = 'inputs'
    outputs = 'outputs'

    f = []
    for (dirpath, dirnames, filenames) in os.walk(inputs_dir):
        inputs = sorted(filenames)

    try:
        index = int(input('Index to start at? [0] '))
    except:
        index = 0

    try:
        index_end = int(input('Index to end at (exclusive)? [' + str(index + 1) + '] '))
    except:
        index_end = index + 1

    for f in range(index, index_end + 1):
        outfile = outputs + '/city-src-' + str(index) + '.csv'
        infile = os.path.join(inputs_dir, inputs[i])
        print('outfile:', outfile)
        print('infile:', infile)
        if os.path.isfile(outfile) and os.stat(outfile).st_size != 0:
            overwrite = input(outfile + ' has data. Overwrite? [y/N] ')
            if overwrite == 'y':
                open(outfile, 'w').close()
            else:
                print("Ok, exiting now.")
                sys.exit(0)

        with open(os.path.join(inputs_dir, inputs[i]), 'r', newline='') as csvfile:
            spamreader = csv.reader(csvfile)
            # uncomment if csv files has header
            # next(csvfile)
            url = 'https://api.teleport.org/api/cities/'
            gurl = 'https://maps.googleapis.com/maps/api/place/photo'

            city_url = 'data._embedded["city:search-results"][0]._links["city:item"].href'
            city_guess = 'data._embedded["city:search-results"][0].matching_full_name'
            urban_url = 'data._links["city:urban_area"].href'
            image_url = 'data._links["ua:images"].href'
            mobile_url = 'data.photos[0].image.mobile'

            for row in spamreader:
                id = row[0]
                city = row[1]
                print(city)

                try:
                    payload = {'search': city}
                    r = requests.get(url, params=payload)

                    city_url = json.loads(r.content).get('_embedded')['city:search-results'][0].get('_links')['city:item'].get('href')
                    r = requests.get(city_url)
                    urban_url = json.loads(r.content).get('_links')['city:urban_area'].get('href')
                    r = requests.get(urban_url)
                    image_url = json.loads(r.content).get('_links')['ua:images'].get('href')
                    r = requests.get(image_url)
                    mobile_url = json.loads(r.content).get('photos')[0].get('image').get('mobile')
                    r = requests.get(mobile_url)
                    result = mobile_url

                except:

                    try:
                        query_result = gmaps.places(city)
                        ref = query_result.get('results')[0].get('photos')[0].get('photo_reference')
                        payload = {'key': key, 'photoreference': ref, 'maxwidth': 400}
                        r = requests.get(gurl, params=payload)
                        result = r.url

                    except:
                        result = 'null'

                print(result)
                with open(outfile, 'a') as out:
                    out.write(city + ',' + id + ',' + result + '\n')
        i += 1

if __name__ == '__main__':
    main()
