import utilities as utils
import gmsUtilities as gms
import os

#TODO 'Scripts' and 'Objects' should not be fixed in here, as resource folders can now be renamed

def locateScripts(workPaths):
	branch = os.path.join('folders/Scripts', workPaths.externalScriptsGroup)
	objects = locateResourceType(workPaths, branch, workPaths.sourceProject.objectsDir)
	return objects

def locateObjects(workPaths):
	branch = os.path.join('folders/Objects', workPaths.externalObjectsGroup)
	objects = locateResourceType(workPaths, branch, workPaths.sourceProject.objectsDir)
	return objects

def locateExtensions(workPaths):
	branch = 'folders/Extensions'
	extensions = locateResourceType(workPaths, branch, workPaths.sourceProject.extensionsDir)
	return extensions

def locateResourceType(workPaths, branch, resourcesDir):
	print('\nLOCATING RESOURCES\n')

	resources = []

	project = workPaths.sourceProject
	projectJson = utils.readJson(project.file)
	resourcesJson = projectJson.resources

	for resource in resourcesDir:
		resourceJson = utils.readJson(resource)
		if branch in resourceJson.parent.path:
			resourceName = resourceJson.name
			resourceNode = [i for i in resourcesJson if i.name == resourceName][0]
			resourcePath = resourceNode.path
			resources.append(resourcePath)

	print('\nRESOURCES LOCATED\n')

	return resources