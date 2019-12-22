#!/usr/bin/python
# Filename : backup_version1.py

import os
import time

# 1. The files and directories to be backed up are given in a list.
source = ['/home/g2swaroop/all', '/home/g2swaroop/bin']
# If you are using Windows, use source = [r'C:\Documents', r'D:\Work']

# 2. The backup must be stored in a main backup directory.
target_dir = '/mnt/d/backup/'

# 3. The files are backed up into a zip file.
# 4. The name of the zip archive is today's date and time.
target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'

# 5. We use the zip command (in Unix/Linux) to put the files in a zip
#    archive
zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))

# Run the backup
if os.system(zip_command) == 0:
        print 'Successful backup to', target
else:
        print 'Backup FAILED'



Another way to copy data


import shutil 
Shutil.copy (****if you want you can use move replace of copy)
('/home/chotomahbub/Downloads/MACOSX.zip','/media/chotomahbub/HUNGRYNAKI/')

