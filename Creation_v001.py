############################################################################
# CREATION TOOL
# Version: 1.00
# Author: Aashi Shukla
#---------------------------------------------------------------------------
# This tool was basically built by  me to counter the need for creating just
# controls based on input. The controls will be created at origin by default
# if nothing  is selected . Rest, they will be created at whatever object is
# selected. It is very direct and user friendly. Untick all the options  you
# don't need beforehand.The Color button works for built-in controls as well  
# as for separate rigs.
#---------------------------------------------------------------------------
# To run this  script, just paste  the following  bit of code in your Maya's
# Script Directory: C:\Users\(Your Name)\Documents\maya\2023\scripts
#
# import Creation_v001
# import imp
# imp.reload(Creation_v001)
# Creation_v001.GUI()
#
# and run!
#---------------------------------------------------------------------------
# (Maya 2023 and all previous versions supported)
# Report any bugs at: riggergirl247@gmail.com 
# For more such tools find me on LinkedIn: 
# https://www.linkedin.com/in/aashi-shukla-04591b217/ 
# Follow my GitHub Repository: https://github.com/Riggergirl247 
# I hope that this tool proves to be useful asset in your rigging mania! 
#---------------------------------------------------------------------------
############################################################################





import maya.cmds as cmds

def GUI():
	# Kill the already existing window
	if cmds.window('Shape_create_UI', exists=True):
		cmds.deleteUI('Shape_create_UI')
		
	# Create a new Window
	Win = cmds.window('Shape_create_UI', t='Creation', wh=(300,400), sizeable= True, mnb=1, mxb=0)
	
	# Parent Layout
	Main_clm = cmds.columnLayout(adj=True)
	cmds.text(l='Shape Creation Tool by @Aashi Shukla')
	cmds.separator(st='in', h=10)
	
	#color slider
	cmds.rowColumnLayout( nr=1, p = Main_clm)
	cmds.separator( w= 5,st='none' )
	cmds.button(l='Color', w=70, c=lambda x:color_all(Color))
	cmds.separator( w= 8 ,st='none' )
	cmds.button( l="", bgc = (0.631, 0.631, .631), w=7 )
	cmds.button( l="", bgc = (0.467, 0.6467, .631), w=7 )
	cmds.button( l="", bgc = (0, 0, 0), w=7 )
	cmds.button( l="", bgc = (0.247, 0.247, .247), w=7 )
	cmds.button( l="", bgc = (0.498, 0.498, .498), w=7 )
	cmds.button( l="", bgc = (0.608, 0.0, .157), w=7 )
	cmds.button( l="", bgc = (0 ,0.016 ,0.373), w=7 )
	cmds.button( l="", bgc = (0 ,0 ,1), w=7 )
	cmds.button( l="", bgc = (0 ,0.275 ,0.094), w=7 )
	cmds.button( l="", bgc = (0.145, 0, 0.263), w=7 )
	cmds.button( l="", bgc = (0.78, 0, 0.78), w=7 )
	cmds.button( l="", bgc = (0.537, 0.278, 0.2), w=7 )
	cmds.button( l="", bgc = (0.243, 0.133, 0.122), w=7 )
	cmds.button( l="", bgc = (0.6, 0.145, 0), w=7 )
	cmds.button( l="", bgc = (1, 0, 0), w=7 )
	cmds.button( l="", bgc = (0, 1, 0), w=7 )
	cmds.button( l="", bgc = (0, 0.255, 0.6), w=7 )
	cmds.button( l="", bgc = (1, 1, 1), w=7 )
	cmds.button( l="", bgc = (1, 1, 0), w=7 )
	cmds.button( l="", bgc = (0.388 , 0.863, 1), w=7 )
	cmds.button( l="", bgc = (0.263, 1, 0.635), w=7 )
	cmds.button( l="", bgc = (1, 0.686, 0.686), w=7 )
	cmds.button( l="", bgc = (0.89, 0.675, 0.475), w=7 )
	cmds.button( l="", bgc = (1, 1, 0.384), w=7 )
	cmds.button( l="", bgc = (0.0, 0.6, 0.325), w=7 )
	cmds.button( l="", bgc = (0.627, 0.412, 0.188), w=7 )
	cmds.button( l="", bgc = (0.62, 0.627, 0.188 ), w=7 )
	cmds.button( l="", bgc = (0.408, 0.627, 0.188 ), w=7 )
	cmds.button( l="", bgc = (0.188, 0.627, 0.365  ), w=7 )
	cmds.button( l="", bgc = (0.188, 0.627, 0.627 ), w=7 )
	cmds.button( l="", bgc = (0.188, 0.404, 0.627), w=7 )
	cmds.button( l="", bgc = (0.435, 0.188, 0.627), w=7 )
	cmds.button( l="", bgc = (0.631, 0.188, 0.412), w=7 )
	Color = cmds.colorIndexSliderGrp(p=Main_clm, max=32, min=0, v=18)
	
	# ask for Parent Cons, Scale Cons and FK Chain
	cmds.rowColumnLayout(nc=3, p = Main_clm, co= ([1,"both",5], [2,"both",5],[3,"both",5]) )
	PC = cmds.checkBox(l= 'Parent Constraint', v=1, onc = pc_on, ofc= pc_off )
	SC = cmds.checkBox(l= 'Scale Constraint', v=1, onc = sc_on, ofc= sc_off)
	FK = cmds.checkBox(l = 'FK Chain', v=1, onc = fk_on, ofc= fk_off)


	cmds.rowColumnLayout( nc=3, co= ([1,"both",3],[2,"both",3],[3,"both",3]), p = Main_clm )
	cmds.button(w=100, l='Cube', bgc= (0.2, 0.2, 0.2), c= lambda x:Create_Cube(Color))
	cmds.button(w=100, l='Circle', bgc= (0.2, 0.2, 0.2), c= lambda x:Create_Circle(Color))
	cmds.button(w=100, l='Square', bgc= (0.2, 0.2, 0.2),c= lambda x:Create_Square(Color))
	
	cmds.separator(h=3, st='none')
	cmds.separator(h=3, st='none')
	cmds.separator(h=3, st='none')
	
	cmds.button(w=100, l='Triangle', bgc= (0.2, 0.2, 0.2),c= lambda x:Create_Triangle(Color))
	cmds.button(w=100, l='Diamond', bgc= (0.2, 0.2, 0.2),c= lambda x:Create_Diamond(Color))
	cmds.button(w=100, l='Pyramid', bgc= (0.2, 0.2, 0.2),c= lambda x:Create_Pyramid(Color))
	
	cmds.separator(h=3, st='none')
	cmds.separator(h=3, st='none')
	cmds.separator(h=3, st='none')
	
	cmds.button(w=100, l='Plus', bgc= (0.2, 0.2, 0.2),c= lambda x:Create_Plus(Color))
	cmds.button(w=100, l='Cross', bgc= (0.2, 0.2, 0.2),c= lambda x:Create_Cross(Color))
	cmds.button(w=100, l='Arrow', bgc= (0.2, 0.2, 0.2),c= lambda x:Create_Arrow(Color))
	
	cmds.separator(h=3, st='none')
	cmds.separator(h=3, st='none')
	cmds.separator(h=3, st='none')
	
	cmds.button(w=100, l='Aim', bgc= (0.2, 0.2, 0.2), c= lambda x:Create_Aim(Color))
	cmds.button(w=100, l='COG', bgc= (0.2, 0.2, 0.2),c= lambda x:Create_COG(Color))
	cmds.button(w=100, l='Pin', bgc= (0.2, 0.2, 0.2),c= lambda x:Create_Pin(Color))
	
	cmds.separator(h=3, st='none')
	cmds.separator(h=3, st='none')
	cmds.separator(h=3, st='none')
	
	cmds.button(w=100, l='Rotate Arrow', bgc= (0.2, 0.2, 0.2),c= lambda x:Create_Rotate_Arrow(Color))
	cmds.button(w=100, l='Flower',  bgc= (0.2, 0.2, 0.2),c= lambda x:Create_Flower(Color))
	cmds.button(w=100, l='Locator', bgc= (0.2, 0.2, 0.2),c= lambda x:Create_Locator(Color))
	
	cmds.separator(h=3, st='none')
	cmds.separator(h=3, st='none')
	cmds.separator(h=3, st='none')
	
	cmds.button(w=100, l='Double Arrow',bgc= (0.2, 0.2, 0.2), c= lambda x:Create_Double_Arrow(Color))
	cmds.button(w=100, l='Four Arrow', bgc= (0.2, 0.2, 0.2), c= lambda x:Create_Four_Arrow(Color))
	cmds.button(w=100, l='Arrow on Ball', bgc= (0.2, 0.2, 0.2),c= lambda x:Create_Arrow_on_Ball(Color))
	
	cmds.showWindow(Win)
	
