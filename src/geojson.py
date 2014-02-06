#!/usr/bin/env python
#-*- coding:utf-8 -*-
#----------------------------------------
# Author: Richard J. Marini (richardjmarini@gmail.com)
# Description: Geometric Relations
# Date: 1/11/14
#----------------------------------------

from codecs import open as open
from optparse import OptionParser, make_option
from sys import argv, stderr
from json import load

from point import Point
from shape import Shape
from autovivification import Autovivification
from geometry import Geometry

def parse_args(argv):
   '''
   parses command line arguments
   '''

   optParser= OptionParser()

   [ optParser.add_option(opt) for opt in [
      make_option('-s', '--shapes', default= None, help= 'json file containing the shapes')
   ]]

   opts, args= optParser.parse_args()

   # if shape file was not pased in, display error and usage
   if opts.shapes == None:
     print >> stderr, "--shape=<filename> argument required"
     optParser.print_help()
     exit(-1)

   return args, opts


if __name__ == '__main__':

   # parse cmd line args
   (args, opts)= parse_args(argv)

   # load the json file
   properties= load(open(opts.shapes, 'r'))

   # process our geometry plane
   geometry= Geometry(**properties.get('geometry'))
   for relation in geometry.relations():
      print relation
