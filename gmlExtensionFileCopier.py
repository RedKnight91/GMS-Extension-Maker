import utilities as utils
from gmsUtilities import includeResourcesToProject
import os

def copyScriptFileToExtension(workPaths, scriptDirs):
	print('\nCOPYING SCRIPT FILES TO EXTENSION\n')

	extensionDir = workPaths.extension.dir

	for dir in scriptDirs:
		script = utils.getDirectoryExtensionFiles(dir, 'gml')
		utils.replaceFilesToDir(script, extensionDir)

	print('\nFUNCTIONS FILE COPIED\n')


def ensureResourceDirExists(project, resourceDir):
	if (not os.path.exists(resourceDir)):
		print('"{}" folder not found for project {}'.format(utils.getDirName(resourceDir), project.name))
		print('Creating "{}" folder'.format(utils.getDirName(resourceDir)))
		os.mkdir(resourceDir)

def copyScriptsToProject(workPaths, project, scriptDirs):
	copyResourcesToProject(workPaths, project, project.scriptsDir, scriptDirs)

def copyObjectsToProject(workPaths, project, objectDirs):
	copyResourcesToProject(workPaths, project, project.objectsDir, objectDirs)

def copyExtensionsToProject(workPaths, project, extensionDirs):
	copyResourcesToProject(workPaths, project, project.extensionsDir, extensionDirs)

def copyResourcesToProject(workPaths, project, resourceDir, resources):
	print('\nCOPYING EXTERNAL RESOURCES\n')

	ensureResourceDirExists(project, resourceDir)
	utils.replaceDirectoriesToDir(resources, resourceDir)
	includeResourcesToProject(resources, project.file)
	
	print('\nRESOURCE DIRECTORIES COPIED\n')