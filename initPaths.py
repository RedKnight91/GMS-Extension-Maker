from os.path import normpath, basename
from utilities import getFileName

def initTest():
	paths = {
		'projectsDir' : normpath(r'C:\Users\mikec\Documents\Python\GmsExtensionMaker_tests'),
		'assetProjectDir' : normpath(r'C:\Users\mikec\Documents\Python\GmsExtensionMaker_tests\GMS_tool'),
	}

	return paths

def initGMS_utilities():
	paths = {
		'projectsDir' : normpath(r'C:\Users\mikec\Documents\GameMakerStudio2'),
		'assetProjectDir' : normpath(r'C:\Users\mikec\Documents\GameMakerStudio2\Assets\GMS_utilities\GMS_utilities')
	}
	return paths

def initGMS_timers(): 
	paths = {
		'projectsDir' : normpath(r'C:\Users\mikec\Documents\GameMakerStudio2'),
		'assetProjectDir' : normpath(r'C:\Users\mikec\Documents\GameMakerStudio2\Assets\GMS_timers\GMS_timers')
	}
	return paths

#TODO FIX FORMAT
# def initGMS_verlet(): 
# 	global workPaths
# 	workPaths = ProductionPaths(
# 		normpath(r'C:\Users\mikec\Documents\GameMakerStudio2'),
# 		normpath(r'C:\Users\mikec\Documents\GameMakerStudio2\Assets\GMS_verlet\GMS_verlet')
# 	)

# def initGMS_events(): 
# 	global workPaths
# 	workPaths = ProductionPaths(
# 		normpath(r'C:\Users\mikec\Documents\GameMakerStudio2'),
# 		normpath(r'C:\Users\mikec\Documents\GameMakerStudio2\Assets\GMS_events\GMS_events')
# 	)

# def initGMS_camera(): 
# 	global workPaths
# 	workPaths = ProductionPaths(
# 		normpath(r'C:\Users\mikec\Documents\GameMakerStudio2'),
# 		normpath(r'C:\Users\mikec\Documents\GameMakerStudio2\Assets\GMS_camera\GMS_camera')
# 	)