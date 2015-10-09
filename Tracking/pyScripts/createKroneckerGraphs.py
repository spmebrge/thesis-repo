#!/usr/bin/python
#Adrian Avila
#Esperanza Medina
#copyright 2015

import os
#This script will generate the Kronecker.txt graphs with 2^[5-10] vertices for the edges [4, 8, 16, 32]
#The .bin files will be created for each .txt previously generated

usertop="/home/kaya3/aavila"
top="%(usertop)s/thesis-repo" %locals()

#os.system("cd /home/kaya1/aavila/pin-2.14-71313-gcc.4.4.7-linux/source/tools/ManualExamples"%locals())
#os.system("make pinatrace_thesis.test"%locals())
for threads in [1]:
  for vertices in range(5,11):
     for edges in [4, 8, 16, 32]:
        #generate graph into .txt
        os.system("%(top)s/graphbench/data/generator/generator_seq %(vertices)i -e %(edges)i -o %(top)s/Tracking/outputs/kroneckerGraphs/KronGraph%(vertices)i_%(edges)i_%(threads)i_Thesis.txt" %locals())
  
        #convert .txt graph to .bin
        os.system("%(top)s/Green-Marl/apps/output_cpp/bin/graph_gen %(top)s/Green-Marl/apps/output_cpp/data/KronGraph%(vertices)i_%(edges)i_%(threads)i_Thesis.bin %(top)s/Tracking/outputs/kroneckerGraphs/KronGraph%(vertices)i_%(edges)i_%(threads)i_Thesis.txt 0" %locals())

