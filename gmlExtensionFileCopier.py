import utilities as utils
from gmsUtilities import includeResourcesToYyp
import os

def fixResourceRelativePaths(resourcesType, assetName, resourcesDir):
	resourceYYs = utils.getDirectoryExtensionFilesRecursive(resourcesDir, 'yy')

	for resYY in resourceYYs:
		resJson = utils.readJson(resYY)

		path = resJson['parent']['path']
		path = resourcesType + '/' + assetName + '.yy'
		resJson['parent']['path'] = path

		utils.writeJson(resYY, resJson)

	return

def ensureResourceDirExists(project, resourceDir):
	if (not os.path.exists(resourceDir)):
		print('"{}" folder not found for project {}'.format(utils.getDirName(resourceDir), project.name))
		print('Creating "{}" folder'.format(utils.getDirName(resourceDir)))
		os.mkdir(resourceDir)

def copyScriptsToProject(workPaths, project, scriptDirs):
	copyResourcesToProject(workPaths, project, 'scripts', project.scriptsDir, scriptDirs)

def copyObjectsToProject(workPaths, project, objectDirs):
	copyResourcesToProject(workPaths, project, 'objects', project.objectsDir, objectDirs)

def copyExtensionsToProject(workPaths, project, extensionDirs):
	copyResourcesToProject(workPaths, project, 'extensions', project.extensionsDir, extensionDirs)

def copyResourcesToProject(workPaths, project, resourcesType, resourcesDir, resourceDirs):
	print('\nCOPYING EXTERNAL RESOURCES\n')

	#TODO
	#1. copy resource dirs over to project
	#2. fix their paths (earlier folders/Scripts/Asset.yy or whatever)
	#3. ensure paths exist in project's 'Folders' node
	#4. include resources to project's 'resources' node

	resourceNames = [utils.getFileName(res, True) for res in resourceDirs]

	ensureResourceDirExists(project, resourcesDir)
	utils.replaceDirectoriesToDir(resourceDirs, resourcesDir)
	fixResourceRelativePaths(resourcesType, workPaths.assetProject.name, resourcesDir)

	includeResourcesToYyp(resourcesType, resourceNames, project.file)
	
	print('\nRESOURCE DIRECTORIES COPIED\n')