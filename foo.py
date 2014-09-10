#! /usr/bin/python

import sys

script, first, second, third = sys.argv
if len(sys.argv) < 3:
  print "not enough arguments"


print "the first argument is ", first
print "the second argument is ", second
print "the third argument is", third
