from gmlExtensionPathInitializer import initExtensionPaths
import gmlExtensionResourceLocator as locator
from gmlExtensionScriptCombiner import combineScripts
import gmlExtensionFileCopier as copier
from gmlExtensionFunctionIncluder import includeFunctionFilesToExtension
from gmlExtensionJsdocInjector import includeFunctionJsdocsToExtension
import gmlExtensionResourceIncluder as resourceIncluder
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
	
	#Get resources to copy from source project
	externalScriptDirs	= locator.locateExternalScripts(workPaths)
	internalScriptDirs	= locator.locateInternalScripts(workPaths)
	objectDirs			= locator.locateObjects(workPaths)
	extensionDirs		= locator.locateExtensions(workPaths)
	
	combineScripts(workPaths, internalScriptDirs)
	
	#Copy resources to extension project
	copier.copyFunctionsFileToExtensionDir(workPaths)
	copier.copyScriptsToExtensionDir(workPaths, externalScriptDirs)
	copier.copyObjectsToExtensionDir(workPaths, objectDirs)
	copier.copyExtensionsToExtensionDir(workPaths, extensionDirs)

	#Include files and functions to extension (.yy)
	includeFunctionFilesToExtension(workPaths)
	includeFunctionJsdocsToExtension(workPaths)

	#Include resources to extension project (.yyp)
	resourceIncluder.includeScriptsToProject(workPaths, workPaths.extensionProject)
	resourceIncluder.includeObjectsToProject(workPaths, workPaths.extensionProject)
	resourceIncluder.includeExtensionsToProject(workPaths, workPaths.extensionProject)
	#TODO Can reutilize these in pushExtension!

	pushExtension(workPaths)