if __name__ == '__main__':
	GUI()




"""

          Functions used in GUI start from here 
          
          
                                                                 """
#________________________________________________________________________________
global pc, sc, fk
pc=1
sc=1
fk=1

def pc_on(*args):
	global pc
	pc=1

def pc_off(*args):
	global pc
	pc=0
	
def sc_on(*args):
	global sc
	sc=1

def sc_off(*args):
	global sc
	sc=0

def fk_on(*args):
	global fk
	fk=1

def fk_off(*args):
	global fk
	fk=0

def color_all(Color):
	col = cmds.colorIndexSliderGrp(Color, query=True, value=True)
	list = cmds.ls(sl=True)
	
	for obj in list:
		shape_node= cmds.listRelatives(obj, shapes=True)[0]
		cmds.setAttr(shape_node + '.overrideEnabled', 1)
		cmds.setAttr(shape_node + '.overrideColor', col-1)



def color_it(col):
	obj = cmds.ls(sl=True)[0]
	cmds.setAttr(obj + '.overrideEnabled', 1)
	cmds.setAttr(obj + '.overrideColor', col-1)


n=1

def Create_Pin(Color):
	global pc, sc, fk
	All_Ctrl_list = []
	list = cmds.ls(sl=True)
	mgs = len(list)
	col = cmds.colorIndexSliderGrp(Color, query=True, value=True)
	if mgs<1:
		# make controller
		v = cmds.circle( d=3, radius=n)
		obj = cmds.ls(sl=True)[0]
		cmds.select(obj +'.cv[3:7]' )
		cmds.scale(0.02, 1, 1, r=True, ocp=True, xc= 'edge')
		cmds.select(obj + '.cv[0:2]')
		cmds.scale(0.414, 1, 1)
		# Clear Selection and Make Identity
		cmds.delete(obj , constructionHistory=True)
		cmds.makeIdentity(obj, apply=True, t=1, s=1, r=1)
		cmds.select(obj)
		color_it(col)
		# make offset groups
		cmds.group(obj, n= obj + '_Grp')
		cmds.group(obj + '_Grp', n = obj + '_Grp_OFF')
		print('Controller made at origin')
	
	else:
		for jnt in list:
			item01 = cmds.circle(n= jnt + '_C', d=3, radius=n)[0]
			obj = cmds.ls(sl=True)[0]
			cmds.select(obj +'.cv[3:7]' )
			cmds.scale(0.02, 1, 1, r=True, ocp=True, xc= 'edge')
			cmds.select(obj + '.cv[0:2]')
			cmds.scale(0.414, 1, 1)
			# Clear Selection and Make Identity
			cmds.delete(obj , constructionHistory=True)
			cmds.makeIdentity(obj, apply=True, t=1, s=1, r=1)
			cmds.select(obj)
			color_it(col)
			# Make Offset Groups
			item02 = cmds.group(obj, n = jnt + '_C_Grp')
			item03 = cmds.group(jnt + '_C_Grp', n = jnt + '_C_Grp_OFF')
			
			All_Ctrl_list.append(item03)
			All_Ctrl_list.append(item02)
			All_Ctrl_list.append(item01)
			# Position the controller at joint
			cmds.delete(cmds.parentConstraint(jnt, jnt + '_C_Grp_OFF' ,mo=False) )
			if pc==1:
				cmds.parentConstraint(obj, jnt, mo=True)
			if sc==1:
				cmds.scaleConstraint(obj, jnt, mo=True)
		i=3
		#Make FK Chain
		if fk==1:
			print(All_Ctrl_list)
			for item in enumerate(All_Ctrl_list):
				if i!= len(All_Ctrl_list):
					cmds.parent(All_Ctrl_list[i],All_Ctrl_list[i-1])
					i+=3
			cmds.select(All_Ctrl_list[-1])
					
# _____________________________________________________________________________	
def Create_Diamond(Color):
	global pc, sc, fk
	All_Ctrl_list = []
	list = cmds.ls(sl=True)
	mgs = len(list)
	col = cmds.colorIndexSliderGrp(Color, query=True, value=True)
	if mgs<1:
		v = cmds.curve( d=1, p =[(1.25*n,0, 0), (0, 0, -1.25*n), (-1.25*n, 0, 0), (0, 0, 1.25*n), (1.25*n, 0, 0), (0, 1.25*n, 0),  (-1.25*n, 0,0) ,(0, -1.25*n, 0), (1.25*n, 0, 0), (0, 0 ,1.25*n), (0, 1.25*n, 0), (0, 0, -1.25*n), (0, -1.25*n, 0), ( 0, 0 ,1.25*n)])
		cmds.xform( ro=(0,45,0), s=(0.8, 0.8, 0.8))
		obj = cmds.ls(sl=True)[0]
		# Clear Selection and Make Identity
		cmds.delete(obj , constructionHistory=True)
		cmds.makeIdentity(obj, apply=True, t=1, s=1, r=1)
		cmds.select(obj)
		color_it(col)
		# make offset groups
		cmds.group(obj, n= obj + '_Grp')
		cmds.group(obj + '_Grp', n = obj + '_Grp_OFF')
		print('Controller made at origin')
	
	else:
		for jnt in list:
			item01 = cmds.curve(n= jnt + '_C', d=1, p =[(1.25*n,0, 0), (0, 0, -1.25*n), (-1.25*n, 0, 0), (0, 0, 1.25*n), (1.25*n, 0, 0), (0, 1.25*n, 0),  (-1.25*n, 0,0) ,(0, -1.25*n, 0), (1.25*n, 0, 0), (0, 0 ,1.25*n), (0, 1.25*n, 0), (0, 0, -1.25*n), (0, -1.25*n, 0), ( 0, 0 ,1.25*n)])
			cmds.xform( ro=(0,45,0), s=(0.8, 0.8, 0.8))
			obj = cmds.ls(sl=True)[0]
			# Clear Selection and Make Identity
			cmds.delete(obj , constructionHistory=True)
			cmds.makeIdentity(obj, apply=True, t=1, s=1, r=1)
			cmds.select(obj)
			color_it(col)
			# Make Offset Groups
			item02 = cmds.group(obj, n = jnt + '_C_Grp')
			item03 = cmds.group(jnt + '_C_Grp', n = jnt + '_C_Grp_OFF')
			
			All_Ctrl_list.append(item03)
			All_Ctrl_list.append(item02)
			All_Ctrl_list.append(item01)
			# Position the controller at joint
			cmds.delete(cmds.parentConstraint(jnt, jnt + '_C_Grp_OFF' ,mo=False) )
			if pc==1:
				cmds.parentConstraint(obj, jnt, mo=True)
			if sc==1:
				cmds.scaleConstraint(obj, jnt, mo=True)
		i=3
		#Make FK Chain
		if fk==1:
			print(All_Ctrl_list)
			for item in enumerate(All_Ctrl_list):
				if i!= len(All_Ctrl_list):
					cmds.parent(All_Ctrl_list[i],All_Ctrl_list[i-1])
					i+=3
			cmds.select(All_Ctrl_list[-1])
	
