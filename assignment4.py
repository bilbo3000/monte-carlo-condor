#!/usr/bin/python

import subprocess; 
import sys; 
import os; 

if (len(sys.argv) != 2): 
    print "Incorrect number of arguments. "; 
    print "Correct usage: python assignment4.py <number_of_iteration>"; 
    sys.exit(1); 
 
numOfIter = int(sys.argv[1]); 
if (numOfIter < 100):
    print "Number of iterations have to be at least 100. "; 
    sys.exit(1); 

numOfIterPerTask = numOfIter / 100; 

# Create directories
if not os.path.exists("out"):
	os.mkdir("out");
if not os.path.exists("log"): 
	os.mkdir("log");
if not os.path.exists("err"): 
	os.mkdir("err");     

# Create condor submit script
fout = open("djin-submit", 'w');
fout.write("Universe = vanilla\n"); 
fout.write("Executable = djin-submit.sh\n"); 
fout.write("Log = log/example_solution.log\n");
fout.write("Output = out/example_solution_$(Process).out\n");
fout.write("Error = err/example_solution_$(Process).err\n");
fout.write("should_transfer_files = YES\n");  
fout.write("when_to_transfer_output = ON_EXIT\n");
fout.write("transfer_input_files = djin-submit.sh,libassignment4.so,example_solution\n"); 
 
for i in range(0, 100): 
    fout.write("Arguments = " + str(numOfIterPerTask) + '\n');  
    fout.write("Queue\n"); 
    
fout.close();  

# Submit condor job script 
subprocess.call(["condor_submit", 'djin-submit']);
subprocess.call(["condor_wait", "log/example_solution.log"]); 

# Collect data from output file
count = 0; 
outputDir = os.path.join(os.curdir, "out");
for root, dirs, files in os.walk(outputDir): 
	for filename in files: 
		if (filename.endswith(".out")):  
			fin = open(os.path.join(root, filename), 'r');
			line = fin.readline(); 
			while line: 
    				count = count + int(line); 
    				line = fin.readline(); 
    
			fin.close();  

print "Area is: ", count / (numOfIterPerTask * 100.0); 
