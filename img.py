#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, division, absolute_import
from PIL import Image as pImage
import numpy
import os

class Image:
   """ Load images """

   BLOCK_SIZE = 20 # var for set mini image size

   def __init__(self,filename):
       self.filename = filename

   def load(self):
       img = pImage.open(self.filename)
       mini_img = img.resize((Image.BLOCK_SIZE, Image.BLOCK_SIZE), pImage.BILINEAR)
       self.t_data = numpy.array(
           [sum(list(x)) for x in mini_img.getdata()]
       )
       del mini_img, img
       return self

   def __repr__(self):
        return self.filename

a = Image('/home/pag/fs/photos/Фото0031.jpg')

print (a.t_data)