# _____________________________________________________________________________	
def Create_Pyramid(Color):
	global pc, sc, fk
	All_Ctrl_list = []
	list = cmds.ls(sl=True)
	mgs = len(list)
	col = cmds.colorIndexSliderGrp(Color, query=True, value=True)
	if mgs<1:
		v = cmds.curve( d=1, p=[(0, 0, -1.25*n), (1.25*n, 0, 0), (0, 0, 1.25*n), (-1.25*n, 0, 0), (0, 0, -1.25*n), (0, 1.25*n, 0), (0, 0, 1.25*n), (1.25*n, 0 ,0), (0, 1.25*n, 0),(-1.25*n, 0 ,0 )])
		obj = cmds.ls(sl=True)[0]
		cmds.select(obj + '.cv[0]',obj + '.cv[1]', obj + '.cv[2]', obj + '.cv[3]', obj + '.cv[4]', obj + '.cv[6]', obj + '.cv[7]', obj + '.cv[9]')
		cmds.scale( 0.6, 0.6, 0.6)
		cmds.xform(obj, ro=(0,45,0))
		# Clear Selection and Make Identity
		cmds.delete(obj , constructionHistory=True)
		cmds.makeIdentity(obj, apply=True, t=1, s=1, r=1)
		cmds.select(obj)
		color_it(col)
		# make offset groups
		cmds.group(obj, n= obj + '_Grp')
		cmds.group(obj + '_Grp', n = obj + '_Grp_OFF')
		print('Controller made at origin')
	
	else:
		for jnt in list:
			item01 = cmds.curve(n= jnt + '_C', d=1, p=[(0, 0, -1.25*n), (1.25*n, 0, 0), (0, 0, 1.25*n), (-1.25*n, 0, 0), (0, 0, -1.25*n), (0, 1.25*n, 0), (0, 0, 1.25*n), (1.25*n, 0 ,0), (0, 1.25*n, 0),(-1.25*n, 0 ,0 )])
			obj = cmds.ls(sl=True)[0]
			cmds.select(obj + '.cv[0]',obj + '.cv[1]', obj + '.cv[2]', obj + '.cv[3]', obj + '.cv[4]', obj + '.cv[6]', obj + '.cv[7]', obj + '.cv[9]')
			cmds.scale( 0.6, 0.6, 0.6)
			cmds.xform(obj, ro=(0,45,0))
			# Clear Selection and Make Identity
			cmds.delete(obj , constructionHistory=True)
			cmds.makeIdentity(obj, apply=True, t=1, s=1, r=1)
			cmds.select(obj)
			color_it(col)
			# Make Offset Groups
			item02 = cmds.group(obj, n = jnt + '_C_Grp')
			item03 = cmds.group(jnt + '_C_Grp', n = jnt + '_C_Grp_OFF')
			
			All_Ctrl_list.append(item03)
			All_Ctrl_list.append(item02)
			All_Ctrl_list.append(item01)
			# Position the controller at joint
			cmds.delete(cmds.parentConstraint(jnt, jnt + '_C_Grp_OFF' ,mo=False) )
			if pc==1:
				cmds.parentConstraint(obj, jnt, mo=True)
			if sc==1:
				cmds.scaleConstraint(obj, jnt, mo=True)
		i=3
		#Make FK Chain
		if fk==1:
			print(All_Ctrl_list)
			for item in enumerate(All_Ctrl_list):
				if i!= len(All_Ctrl_list):
					cmds.parent(All_Ctrl_list[i],All_Ctrl_list[i-1])
					i+=3
			cmds.select(All_Ctrl_list[-1])
	

# _____________________________________________________________________________	
def Create_Aim(Color):
	global pc, sc, fk
	All_Ctrl_list = []
	list = cmds.ls(sl=True)
	mgs = len(list)
	col = cmds.colorIndexSliderGrp(Color, query=True, value=True)
	if mgs<1:
		v = cmds.curve( d=1, p= [(0, -1.25*n, 0), (0, 0, 0), (1.25*n, 0, 0), (0, 1.25*n, 0), (-1.25*n, 0, 0), (0, 0, 0), (0, 0, -1.25*n), (0, 1.25*n, 0) ,(0, 0, 1.25*n), (0, 0, 0), (0, 1.25*n ,0 )] )
		obj = cmds.ls(sl=True)[0]
		# Clear Selection and Make Identity
		cmds.delete(obj , constructionHistory=True)
		cmds.makeIdentity(obj, apply=True, t=1, s=1, r=1)
		cmds.select(obj)
		color_it(col)
		# make offset groups
		cmds.group(obj, n= obj + '_Grp')
		cmds.group(obj + '_Grp', n = obj + '_Grp_OFF')
		print('Controller made at origin')
	
	else:
		for jnt in list:
			item01 =cmds.curve(n= jnt + '_C', d=1, p= [(0, -1.25*n, 0), (0, 0, 0), (1.25*n, 0, 0), (0, 1.25*n, 0), (-1.25*n, 0, 0), (0, 0, 0), (0, 0, -1.25*n), (0, 1.25*n, 0) ,(0, 0, 1.25*n), (0, 0, 0), (0, 1.25*n ,0 )] )
			obj = cmds.ls(sl=True)[0]
			# Clear Selection and Make Identity
			cmds.delete(obj , constructionHistory=True)
			cmds.makeIdentity(obj, apply=True, t=1, s=1, r=1)
			cmds.select(obj)
			color_it(col)
			# Make Offset Groups
			item02 = cmds.group(obj, n = jnt + '_C_Grp')
			item03 = cmds.group(jnt + '_C_Grp', n = jnt + '_C_Grp_OFF')
			
			All_Ctrl_list.append(item03)
			All_Ctrl_list.append(item02)
			All_Ctrl_list.append(item01)
			# Position the controller at joint
			cmds.delete(cmds.parentConstraint(jnt, jnt + '_C_Grp_OFF' ,mo=False) )
			if pc==1:
				cmds.parentConstraint(obj, jnt, mo=True)
			if sc==1:
				cmds.scaleConstraint(obj, jnt, mo=True)
		i=3
		#Make FK Chain
		if fk==1:
			print(All_Ctrl_list)
			for item in enumerate(All_Ctrl_list):
				if i!= len(All_Ctrl_list):
					cmds.parent(All_Ctrl_list[i],All_Ctrl_list[i-1])
					i+=3
			cmds.select(All_Ctrl_list[-1])
# __________________________________________________________
def Create_Cube(Color):
	global pc, sc, fk
	All_Ctrl_list = []
	list = cmds.ls(sl=True)
	mgs = len(list)
	col = cmds.colorIndexSliderGrp(Color, query=True, value=True)
	if mgs<1:
		v = cmds.curve( d=1, p=[(-n, n, n), (-n, -n, n),(n, -n, n),(n, n, n),(-n, n, n), (-n, n, -n), (-n, -n, -n), (n, -n, -n), (n, n, -n), (-n, n, -n), (n, n, -n), (n, n, n), (n, -n, n), (n, -n, -n), (-n, -n, -n), (-n, -n, n)])
		obj = cmds.ls(sl=True)[0]
		# Clear Selection and Make Identity
		cmds.delete(obj , constructionHistory=True)
		cmds.makeIdentity(obj, apply=True, t=1, s=1, r=1)
		cmds.select(obj)
		color_it(col)
		# make offset groups
		cmds.group(obj, n= obj + '_Grp')
		cmds.group(obj + '_Grp', n = obj + '_Grp_OFF')
		print('Controller made at origin')
	
	else:
		for jnt in list:
			item01= cmds.curve(n= jnt + '_C', d=1, p=[(-n, n, n), (-n, -n, n),(n, -n, n),(n, n, n),(-n, n, n), (-n, n, -n), (-n, -n, -n), (n, -n, -n), (n, n, -n), (-n, n, -n), (n, n, -n), (n, n, n), (n, -n, n), (n, -n, -n), (-n, -n, -n), (-n, -n, n)])
			obj = cmds.ls(sl=True)[0]
			# Clear Selection and Make Identity
			cmds.delete(obj , constructionHistory=True)
			cmds.makeIdentity(obj, apply=True, t=1, s=1, r=1)
			cmds.select(obj)
			color_it(col)
			# Make Offset Groups
			item02 = cmds.group(obj, n = jnt + '_C_Grp')
			item03 = cmds.group(jnt + '_C_Grp', n = jnt + '_C_Grp_OFF')
			
			All_Ctrl_list.append(item03)
			All_Ctrl_list.append(item02)
			All_Ctrl_list.append(item01)
			# Position the controller at joint
			cmds.delete(cmds.parentConstraint(jnt, jnt + '_C_Grp_OFF' ,mo=False) )
			if pc==1:
				cmds.parentConstraint(obj, jnt, mo=True)
			if sc==1:
				cmds.scaleConstraint(obj, jnt, mo=True)
		i=3
		#Make FK Chain
		if fk==1:
			print(All_Ctrl_list)
			for item in enumerate(All_Ctrl_list):
				if i!= len(All_Ctrl_list):
					cmds.parent(All_Ctrl_list[i],All_Ctrl_list[i-1])
					i+=3
			cmds.select(All_Ctrl_list[-1])
# _____________________________________________________________________________	
def Create_Circle(Color):
	global pc, sc, fk
	All_Ctrl_list = []
	list = cmds.ls(sl=True)
	mgs = len(list)
	col = cmds.colorIndexSliderGrp(Color, query=True, value=True)
	if mgs<1:
		v = cmds.circle( radius = n)
		cmds.xform(ro=(-90,0,0), r=True, os=True)
		obj = cmds.ls(sl=True)[0]
		# Clear Selection and Make Identity
		cmds.delete(obj , constructionHistory=True)
		cmds.makeIdentity(obj, apply=True, t=1, s=1, r=1)
		cmds.select(obj)
		color_it(col)
		# make offset groups
		cmds.group(obj, n= obj + '_Grp')
		cmds.group(obj + '_Grp', n = obj + '_Grp_OFF')
		print('Controller made at origin')
	
	else:
		for jnt in list:
			item01 = cmds.circle(n= jnt + '_C', radius = n)[0]
			cmds.xform(ro=(-90,0,0), r=True, os=True)
			obj = cmds.ls(sl=True)[0]
			# Clear Selection and Make Identity
			cmds.delete(obj , constructionHistory=True)
			cmds.makeIdentity(obj, apply=True, t=1, s=1, r=1)
			cmds.select(obj)
			color_it(col)
			# Make Offset Groups
			item02 = cmds.group(obj, n = jnt + '_C_Grp')
			item03 = cmds.group(jnt + '_C_Grp', n = jnt + '_C_Grp_OFF')
			
			All_Ctrl_list.append(item03)
			All_Ctrl_list.append(item02)
			All_Ctrl_list.append(item01)
			# Position the controller at joint
			cmds.delete(cmds.parentConstraint(jnt, jnt + '_C_Grp_OFF' ,mo=False) )
			if pc==1:
				cmds.parentConstraint(obj, jnt, mo=True)
			if sc==1:
				cmds.scaleConstraint(obj, jnt, mo=True)
		i=3
		#Make FK Chain
		if fk==1:
			print(All_Ctrl_list)
			for item in enumerate(All_Ctrl_list):
				if i!= len(All_Ctrl_list):
					cmds.parent(All_Ctrl_list[i],All_Ctrl_list[i-1])
					i+=3
			cmds.select(All_Ctrl_list[-1])
