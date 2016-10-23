#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, division, absolute_import
from PIL import Image as pImage
import numpy
import os
import random

class Image:
   """ Load images """

   BLOCK_SIZE = 20  # var for set mini image size
   TRESHOLD = 60  #  max number between the same pictures

   def __init__(self, filename):
       self.filename = filename

   def load(self):
       try:
           img = pImage.open(self.filename) #load file
           mini_img = img.resize((Image.BLOCK_SIZE, Image.BLOCK_SIZE), pImage.BILINEAR) #resize image
           self.t_data = numpy.array(
              [sum(list(x)) for x in mini_img.getdata()]      # create array base on image data
           )
           del mini_img, img    # clear vars
       except:
             print('\n Load error:  %s' % self.filename)
       return self

   def __repr__(self):
        return self.filename      # return filename

   def __mul__(self, other):
       return sum(1 for x in self.t_data - other.t_data if abs(x) > Image.TRESHOLD)


class ImageList:
    """Build images list for directory"""

    def __init__(self, dirname):
        self.dirname = dirname
        self.load()

    def load(self):
        self.images = [Image(os.path.join(self.dirname, filename)).load() for filename in os.listdir(self.dirname)
                       if filename.endswith('.jpg')]
        random.shuffle(self.images)
        return self

    def __repr__(self):
        return '\n'.join((x.filename for x in self.images))

    def html(self, indexfile):
        body = ['<html><body>']
        for img in self.images:
            distance = sorted([(img * x, x) for x in self.images], key=lambda x: x[0])
            body += [
                '<img src="'+x.filename+'" width="200"/>'
                for dist, x in distance if dist < 220]
            body += ['<hr>']
        body += ['</body</html>']
        content = '\n'.join(body)
        try:
            indexhtml = open(indexfile, 'w')
            indexhtml.write(content)
        except:
            print("error build index.html")


if __name__ == '__main__':
   my = ImageList('/home/pag/fs/photos/')
   my.html('/home/pag/fs/index.html')

