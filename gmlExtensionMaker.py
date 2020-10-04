from gmlExtensionPathInitializer import validateWorkPaths, printWorkPaths
import gmlExtensionResourceLocator as locator
from gmlExtensionScriptCombiner import combineScripts
from gmlExtensionUpdater import updateExtensionToProjects
from gmlExtensionGenerator import generateAssetExtension
import utilities as utils

debugMode = False

def makeExtension(workPaths):
	validateWorkPaths(workPaths)
	if debugMode:
		printWorkPaths(workPaths)
	
	generateAssetExtension(workPaths)

	assetScriptDirs = locator.locateScripts(workPaths)
	combineScripts(workPaths, assetScriptDirs)

	updateExtensionToProjects(workPaths)

	#TODO delete combined files in 'results' dir