# _____________________________________________________________________________	
def Create_Square(Color):
	global pc, sc, fk
	All_Ctrl_list = []
	list = cmds.ls(sl=True)
	mgs = len(list)
	col = cmds.colorIndexSliderGrp(Color, query=True, value=True)
	if mgs<1:
		# make controller
		v = cmds.curve( d=1, p=[(-n, 0, -n),(n,0,-n),(n,0,n),(-n,0,n),(-n,0,-n)])
		obj = cmds.ls(sl=True)[0]
		# Clear Selection and Make Identity
		cmds.delete(obj , constructionHistory=True)
		cmds.makeIdentity(obj, apply=True, t=1, s=1, r=1)
		cmds.select(obj)
		color_it(col)
		# make offset groups
		cmds.group(obj, n= obj + '_Grp')
		cmds.group(obj + '_Grp', n = obj + '_Grp_OFF')
		print('Controller made at origin')
	
	else:
		for jnt in list:
			item01 = cmds.curve(n= jnt + '_C', d=1, p=[(-n, 0, -n),(n,0,-n),(n,0,n),(-n,0,n),(-n,0,-n)])
			obj = cmds.ls(sl=True)[0]
			# Clear Selection and Make Identity
			cmds.delete(obj , constructionHistory=True)
			cmds.makeIdentity(obj, apply=True, t=1, s=1, r=1)
			cmds.select(obj)
			color_it(col)
			# Make Offset Groups
			item02 = cmds.group(obj, n = jnt + '_C_Grp')
			item03 = cmds.group(jnt + '_C_Grp', n = jnt + '_C_Grp_OFF')
			
			All_Ctrl_list.append(item03)
			All_Ctrl_list.append(item02)
			All_Ctrl_list.append(item01)
			# Position the controller at joint
			cmds.delete(cmds.parentConstraint(jnt, jnt + '_C_Grp_OFF' ,mo=False) )
			if pc==1:
				cmds.parentConstraint(obj, jnt, mo=True)
			if sc==1:
				cmds.scaleConstraint(obj, jnt, mo=True)
		i=3
		#Make FK Chain
		if fk==1:
			print(All_Ctrl_list)
			for item in enumerate(All_Ctrl_list):
				if i!= len(All_Ctrl_list):
					cmds.parent(All_Ctrl_list[i],All_Ctrl_list[i-1])
					i+=3
			cmds.select(All_Ctrl_list[-1])
# _____________________________________________________________________________	
def Create_Triangle(Color):
	global pc, sc, fk
	All_Ctrl_list = []
	list = cmds.ls(sl=True)
	mgs = len(list)
	col = cmds.colorIndexSliderGrp(Color, query=True, value=True)
	if mgs<1:
		# make controller
		v = cmds.curve( d=1, p=[(n,0,n),(-n,0,0),(n,0,-n),(n,0,n)] )
		obj = cmds.ls(sl=True)[0]
		# Clear Selection and Make Identity
		cmds.delete(obj , constructionHistory=True)
		cmds.makeIdentity(obj, apply=True, t=1, s=1, r=1)
		cmds.select(obj)
		color_it(col)
		# make offset groups
		cmds.group(obj, n= obj + '_Grp')
		cmds.group(obj + '_Grp', n = obj + '_Grp_OFF')
		print('Controller made at origin')
	
	else:
		for jnt in list:
			item01 = cmds.curve(n= jnt + '_C', d=1, p=[(n,0,n),(-n,0,0),(n,0,-n),(n,0,n)] )
			obj = cmds.ls(sl=True)[0]
			# Clear Selection and Make Identity
			cmds.delete(obj , constructionHistory=True)
			cmds.makeIdentity(obj, apply=True, t=1, s=1, r=1)
			cmds.select(obj)
			color_it(col)
			# Make Offset Groups
			item02 = cmds.group(obj, n = jnt + '_C_Grp')
			item03 = cmds.group(jnt + '_C_Grp', n = jnt + '_C_Grp_OFF')
			
			All_Ctrl_list.append(item03)
			All_Ctrl_list.append(item02)
			All_Ctrl_list.append(item01)
			# Position the controller at joint
			cmds.delete(cmds.parentConstraint(jnt, jnt + '_C_Grp_OFF' ,mo=False) )
			if pc==1:
				cmds.parentConstraint(obj, jnt, mo=True)
			if sc==1:
				cmds.scaleConstraint(obj, jnt, mo=True)
		i=3
		#Make FK Chain
		if fk==1:
			print(All_Ctrl_list)
			for item in enumerate(All_Ctrl_list):
				if i!= len(All_Ctrl_list):
					cmds.parent(All_Ctrl_list[i],All_Ctrl_list[i-1])
					i+=3
			cmds.select(All_Ctrl_list[-1])
# _____________________________________________________________________________	
def Create_Plus(Color):
	global pc, sc, fk
	All_Ctrl_list = []
	list = cmds.ls(sl=True)
	mgs = len(list)
	col = cmds.colorIndexSliderGrp(Color, query=True, value=True)
	if mgs<1:
		# make controller
		v = cmds.curve( d=1, p=[(n, 0 ,n ),( n, 0, 3*n),(-n, 0, 3*n),(-n, 0, n),(-3*n, 0, n), (-3*n, 0, -n), (-n, 0, -n), (-n, 0, -3*n),( n, 0, -3*n),(n, 0, -n), (3*n, 0, -n), (3*n,0, n), (n, 0, n)] )
		cmds.xform(s=(0.3, 0.3, 0.3))
		obj = cmds.ls(sl=True)[0]
		# Clear Selection and Make Identity
		cmds.delete(obj , constructionHistory=True)
		cmds.makeIdentity(obj, apply=True, t=1, s=1, r=1)
		cmds.select(obj)
		color_it(col)
		# make offset groups
		cmds.group(obj, n= obj + '_Grp')
		cmds.group(obj + '_Grp', n = obj + '_Grp_OFF')
		print('Controller made at origin')
	
	else:
		for jnt in list:
			item01 = cmds.curve(n= jnt + '_C', d=1, p=[(n, 0 ,n ),( n, 0, 3*n),(-n, 0, 3*n),(-n, 0, n),(-3*n, 0, n), (-3*n, 0, -n), (-n, 0, -n), (-n, 0, -3*n),( n, 0, -3*n),(n, 0, -n), (3*n, 0, -n), (3*n,0, n), (n, 0, n)] )
			cmds.xform(s=(0.3, 0.3, 0.3))
			obj = cmds.ls(sl=True)[0]
			# Clear Selection and Make Identity
			cmds.delete(obj , constructionHistory=True)
			cmds.makeIdentity(obj, apply=True, t=1, s=1, r=1)
			cmds.select(obj)
			color_it(col)
			# Make Offset Groups
			item02 = cmds.group(obj, n = jnt + '_C_Grp')
			item03 = cmds.group(jnt + '_C_Grp', n = jnt + '_C_Grp_OFF')
			
			All_Ctrl_list.append(item03)
			All_Ctrl_list.append(item02)
			All_Ctrl_list.append(item01)
			# Position the controller at joint
			cmds.delete(cmds.parentConstraint(jnt, jnt + '_C_Grp_OFF' ,mo=False) )
			if pc==1:
				cmds.parentConstraint(obj, jnt, mo=True)
			if sc==1:
				cmds.scaleConstraint(obj, jnt, mo=True)
		i=3
		#Make FK Chain
		if fk==1:
			print(All_Ctrl_list)
			for item in enumerate(All_Ctrl_list):
				if i!= len(All_Ctrl_list):
					cmds.parent(All_Ctrl_list[i],All_Ctrl_list[i-1])
					i+=3
			cmds.select(All_Ctrl_list[-1])
	
