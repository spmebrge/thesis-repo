#!/usr/bin/python

import os, time
from threading import Thread

####################################################################
# workloads
# name, sub-directory, command line

debug_workloads = [
     ("isp09_BFS",	"BFS",	"../bin/release/BFS ./data/graph65536.txt"),
]

ispass09_workloads = [
     ("isp09_AES",	"AES",	"../bin/release/AES  e 128 ./data/output.bmp ./data/key128.txt"),
     ("isp09_BFS",	"BFS",	"../bin/release/BFS ./data/graph65536.txt"),
     ("isp09_CP",	"CP",	"../bin/release/CP"),	# not working (mesh)
     ("isp09_LIB",	"LIB",	"../bin/release/LIB"),
     ("isp09_LPS",	"LPS",	'../bin/release/LPS'),
     ("isp09_MUM",	"MUM",	"../bin/release/MUM ./data/NC_003997.20k.fna ./data/NC_003997_q25bp.50k.fna"),
     ("isp09_NN",	"NN",	"../bin/release/NN 28"),
     ("isp09_NQU",	"NQU",	"../bin/release/NQU"),	# not working: stack smashing detected
     ("isp09_RAY",	"RAY",	"../bin/release/RAY 256 256"), # not working: stack smashing detected
     ("isp09_STO",	"STO",	"../bin/release/STO"),
     ("isp09_WP",	"WP",	'echo "10 ./data/" | ../bin/release/WP'),

     # ("isp09_DG",	"DG",	"../bin/release/DG ./data/cubeK268.neu"),	# not working (MPI failure)
]

rodina30_workloads = [
     ("R30_backprop",	"backprop",	"./backprop 65536"),
     ("R30_bfs",	"bfs",		"./bfs ../../data/bfs/graph1MW_6.txt"),
     ("R30_bplustree",	"b+tree",	"./b+tree.out file ../../data/b+tree/mil.txt command ../../data/b+tree/command.txt"),
     ("R30_cfd",	"cfd",		"./euler3d ../../data/cfd/fvcorr.domn.097K"),
     ("R30_dwt2d",	"dwt2d",	"./dwt2d rgb.bmp -d 1024x1024 -f -5 -l 3"),
     ("R30_gaussian",	"gaussian",	"./gaussian -f ../../data/gaussian/matrix208.txt"),
     ("R30_heartwall",	"heartwall",	"./heartwall ../../data/heartwall/test.avi 20"),
     ("R30_hotspot",	"hotspot",	"./hotspot 512 2 2 ../../data/hotspot/temp_512 ../../data/hotspot/power_512 output.out"),
     ("R30_hybridsort",	"hybridsort",	"./hybridsort r"),
     ("R30_kmeans",	"kmeans",	"./kmeans -o -i kdd_cup "),
     ("R30_lavaMD",	"lavaMD",	"./lavaMD -boxes1d 10"),
     ("R30_leukocyte",	"leukocyte",	"./CUDA/leukocyte  ../../data/leukocyte/testfile.avi 5"),
     ("R30_lud",	"lud",		"./cuda/lud_cuda -s 512 -v"),
     # ("R30_mummergpu",	"mummergpu",	"./bin/mummergpu ../../data/mummergpu/NC_003997.fna ../../data/mummergpu/NC_003997_q100bp.fna > NC_00399.out"), # Cuda driver error 3 in file 'mummergpu.cu' in line 468.
     ("R30_myocyte",	"myocyte",	"./myocyte.out 100 1 0"),
     ("R30_nw",	"nw",		"./needle 2048 10"),
     ("R30_particlefilter",	"particlefilter",	"./particlefilter_float -x 128 -y 128 -z 10 -np 1000"),
     ("R30_pathfinder",	"pathfinder",	"./pathfinder 100000 100 20"),
     ("R30_srad_v1",	"srad_v1",	"./srad 100 0.5 502 458"),
     ("R30_srad_v2",	"srad_v2",	"./srad 2048 2048 0 127 0 127 0.5 2"),
     ("R30_streamcluster",	"streamcluster",	"./sc_gpu 10 20 256 65536 65536 1000 none output.txt 1"),

     #("R30_nn",	"nn",		"./nn filelist_4 -r 5 -lat 30 -lng 90"),	# not working
]

