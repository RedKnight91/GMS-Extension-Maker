from gmsUtilities import ProductionPaths
from os.path import normpath

class Projects():
	Test = ProductionPaths(
		normpath(r'C:\Users\mikec\Documents\Python\GmsExtensionMaker_tests'),
		normpath(r'C:\Users\mikec\Documents\Python\GmsExtensionMaker_tests\Asset'),
		normpath(r'C:\Users\mikec\Documents\Python\GmsExtensionMaker\results'),
		'Asset',
		'Asset'
	)

	GMS_utilities = ProductionPaths(
		normpath(r'C:/Users/mikec/Documents/GameMakerStudio2'),
		normpath(r'C:/Users/mikec/Documents/GameMakerStudio2/Assets/GMS_utilities/GMS_utilities'),
		normpath(r'C:/Users/mikec/Desktop/GMLCombinerResults'),
		'Asset',
		'Asset'
	)

	GMS_timers = ProductionPaths(
		normpath(r'C:/Users/mikec/Documents/GameMakerStudio2'),
		normpath(r'C:/Users/mikec/Documents/GameMakerStudio2/Assets/GMS_timers/GMS_timers'),
		normpath(r'C:/Users/mikec/Desktop/GMLCombinerResults'),
		'Asset',
		'Asset'
	)

	GMS_verlet = ProductionPaths(
		normpath(r'C:/Users/mikec/Documents/GameMakerStudio2'),
		normpath(r'C:/Users/mikec/Documents/GameMakerStudio2/Assets/GMS_verlet/GMS_verlet'),
		normpath(r'C:/Users/mikec/Desktop/GMLCombinerResults'),
		'Asset',
		'Asset'
	)

	GMS_events = ProductionPaths(
		normpath(r'C:/Users/mikec/Documents/GameMakerStudio2'),
		normpath(r'C:/Users/mikec/Documents/GameMakerStudio2/Assets/GMS_events/GMS_events'),
		normpath(r'C:/Users/mikec/Desktop/GMLCombinerResults'),
		'Asset',
		'Asset'
	)

	GMS_camera = ProductionPaths(
		normpath(r'C:/Users/mikec/Documents/GameMakerStudio2'),
		normpath(r'C:/Users/mikec/Documents/GameMakerStudio2/Assets/GMS_camera/GMS_camera'),
		normpath(r'C:/Users/mikec/Desktop/GMLCombinerResults'),
		'Asset',
		'Asset'
	)