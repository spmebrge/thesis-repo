#!/usr/bin/python
#Adrian Avila
#Esperanza Medina
#copyright 2015

import os
#This script will generate the Kronecker.txt graphs with 2^[5-10] vertices for the edges [4, 8, 16, 32]
#The .bin files will be created for each .txt previously generated
#The pin tool will use the .so algorithm to count the number of metrics on the sssp benchmark with the given .bins

usertop="/home/kaya3/aavila"
top="%(usertop)s/thesis-repo" %locals()

#os.system("cd /home/kaya1/aavila/pin-2.14-71313-gcc.4.4.7-linux/source/tools/ManualExamples"%locals())
#os.system("make pinatrace_thesis.test"%locals())
for threads in [1]:
  for vertices in range(5,8):
     for edges in [4, 8, 16, 32]:
  
        #run pin using pinatrace (Mem R/W) on sssp program
        os.system("time (%(top)s/pin-2.14-71313-gcc.4.4.7-linux/pin -t %(top)s/pin-2.14-71313-gcc.4.4.7-linux/source/tools/ManualExamples/obj-intel64/pinatrace_thesis.so -- %(top)s/Green-Marl/apps/output_cpp/bin/sssp %(top)s/Green-Marl/apps/output_cpp/data/KronGraph%(vertices)i_%(edges)i_%(threads)i_Thesis.bin %(threads)i) &> %(top)s/Tracking/outputs/MetricParsed/ssspOutput%(vertices)i_%(edges)i_%(threads)i.txt" %locals())
  
        #run pin using new MyPinTool (Mem R/W) on sssp program
        os.system("time (%(top)s/pin-2.14-71313-gcc.4.4.7-linux/pin -t %(top)s/pin-2.14-71313-gcc.4.4.7-linux/source/tools/MyPinTool/obj-intel64/MyPinTool_Thesis.so -o %(top)s/Tracking/outputs/kroneckerMetrics/kroneckerMetric%(vertices)i_%(edges)i_%(threads)i.txt -- %(top)s/Green-Marl/apps/output_cpp/bin/sssp %(top)s/Green-Marl/apps/output_cpp/data/KronGraph%(vertices)i_%(edges)i_%(threads)i_Thesis.bin %(threads)i) &>> %(top)s/Tracking/outputs/MetricParsed/ssspOutput%(vertices)i_%(edges)i_%(threads)i.txt" %locals())
  
        #copy default .out info into a metric .txt file
        os.system("cat %(top)s/Tracking/pyScripts/pinatrace_thesis.out >> %(top)s/Tracking/outputs/kroneckerMetrics/kroneckerMetric%(vertices)i_%(edges)i_%(threads)i.txt" %locals())
