#!/usr/bin/env python
# coding: utf-8

from __future__ import print_function, unicode_literals, with_statement
import argparse
import requests
import json
import numpy
import csv
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap


def get_ip(ip_file):
    """
    Returns a list of IP addresses from a file containing one IP per line.
    """
    #ip_list = []
    with open(ip_file, 'r') as f:
        ip_list = [line.strip() for line in f]
    return ip_list


def get_lat_lon(ip_list=[], lats=[], lons=[]):
    """
    This function connects to the FreeGeoIP web service to get info from
    a list of IP addresses.
    Returns two lists (latitude and longitude).
    """
    print("Processing {} IPs...".format(len(ip_list)))
    for ip in ip_list:
        r = requests.get("https://freegeoip.net/json/"+ip)
        #json_response = json.loads(r.content.decode('utf-8'))
        json_response = r.json()
        print("{ip}, {city}, {country_name}, {latitude}, {longitude}".format(**json_response))
        if json_response['latitude'] and json_response['longitude']:
            lats.append(json_response['latitude'])
            lons.append(json_response['longitude'])
    return lats, lons


def get_lat_lon_from_csv(csv_file, lats=[], lons=[]):
    """
    Retrieves the last two rows of a CSV formatted file to use as latitude
    and longitude.
    Returns two lists (latitudes and longitudes).

    Example CSV file:
    119.80.39.54, Beijing, China, 39.9289, 116.3883
    101.44.1.135, Shanghai, China, 31.0456, 121.3997
    219.144.17.74, Xian, China, 34.2583, 108.9286
    64.27.26.7, Los Angeles, United States, 34.053, -118.2642
    """
    with open(csv_file, 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            lats.append(row[-2])
            lons.append(row[-1])
    return lats, lons


def generate_map(output, lats=[], lons=[]):
    """
    Using Basemap and the matplotlib toolkit, this function generates a map and
    puts a red dot at the location of every IP addresses found in the list.
    The map is then saved in the file specified in `output`.
    """
    print("Generating map and saving it to {}".format(output))
    m = Basemap(projection='cyl', resolution='l')
    m.bluemarble()
    x, y = m(lons, lats)
    m.scatter(x, y, s=1, color='#ff0000', marker='o', alpha=0.3)
    plt.savefig(output, dpi=300, bbox_inches='tight')


def main():
    parser = argparse.ArgumentParser(description='Visualize community on a map.')
    parser.add_argument('input', type=str, help='Input file. One IP per line or, if FORMAT set to \'csv\', CSV formatted file ending with latitude and longitude positions')
    parser.add_argument('-o', '--output', default='output.png', help='Path to save the file (e.g. /tmp/output.png)')
    parser.add_argument('-f', '--format', default='ip', choices=['ip', 'csv'], help='Format of the input file.')

    args = parser.parse_args()

    output = args.output

    if args.format == 'ip':
        ip_list = get_ip(args.input)
        lats, lons = get_lat_lon(ip_list)
    elif args.format == 'csv':
        lats, lons = get_lat_lon_from_csv(args.input)

    generate_map(output, lats, lons)

if __name__ == '__main__':
    main()
