from gmlExtensionPathInitializer import validateWorkPaths, printWorkPaths
import gmlExtensionResourceLocator as locator
from gmlExtensionScriptCombiner import combineScripts
from gmlExtensionUpdater import updateExtensionToProjects
from gmlExtensionGenerator import generateAssetExtension
import utilities as utils

debugMode = False

def printHeader(workPaths):
	extensionName = workPaths.extension.name
	extensionProjectName = workPaths.extensionProject.name
	sourceProjectName = workPaths.sourceProject.name
	print('Making extension "{}" in project {}, combining project {}'.format(extensionName, extensionProjectName, sourceProjectName))


def makeExtension(workPaths):
	printHeader(workPaths)

	validateWorkPaths(workPaths)
	if debugMode:
		printWorkPaths(workPaths)
	
	generateAssetExtension(workPaths)

	sourceScriptDirs = locator.locateScripts(workPaths)
	combineScripts(workPaths, sourceScriptDirs)

	updateExtensionToProjects(workPaths)