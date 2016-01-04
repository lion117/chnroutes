#!/usr/bin/env python

import re
import urllib2
import sys
import argparse
import math
import textwrap




def generate_win(metric,first_ip , second_ip , third_ip , forth_ip):
    results = fetch_unVPN_ip(first_ip,second_ip,third_ip,forth_ip)

    upscript_header=textwrap.dedent("""@echo off
    for /F "tokens=3" %%* in ('route print ^| findstr "\\<0.0.0.0\\>"') do set "gw=%%*"
    
    """)
    
    upfile=open('vpnup.bat','w')
    downfile=open('vpndown.bat','w')
    
    upfile.write(upscript_header)
    upfile.write('\n')
    upfile.write('ipconfig /flushdns\n\n')
    
    downfile.write("@echo off")
    downfile.write('\n')
    
    for ip,mask in results:
        upfile.write('route add %s mask %s %s metric %d\n'%(ip,mask,"%gw%",metric))
        downfile.write('route delete %s\n'%(ip))
    
    upfile.close()
    downfile.close()
    
#    up_vbs_wrapper=open('vpnup.vbs','w')
#    up_vbs_wrapper.write('Set objShell = CreateObject("Wscript.shell")\ncall objShell.Run("vpnup.bat",0,FALSE)')
#    up_vbs_wrapper.close()
#    down_vbs_wrapper=open('vpndown.vbs','w')
#    down_vbs_wrapper.write('Set objShell = CreateObject("Wscript.shell")\ncall objShell.Run("vpndown.bat",0,FALSE)')
#    down_vbs_wrapper.close()
    
    print "For pptp on windows only, run vpnup.bat before dialing to vpn," \
          "and run vpndown.bat after disconnected from the vpn."


def fetch_unVPN_ip(first_ip, second_ip, third_ip, forth_ip):
    results = []
    # results.append(("0.0.0.0" ,'0.0.0.0'))

    for item_1 in range(1, 256):
        if item_1 != first_ip:
            i_ip = '%s.0.0.0' % item_1
            i_mask = '255.0.0.0'
            results.append((i_ip, i_mask))
        else:
            for item_2 in range(0, 256):
                if item_2 != second_ip:
                    i_ip = '%s.%s.0.0' % (first_ip,item_2)
                    i_mask = '255.255.0.0'
                    results.append((i_ip, i_mask))
                else:
                    for item_3 in range(0, 256):
                        if item_3 != third_ip:
                            i_ip = '%s.%s.%s.0' %(first_ip,second_ip, item_3)
                            i_mask = '255.255.255.0'
                            results.append((i_ip, i_mask))
                        else:
                            for item_4 in range(0, 256):
                                if item_4 != forth_ip:
                                    i_ip = '%s.%s.%s.%s' %(first_ip,second_ip,third_ip, item_4)
                                    i_mask = '255.255.255.255'
                                    results.append((i_ip, i_mask))
    return results




if __name__=='__main__':
    parser=argparse.ArgumentParser(description="Generate routing rules for vpn.")
    parser.add_argument('-p','--platform',
                        dest='platform',
                        default='openvpn',
                        nargs='?',
                        help="Target platforms, it can be openvpn, mac, linux," 
                        "win, android. openvpn by default.")
    parser.add_argument('-m','--metric',
                        dest='metric',
                        default=5,
                        nargs='?',
                        type=int,
                        help="Metric setting for the route rules")
    args = parser.parse_args()

    generate_win(args.metric , 192,168,4,15)   # 修改需要单独走VPN 通道的ip
