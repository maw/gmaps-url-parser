#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re


def parse(url):
    coords = {}
    
    try:
        coords_re = re.compile(r'place/(.+)/@(.+),(.+),(.+)/')
        coords['latitude'] = float(coords_re.search(url).group(2))
        coords['longitude'] = float(coords_re.search(url).group(3))
        coords['place'] = coords_re.search(url).group(1).replace('+', ' ')
        type_string = coords_re.search(url).group(4)
        if type_string.endswith('m'):
            coords['maptype'] = 'earth'
            coords['zoom_level'] = type_string.strip('m')
        elif type_string.endswith('z'):
            coords['maptype'] = 'map'
            coords['zoom_level'] = type_string.strip('z')
        return coords
    except AttributeError:
        pass

    # if the second attempt fails, just let the exception through :(

    """
    compare
    https://www.google.com.mx/maps/place/Sala+Nezahualc%C3%B3yotl/@19.3143748,-99.1844542,15z/data=!4m5!3m4!1s0x0:0x332d337be253c646!8m2!3d19.3143748!4d-99.1844542
    https://www.google.com.mx/maps/@49.4510132,11.0768289,18.24z
    https://www.google.com/maps/@19.3902065,-99.1615174,20.92z
    """
    coords_re = re.compile(r'maps/@(.+),(.+),(.+)')
    coords['latitude'] = float(coords_re.search(url).group(1))
    coords['longitude'] = float(coords_re.search(url).group(2))
    type_string = coords_re.search(url).group(3)
    if type_string.endswith('m'):
        coords['maptype'] = 'earth'
        coords['zoom_level'] = type_string.strip('m')
    elif type_string.endswith('z'):
        coords['maptype'] = 'map'
        coords['zoom_level'] = type_string.strip('z')
    
    return coords

if __name__ == '__main__':
    url1 = 'https://www.google.com.mx/maps/place/Sala+Nezahualc%C3%B3yotl/@19.3143748,-99.1844542,15z/data=!4m5!3m4!1s0x0:0x332d337be253c646!8m2!3d19.3143748!4d-99.1844542'
    url2 = 'https://www.google.com.mx/maps/@49.4510132,11.0768289,18.24z'
    url3 = 'https://www.google.com.mx/maps/@28.4957785,108.0734364,14.8z'
    
    print(parse(url1))
    print(parse(url2))
    print(parse(url3))
