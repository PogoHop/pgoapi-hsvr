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
import sys
import json
import time
import pprint
import logging
import getpass
import argparse
import requests
import re
import uuid

# add directory of this file to PATH, so that the package will be found
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

# import Pokemon Go API lib
from pgoapi import pgoapi
from pgoapi import utilities as util


log = logging.getLogger(__name__)

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
    parser.add_argument("-p", "--password", help="Password")
    parser.add_argument("-l", "--location", help="Location", required=required("location"))
    parser.add_argument("-d", "--debug", help="Debug Mode", action='store_true')
    parser.add_argument("-t", "--test", help="Only parse the specified location", action='store_true')
    parser.add_argument("-px", "--proxy", help="Specify a socks5 proxy url")
    parser.set_defaults(DEBUG=False, TEST=False)
    config = parser.parse_args()

    # Passed in arguments shoud trump
    for key in config.__dict__:
        if key in load and config.__dict__[key] == None:
            config.__dict__[key] = str(load[key])

    if config.__dict__["password"] is None:
        log.info("Secure Password Input (if there is no password prompt, use --password <pw>):")
        config.__dict__["password"] = getpass.getpass()

    if config.auth_service not in ['ptc', 'google']:
      log.error("Invalid Auth service specified! ('ptc' or 'google')")
      return None

    return config


def main():
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

    device_info = {
        'device_id': uuid.uuid4().hex,
        'device_brand': 'Apple',
        'device_model': 'iPhone',
        'device_comms_model': 'iPhone8,2',
        'hardware_manufacturer': 'Apple',
        'hardware_model': 'N66AP',
        'firmware_brand': 'iPhone OS',
        'firmware_type': '9.3.3'
    }
    # instantiate pgoapi
    api = pgoapi.PGoApi(device_info=device_info)
    if config.proxy:
        api.set_proxy({'http': config.proxy, 'https': config.proxy})

    # parse position TODO
    position = util.get_pos_by_name(config.location)
    if not position:
        log.error('Your given location could not be found by name')
        return
    elif config.test:
        return

    #set player position on the earth
    api.set_position(*position)

    # new authentication initialitation
    if config.proxy:
        api.set_authentication(provider = config.auth_service, username = config.username, password =  config.password, proxy_config = {'http': config.proxy, 'https': config.proxy})
    else:
        api.set_authentication(provider = config.auth_service, username = config.username, password =  config.password)

    # provide the path for your encrypt dll
    api.activate_signature(os.path.join(os.path.dirname(os.path.realpath(__file__)), "libencrypt.so"))
    api.app_simulation_login()

    time.sleep(10)

    cell_ids = util.get_cell_ids(position[0], position[1])
    timestamps = [0,] * len(cell_ids)
    request = api.create_request()
    request.get_map_objects(latitude =position[0], longitude = position[1], since_timestamp_ms = timestamps, cell_id = cell_ids)
    request.check_challenge()
    #request.get_hatched_eggs()
    #request.get_inventory()
    #request.check_awarded_badges()
    #request.download_settings(hash="8631c515a4c084ef30ef4d6eee8f5f5b250db697")#old54b359c97e46900f87211ef6e6dd0b7f2a3ea1f5
    #request.get_buddy_walked()
    response_dict = request.call()
    #print('Response dictionary (map_objects): \n\r{}'.format(pprint.PrettyPrinter(indent=4).pformat(response_dict)))

    if 'status' not in response_dict['responses']['GET_MAP_OBJECTS']:
        raise ValueError("Invalid response: {}".format(json.dumps(response_dict, indent=2)))
    if response_dict['responses']['GET_MAP_OBJECTS']['status'] == 1:
        for cell in response_dict['responses']['GET_MAP_OBJECTS']['map_cells']:
            if 'nearby_pokemons' in cell:
                print "nearby_pokemons in cell: " + cell['s2_cell_id']
                print cell['nearby_pokemons']
            if 'wild_pokemons' in cell:
                pprint.PrettyPrinter(indent=2).pformat(cell['wild_pokemons'])

        print response_dict['responses']['CHECK_CHALLENGE']

    """
    response_token = raw_input()
    request = api.create_request()
    request.verify_challenge(token=response_token)
    response_dict = request.call()
    print('Response dictionary (get_player): \n\r{}'.format(pprint.PrettyPrinter(indent=4).pformat(response_dict)))
    
    """

if __name__ == '__main__':
    main()