# _____________________________________________________________________________	
def Create_Cross(Color):
	global pc, sc, fk
	All_Ctrl_list = []
	list = cmds.ls(sl=True)
	mgs = len(list)
	col = cmds.colorIndexSliderGrp(Color, query=True, value=True)
	if mgs<1:
		# make controller
		v = cmds.curve( d=1, p=[(n, 0 ,n ),( n, 0, 3*n),(-n, 0, 3*n),(-n, 0, n),(-3*n, 0, n), (-3*n, 0, -n), (-n, 0, -n), (-n, 0, -3*n),( n, 0, -3*n),(n, 0, -n), (3*n, 0, -n), (3*n,0, n), (n, 0, n)] )
		obj = cmds.ls(sl=True)[0]
		cmds.xform(obj, s=(0.2, 0.2, 0.2), ro=(0,45,0))
		cmds.select(obj + '.cv[1:2]', obj + '.cv[4:5]', obj + '.cv[7:8]', obj + '.cv[10:11]')
		cmds.scale(1.65, 1.65, 1.65)
		# Clear Selection and Make Identity
		cmds.delete(obj , constructionHistory=True)
		cmds.makeIdentity(obj, apply=True, t=1, s=1, r=1)
		cmds.select(obj)
		color_it(col)
		# make offset groups
		cmds.group(obj, n= obj + '_Grp')
		cmds.group(obj + '_Grp', n = obj + '_Grp_OFF')
		print('Controller made at origin')
	
	else:
		for jnt in list:
			item01 = cmds.curve(n= jnt + '_C', d=1, p=[(n, 0 ,n ),( n, 0, 3*n),(-n, 0, 3*n),(-n, 0, n),(-3*n, 0, n), (-3*n, 0, -n), (-n, 0, -n), (-n, 0, -3*n),( n, 0, -3*n),(n, 0, -n), (3*n, 0, -n), (3*n,0, n), (n, 0, n)] )
			obj = cmds.ls(sl=True)[0]
			cmds.xform(obj, s=(0.2, 0.2, 0.2), ro=(0,45,0))
			cmds.select(obj + '.cv[1:2]', obj + '.cv[4:5]', obj + '.cv[7:8]', obj + '.cv[10:11]')
			cmds.scale(1.65, 1.65, 1.65)
			# Clear Selection and Make Identity
			cmds.delete(obj , constructionHistory=True)
			cmds.makeIdentity(obj, apply=True, t=1, s=1, r=1)
			cmds.select(obj)
			color_it(col)
			# Make Offset Groups
			item02 = cmds.group(obj, n = jnt + '_C_Grp')
			item03 = cmds.group(jnt + '_C_Grp', n = jnt + '_C_Grp_OFF')
			
			All_Ctrl_list.append(item03)
			All_Ctrl_list.append(item02)
			All_Ctrl_list.append(item01)
			# Position the controller at joint
			cmds.delete(cmds.parentConstraint(jnt, jnt + '_C_Grp_OFF' ,mo=False) )
			if pc==1:
				cmds.parentConstraint(obj, jnt, mo=True)
			if sc==1:
				cmds.scaleConstraint(obj, jnt, mo=True)
		i=3
		#Make FK Chain
		if fk==1:
			print(All_Ctrl_list)
			for item in enumerate(All_Ctrl_list):
				if i!= len(All_Ctrl_list):
					cmds.parent(All_Ctrl_list[i],All_Ctrl_list[i-1])
					i+=3
			cmds.select(All_Ctrl_list[-1])

# _____________________________________________________________________________	
def Create_Arrow(Color):
	global pc, sc, fk
	All_Ctrl_list = []
	list = cmds.ls(sl=True)
	mgs = len(list)
	col = cmds.colorIndexSliderGrp(Color, query=True, value=True)
	if mgs<1:
		# make controller
		v = m=n*0.25
		v = cmds.curve(d=1, p = [(-1.25*m, 0, 2.5*m), (-1.25*m,0,0), (-2.5*m,0,0),(0,0,-2.5*m),(2.5*m,0,0),(1.25*m,0,0),(1.25*m,0,2.5*m), (-1.25*m, 0,2.5*m)] )
		cmds.rotate(0,-90,0)
		obj = cmds.ls(sl=True)[0]
		# Clear Selection and Make Identity
		cmds.delete(obj , constructionHistory=True)
		cmds.makeIdentity(obj, apply=True, t=1, s=1, r=1)
		cmds.select(obj)
		color_it(col)
		# make offset groups
		cmds.group(obj, n= obj + '_Grp')
		cmds.group(obj + '_Grp', n = obj + '_Grp_OFF')
		print('Controller made at origin')
	
	else:
		for jnt in list:
			m=n*0.25
			item01 = cmds.curve(n= jnt + '_C', d=1, p = [(-1.25*m, 0, 2.5*m), (-1.25*m,0,0), (-2.5*m,0,0),(0,0,-2.5*m),(2.5*m,0,0),(1.25*m,0,0),(1.25*m,0,2.5*m), (-1.25*m, 0,2.5*m)] )
			cmds.rotate(0,-90,0)
			obj = cmds.ls(sl=True)[0]
			# Clear Selection and Make Identity
			cmds.delete(obj , constructionHistory=True)
			cmds.makeIdentity(obj, apply=True, t=1, s=1, r=1)
			cmds.select(obj)
			color_it(col)
			# Make Offset Groups
			item02 = cmds.group(obj, n = jnt + '_C_Grp')
			item03 = cmds.group(jnt + '_C_Grp', n = jnt + '_C_Grp_OFF')
			
			All_Ctrl_list.append(item03)
			All_Ctrl_list.append(item02)
			All_Ctrl_list.append(item01)
			# Position the controller at joint
			cmds.delete(cmds.parentConstraint(jnt, jnt + '_C_Grp_OFF' ,mo=False) )
			if pc==1:
				cmds.parentConstraint(obj, jnt, mo=True)
			if sc==1:
				cmds.scaleConstraint(obj, jnt, mo=True)
		i=3
		#Make FK Chain
		if fk==1:
			print(All_Ctrl_list)
			for item in enumerate(All_Ctrl_list):
				if i!= len(All_Ctrl_list):
					cmds.parent(All_Ctrl_list[i],All_Ctrl_list[i-1])
					i+=3
			cmds.select(All_Ctrl_list[-1])
# _____________________________________________________________________________	
def Create_Double_Arrow(Color):
	global pc, sc, fk
	All_Ctrl_list = []
	list = cmds.ls(sl=True)
	mgs = len(list)
	col = cmds.colorIndexSliderGrp(Color, query=True, value=True)
	if mgs<1:
		# make controller
		v = cmds.curve(d=1, p = [(-2.5*n, 0, -1.25*n), (2.5*n, 0, -1.25*n), (2.5*n, 0, -2.5*n) , (5*n, 0, 0), (2.5*n, 0, 2.5*n), (2.5*n, 0, 1.25*n), (-2.5*n, 0, 1.25*n), (-2.5*n, 0, 2.5*n), (-5*n, 0 ,0), (-2.5*n, 0, -2.5*n), (-2.5*n, 0, -1.25*n)] )
		cmds.scale(0.25, 0.25, 0.25)
		obj = cmds.ls(sl=True)[0]
		# Clear Selection and Make Identity
		cmds.delete(obj , constructionHistory=True)
		cmds.makeIdentity(obj, apply=True, t=1, s=1, r=1)
		cmds.select(obj)
		color_it(col)
		# make offset groups
		cmds.group(obj, n= obj + '_Grp')
		cmds.group(obj + '_Grp', n = obj + '_Grp_OFF')
		print('Controller made at origin')
	
	else:
		for jnt in list:
			item01 =  cmds.curve(n= jnt + '_C', d=1, p = [(-2.5*n, 0, -1.25*n), (2.5*n, 0, -1.25*n), (2.5*n, 0, -2.5*n) , (5*n, 0, 0), (2.5*n, 0, 2.5*n), (2.5*n, 0, 1.25*n), (-2.5*n, 0, 1.25*n), (-2.5*n, 0, 2.5*n), (-5*n, 0 ,0), (-2.5*n, 0, -2.5*n), (-2.5*n, 0, -1.25*n)] )
			cmds.scale(0.25, 0.25, 0.25)
			obj = cmds.ls(sl=True)[0]
			# Clear Selection and Make Identity
			cmds.delete(obj , constructionHistory=True)
			cmds.makeIdentity(obj, apply=True, t=1, s=1, r=1)
			cmds.select(obj)
			color_it(col)
			# Make Offset Groups
			item02 = cmds.group(obj, n = jnt + '_C_Grp')
			item03 = cmds.group(jnt + '_C_Grp', n = jnt + '_C_Grp_OFF')
			
			All_Ctrl_list.append(item03)
			All_Ctrl_list.append(item02)
			All_Ctrl_list.append(item01)
			# Position the controller at joint
			cmds.delete(cmds.parentConstraint(jnt, jnt + '_C_Grp_OFF' ,mo=False) )
			if pc==1:
				cmds.parentConstraint(obj, jnt, mo=True)
			if sc==1:
				cmds.scaleConstraint(obj, jnt, mo=True)
		i=3
		#Make FK Chain
		if fk==1:
			print(All_Ctrl_list)
			for item in enumerate(All_Ctrl_list):
				if i!= len(All_Ctrl_list):
					cmds.parent(All_Ctrl_list[i],All_Ctrl_list[i-1])
					i+=3
			cmds.select(All_Ctrl_list[-1])

