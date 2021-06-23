#!/usr/bin/env python3
# encoding: utf-8
# Developer: Lenin Tarrillo (lenin.tarrillo.v@gmail.com)
# recorrer loop through the files on the ftp server and write a csv file with the names and addresses of the large files (filterSize)

import sys
import os
import ftplib
import ftputil
import fnmatch
import time
import csv

filterSize=3


print("******logging into FTP")
host = ftputil.FTPHost("server","user","pass",session_factory=ftplib.FTP)  
ini_root="/files"
pathFileUp=ini_root
print("******logging OK")


csv_files=open('filesMegas.csv', mode='w')
scv_writer = csv.writer(csv_files, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)


def printFile(_path,_name):
    size = host.path.getsize(_path) / 1000000
    if(size>=filterSize):
        scv_writer.writerow([size, _path, _name])
        print("Size MB:{}  - File Name:{}".format(size,_name))

def listFiles(_path):
     listFilesDir=host.listdir(_path)
     for name in listFilesDir:
         pathFileUp=host.path.join(_path, name)
         if(host.path.isfile(pathFileUp)):
             printFile(pathFileUp,name)
         else:
             listFiles(pathFileUp)



listFiles(ini_root)


host.close  
print("****End process and close  FTP connection ")