import utilities as utils
import gmsUtilities as gms
from os.path import dirname

#TODO 'Scripts' and 'Objects' should not be fixed in here, as resource folders can now be renamed

def locateScripts(workPaths):
	branch = 'folders/Scripts/' + workPaths.assetScriptsGroup
	objects = locateResourceType(workPaths, branch, workPaths.assetProject.scriptsDir)
	return objects

def locateObjects(workPaths):
	branch = 'folders/Objects/' + workPaths.assetObjectsGroup
	objects = locateResourceType(workPaths, branch, workPaths.assetProject.objectsDir)
	return objects

def locateExtensions(workPaths):
	branch = 'folders/Extensions'
	extensions = locateResourceType(workPaths, branch, workPaths.assetProject.extensionsDir)
	return extensions

def locateResourceType(workPaths, branch, resourcesDir):
	print('\nLOCATING RESOURCES\n')

	okResources = []

	projectFile = workPaths.assetProject.file
	projectJson = utils.readJson(projectFile)
	resourcesJson = projectJson['resources']
	resources = utils.getDirectoryExtensionFilesRecursive(resourcesDir, '.yy')

	for resource in resources:
		resourceJson = utils.readJson(resource)
		resourcePath = resourceJson['parent']['path']

		if branch in resourcePath:
			resourceName = resourceJson['name']
			resourceNode = [i for i in resourcesJson if i['id']['name'] == resourceName][0]
			resourcePath = resourceNode['id']['path']
			okResources.append(dirname(resource))

	print('\nRESOURCES LOCATED\n')

	return okResources