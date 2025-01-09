#!/usr/local/bin/python2.7
# encoding: utf-8
'''
diskio.diskio -- shortdesc

diskio.diskio is a description

It defines classes_and_methods

@author:     user_name

@copyright:  2015 organization_name. All rights reserved.

@license:    license

@contact:    user_email
@deffield    updated: Updated
'''

import sys
import os
import psutil
import time

from argparse import ArgumentParser
from argparse import RawDescriptionHelpFormatter

__all__ = []
__version__ = 0.1
__date__ = '2015-05-20'
__updated__ = '2015-05-20'


class CLIError(Exception):
    '''Generic exception to raise and log different fatal errors.'''
    def __init__(self, msg):
        super(CLIError).__init__(type(self))
        self.msg = "E: %s" % msg
    def __str__(self):
        return self.msg
    def __unicode__(self):
        return self.msg


import subprocess

def getDevice(mountPoint):
    mounts = {}
    for line in subprocess.check_output(['mount', '-l']).decode("utf-8").split("\n"):
        parts = line.split(' ')
        if len(parts) > 2:
            mounts[parts[2]] = parts[0]
    
    return mounts[mountPoint]
    
    
        
    
def getMount(path):
    path = os.path.realpath(path)
    while path != os.path.sep:
        if os.path.ismount(path):
            return path
        path = os.path.abspath(os.path.join(path, os.pardir))
    return path

def main(argv=None): # IGNORE:C0111
    '''Command line options.'''

    if argv is None:
        argv = sys.argv
    else:
        sys.argv.extend(argv)

    program_name = os.path.basename(sys.argv[0])
    program_version = "v%s" % __version__
    program_build_date = str(__updated__)
    program_version_message = '%%(prog)s %s (%s)' % (program_version, program_build_date)
    program_shortdesc = __import__('__main__').__doc__.split("\n")[1]
    program_license = '''%s

  Created by user_name on %s.
  Copyright 2015 organization_name. All rights reserved.

  Licensed under the Apache License 2.0
  http://www.apache.org/licenses/LICENSE-2.0

  Distributed on an "AS IS" basis without warranties
  or conditions of any kind, either express or implied.

USAGE
''' % (program_shortdesc, str(__date__))

    # Setup argument parser
    parser = ArgumentParser(description=program_license, formatter_class=RawDescriptionHelpFormatter)

    # Process arguments
    args = parser.parse_args()
    
    prevMountPoint = "/home/brian/files.log"
    newMountPoint = ""
    while newMountPoint != "udev":
        curMountPoint=newMountPoint
        mountPoint=getMount(curMountPoint)
        devicePath=getDevice(mountPoint)
        newMountPoint=devicePath
        prevMountPoint=curMountPoint
    
    print(curMountPoint)
    
    while True:
        time.sleep(2)
        cputimes=psutil.cpu_times_percent()
        cpucount=psutil.cpu_count(logical=True)
        loadavgs=os.getloadavg()[0]
        print("IOWait: %s LoadAvgs: %s AvgLoadPercent: %s" % (cputimes.iowait, loadavgs, loadavgs/cpucount))
      
    return 0
    

if __name__ == "__main__":
    sys.exit(main())
