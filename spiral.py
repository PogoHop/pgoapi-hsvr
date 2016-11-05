#!/usr/bin/env python
"""
pgoapi - Pokemon Go API
Copyright (c) 2016 tjado <https://github.com/tejado>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
OR OTHER DEALINGS IN THE SOFTWARE.

Author: tjado <https://github.com/tejado>
"""

import os
import re
import sys
import json
import math
import time
import struct
import random
import logging
import requests
import argparse

from pgoapi import PGoApi
from pgoapi.utilities import f2i, h2f

from google.protobuf.internal import encoder
from geopy.geocoders import GoogleV3
from s2sphere import Cell, CellId, LatLng

log = logging.getLogger(__name__)

#radius of visible pokemon in m 
#VISIBILITY_RADIUS = 70
#DG_PER_M_LAT = 1.0/111210.0
#DG_PER_M_LNG = 1.0/73170.0
#DISTANCE_SCANPOINTS = (3.0*VISIBILITY_RADIUS)/(2.0*math.cos(math.radians(30)))


def get_pos_by_name(location_name):
    geolocator = GoogleV3()
    loc = geolocator.geocode(location_name)

    log.info('Your given location: %s', loc.address.encode('utf-8'))
    log.info('lat/long/alt: %s %s %s', loc.latitude, loc.longitude, loc.altitude)

    return (loc.latitude, loc.longitude, loc.altitude)

def get_cellid(lat, long):
    origin = CellId.from_lat_lng(LatLng.from_degrees(lat, long)).parent(15)
    walk = [origin.id()]

    # 10 before and 10 after
    next = origin.next()
    prev = origin.prev()
    for i in range(10):
        walk.append(prev.id())
        walk.append(next.id())
        next = next.next()
        prev = prev.prev()
    return sorted(walk)

def encode(cellid):
    output = []
    encoder._VarintEncoder()(output.append, cellid)
    return ''.join(output)

def init_config():
    parser = argparse.ArgumentParser()
    config_file = "config.json"

    # If config file exists, load variables from json
    load   = {}
    if os.path.isfile(config_file):
        with open(config_file) as data:
            load.update(json.load(data))

    # Read passed in Arguments
    required = lambda x: not x in load
    parser.add_argument("-a", "--auth_service", help="Auth Service ('ptc' or 'google')",
        required=required("auth_service"))
    parser.add_argument("-u", "--username", help="Username", required=required("username"))
    parser.add_argument("-p", "--password", help="Password", required=required("password"))
    parser.add_argument("-l", "--location", help="Location", required=required("location"))
    parser.add_argument("-d", "--debug", help="Debug Mode", action='store_true')
    parser.add_argument("-t", "--test", help="Only parse the specified location", action='store_true')
    parser.set_defaults(DEBUG=False, TEST=False)
    config = parser.parse_args()

    # Passed in arguments shoud trump
    for key in config.__dict__:
        if key in load and config.__dict__[key] == None:
            config.__dict__[key] = load[key]

    if config.auth_service not in ['ptc', 'google']:
      log.error("Invalid Auth service specified! ('ptc' or 'google')")
      return None

    return config

def main():
    timeStart = time.time()
    # log settings
    # log format
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(module)10s] [%(levelname)5s] %(message)s')
    # log level for http request class
    logging.getLogger("requests").setLevel(logging.WARNING)
    # log level for main pgoapi class
    logging.getLogger("pgoapi").setLevel(logging.INFO)
    # log level for internal pgoapi class
    logging.getLogger("rpc_api").setLevel(logging.INFO)

    config = init_config()
    if not config:
        return

    if config.debug:
        logging.getLogger("requests").setLevel(logging.DEBUG)
        logging.getLogger("pgoapi").setLevel(logging.DEBUG)
        logging.getLogger("rpc_api").setLevel(logging.DEBUG)

    position = get_pos_by_name(config.location)
    if config.test:
        return

    # instantiate pgoapi
    api = PGoApi()

    # provide player position on the earth
    api.set_position(*position)

    if not api.login(config.auth_service, config.username, config.password):
        return

    # chain subrequests (methods) into one RPC call

    # get player profile call
    # ----------------------
    #api.get_player()

    # execute the RPC call
    #response_dict = api.call()
    #print('Response dictionary: \n\r{}'.format(json.dumps(response_dict, indent=2)))
    find_poi(api, position[0], position[1])

