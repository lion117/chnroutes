# -*- coding: utf-8 -*-
"""
@author: LEO
Date:  2015/12/31
Email:	lion_117@126.com
All Rights Reserved Licensed under the Apache License
"""

import os
import re
import urllib2
import sys
import argparse
import math
import textwrap


def itorate_ip(t_index , t_mask):
    i_result = []
    if t_index < 0 or t_index >255 :
        return  i_result
    for item in range(0,256):
        i_ip = '%s.0.0.0'%item
        i_result.append((i_ip , t_mask))
    return  i_result


def fetch_unVPN_ip(first_ip, second_ip, third_ip, forth_ip):
    results = []
    results.append(("0.0.0.0" ,'0.0.0.0'))

    for item_1 in range(1, 256):
        if item_1 != first_ip:
            i_ip = '%s.0.0.0' % item_1
            i_mask = '255.0.0.0'
            results.append((i_ip, i_mask))
        else:
            for item_2 in range(0, 256):
                if item_2 != second_ip:
                    i_ip = '%s.0.0.0' % item_2
                    i_mask = '255.255.0.0'
                    results.append((i_ip, i_mask))
                else:
                    for item_3 in range(0, 256):
                        if item_3 != second_ip:
                            i_ip = '%s.0.0.0' % item_3
                            i_mask = '255.255.255.0'
                            results.append((i_ip, i_mask))
                        else:
                            for item_4 in range(0, 256):
                                if item_4 != second_ip:
                                    i_ip = '%s.0.0.0' % item_4
                                    i_mask = '255.255.255.255'
                                    results.append((i_ip, i_mask))
    return results






def main():
   print  fetch_unVPN_ip(192,168,4,11)







if __name__ == '__main__':
    main()
    pass
