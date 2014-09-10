#!/usr/bin/python
#
# Copyright 2011 Google Inc. All Rights Reserved.

"""One-line documentation for prod module.

A detailed description of prod.
"""

__author__ = 'gboland@google.com (Gary Boland)'


import serial
import os
import feedparser
import time
from subprocess import Popen, PIPE
myserial = serial.Serial('/dev/ttyACM0', 9600)
while True:
  result = Popen(('/usr/local/symlinks/prodcertstatus'), stdout=PIPE).stdout
  data = result.readline()
  result.close()
  data1 = data.strip()
  data2 = data1.split()
  data3 = data2[2:]
  data4 = ' '.join(data3)
  myserial.write(data4)
  myserial.flushOutput()
  time.sleep(100)
def main(argv):
  pass


if __name__ == '__main__':
  app.run()
