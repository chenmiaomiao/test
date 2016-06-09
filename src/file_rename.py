# _*_ coding: utf8 _*_

import os
import sys
# path = u'D:\\(专辑)jQuery Tutorials Playlist\\'

path = raw_input('Type the path: ')

print path

path = path.replace('\\', '/')

path = path.decode('utf8')

print path

assert os.path.exists(path), "I did not find the file at, "+str(path)

for (path, dirs, files) in os.walk(path):
    print path
    print dirs
    prefix_len = len(str(len(files)))
    print prefix_len
    for filename in files:
        filename_frag = filename.split('_')
        print filename, len(filename_frag[0])
        if len(filename_frag[0]) < prefix_len:
            prefix_new = '%0*d' % (prefix_len, int(filename_frag[0]))
            filename_frag[0] = prefix_new
            filename_new = '_'.join(filename_frag)
            os.rename(path + '/' + filename, path + '/' + filename_new)
            print 'Old: %s --> New: %s' % (filename, filename_new)
            
    print 'Bingo!'