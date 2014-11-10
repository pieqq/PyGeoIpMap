PyGeoIpMap
==========

Little Python script to show where IP addresses are coming from by plotting them on a World map

# Requirements
* [numpy](http://www.numpy.org/)
* [matplotlib](http://matplotlib.org/)
* [Basemap](http://matplotlib.org/basemap/)

You can install these dependencies easily on Ubuntu Linux like this:

```
sudo apt install python-numpy python-matplotlib python-mpltoolkits.basemap
```

Unfortunately, there is no Python3 version of `python-mpltoolkits.basemap` for the moment so this script is Python 2.7+ only.

# Usage

```bash
pygeoipmap.py [-h] [-o OUTPUT] [-f {ip,csv}] input

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
```

# Examples

##Using a list of IP addresses (and the FreeGeoIp web service)

Say you have a list of IP addresses in a file `/tmp/ip.txt` that looks like this:

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

Run the following command to generate a map:

```
python pygeoipmap.py /tmp/ip.txt
```

In that case, the program will use data available from [FreeGeoIp](http://freegeoip.net/) to find the location of each of these IPs and generate a World map in `output.png`.

##Using a CSV file already containing latitude/longitude data

If you already have the latitude/longitude data, you can use the program to generate the World map without connecting to FreeGeoIp. In that case you need a CSV file where the two last columns are latitude and longitude data.

For instance, here is a `data.csv` file:

```
198.23.67.201, Dallas, United States, 32.9299, -96.8353
223.4.240.25, Hangzhou, China, 30.2936, 120.1614
74.208.213.28, Wayne, United States, 40.0548, -75.4083
119.80.39.54, Beijing, China, 39.9289, 116.3883
101.44.1.135, Shanghai, China, 31.0456, 121.3997
219.144.17.74, Xian, China, 34.2583, 108.9286
64.27.26.7, Los Angeles, United States, 34.053, -118.2642
```

I can then generate the World map in `/tmp/evil_hackers.jpg` with:

```
python pygeoipmap.py -o /tmp/evil_hackers.jpg -f csv data.csv
```

And I'll get the following output in `/tmp/evil_hackers.jpg`:

![](http://i.imgur.com/IGIaKDb.jpg)
