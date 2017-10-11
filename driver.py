#!/bin/python

REPEAT_MEASURE_NB=1

def benchmark_bin(filename,is_reference):
    for i in range(0,REPEAT_MEASURE_NB):
        ps=subprocess.Popen([filename], shell=True ,stdout=subprocess.PIPE)

