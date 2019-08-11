# PyGeoIpMap


A Python script to show where IP addresses are coming from by plotting them on a World map. Now compatible with Python3.

![screenshot.jpg](https://raw.githubusercontent.com/lgg-awesome/PyGeoIpMap/master/screenshot.jpg)

## Requirements

* [numpy](http://www.numpy.org/)
* [matplotlib](http://matplotlib.org/)
* [Basemap](http://matplotlib.org/basemap/)
* [GeoIP2-python](https://github.com/maxmind/GeoIP2-python)

PyGeoIpMap can be installed along with its dependencies easily on ubuntu / mint / etc with the following command:

```bash
sudo apt install python3-numpy python3-matplotlib libgeos-dev python3-geoip2 python3-mpltoolkits.basemap
```

## Usage

```
usage: pygeoipmap.py [-h] [-i INPUT] [-o OUTPUT] [-f {ip,csv}] [-s {f,m}]
                     [-db DB] [--extents EXTENTS]

Visualize community on a map.

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input file. One IP per line or, if FORMAT set to
                        'csv', CSV formatted file ending with latitude and
                        longitude positions
  -o OUTPUT, --output OUTPUT
                        Path to save the file (e.g. /tmp/output.png)
  -a APIKEY, --apikey APIKEY
                        API-KEY from ipstack.com
  -f {ip,csv}, --format {ip,csv}
                        Format of the input file.
  -s {f,m}, --service {f,m}
                        Geolocation service (f=ipstack, m=MaxMind local
                        database)
  -db DB, --db DB       Full path to MaxMind database file (default =
                        ./GeoLiteCity.dat)
  --extents W/E/S/N     Spatial extents for the figure
                        (west/east/south/north). Defaults to global.
```

## Examples

### Using a list of IP addresses (and the Ipstack.com web service)

For use this service you need the API-KEY from https://ipstack.com/

A World map can be generated from a list of IP addresses by running the following command:

```bash
python3 pygeoipmap.py --apikey "YOUR-API-KEY" -i /tmp/ip.txt 
```

The list of IP address must be saved to a text file with each IP
address separated by a newline as shown below:

```
218.60.148.32
59.63.175.24
109.207.56.22
59.63.175.25
59.39.71.222
222.186.62.17
72.80.16.100
60.199.196.144
…
```

In that example above, the program will use data available from
[FreeGeoIp](http://freegeoip.net/) to find the location of each IP address and generate a World map called `output.png`.

### Using a MaxMind offline database (Recommended)

Local [MaxMind](https://dev.maxmind.com/geoip/geoip2/geolite2/) database files can be used with the MaxMind [GeoIP](https://github.com/maxmind/GeoIP2-python) library with the `--service` option:

```bash
python3 pygeoipmap.py -i /tmp/ip.txt --service m --db /path/to/GeoLite2-City.mmdb
```

You can download and unzip a copy of the latest MaxMind database as follows:

```bash
wget https://geolite.maxmind.com/download/geoip/database/GeoLite2-City.tar.gz && tar -xzvf GeoLite2-City.tar.gz
```

### Specifying a region for the plot

```bash
python3 pygeoipmap.py -i /tmp/ip.txt --extents=-12/45/30/65 --output=ip.png
```

This limits the plot to Europe.

### Using a CSV file already containing latitude and longitude data

PyGeoIpMap can generate a World map without connecting to FreeGeoIp if the latitude and longitude data are available.
A CSV file where the two last columns are the IP address' corresponding latitude and longitude values.

An example of a CSV file with each IP address' latitude and longitude values provided:

```
198.23.67.201, Dallas, United States, 32.9299, -96.8353
223.4.240.25, Hangzhou, China, 30.2936, 120.1614
74.208.213.28, Wayne, United States, 40.0548, -75.4083
119.80.39.54, Beijing, China, 39.9289, 116.3883
101.44.1.135, Shanghai, China, 31.0456, 121.3997
219.144.17.74, Xian, China, 34.2583, 108.9286
64.27.26.7, Los Angeles, United States, 34.053, -118.2642
```

The World map can be generated from the CSV file by running the following command:

```bash
python3 pygeoipmap.py -o /tmp/evil_hackers.jpg -f csv data.csv
```

PyGeoIpMap will output the World map `/tmp/evil_hackers.jpg` as seen below.

![screenshot.jpg](https://raw.githubusercontent.com/lgg-awesome/PyGeoIpMap/master/screenshot.jpg)
