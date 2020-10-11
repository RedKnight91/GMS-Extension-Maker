from classes import ProductionPaths
from os.path import normpath

workPaths = ''

def initTest():
	global workPaths #This lets the function know we're referencing the module-level variable workPaths
	workPaths = ProductionPaths(
		normpath(r'C:\Users\mikec\Documents\Python\GmsExtensionMaker_tests'),
		normpath(r'C:\Users\mikec\Documents\Python\GmsExtensionMaker_tests\GMS_tool'),
		normpath(r'C:\Users\mikec\Documents\Python\GmsExtensionMaker\results')
	)

def initGMS_utilities():
	global workPaths
	workPaths = ProductionPaths(
		normpath(r'C:\Users\mikec\Documents\GameMakerStudio2'),
		normpath(r'C:\Users\mikec\Documents\GameMakerStudio2\Assets\GMS_utilities\GMS_utilities'),
		normpath(r'C:\Users\mikec\Documents\Python\GmsExtensionMaker\results')
	)

def initGMS_timers(): 
	global workPaths
	workPaths = ProductionPaths(
		normpath(r'C:\Users\mikec\Documents\GameMakerStudio2'),
		normpath(r'C:\Users\mikec\Documents\GameMakerStudio2\Assets\GMS_timers\GMS_timers'),
		normpath(r'C:\Users\mikec\Documents\Python\GmsExtensionMaker\results')
	)

def initGMS_verlet(): 
	global workPaths
	workPaths = ProductionPaths(
		normpath(r'C:\Users\mikec\Documents\GameMakerStudio2'),
		normpath(r'C:\Users\mikec\Documents\GameMakerStudio2\Assets\GMS_verlet\GMS_verlet'),
		normpath(r'C:\Users\mikec\Documents\Python\GmsExtensionMaker\results')
	)

def initGMS_events(): 
	global workPaths
	workPaths = ProductionPaths(
		normpath(r'C:\Users\mikec\Documents\GameMakerStudio2'),
		normpath(r'C:\Users\mikec\Documents\GameMakerStudio2\Assets\GMS_events\GMS_events'),
		normpath(r'C:\Users\mikec\Documents\Python\GmsExtensionMaker\results')
	)

def initGMS_camera(): 
	global workPaths
	workPaths = ProductionPaths(
		normpath(r'C:\Users\mikec\Documents\GameMakerStudio2'),
		normpath(r'C:\Users\mikec\Documents\GameMakerStudio2\Assets\GMS_camera\GMS_camera'),
		normpath(r'C:\Users\mikec\Documents\Python\GmsExtensionMaker\results')
	)