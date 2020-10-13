import utilities as utils
from os.path import dirname

#TODO 'Scripts' and 'Objects' should not be fixed in here, as resource folders can now be renamed

def findScripts(project, assetName):
	branch = 'folders/Scripts/{}'.format(assetName)
	scripts = findResourceType(project, branch, project.scriptsDir)
	return scripts

def findObjects(project, assetName):
	branch = 'folders/Objects/{}'.format(assetName)
	objects = findResourceType(project, branch, project.objectsDir)
	return objects

def findExtensions(project, assetName):
	branch = 'folders/Extensions/{}'.format(assetName)
	extensions = findResourceType(project, branch, project.extensionsDir)
	return extensions

def validResource(resourcesJson, resource, branch):
	resourceJson = utils.readJson(resource)
	resourcePath = resourceJson['parent']['path']

	valid = branch in resourcePath
	
	return valid

def findResourceType(project, branch, resourcesDir):
	print('\nLOCATING RESOURCES\n')

	projectJson = utils.readJson(project.file)
	resourcesJson = projectJson['resources']
	resources = utils.getDirExtensionFilesRecursive(resourcesDir, '.yy')

	okResources = [res for res in resources if validResource(resourcesJson, res, branch)]

	print('\nRESOURCES LOCATED\n')

	return okResources