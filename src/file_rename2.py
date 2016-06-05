# _*_ coding: utf8 _*_

import os
import sys
import re

path = u'C:/Users/oldse/Favorites/Links'

for (path, dirs, files) in os.walk(path):
    print path
    print dirs
    for filename in files:
        print filename
        filename_frag = list(filename)
        is_duplicate = re.search('_+\d\.url', filename)
        print is_duplicate
        
        if filename_frag[0] == "#":
            print 'starts with #: ' + filename
            filename_new = ''.join(filename_frag[1:])
            os.rename(path+filename, path+filename_new)
            print 'Old: %s --> New: %s' % (filename, filename_new)
        if is_duplicate:
            print 'ends with suffix: ' + filename
            filename_new = re.sub('_+\d(\.url)', '\1', filename)
            os.rename(path+filename, path+filename_new)
            print 'Old: %s --> New: %s' % (filename, filename_new)
            
    print 'Bingo!'