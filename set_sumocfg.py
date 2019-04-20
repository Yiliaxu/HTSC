import os,sys
import xml.etree.ElementTree as etree
import xml.dom.minidom as doc
import random

 
demand_level = 8
MethodName = 'FTC'

###loops
loop_name = 'loops.xml'
# loop_name = 'loops_actuated.xml'

 

cfg_net = etree.parse('./chj.sumocfg')
CfgRoot = cfg_net.getroot()

Sumocfg_files = doc.Document()
Sumocfg = Sumocfg_files.createElement('configuration')
Sumocfg_files.appendChild(Sumocfg)

inputs = Sumocfg_files.createElement('input')
netfile = Sumocfg_files.createElement('net-file')
netfile.setAttribute('value','Chj_final.net.xml')
inputs.appendChild(netfile)
routefile = Sumocfg_files.createElement('route-files')
routefile.setAttribute('value','Chj_Demand'+str(demand_level)+'.rou.xml')
inputs.appendChild(routefile)
additionalfile = Sumocfg_files.createElement('additional-files')
additionalfile.setAttribute('value',loop_name)
inputs.appendChild(additionalfile)
Sumocfg.appendChild(inputs)


time = Sumocfg_files.createElement('time')
begin = Sumocfg_files.createElement('begin')
begin.setAttribute('value','0')
time.appendChild(begin)
end = Sumocfg_files.createElement('end')
end.setAttribute('value','3600')
time.appendChild(end)
Sumocfg.appendChild(time)

outputs = Sumocfg_files.createElement('output')
queueout = Sumocfg_files.createElement('queue-output')
queueout.setAttribute('value',MethodName+'queue'+str(demand_level)+'.xml')
outputs.appendChild(queueout)
summary = Sumocfg_files.createElement('summary')
summary.setAttribute('value',MethodName+'summary'+str(demand_level)+'.xml')
outputs.appendChild(summary)
trip = Sumocfg_files.createElement('tripinfo-output')
trip.setAttribute('value',MethodName+'trip'+str(demand_level)+'.xml')
outputs.appendChild(trip)
Sumocfg.appendChild(outputs)

outputs = Sumocfg_files.createElement('report')
queueout = Sumocfg_files.createElement('xml-validation')
queueout.setAttribute('value','never')
outputs.appendChild(queueout)
summary = Sumocfg_files.createElement('duration-log.disable')
summary.setAttribute('value','true')
outputs.appendChild(summary)
trip = Sumocfg_files.createElement('no-step-log')
trip.setAttribute('value','true')
outputs.appendChild(trip)
Sumocfg.appendChild(outputs)
 



# fp = open('./Chj_Dynamic.rou.xml','w')
fp = open('./'+MethodName+str(demand_level)+'.sumocfg','w')
	
try:
	Sumocfg_files.writexml(fp,indent='\t', addindent='\t',newl='\n',encoding="utf-8")
except:
	trackback.print_exc() 
finally: 
	fp.close() 