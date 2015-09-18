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
#os.system("make BlockFunction_Thesis.test"%locals())
for vertices in range(5,11):
   for edges in [4, 8, 16, 32]:
      os.system("%(top)s/graphbench/data/generator/generator_seq %(vertices)i -e %(edges)i -o %(top)s/Tracking/outputs/kroneckerTexts/KronGraph%(vertices)i_%(edges)i_Thesis.txt" %locals())

      os.system("%(top)s/Green-Marl/apps/output_cpp/bin/graph_gen %(top)s/Green-Marl/apps/output_cpp/data/KronGraph%(vertices)i_%(edges)i_Thesis.bin %(top)s/graphbench/data/generator/KronGraph%(vertices)i_%(edges)i_Thesis.txt 0" %locals())

      os.system("%(usertop)s/pin-2.14-71313-gcc.4.4.7-linux/pin -t %(usertop)s/pin-2.14-71313-gcc.4.4.7-linux/source/tools/ManualExamples/obj-intel64/BlockFunction_Thesis.so -- %(top)s/Green-Marl/apps/output_cpp/bin/sssp %(top)s/Green-Marl/apps/output_cpp/data/KronGraph%(vertices)i_%(edges)i_Thesis.bin 1" %locals())

      os.system("cp %(top)s/Tracking/pyScripts/BlockFunction_Thesis.out %(top)s/Tracking/outputs/kroneckerMetrics/kroneckerMetric%(vertices)i_%(edges)i.out" %locals())

      sortCommand=""" sed '1,7d'  %(top)s/Tracking/outputs/kroneckerMetrics/kroneckerMetric%(vertices)i_%(edges)i.out | sort -s -n -k 4,4  |  awk '{sum = sum + $4}END{print sum}'>%(top)s/Tracking/outputs/kroneckerTotals/kroneckerTotal%(vertices)i_%(edges)i.txt""" %locals()

      os.system(sortCommand)

