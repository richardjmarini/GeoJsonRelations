#!/usr/bin/env python
#-*- coding:utf-8 -*-
#----------------------------------------
# Author: Richard J. Marini (richardjmarini@gmail.com)
# Company: Shape container object
# Date: 1/11/14
#----------------------------------------

from math import atan2, degrees

from autovivification import Autovivification

class Shape(Autovivification):

   def __init__(self, **properties):

      super(Shape, self).__init__(**properties)

      self.num_points= len(self.point)
      self.x_min= min([p.x for p in self.point])
      self.x_max= max([p.x for p in self.point])
      self.y_min= min([p.y for p in self.point])
      self.y_max= max([p.y for p in self.point])

   def isConvexPolygon(self):
      '''
      checks to see if the sum of the internal angles is 180 degrees
      '''
       
      sum_of_angles= sum([degrees(atan2(self.point[i].y - self.point[i-1].y, self.point[i].x - self.point[i-1].x)) for i in range(0, len(self.point))])

      return sum_of_angles <= 180
