#!/usr/bin/env python
# encoding: utf-8

import csv
# import commands
import subprocess


with open('/nfs/t3/workingshop/jiangjian/coordinate_LXQ/data/peakcoordIGK.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    i = 0

    for row in reader:
        # print row
        pre = str(row)
        # print type(pre)
        pre = pre.replace("[", "")
        pre = pre.replace("]", "")+"\n"
        pre = pre.replace(".  ", ",")
        pre = pre.replace(".", "")
        pre = pre.replace("n  ", "n,")
        pre = pre.replace(" ", "")
        pre = pre.replace("','", "\n")
        pre = pre.replace("'", "")
        # pre = pre.replace(" ", "\n")
        # print pre
        file = open('data%d.txt' %(i), 'w')
        file.write(pre)
        i = i + 1
        file.close()

        if row[0] == 'r_OFA':
            continue
        subprocess.call(["coord2roi -fcoord data%d.txt -resolution 2mm -size 4 -shape sphere -basename result%d.nii.gz" % (i-1, i-1)], shell=True)
        # commands.getoutput("coord2roi -fcoord 'data%d.txt' %(i) -resolution 2mm -size 4 -shape sphere -basename 'data%d.nii.gz' %(i)")

