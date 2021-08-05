#!/usr/bin/env python3

import requests
import socket

def check_localhost():
    localhost = socket.gethostbyname('localhost')
    if localhost:
        return True

def check_connectivity():
    request = requests.get("http://www.google.com")
    if request:
        return True