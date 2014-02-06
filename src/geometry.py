#!/usr/bin/env python
#-*- coding:utf-8 -*-
#----------------------------------------
# Author: Richard J. Marini (richardjmarini@gmail.com)
# Description: Geometry -- polygon operations
# Date: 1/11/14
#----------------------------------------

from sys import stderr
from itertools import product

from autovivification import Autovivification
from shape import Shape

class Geometry(Autovivification):
   '''
   Main processing class for our geometry plane
   '''
   def __init__(self, **properties):

      super(Geometry, self).__init__(**properties)
      self.previously_rejected= []

   def validPolygons(self):
      '''
      returns only 'valid' polygons within our list of geometric shapes
      '''

      previously_rejected= []
      for properties in self.shape:

         # create instance of shape 
         shape= Shape(**properties.__dict__)

         # if we found a valid convex polygon yield it to our caller but no need to test twice
         if shape.id not in self.previously_rejected and shape.isConvexPolygon():
            yield shape

         else:

            # if this is a new reject display warning
            if shape.id not in self.previously_rejected:
               print  >> stderr, shape.id, "is not a polygon" 

            # keep trace of which shapes we've previoulsy rejected
            self.previously_rejected.append(shape.id)

   def inPolygon(self, point, shape):
      '''
      determines if the given point is within the given shape
      returns 1 if True, 0 if False
      '''
      in_poly= 0

      # if point is within the bounding area then we're within the polygon
      if not (point.x < shape.x_min or point.x > shape.x_max or point.y < shape.y_min or point.y > shape.y_max):
         in_poly= 1

      return in_poly

   def isNested(self, s1, s2):
      '''
      determines if all points within s1 are within s2
      '''

      # calculate how may points of one shape are within the other shape
      s1_nested_points= sum([self.inPolygon(v, s2) for v in s1.point])

      is_nested= (s1.num_points == s1_nested_points)

      return is_nested

   def isIntersected(self, s1, s2):
      '''
         determintes if some points of s1 are within s2
      '''

      # calculate how may points of one shape are within the other shape
      s1_nested_points= sum([self.inPolygon(v, s2) for v in s1.point])

      is_intersected= (s1_nested_points > 0 and s1_nested_points < s1.num_points)

      return is_intersected

   def isSeperate(self, s1, s2):
      '''
      determines if all points from s1 are outside of s2
      '''

      # calculate how may points of one shape are within the other shape
      s1_nested_points= sum([self.inPolygon(v, s2) for v in s1.point])
      s2_nested_points= sum([self.inPolygon(v, s1) for v in s2.point])

      is_separate= (s1_nested_points == 0 and s2_nested_points == 0)

      return is_separate

   def relations(self):
      '''
      figure out relations between shapes within our geometry plane
      '''
      # create cartesian and compare each shape with every other shape (filter out comparing with itself)
      valid_polygons= filter(lambda s: s[0].id != s[1].id, product(self.validPolygons(), self.validPolygons()))

      # for each comparison determine how the shape interacts with each other
      for s1, s2 in valid_polygons:

         # inside: all the points are nested, therefore one surrounds the other
         if self.isNested(s1, s2):
            yield "%s is inside %s" % (s1.id, s2.id)
            yield "%s is surrounds %s" % (s2.id, s1.id)

         # intersects: there are some nested points but not all nested
         if self.isIntersected(s1, s2):
            yield "%s intersects %s" % (s1.id, s2.id)

         # separate: there are no nested points
         if self.isSeperate(s1, s2):
            yield "%s is separate from %s" % (s1.id, s2.id)
