#!/usr/bin/env python
#-*- coding:utf-8 -*-
#----------------------------------------
# Author: Richard J. Marini (richardjmarini@gmail.com)
# Description: Represents a vertex point
# Date: 1/11/14
#----------------------------------------

from autovivification import Autovivification

class Point(Autovivification):
   '''
   object holder for coordinates
   '''
   def __init__(self, **properties):

      super(Point, self).__init__(**properties)
