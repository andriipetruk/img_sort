#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, division, absolute_import
from PIL import Image as pImage
import numpy
import os
import random

class Image:
   """ Load images """

   BLOCK_SIZE = 20 # var for set mini image size

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


class ImageList:
    """Build images list for directory"""

    def __init__(self, dirname):
        self.dirname = dirname
        self.load()

    def load(self):
        self.images = \
            [Image(os.path.join(self.dirname, filename)).load() \
                       for filename in os.listdir(self.dirname)
                           if filename.endswith('.jpg')]
        random.shuffle(self.images)
        return self

    def __repr__(self):
        return '\n'.join((x.filename for x in self.images))

    def html(self, indexfile):
        body = ['<html><body>']
        body += ['<img src="'+x.filename+'" width="200"/>' for x in self.images]
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




