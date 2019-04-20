import numpy as np
from scipy.stats import norm 
from scipy.stats import poisson
import matplotlib.pyplot as plt
from collections import defaultdict
import os, sys
import xml.etree.ElementTree as etree
import xml.dom.minidom as doc

doc1 = etree.parse('./TLSAction1.xml')
ActionRoot = doc1.getroot() 
doc3 = etree.parse('./loops_ctrl.xml')
LoopsRoot = doc3.getroot()
# doc4 = etree.parse('D:./Chj_ctrl.net.xml')
# NetRoot = doc4.getroot()
doc5 = etree.parse('./TLSconnections.xml')
MovementPhaseRoot = doc5.getroot()
doc6 = etree.parse('./TLSconnections2.xml')
MovementLaneRoot = doc6.getroot()


PhaseLanes = doc.Document()
Intersections = PhaseLanes.createElement('Intersections')
PhaseLanes.appendChild(Intersections)

for junction in ActionRoot.findall('Intersection'):
	intersection = PhaseLanes.createElement('Intersection')
	intersection.setAttribute('id',junction.get('id'))
	intersection.setAttribute('PhaseNum',junction.get('PhaseNum'))
	junction_looplanes = []
	PhaseNum = int(junction.get('PhaseNum'))
	for i in xrange(PhaseNum):
		phase = PhaseLanes.createElement('Phase')
		phase.setAttribute('No',str(i+1))
		phase.setAttribute('action',junction.get('phase'+str(i+1)))
		for node in MovementPhaseRoot.findall('Intersection'):
			if node.get('id')==junction.get('id'):
				linkIndex = []
				for connection in node.findall('connection'):
					if connection.get('phase')==str(i+1):
						linkIndex.append(connection.get('linkIndex'))
		for node in MovementLaneRoot.findall('Intersection'):
			if node.get('id')==junction.get('id'):
				LaneNumber = []
				for connection in node.findall('connection'):
					if connection.get('linkIndex') in linkIndex:
						laneNo = connection.get('from')+'_'+connection.get('fromLane')
						LaneNumber.append(laneNo)
		junction_looplanes+=LaneNumber
		Lanes = ' '.join(LaneNumber)
		phase.setAttribute('fromLanes',Lanes)
		intersection.appendChild(phase)

	intersection.setAttribute('LoopLanes',' '.join(junction_looplanes))
	Intersections.appendChild(intersection)

fp = open('./PhaseLanesCont.xml','w')
	
try:
	PhaseLanes.writexml(fp,indent='\t', addindent='\t',newl='\n',encoding="utf-8")
except:
	trackback.print_exc() 
finally: 
	fp.close() 