# _____________________________________________________________________________
def Create_Four_Arrow(Color):
	global pc, sc, fk
	All_Ctrl_list = []
	list = cmds.ls(sl=True)
	mgs = len(list)
	col = cmds.colorIndexSliderGrp(Color, query=True, value=True)
	if mgs<1:
		# make controller
		v = cmds.curve(d=1, p = [(-1.25*n, 0, -1.25*n), (-1.25*n, 0, -3.75*n), (-2.5*n, 0, -3.75*n), (0, 0, -6.25*n), (2.5*n, 0, -3.75*n), (1.25*n, 0, -3.75*n), (1.25*n, 0, -1.25*n),  (3.75*n, 0, -1.25*n), (3.75*n, 0, -2.5*n), (6.25*n, 0, 0),  (3.75*n, 0 ,2.5*n), (3.75*n, 0, 1.25*n), (1.25*n, 0 ,1.25*n), (1.25*n, 0, 3.75*n), (2.5*n, 0, 3.75*n),  (0, 0, 6.25*n), (-2.5*n, 0, 3.75*n),  (-1.25*n, 0, 3.75*n), (-1.25*n, 0, 1.25*n), (-3.75*n, 0, 1.25*n), (-3.75*n, 0 ,2.5*n), (-6.25*n, 0, 0), (-3.75*n, 0 ,-2.5*n), (-3.75*n, 0 ,-1.25*n), (-1.25*n, 0 ,-1.25*n)] )
		cmds.scale(0.2, 0.2, 0.2)
		obj = cmds.ls(sl=True)[0]
		# Clear Selection and Make Identity
		cmds.delete(obj , constructionHistory=True)
		cmds.makeIdentity(obj, apply=True, t=1, s=1, r=1)
		cmds.select(obj)
		color_it(col)
		# make offset groups
		cmds.group(obj, n= obj + '_Grp')
		cmds.group(obj + '_Grp', n = obj + '_Grp_OFF')
		print('Controller made at origin')
	
	else:
		for jnt in list:
			item01 =  cmds.curve(n= jnt + '_C', d=1, p = [(-1.25*n, 0, -1.25*n), (-1.25*n, 0, -3.75*n), (-2.5*n, 0, -3.75*n), (0, 0, -6.25*n), (2.5*n, 0, -3.75*n), (1.25*n, 0, -3.75*n), (1.25*n, 0, -1.25*n),  (3.75*n, 0, -1.25*n), (3.75*n, 0, -2.5*n), (6.25*n, 0, 0),  (3.75*n, 0 ,2.5*n), (3.75*n, 0, 1.25*n), (1.25*n, 0 ,1.25*n), (1.25*n, 0, 3.75*n), (2.5*n, 0, 3.75*n),  (0, 0, 6.25*n), (-2.5*n, 0, 3.75*n),  (-1.25*n, 0, 3.75*n), (-1.25*n, 0, 1.25*n), (-3.75*n, 0, 1.25*n), (-3.75*n, 0 ,2.5*n), (-6.25*n, 0, 0), (-3.75*n, 0 ,-2.5*n), (-3.75*n, 0 ,-1.25*n), (-1.25*n, 0 ,-1.25*n)] )
			cmds.scale(0.2, 0.2, 0.2)
			obj = cmds.ls(sl=True)[0]
			# Clear Selection and Make Identity
			cmds.delete(obj , constructionHistory=True)
			cmds.makeIdentity(obj, apply=True, t=1, s=1, r=1)
			cmds.select(obj)
			color_it(col)
			# Make Offset Groups
			item02 = cmds.group(obj, n = jnt + '_C_Grp')
			item03 = cmds.group(jnt + '_C_Grp', n = jnt + '_C_Grp_OFF')
			
			All_Ctrl_list.append(item03)
			All_Ctrl_list.append(item02)
			All_Ctrl_list.append(item01)
			# Position the controller at joint
			cmds.delete(cmds.parentConstraint(jnt, jnt + '_C_Grp_OFF' ,mo=False) )
			if pc==1:
				cmds.parentConstraint(obj, jnt, mo=True)
			if sc==1:
				cmds.scaleConstraint(obj, jnt, mo=True)
		i=3
		#Make FK Chain
		if fk==1:
			print(All_Ctrl_list)
			for item in enumerate(All_Ctrl_list):
				if i!= len(All_Ctrl_list):
					cmds.parent(All_Ctrl_list[i],All_Ctrl_list[i-1])
					i+=3
			cmds.select(All_Ctrl_list[-1])

# _____________________________________________________________________________
def Create_Arrow_on_Ball(Color):
	global pc, sc, fk
	All_Ctrl_list = []
	list = cmds.ls(sl=True)
	mgs = len(list)
	col = cmds.colorIndexSliderGrp(Color, query=True, value=True)
	if mgs<1:
		# make controller
		v = cmds.curve(d=1, p= [(0,0.35, -1.00), (-0.336, 0.677, -0.751), (-0.0959, 0.677, -0.751), (-0.0959, 0.850, -0.500), ( -0.0959, 0.954, -0.0987),( -0.500, 0.850, -0.0987), (-0.751, 0.677, -0.0987) ,(-0.7511, 0.677, -0.336), ( -1.001567, 0.35,0 ),(-0.751, 0.677, 0.336), ( -0.751, 0.677, 0.0987), ( -0.500,0.8504, 0.0987),( -0.0959835, 0.954001 ,0.0987656), (-0.0959835, 0.850458, 0.500783), (-0.0959835, 0.677886, 0.751175), (-0.336638, 0.677886, 0.751175), (0, 0.35, 1.001567), (0.336638, 0.677886, 0.751175), (0.0959835, 0.677886, 0.751175), (0.0959835, 0.850458, 0.500783), ( 0.0959835, 0.954001, 0.0987656),(0.500783, 0.850458, 0.0987656) , (0.751175, 0.677886, 0.0987656), (0.751175, 0.677886, 0.336638), ( 1.001567, 0.35, 0 ), (0.751175, 0.677886 ,-0.336638), ( 0.751175, 0.677886, -0.0987656) , (0.500783, 0.850458 ,-0.0987656), (0.0959835, 0.954001, -0.0987656),(0.0959835, 0.850458, -0.500783), (0.0959835, 0.677886, -0.751175), (0.336638, 0.677886, -0.751175), (0, 0.35, -1.001567)] )
		obj = cmds.ls(sl=True)[0]
		# Clear Selection and Make Identity
		cmds.delete(obj , constructionHistory=True)
		cmds.makeIdentity(obj, apply=True, t=1, s=1, r=1)
		cmds.select(obj)
		color_it(col)
		# make offset groups
		cmds.group(obj, n= obj + '_Grp')
		cmds.group(obj + '_Grp', n = obj + '_Grp_OFF')
		print('Controller made at origin')
	
	else:
		for jnt in list:
			item01 =  cmds.curve(n= jnt + '_C', d=1, p= [(0,0.35, -1.00), (-0.336, 0.677, -0.751), (-0.0959, 0.677, -0.751), (-0.0959, 0.850, -0.500), ( -0.0959, 0.954, -0.0987),( -0.500, 0.850, -0.0987), (-0.751, 0.677, -0.0987) ,(-0.7511, 0.677, -0.336), ( -1.001567, 0.35,0 ),(-0.751, 0.677, 0.336), ( -0.751, 0.677, 0.0987), ( -0.500,0.8504, 0.0987),( -0.0959835, 0.954001 ,0.0987656), (-0.0959835, 0.850458, 0.500783), (-0.0959835, 0.677886, 0.751175), (-0.336638, 0.677886, 0.751175), (0, 0.35, 1.001567), (0.336638, 0.677886, 0.751175), (0.0959835, 0.677886, 0.751175), (0.0959835, 0.850458, 0.500783), ( 0.0959835, 0.954001, 0.0987656),(0.500783, 0.850458, 0.0987656) , (0.751175, 0.677886, 0.0987656), (0.751175, 0.677886, 0.336638), ( 1.001567, 0.35, 0 ), (0.751175, 0.677886 ,-0.336638), ( 0.751175, 0.677886, -0.0987656) , (0.500783, 0.850458 ,-0.0987656), (0.0959835, 0.954001, -0.0987656),(0.0959835, 0.850458, -0.500783), (0.0959835, 0.677886, -0.751175), (0.336638, 0.677886, -0.751175), (0, 0.35, -1.001567)] )
			obj = cmds.ls(sl=True)[0]
			# Clear Selection and Make Identity
			cmds.delete(obj , constructionHistory=True)
			cmds.makeIdentity(obj, apply=True, t=1, s=1, r=1)
			cmds.select(obj)
			color_it(col)
			# Make Offset Groups
			item02 = cmds.group(obj, n = jnt + '_C_Grp')
			item03 = cmds.group(jnt + '_C_Grp', n = jnt + '_C_Grp_OFF')
			
			All_Ctrl_list.append(item03)
			All_Ctrl_list.append(item02)
			All_Ctrl_list.append(item01)
			# Position the controller at joint
			cmds.delete(cmds.parentConstraint(jnt, jnt + '_C_Grp_OFF' ,mo=False) )
			if pc==1:
				cmds.parentConstraint(obj, jnt, mo=True)
			if sc==1:
				cmds.scaleConstraint(obj, jnt, mo=True)
		i=3
		#Make FK Chain
		if fk==1:
			print(All_Ctrl_list)
			for item in enumerate(All_Ctrl_list):
				if i!= len(All_Ctrl_list):
					cmds.parent(All_Ctrl_list[i],All_Ctrl_list[i-1])
					i+=3
			cmds.select(All_Ctrl_list[-1])
