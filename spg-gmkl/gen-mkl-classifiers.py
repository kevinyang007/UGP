import subprocess
CONST_s = "_all"

kernelfile = 'mainkernel'
for i in range(1,103):
	print "Training for ",i
	base = "model"+CONST_s"/"+str(i)+"/"
	bashCommand = "./svm-train -a 16 -k "+kernelfile+" -b 1 -f 2 " + base + "mkl_train "+base+"model"
	print "		", bashCommand
	process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
	output = process.communicate()[0]

	print "Testing for ",i
	bashCommand = "./svm-predict -b 1 " + base + "mkl_test "+base+"model "+base+"prediction"
	print "		", bashCommand
	process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
	output = process.communicate()[0]
	print output
