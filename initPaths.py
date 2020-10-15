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
		'assetProjectDir' : normpath(r'C:\Users\mikec\Documents\GameMakerStudio2\Assets\GMS_utilities')
	}
	return paths

def initGMS_timers(): 
	paths = {
		'projectsDir' : normpath(r'C:\Users\mikec\Documents\GameMakerStudio2'),
		'assetProjectDir' : normpath(r'C:\Users\mikec\Documents\GameMakerStudio2\Assets\GMS_timers')
	}
	return paths

def initGMS_verlet(): 
	paths = {
		'projectsDir' : normpath(r'C:\Users\mikec\Documents\GameMakerStudio2'),
		'assetProjectDir' : normpath(r'C:\Users\mikec\Documents\GameMakerStudio2\Assets\GMS_verlet')
	}
	return paths

def initGMS_events(): 
	paths = {
		'projectsDir' : normpath(r'C:\Users\mikec\Documents\GameMakerStudio2'),
		'assetProjectDir' : normpath(r'C:\Users\mikec\Documents\GameMakerStudio2\Assets\GMS_events\GMS_events')
	}
	return paths

def initGMS_camera(): 
	paths = {
		'projectsDir' : normpath(r'C:\Users\mikec\Documents\GameMakerStudio2'),
		'assetProjectDir' : normpath(r'C:\Users\mikec\Documents\GameMakerStudio2\Assets\GMS_camera')
	}
	return paths
		