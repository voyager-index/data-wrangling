# Airports

This python script queries the Google [Geocoding API](https://developers.google.com/maps/documentation/geocoding/intro) to get the lat and lng of various airports (defined in the "intl-airports.csv" file).

# Requirements

- [Python 3](https://www.python.org/)
- [pip](https://pypi.org/project/pip/)

# Quickstart

```sh
source venv/bin/activate

pip install -r requirements.txt

cp config-example.ini config.ini
# change "myCoolKey" to your API key

python airports.py
```

# Output/Results

```sh
# airports.py will output the Cities, Airports queried.
A Coruña, Alvedro Airport                                 
Aalborg, Aalborg Airport                                                                                                                     
Aarhus, Aarhus Airport                                       
Abakan, Abakan International Airport                                                                                                             
Aberdeen, Aberdeen Airport                                                                                                                       
Abidjan, Port Bouet Airport                                                                                                                   
...
...
...
Ürümqi, Ürümqi Diwopu International Airport
İzmir, Adnan Menderes Airport
Łódź, Łódź Władysław Reymont Airport
Šiauliai, Šiauliai International Airport
Žilina, Žilina Airport

# airports.py will also write Airport,Lat,Lng to the "lat-lng.txt" file.
cat lat-lng.txt
Alvedro Airport,43.301164,-8.3792087                                       
Aalborg Airport,57.0969187,9.8564632                                      
Aarhus Airport,56.3075123,10.6281027                                            
Abakan International Airport,53.7511881,91.3997373                  
Aberdeen Airport,45.4534583,-98.4177261 
...
...
...
Diwopu International Airport,43.9072222,87.4741667
Adnan Menderes Airport,38.293763,27.1520285
Łódź Władysław Reymont Airport,51.7197051,19.3908091
Šiauliai International Airport,55.8938895,23.3950107
Žilina Airport,49.2336593,18.6141831
```

# Uninstallation

```sh
rm airports.py
```