####################################################################


####################################################################
# environment parameters
ispass09_workloads_path = '/home/kaya1/yjin/gpgpu/gpgpu-sim/ispass2009-benchmarks'
rodina30_workloads_path = '/home/kaya1/yjin/gpgpu/gpgpu-sim/rodinia_3.0/cuda'

#sim_output_dir = '/home/kaya1/yjin/gpgpu/yuho_results/fly_test'
#sim_output_dir = '/home/kaya1/yjin/gpgpu/yuho_results/kh_test'
sim_output_dir = '/home/kaya1/yjin/gpgpu/yuho_results/kh_mesh_dor_vcs2'
#sim_output_dir = '/home/kaya1/yjin/gpgpu/yuho_results/mesh_dor_vcs2'
#sim_output_dir = '/home/kaya1/yjin/gpgpu/yuho_results/mesh_dor_vcs4'
#sim_output_dir = '/home/kaya1/yjin/gpgpu/yuho_results/mesh_dor_vcs8'
#sim_output_dir = '/home/kaya1/yjin/gpgpu/yuho_results/mesh_romm_vcs2'
#sim_output_dir = '/home/kaya1/yjin/gpgpu/yuho_results/mesh_vcs2_romm_ni'
#sim_output_dir = '/home/kaya1/yjin/gpgpu/yuho_results/mesh_xy_yx_vcs2'
#sim_output_dir = '/home/kaya1/yjin/gpgpu/yuho_results/mesh_min_adapt_vcs2'
#sim_output_dir = '/home/kaya1/yjin/gpgpu/yuho_results/mesh_vcs2_adaptive_xy_yx'

run_debug = True
#run_debug = False

run_ispass09 = True
run_rodina30 = False

if run_debug:
    run_ispass09 = False
    run_rodina30 = False
    sim_output_dir = '/home/kaya1/yjin/gpgpu/yuho_results/debug'
####################################################################


####################################################################
class worker(Thread):
    def __init__ (self, workload_name, workload_path, command_str):
        Thread.__init__(self)
        self.workload_name = workload_name
        self.workload_path = workload_path
        self.command_str = command_str

    def run(self):
        os.chdir(self.workload_path)

        start_time = time.time()
        print self.workload_name + " started."

        #print self.command_str
        os.system(self.command_str)

        end_time = time.time()
        elapsed_time = end_time - start_time	# seconds
        print self.workload_name + " done: " + str(elapsed_time/(60*60)) + " hours"

####################################################################


runlist = []

####################################################################

if run_debug:
    for workload in debug_workloads:
        workload_path = ispass09_workloads_path + '/' + workload[1]

        output_filename = sim_output_dir + '/' + workload[0] + '.txt'

        command_str = workload[2]
        command_str += ' > ' + output_filename

        current = worker(workload_name=workload[0], workload_path=workload_path, command_str=command_str)

        runlist.append(current)
        current.start()

        time.sleep(1)   # sleep for 

if run_ispass09:
    for workload in ispass09_workloads:
        workload_path = ispass09_workloads_path + '/' + workload[1]

        output_filename = sim_output_dir + '/' + workload[0] + '.txt'

        command_str = workload[2]
        command_str += ' >& ' + output_filename

        current = worker(workload_name=workload[0], workload_path=workload_path, command_str=command_str)

        runlist.append(current)
        current.start()

        time.sleep(1)   # sleep for 

if run_rodina30:
    for workload in rodina30_workloads:
        workload_path = rodina30_workloads_path + '/' + workload[1]

        output_filename = sim_output_dir + '/' + workload[0] + '.txt'

        command_str = workload[2]
        command_str += ' >& ' + output_filename

        current = worker(workload_name=workload[0], workload_path=workload_path, command_str=command_str)

        runlist.append(current)
        current.start()
        time.sleep(1)   # sleep for 

for worker in runlist:
    worker.join()
