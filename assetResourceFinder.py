import utilities as utils
import gmUtilities as gms
from os.path import dirname

#TODO 'Scripts' and 'Objects' should not be fixed in here, as resource folders can now be renamed

def findScripts(project):
	branch = 'folders/Scripts/{}'.format(project.name)
	scripts = findResourceType(project, branch, project.scriptsDir)
	return scripts

def findObjects(project):
	branch = 'folders/Objects/{}'.format(project.name)
	objects = findResourceType(project, branch, project.objectsDir)
	return objects

def findExtensions(project):
	branch = 'folders/Extensions/{}'.format(project.name)
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