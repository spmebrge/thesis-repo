#!/usr/bin/python
import os
line="Hello world!"
num=5
os.system("echo %(num)i" %locals())

