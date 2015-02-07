__author__ = 'buckbaskin'

import os
from shutil import copy

start_folder = r'C:\Users\mlh\Downloads'
destination_folder = r'C:\Users\mlh\Documents\GitHub\CWRUHacks2015\Assets\images'

def main():
    print 'main'
    count = 0
    for dirName, subdirList, fileList in os.walk(start_folder):
        print('Processing directory: %s' % dirName)
        for fname in fileList:
            if fname[-4:] == '.jpg': # or fname[-4:] == '.png':
                print('\timage copied from file %s to location %s' % (fname , destination_folder))
                count += 1
                copy(start_folder+fname , destination_folder)
        break

if __name__ == '__main__':
    main()