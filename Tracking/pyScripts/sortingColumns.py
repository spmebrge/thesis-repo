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


#Note: 1) cut
# 2) sort
# 3) add
# 4) print to file
sortCommand="""sort -s -n -k 4,4 %(top)s/Tracking/outputs/kroneckerMetrics/kroneckerMetric5,16.out | sed '1,4d' |  awk '{print $1,"\t" ,$4}'"""


#sortCommand="""sort -s -n -k 4,4 %(top)s/Tracking/outputs/kroneckerMetrics/kroneckerMetric5,16.out | sed '1,4d' |  awk '{ sum = sum + $4 }END{print sum}' """

addingTotalCallsCmd="""sed '1,7d' kroneckerMetric5,16.out | awk '{sum = sum + $4}END{print sum}' """

os.system(sortCommand %locals())


