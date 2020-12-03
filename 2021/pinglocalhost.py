#!/usr/bin/env python3 
# this code will display a localhost ip and ping 127.0.0.1 3 times.
# Both 'ip a' and 'ping 127.0.0.1 -c3' are strings.
import os
os.system('ip a')
os.system('ping 127.0.0.1 -c3')
