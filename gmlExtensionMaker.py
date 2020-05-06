from gmlExtensionPathInitializer import validateWorkPaths, printWorkPaths
import gmlExtensionResourceLocator as locator
from gmlExtensionScriptCombiner import combineScripts
import gmlExtensionFileCopier as copier
from gmlExtensionFunctionIncluder import includeFunctionFilesToExtension
from gmlExtensionJsdocInjector import includeFunctionJsdocsToExtension
from gmlExtensionUpdater import updateExtensionInProjects
import utilities as utils

def printHeader(workPaths):
	extensionName = workPaths.extension.name
	extensionProjectName = workPaths.extensionProject.name
	sourceProjectName = workPaths.sourceProject.name
	print('Making extension "{}" in project {}, combining project {}'.format(extensionName, extensionProjectName, sourceProjectName))


def makeExtension(workPaths):
	printHeader(workPaths)

	validateWorkPaths(workPaths)
	# printWorkPaths(workPaths)
	
	#Get resources to copy from source project
	externalScriptDirs	= locator.locateExternalScripts(workPaths)
	internalScriptDirs	= locator.locateInternalScripts(workPaths)
	objectDirs			= locator.locateObjects(workPaths)
	extensionDirs		= locator.locateExtensions(workPaths)
	
	combineScripts(workPaths, internalScriptDirs)
	
	#Copy resources to extension project
	extensionProject = workPaths.extensionProject
	copier.copyFunctionsFileToExtension(workPaths)
	copier.copyScriptsToProject(workPaths, extensionProject, externalScriptDirs)
	copier.copyObjectsToProject(workPaths, extensionProject, objectDirs)
	copier.copyExtensionsToProject(workPaths, extensionProject, extensionDirs)

	#Include files and functions to extension (.yy)
	includeFunctionFilesToExtension(workPaths)
	includeFunctionJsdocsToExtension(workPaths)

	updateExtensionInProjects(workPaths)