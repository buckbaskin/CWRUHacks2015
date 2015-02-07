__author__ = 'buckbaskin'

import os
from shutil import copytree

start_folder = r'C:\Users\mlh\Music\iTunes\iTunes Media\Music'
destination_folder = r'C:\Users\mlh\Documents\GitHub\CWRUHacks2015\Assets\sounds'

def short_dir(full_name):
    for i in range(len(full_name)-1, 0, -1):
        if full_name[i:i+1] == "\\":
            return full_name[i:]

def main():
    count = 0
    print 'count'
    for dirName, subdirList, fileList in os.walk(start_folder):
        print('Processing directory: %s' % dirName)
        for fname in fileList:
            if fname[-4:] == '.mp3':
                print('\tmusic copied from dir %s to location %s' % (dirName , destination_folder+short_dir(dirName)))
                count += len(fileList)
                copytree(dirName , destination_folder+short_dir(dirName))
                break
    print 'count ' + str(count)

if __name__ == '__main__':
    main()
