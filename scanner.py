#!/bin/bash
import netifaces as ni
import nmap

ni.ifaddresses('enp1s0')
ip=ifaddresses('enp1s0')[ni.AF_INET][0]['addr']
print(ip)

sudo nmap -sn ip

