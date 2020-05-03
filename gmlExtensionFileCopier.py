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



def copyScriptsToExtensionDir(workPaths, scriptDirs):
	copyResourcesToExtensionDir(workPaths, 'GMScript', 'ResourceTree_Scripts', workPaths.extensionProject.scriptsDir, scriptDirs)

def copyObjectsToExtensionDir(workPaths, objectDirs):
	copyResourcesToExtensionDir(workPaths, 'GMObject', 'ResourceTree_Objects', workPaths.extensionProject.objectsDir, objectDirs)

def copyExtensionsToExtensionDir(workPaths, extensionDirs):
	copyResourcesToExtensionDir(workPaths, 'GMExtension', 'ResourceTree_Extensions', workPaths.extensionProject.extensionsDir, extensionDirs)


def copyResourcesToExtensionDir(workPaths, filterType, resourceType, resourceDir, externalResources):
	print('\nCOPYING EXTERNAL RESOURCES\n')

	prompt = 'Copy external resources to this folder? (Y/N)\n{}'.format(resourceDir)
	confirmed = utils.promptChoice(prompt)

	if (confirmed):
		utils.replaceDirectoriesToDir(externalResources, resourceDir)
		projectFile = workPaths.extensionProject.file

		newResourceUuids = gms.includeResourcesToProject(externalResources, projectFile, filterType)
		gms.addResourcesToRootView(newResourceUuids, filterType, resourceType, workPaths)

	print('\nRESOURCE DIRECTORIES COPIED\n')