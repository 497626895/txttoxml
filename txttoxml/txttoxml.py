
from xml.dom.minidom import Document

import numpy as np
import os

def writeEle(doc,annotation,nrow,data):
	if nrow==1:
		object=doc.createElement('object')
		annotation.appendChild(object)
		
		name=doc.createElement('name')
		name_txt=doc.createTextNode(str(int(data[0])))
		name.appendChild(name_txt)
		object.appendChild(name)
		
		difficult=doc.createElement('difficult')
		difficult_txt=doc.createTextNode('0')
		difficult.appendChild(difficult_txt)
		object.appendChild(difficult)
		
		pose=doc.createElement('pose')
		pose_txt=doc.createTextNode('Frontal')
		pose.appendChild(pose_txt)
		object.appendChild(pose)
		
		truncated=doc.createElement('truncated')
		truncated_txt=doc.createTextNode('0')
		truncated.appendChild(truncated_txt)
		object.appendChild(truncated)
		
		bndbox=doc.createElement('bndbox')
		object.appendChild(bndbox)
		
		xmin=doc.createElement('xmin')
		xmin_txt=doc.createTextNode(str(int(data[1])))
		xmin.appendChild(xmin_txt)
		bndbox.appendChild(xmin)
		
		ymin=doc.createElement('ymin')
		ymin_txt=doc.createTextNode(str(int(data[2])))
		ymin.appendChild(ymin_txt)
		bndbox.appendChild(ymin)
		
		xmax=doc.createElement('xmax')
		xmax_txt=doc.createTextNode(str(int(data[3])))
		xmax.appendChild(xmax_txt)
		bndbox.appendChild(xmax)
		
		ymax=doc.createElement('ymax')
		ymax_txt=doc.createTextNode(str(int(data[4])))
		ymax.appendChild(ymax_txt)
		bndbox.appendChild(ymax)
		
		return
		
		
	for i in range(nrow):
		object=doc.createElement('object')
		annotation.appendChild(object)
		
		name=doc.createElement('name')
		name_txt=doc.createTextNode(str(int(data[i][0])))
		name.appendChild(name_txt)
		object.appendChild(name)
		
		difficult=doc.createElement('difficult')
		difficult_txt=doc.createTextNode('0')
		difficult.appendChild(difficult_txt)
		object.appendChild(difficult)
		
		pose=doc.createElement('pose')
		pose_txt=doc.createTextNode('Frontal')
		pose.appendChild(pose_txt)
		object.appendChild(pose)
		
		truncated=doc.createElement('truncated')
		truncated_txt=doc.createTextNode('0')
		truncated.appendChild(truncated_txt)
		object.appendChild(truncated)
		
		bndbox=doc.createElement('bndbox')
		object.appendChild(bndbox)
		
		xmin=doc.createElement('xmin')
		xmin_txt=doc.createTextNode(str(int(data[i][1])))
		xmin.appendChild(xmin_txt)
		bndbox.appendChild(xmin)
		
		ymin=doc.createElement('ymin')
		ymin_txt=doc.createTextNode(str(int(data[i][2])))
		ymin.appendChild(ymin_txt)
		bndbox.appendChild(ymin)
		
		xmax=doc.createElement('xmax')
		xmax_txt=doc.createTextNode(str(int(data[i][3])))
		xmax.appendChild(xmax_txt)
		bndbox.appendChild(xmax)
		
		ymax=doc.createElement('ymax')
		ymax_txt=doc.createTextNode(str(int(data[i][4])))
		ymax.appendChild(ymax_txt)
		bndbox.appendChild(ymax)

path='D:\\Zsb\\test\\centre_txt'



filenames=os.listdir(path)
for file in filenames:
	
	doc=Document()

	annotation=doc.createElement('annotation')
	doc.appendChild(annotation)

	folder=doc.createElement('folder')
	folder_text=doc.createTextNode('VOC')
	folder.appendChild(folder_text)
	annotation.appendChild(folder)

	filename=doc.createElement('filename')
	filename_text=doc.createTextNode(file[0:-4])
	filename.appendChild(filename_text)
	annotation.appendChild(filename)
	
	
	data=np.loadtxt(os.path.join(path,file))
	rows=np.size(data,0)
	#cols=np.size(data,1)
	#data2=data.copy()
	if np.ndim(data)==1:#rows=1
		
		object_num=doc.createElement('object_num')
		object_num_txt=doc.createTextNode('1')
		object_num.appendChild(object_num_txt)
		annotation.appendChild(object_num)
		
		size=doc.createElement('size')
		annotation.appendChild(size)
		
		width=doc.createElement('width')
		width_txt=doc.createTextNode('500')
		width.appendChild(width_txt)
		size.appendChild(width)
		
		height=doc.createElement('height')
		height_txt=doc.createTextNode('350')
		height.appendChild(height_txt)
		size.appendChild(height)
		
		depth=doc.createElement('depth')
		depth_txt=doc.createTextNode('3')
		depth.appendChild(depth_txt)
		size.appendChild(depth)
		
		writeEle(doc,annotation,1,data)
		
		f=open('D:\\Zsb\\test\\annotations\\'+file[0:-4]+'.xml','w')
		doc.writexml(f,indent='\t',newl='\n',addindent='\t',encoding='utf-8')
		f.close()
		print(1)
		continue
	#for i in range(rows):#rows>1
		#print(rows)
		#print(cols)
	object_num=doc.createElement('object_num')
	object_num_txt=doc.createTextNode(str(rows))
	object_num.appendChild(object_num_txt)
	annotation.appendChild(object_num)
		
	size=doc.createElement('size')
	annotation.appendChild(size)
		
	width=doc.createElement('width')
	width_txt=doc.createTextNode('500')
	width.appendChild(width_txt)
	size.appendChild(width)
		
	height=doc.createElement('height')
	height_txt=doc.createTextNode('350')
	height.appendChild(height_txt)
	size.appendChild(height)
		
	depth=doc.createElement('depth')
	depth_txt=doc.createTextNode('3')
	depth.appendChild(depth_txt)
	size.appendChild(depth)
		
	writeEle(doc,annotation,rows,data)
		
	f=open('D:\\Zsb\\test\\annotations\\'+file[0:-4]+'.xml','w')
	doc.writexml(f,indent='\t',newl='\n',addindent='\t',encoding='utf-8')
	f.close()
	#doc.empty()
	print(rows)
	

	
	
	

	
	
	
	
	
	
