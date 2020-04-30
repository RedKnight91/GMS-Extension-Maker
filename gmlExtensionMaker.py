from gmlExtensionPathInitializer import initExtensionPaths
from gmlExtensionResourceLocator import locateScripts, locateObjects
from gmlExtensionScriptCombiner import combineScripts
from gmlExtensionFileCopier import copyFunctionsFileToExtensionDir, copyExternalScriptsToExtensionDir, copyExternalObjectsToExtensionDir
from gmlExtensionFunctionIncluder import includeFunctionFilesToExtension
from gmlExtensionFunctionJsonMaker import includeFunctionsToExtension
from gmlExtensionJsdocInjector import includeFunctionJsdocsToExtension
from gmlExtensionUpdater import pushExtension
import utilities as utils

def printHeader(workPaths):
	extensionName = workPaths.extension.name
	extensionProjectName = workPaths.extensionProject.name
	sourceProjectName = workPaths.sourceProject.name
	print('Making extension "{}" in project {}, combining project {}'.format(extensionName, extensionProjectName, sourceProjectName))


def makeExtension(paths):
	workPaths = initExtensionPaths(paths)

	printHeader(workPaths)
	
	scriptDirs = locateScripts(workPaths)
	objectDirs = locateObjects(workPaths)
	
	internalScriptDirs = scriptDirs['internal']
	combineScripts(workPaths, internalScriptDirs)
	copyFunctionsFileToExtensionDir(workPaths)

	externalScriptDirs = scriptDirs['external']
	copyExternalScriptsToExtensionDir(workPaths, externalScriptDirs)

	externalObjectDirs = objectDirs['external']
	copyExternalObjectsToExtensionDir(workPaths, externalObjectDirs)

	#Editing extension's .yy file
	includeFunctionFilesToExtension(workPaths)
	includeFunctionsToExtension(workPaths)
	includeFunctionJsdocsToExtension(workPaths)
	
	pushExtension(workPaths)