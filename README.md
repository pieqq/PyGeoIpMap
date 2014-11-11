# PyGeoIpMap


A Python script to show where IP addresses are coming from by plotting them on a World map.

##Requirements

* [numpy](http://www.numpy.org/)
* [matplotlib](http://matplotlib.org/)
* [Basemap](http://matplotlib.org/basemap/)

PyGeoIpMap can be installed along with its dependencies easily on Ubuntu Linux with the following command:

```bash
sudo apt-get install python-numpy python-matplotlib python-mpltoolkits.basemap
```

or using the [Anaconda](http://continuum.io/downloads) distribution:

```
conda install numpy matplotlib basemap
```

Unfortunately, there is no Python3 version of `python-mpltoolkits.basemap` for the moment so this script is Python 2.7+ only.
=======
Unfortunately, there is no Python3 version of `python-mpltoolkits.basemap` at the moment.
Consequently this script is Python 2.7+ only.

##Usage

```
usage: pygeoipmap.py [-h] [-o OUTPUT] [-f {ip,csv}] [-s {f,m}] [-db DB] input

Visualize community on a map.

positional arguments:
  input                 Input file. One IP per line or, if FORMAT set to
                        'csv', CSV formatted file ending with latitude and
                        longitude positions

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Path to save the file (e.g. /tmp/output.png)
  -f {ip,csv}, --format {ip,csv}
                        Format of the input file.
  -s {f,m}, --service {f,m}
                        Geolocation service (f=FreeGeoIP, m=MaxMind local
                        database)
  -db DB, --db DB       Full path to MaxMind database file (default =
                        ./GeoLiteCity.dat)
```

##Examples

###Using a list of IP addresses (and the FreeGeoIp web service)

A World map can be generated from a list of IP addresses by running the following command:

```bash
python pygeoipmap.py /tmp/ip.txt
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

###Using a CSV file already containing latitude and longitude data

In that case, the program will use data available from [FreeGeoIp](http://freegeoip.net/) to find the location of each of these IPs and generate a World map in `output.png`. Alternatively, local [MaxMind](http://dev.maxmind.com/geoip/legacy/geolite/) database files can be used with the MaxMind [GeoIP](https://github.com/maxmind/geoip-api-python) library.

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
python pygeoipmap.py -o /tmp/evil_hackers.jpg -f csv data.csv
```

PyGeoIpMap will output the World map `/tmp/evil_hackers.jpg` as seen below.

![evil_hackers.jpg](http://i.imgur.com/IGIaKDb.jpg)
