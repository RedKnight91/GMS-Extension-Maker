import utilities as utils
import gmsUtilities as gms
import os

def copyFunctionsFileToExtensionDir(workPaths):
	print('\nCOPYING FUNCTIONS FILE\n')

	extensionDir = workPaths.extension.dir

	prompt = 'Would you like to copy the combined functions file to the extension folder? (Y/N)\n {}'.format(extensionDir)
	confirmed = utils.promptChoice(prompt)

	if (confirmed):
		functions = [workPaths.combinedFunctions.file]
		utils.replaceFilesToDir(functions, extensionDir)

	print('\nFUNCTIONS FILE COPIED\n')



def copyExternalScriptsToExtensionDir(workPaths, externalScriptDirs):
	copyExternalResourcesToExtensionDir(workPaths, 'GMScript', 'ResourceTree_Scripts', workPaths.extensionProject.scriptsDir, externalScriptDirs)

def copyExternalObjectsToExtensionDir(workPaths, externalObjectDirs):
	copyExternalResourcesToExtensionDir(workPaths, 'GMObject', 'ResourceTree_Objects', workPaths.extensionProject.objectsDir, externalObjectDirs)


def copyExternalResourcesToExtensionDir(workPaths, filterType, resourceType, resourceDir, externalResources):
	print('\nCOPYING EXTERNAL RESOURCES\n')

	prompt = 'Copy external resources to this folder? (Y/N)\n{}'.format(resourceDir)
	confirmed = utils.promptChoice(prompt)

	if (confirmed):
		utils.replaceDirectoriesToDir(externalResources, resourceDir)
		projectFile = workPaths.extensionProject.file

		newResourceUuids = gms.includeResourcesToProject(externalResources, projectFile, filterType)
		gms.addResourcesToRootView(newResourceUuids, filterType, resourceType, workPaths)

	print('\nRESOURCE DIRECTORIES COPIED\n')