def find_poi(api, lat, lng):
    poi = {'pokemons': [], 'forts': []}
    step_size = 0.003
    step_limit = 28
    coords = generate_spiral(lat, lng, step_size, step_limit)
    #timestamp = "\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000"
    pokeCount = 0
    for coord in coords:
        lat = coord['lat']
        lng = coord['lng']
        api.set_position(lat, lng, 0)

        cellid = get_cellid(lat, lng)
        timestamp = [0,] * len(cellid)
        
        response_dict = api.get_map_objects(latitude=f2i(lat), longitude=f2i(lng), since_timestamp_ms=timestamp, cell_id=cellid)
        print response_dict
        if 'status' not in response_dict['responses']['GET_MAP_OBJECTS']:
            raise ValueError("Invalid response: {}".format(json.dumps(response_dict, indent=2)))
        if response_dict['responses']['GET_MAP_OBJECTS']['status'] == 1:
            for cell in response_dict['responses']['GET_MAP_OBJECTS']['map_cells']:
                if 'wild_pokemons' in cell:
                    for wpoke in cell['wild_pokemons']:
                        poke = {"type": wpoke['pokemon_data']['pokemon_id'], "lon": wpoke['longitude'], "lat": wpoke['latitude'], "time_vanish": wpoke['time_till_hidden_ms']/1000}
                        poi['pokemons'].append(poke)
                        pokeCount = pokeCount + 1
                #TODO: what about nearby pokemons??

        time.sleep(30)
    print('POI dictionary: \n\r{}'.format(json.dumps(poi, indent=2)))
    print "pokecount: {} pokemons {}".format(pokeCount, len(poi['pokemons'])) 
    print('Open this in a browser to see the path the spiral search took:')
    print_gmaps_dbug(coords)

def get_key_from_pokemon(pokemon):
    return '{}-{}'.format(pokemon['spawnpoint_id'], pokemon['pokemon_data']['pokemon_id'])

def print_gmaps_dbug(coords):
    url_string = 'http://maps.googleapis.com/maps/api/staticmap?size=400x400&path='
    for coord in coords:
        url_string += '{},{}|'.format(coord['lat'], coord['lng'])
    print(url_string[:-1])

def generate_spiral(starting_lat, starting_lng, step_size, step_limit):
    return generate_location_steps(starting_lat, starting_lng, 2)

def generate_location_steps(origin_lat, origin_lng, step_count):
    #Bearing (degrees)
    NORTH = 0
    EAST = 90
    SOUTH = 180
    WEST = 270

    pulse_radius = 0.07                  # km - radius of players heartbeat is 100m
    xdist = math.sqrt(3)*pulse_radius   # dist between column centers
    ydist = 3*(pulse_radius/2)          # dist between row centers

    coords = [{'lat': origin_lat, 'lng': origin_lng}] #insert initial location
    loc = (origin_lat, origin_lng, 0)
    ring = 1            
    while ring < step_count:
        #Set loc to start at top left
        loc = get_new_coords(loc, ydist, NORTH)
        loc = get_new_coords(loc, xdist/2, WEST)
        for direction in range(6):
            for i in range(ring):
                if direction == 0: # RIGHT
                    loc = get_new_coords(loc, xdist, EAST)
                if direction == 1: # DOWN + RIGHT
                    loc = get_new_coords(loc, ydist, SOUTH)
                    loc = get_new_coords(loc, xdist/2, EAST)
                if direction == 2: # DOWN + LEFT
                    loc = get_new_coords(loc, ydist, SOUTH)
                    loc = get_new_coords(loc, xdist/2, WEST)
                if direction == 3: # LEFT
                    loc = get_new_coords(loc, xdist, WEST)
                if direction == 4: # UP + LEFT
                    loc = get_new_coords(loc, ydist, NORTH)
                    loc = get_new_coords(loc, xdist/2, WEST)
                if direction == 5: # UP + RIGHT
                    loc = get_new_coords(loc, ydist, NORTH)
                    loc = get_new_coords(loc, xdist/2, EAST)
                coords.append({'lat': loc[0], 'lng': loc[1]})
        ring += 1
    return coords

def get_new_coords(init_loc, distance, bearing):
    """ Given an initial lat/lng, a distance(in kms), and a bearing (degrees),
    this will calculate the resulting lat/lng coordinates.
    """ 
    R = 6378.1 #km radius of the earth
    bearing = math.radians(bearing)

    init_coords = [math.radians(init_loc[0]), math.radians(init_loc[1])] # convert lat/lng to radians

    new_lat = math.asin( math.sin(init_coords[0])*math.cos(distance/R) +
        math.cos(init_coords[0])*math.sin(distance/R)*math.cos(bearing))

    new_lon = init_coords[1] + math.atan2(math.sin(bearing)*math.sin(distance/R)*math.cos(init_coords[0]),
        math.cos(distance/R)-math.sin(init_coords[0])*math.sin(new_lat))

    return [math.degrees(new_lat), math.degrees(new_lon)]


if __name__ == '__main__':
    main()
