import os, sys
import xml.etree.ElementTree as etree
import xml.dom.minidom as doc
import math
import numpy as np
import pdb

demand_level = [2,3,4,5,6,7,8]

# control_file = 'Actuated_ctrl.py'
# control_file = 'Fix_ctrl.py'
control_file = 'Hierarchical_ctrl.py'
control_name = 'Hierarchical_ctrl'



def alter(file,i):
	file_data = ""
	lineno = 0
	with open(file,'r') as f:
		for line in f:
			if lineno==0:
				line = 'demand_level = '+str(i)+'\n'
				file_data += line
				lineno+=1
			else:
				file_data += line
 

	f2 = open('./'+control_name+str(i)+'.py',"w")
	f2.write(file_data)
	
	# with open(file,"w") as f:
	# 	f.write(file_data)

	return f2
 


file = './'+control_file
for i in demand_level:
	f2 = alter(file,i)	
	#execfile(f2)#+Bargaining






	

