#!/usr/bin/env python
#-*- coding:utf-8 -*-
#----------------------------------------
# Author: Richard J. Marini (richardjmarini@gmail.com)
# Description: Autovivification  -- turns python structure into object structure
# Date: 1/11/14
#----------------------------------------

class Autovivification(object):
   '''
   dynamically creates object based on nested dictionary/list structures
   '''

   def __init__(self, **properties):
      '''
      initializes object properties via arbitrary key/value pairs 
      revcursively walks any nested structures
      '''
     
      # convert key/value paris passed into object properties 
      for pname, pvalue in properties.items():

         if type(pvalue) == dict:
            setattr(self, pname, Autovivification(**pvalue))

         elif type(pvalue) in (list, tuple):
            setattr(self, pname, [Autovivification(**element) if type(element) == dict else element for element in pvalue])

         else:
            setattr(self, pname, pvalue)
