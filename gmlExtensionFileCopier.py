import utilities as utils
import gmsUtilities as gms
import os

def copyFunctionsFileToExtension(workPaths):
	print('\nCOPYING FUNCTIONS FILE\n')

	extensionDir = workPaths.extension.dir

	functions = [workPaths.combinedFunctions.file]
	utils.replaceFilesToDir(functions, extensionDir)

	print('\nFUNCTIONS FILE COPIED\n')


def copyScriptsToProject(workPaths, project, scriptDirs):
	copyResourcesToProject(workPaths, project, 'GMScript', 'ResourceTree_Scripts', project.scriptsDir, scriptDirs)

def copyObjectsToProject(workPaths, project, objectDirs):
	copyResourcesToProject(workPaths, project, 'GMObject', 'ResourceTree_Objects', project.objectsDir, objectDirs)

def copyExtensionsToProject(workPaths, project, extensionDirs):
	copyResourcesToProject(workPaths, project, 'GMExtension', 'ResourceTree_Extensions', project.extensionsDir, extensionDirs)

def copyResourcesToProject(workPaths, project, filterType, resourceType, resourceDir, resources):
	print('\nCOPYING EXTERNAL RESOURCES\n')

	#Copy resources to Extension Project
	utils.replaceDirectoriesToDir(resources, resourceDir)

	#Include resources to project
	newResourceUuids = gms.includeResourcesToProject(resources, project.file, filterType)
	gms.addResourcesToRootView(newResourceUuids, project, filterType, resourceType)

	print('\nRESOURCE DIRECTORIES COPIED\n')