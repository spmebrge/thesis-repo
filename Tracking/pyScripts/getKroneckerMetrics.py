#!/usr/bin/python
#Adrian Avila
#Esperanza Medina
#copyright 2015

import os
#This script will generate the Kronecker.txt graphs with 2^[5-10] vertices for the edges [4, 8, 16, 32]
#The .bin files will be created for each .txt previously generated
#The pin tool will use the .so algorithm to count the number of metrics on the sssp benchmark with the given .bins

usertop="/home/kaya1/aavila"
top="%(usertop)s/thesis-repo" %locals()

#os.system("cd /home/kaya1/aavila/pin-2.14-71313-gcc.4.4.7-linux/source/tools/ManualExamples"%locals())
#os.system("make pinatrace_thesis.test"%locals())
for vertices in range(5,11):
   for edges in [4, 8, 16, 32]:
     os.system("echo '%(vertices)i_%(edges)i'"%locals())
     #output info of specific metric (excluding lines 1-9)
     os.system("sed '1,9d' /home/kaya1/aavila/thesis-repo/Tracking/outputs/kroneckerMetrics/kroneckerMetric%(vertices)i_%(edges)i.txt " %locals())
    