# _____________________________________________________________________________	
def Create_Rotate_Arrow(Color):
	global pc, sc, fk
	All_Ctrl_list = []
	list = cmds.ls(sl=True)
	mgs = len(list)
	col = cmds.colorIndexSliderGrp(Color, query=True, value=True)
	if mgs<1:
		# make controller
		v = cmds.curve(d = 1, p= [(-0.124*n, 0, -1.096*n),  (-0.975*n, 0, -1.036*n),  (-0.559*n, 0 ,-0.944*n), (-0.798*n, 0 ,-0.798*n), (-1.042*n, 0, -0.431*n), (-1.128*n, 0, 0),  (-1.042*n, 0, 0.431*n), (-0.798*n, 0, 0.798*n),  (-0.560*n, 0, 0.946*n), (-0.975*n, 0, 1.036*n),  (-0.124*n, 0, 1.096*n), (-0.537*n, 0, 0.349*n), (-0.440*n, 0, 0.788*n),  (-0.652*n, 0, 0.652*n), (-0.853*n, 0, 0.353*n),  (-0.923*n, 0 ,0 ), (-0.853*n, 0, -0.353*n),  (-0.652*n, 0, -0.652*n), (-0.439*n, 0, -0.785*n),  (-0.537*n, 0 ,-0.349*n), (-0.124*n, 0, -1.096*n)] )
		cmds.xform(ro=(0,0,-90) )
		obj = cmds.ls(sl=True)[0]
		# Clear Selection and Make Identity
		cmds.delete(obj , constructionHistory=True)
		cmds.makeIdentity(obj, apply=True, t=1, s=1, r=1)
		cmds.select(obj)
		color_it(col)
		# make offset groups
		cmds.group(obj, n= obj + '_Grp')
		cmds.group(obj + '_Grp', n = obj + '_Grp_OFF')
		print('Controller made at origin')
	
	else:
		for jnt in list:
			item01 = cmds.curve(n= jnt + '_C', d = 1, p= [(-0.124*n, 0, -1.096*n),  (-0.975*n, 0, -1.036*n),  (-0.559*n, 0 ,-0.944*n), (-0.798*n, 0 ,-0.798*n), (-1.042*n, 0, -0.431*n), (-1.128*n, 0, 0),  (-1.042*n, 0, 0.431*n), (-0.798*n, 0, 0.798*n),  (-0.560*n, 0, 0.946*n), (-0.975*n, 0, 1.036*n),  (-0.124*n, 0, 1.096*n), (-0.537*n, 0, 0.349*n), (-0.440*n, 0, 0.788*n),  (-0.652*n, 0, 0.652*n), (-0.853*n, 0, 0.353*n),  (-0.923*n, 0 ,0 ), (-0.853*n, 0, -0.353*n),  (-0.652*n, 0, -0.652*n), (-0.439*n, 0, -0.785*n),  (-0.537*n, 0 ,-0.349*n), (-0.124*n, 0, -1.096*n)] )
			cmds.xform(ro=(0,0,-90) )
			obj = cmds.ls(sl=True)[0]
			# Clear Selection and Make Identity
			cmds.delete(obj , constructionHistory=True)
			cmds.makeIdentity(obj, apply=True, t=1, s=1, r=1)
			cmds.select(obj)
			color_it(col)
			# Make Offset Groups
			item02 = cmds.group(obj, n = jnt + '_C_Grp')
			item03 = cmds.group(jnt + '_C_Grp', n = jnt + '_C_Grp_OFF')
			
			All_Ctrl_list.append(item03)
			All_Ctrl_list.append(item02)
			All_Ctrl_list.append(item01)
			# Position the controller at joint
			cmds.delete(cmds.parentConstraint(jnt, jnt + '_C_Grp_OFF' ,mo=False) )
			if pc==1:
				cmds.parentConstraint(obj, jnt, mo=True)
			if sc==1:
				cmds.scaleConstraint(obj, jnt, mo=True)
		i=3
		#Make FK Chain
		if fk==1:
			print(All_Ctrl_list)
			for item in enumerate(All_Ctrl_list):
				if i!= len(All_Ctrl_list):
					cmds.parent(All_Ctrl_list[i],All_Ctrl_list[i-1])
					i+=3
			cmds.select(All_Ctrl_list[-1])

# _____________________________________________________________________________
def Create_Flower(Color):
	global pc, sc, fk
	All_Ctrl_list = []
	list = cmds.ls(sl=True)
	mgs = len(list)
	col = cmds.colorIndexSliderGrp(Color, query=True, value=True)
	if mgs<1:
		# make controller
		v = cmds.circle(radius=n, d=3, s=16)
		obj = cmds.ls(sl=True)[0]
		cmds.select(obj + '.cv[0]', obj + '.cv[2]' , obj + '.cv[4]', obj + '.cv[6]', obj + '.cv[8]', obj + '.cv[10]', obj + '.cv[12]', obj  + '.cv[14]')
		cmds.scale( 0.32,0.32,0.32)
		cmds.xform(obj, ro=(90,0,0))
		# Clear Selection and Make Identity
		cmds.delete(obj , constructionHistory=True)
		cmds.makeIdentity(obj, apply=True, t=1, s=1, r=1)
		cmds.select(obj)
		color_it(col)
		# make offset groups
		cmds.group(obj, n= obj + '_Grp')
		cmds.group(obj + '_Grp', n = obj + '_Grp_OFF')
		print('Controller made at origin')
	
	else:
		for jnt in list:
			item01 = cmds.circle(n= jnt + '_C', radius=n, d=3, s=16)[0]
			cmds.select(jnt + '_C' + '.cv[0]', jnt + '_C' + '.cv[2]' , jnt + '_C'+ '.cv[4]', jnt + '_C' + '.cv[6]', jnt + '_C' + '.cv[8]', jnt + '_C' + '.cv[10]',jnt + '_C' + '.cv[12]',jnt + '_C'  + '.cv[14]')
			cmds.scale( 0.32,0.32,0.32)
			cmds.xform(jnt + '_C', ro=(90,0,0))
			cmds.select(item01)
			obj = cmds.ls(sl=True)[0]
			# Clear Selection and Make Identity
			cmds.delete(obj , constructionHistory=True)
			cmds.makeIdentity(obj, apply=True, t=1, s=1, r=1)
			cmds.select(obj)
			color_it(col)
			# Make Offset Groups
			item02 = cmds.group(obj, n = jnt + '_C_Grp')
			item03 = cmds.group(jnt + '_C_Grp', n = jnt + '_C_Grp_OFF')
			
			All_Ctrl_list.append(item03)
			All_Ctrl_list.append(item02)
			All_Ctrl_list.append(item01)
			# Position the controller at joint
			cmds.delete(cmds.parentConstraint(jnt, jnt + '_C_Grp_OFF' ,mo=False) )
			if pc==1:
				cmds.parentConstraint(obj, jnt, mo=True)
			if sc==1:
				cmds.scaleConstraint(obj, jnt, mo=True)
		i=3
		#Make FK Chain
		if fk==1:
			print(All_Ctrl_list)
			for item in enumerate(All_Ctrl_list):
				if i!= len(All_Ctrl_list):
					cmds.parent(All_Ctrl_list[i],All_Ctrl_list[i-1])
					i+=3
			cmds.select(All_Ctrl_list[-1])
