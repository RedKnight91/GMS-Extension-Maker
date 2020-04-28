from gmlExtensionPathInitializer import initExtensionPaths
from gmlExtensionResourceLocator import locateScripts, locateObjects
from gmlExtensionScriptCombiner import combineScripts
from gmlExtensionFileCopier import copyFunctionsFileToExtensionDir, copyExternalResourcesToExtensionDir
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

	scripts = locateScripts(workPaths)
	# objects = locateObject(workPaths)
	
	internalScripts = scripts['internal']
	combineScripts(workPaths, internalScripts)
	copyFunctionsFileToExtensionDir(workPaths)

	# externalScripts = scripts['external']
	# copyExternalResourcesToExtensionDir(workPaths['extensionScriptsDir'], externalScripts)
	# TODO: When copying the external resources you also need to recreate the scripts/ProjectName view and include the scripts in the .yyp... tough!

	# externalObjects = objects['external']
	# copyExternalResourcesToExtensionDir(workPaths['extensionObjectsDir'], externalObjects)

	#Editing extension's .yy file
	includeFunctionFilesToExtension(workPaths)
	includeFunctionsToExtension(workPaths)
	includeFunctionJsdocsToExtension(workPaths)

	# pushExtension(workPaths)