# _____________________________________________________________________________
def Create_Locator(Color):
	global pc, sc, fk
	All_Ctrl_list = []
	list = cmds.ls(sl=True)
	mgs = len(list)
	col = cmds.colorIndexSliderGrp(Color, query=True, value=True)
	n=1
	if mgs<1:
		# make controller
		v = cmds.curve( d=1, p=[(0, 1.25*n, 0), (0, 0, 0), (0,-1.25*n, 0),(0,0,0),(1.25*n,0,0) ,(0,0,0),(-1.25*n,0,0),(0,0,0),(0,0,1.25*n),(0,0,0),(0,0,-1.25*n)] )
		obj = cmds.ls(sl=True)[0]
		# Clear Selection and Make Identity
		cmds.delete(obj , constructionHistory=True)
		cmds.makeIdentity(obj, apply=True, t=1, s=1, r=1)
		cmds.select(obj)
		color_it(col)
		# make offset groups
		cmds.group(obj, n= obj + '_Grp')
		cmds.group(obj + '_Grp', n = obj + '_Grp_OFF')
		print('Controller made at origin')
	
	else:
		for jnt in list:
			item01 = cmds.curve(n= jnt + '_C', d=1, p=[(0, 1.25*n, 0), (0, 0, 0), (0,-1.25*n, 0),(0,0,0),(1.25*n,0,0) ,(0,0,0),(-1.25*n,0,0),(0,0,0),(0,0,1.25*n),(0,0,0),(0,0,-1.25*n)] )
			obj = cmds.ls(sl=True)[0]
			# Clear Selection and Make Identity
			cmds.delete(obj , constructionHistory=True)
			cmds.makeIdentity(obj, apply=True, t=1, s=1, r=1)
			cmds.select(obj)
			color_it(col)
			# Make Offset Groups
			item02 = cmds.group(obj, n = jnt + '_C_Grp')
			item03 = cmds.group(jnt + '_C_Grp', n = jnt + '_C_Grp_OFF')
			
			All_Ctrl_list.append(item03)
			All_Ctrl_list.append(item02)
			All_Ctrl_list.append(item01)
			# Position the controller at joint
			cmds.delete(cmds.parentConstraint(jnt, jnt + '_C_Grp_OFF' ,mo=False) )
			if pc==1:
				cmds.parentConstraint(obj, jnt, mo=True)
			if sc==1:
				cmds.scaleConstraint(obj, jnt, mo=True)
		i=3
		#Make FK Chain
		if fk==1:
			print(All_Ctrl_list)
			for item in enumerate(All_Ctrl_list):
				if i!= len(All_Ctrl_list):
					cmds.parent(All_Ctrl_list[i],All_Ctrl_list[i-1])
					i+=3
			cmds.select(All_Ctrl_list[-1])
# _____________________________________________________________________________
def Create_COG(Color):
	
	global pc, sc, fk
	All_Ctrl_list = []
	list = cmds.ls(sl=True)
	mgs = len(list)
	col = cmds.colorIndexSliderGrp(Color, query=True, value=True)
	n=1
	if mgs<1:
		# make controller
		v = cmds.circle( radius = n, ch=0)
		cmds.xform( ro=(-90,0,0), r=True, os=True)
		cmds.makeIdentity(v, apply=True, t=1, r=1, s=1)
		
		child_curve = cmds.curve(n= '_C1', d=1, p = [(-1.25*n, 0, -1.25*n), (-1.25*n, 0, -3.75*n), (-2.5*n, 0, -3.75*n), (0, 0, -6.25*n), (2.5*n, 0, -3.75*n), (1.25*n, 0, -3.75*n), (1.25*n, 0, -1.25*n),  (3.75*n, 0, -1.25*n), (3.75*n, 0, -2.5*n), (6.25*n, 0, 0),  (3.75*n, 0 ,2.5*n), (3.75*n, 0, 1.25*n), (1.25*n, 0 ,1.25*n), (1.25*n, 0, 3.75*n), (2.5*n, 0, 3.75*n),  (0, 0, 6.25*n), (-2.5*n, 0, 3.75*n),  (-1.25*n, 0, 3.75*n), (-1.25*n, 0, 1.25*n), (-3.75*n, 0, 1.25*n), (-3.75*n, 0 ,2.5*n), (-6.25*n, 0, 0), (-3.75*n, 0 ,-2.5*n), (-3.75*n, 0 ,-1.25*n), (-1.25*n, 0 ,-1.25*n)] )
		cmds.scale(0.35, 0.35, 0.35)
		cmds.select('_C1' + '.cv[0]', '_C1' + '.cv[6]', '_C1' + '.cv[12]', '_C1' + '.cv[18]', '_C1' + '.cv[24]' )
		cmds.scale( 2.4, 2.4, 2.4, r=True, ocp=True, xc='edge',a=True)
		cmds.makeIdentity(child_curve, apply=True, t=1, r=1, s=1)
		
		cmds.select( child_curve, r=True)
		cmds.pickWalk(d= 'down')
		cmds.select( v, tgl=True)
		cmds.parent(s=True, r=True)
		cmds.delete(child_curve)
		cmds.pickWalk(d= 'up')
		obj = cmds.ls(sl=1)[0]
		# Clear Selection and Make Identity
		cmds.delete(obj , constructionHistory=True)
		cmds.makeIdentity(obj, apply=True, t=1, s=1, r=1)
		cmds.select(obj)
		color_it(col)
		# make offset groups
		cmds.group(obj, n= obj + '_Grp')
		cmds.group(obj + '_Grp', n = obj + '_Grp_OFF')
		print('Controller made at origin')
	
	else:
		for jnt in list:
			item01 = cmds.circle(n= jnt + '_C', radius = n, ch=0)
			cmds.xform( ro=(-90,0,0), r=True, os=True)
			cmds.makeIdentity(item01 , apply=True, t=1, r=1, s=1)
			
			child_curve = cmds.curve(n= '_C1', d=1, p = [(-1.25*n, 0, -1.25*n), (-1.25*n, 0, -3.75*n), (-2.5*n, 0, -3.75*n), (0, 0, -6.25*n), (2.5*n, 0, -3.75*n), (1.25*n, 0, -3.75*n), (1.25*n, 0, -1.25*n),  (3.75*n, 0, -1.25*n), (3.75*n, 0, -2.5*n), (6.25*n, 0, 0),  (3.75*n, 0 ,2.5*n), (3.75*n, 0, 1.25*n), (1.25*n, 0 ,1.25*n), (1.25*n, 0, 3.75*n), (2.5*n, 0, 3.75*n),  (0, 0, 6.25*n), (-2.5*n, 0, 3.75*n),  (-1.25*n, 0, 3.75*n), (-1.25*n, 0, 1.25*n), (-3.75*n, 0, 1.25*n), (-3.75*n, 0 ,2.5*n), (-6.25*n, 0, 0), (-3.75*n, 0 ,-2.5*n), (-3.75*n, 0 ,-1.25*n), (-1.25*n, 0 ,-1.25*n)] )
			cmds.scale(0.35, 0.35, 0.35)
			cmds.select('_C1' + '.cv[0]', '_C1' + '.cv[6]', '_C1' + '.cv[12]', '_C1' + '.cv[18]', '_C1' + '.cv[24]' )
			cmds.scale( 2.4, 2.4, 2.4, r=True, ocp=True, xc='edge',a=True)
			cmds.makeIdentity(child_curve, apply=True, t=1, r=1, s=1)
			
			cmds.select( child_curve, r=True)
			cmds.pickWalk(d= 'down')
			cmds.select( item01, tgl=True)
			cmds.parent(s=True, r=True)
			cmds.delete(child_curve)
			cmds.pickWalk(d= 'up')
			obj = cmds.ls(sl=1)[0]
			# Clear Selection and Make Identity
			cmds.delete(obj , constructionHistory=True)
			cmds.makeIdentity(obj, apply=True, t=1, s=1, r=1)
			cmds.select(obj)
			color_it(col)
			# Make Offset Groups
			item02 = cmds.group(obj, n = jnt + '_C_Grp')
			item03 = cmds.group(jnt + '_C_Grp', n = jnt + '_C_Grp_OFF')
			
			All_Ctrl_list.append(item03)
			All_Ctrl_list.append(item02)
			All_Ctrl_list.append(item01)
			# Position the controller at joint
			cmds.delete(cmds.parentConstraint(jnt, jnt + '_C_Grp_OFF' ,mo=False) )
			if pc==1:
				cmds.parentConstraint(obj, jnt, mo=True)
			if sc==1:
				cmds.scaleConstraint(obj, jnt, mo=True)
		i=3
		#Make FK Chain
		if fk==1:
			print(All_Ctrl_list)
			for item in enumerate(All_Ctrl_list):
				if i!= len(All_Ctrl_list):
					cmds.parent(All_Ctrl_list[i],All_Ctrl_list[i-1])
					i+=3
			cmds.select(All_Ctrl_list[-1])
