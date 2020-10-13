import utilities as utils
from models import folderJson, resourceJson, resourceRelativePath
from os.path import join, basename, dirname, normpath, split, exists
from workPaths import workPaths

def excludeResourceFoldersFromProject(type, projectJson):
	assetName = workPaths.assetProject.name
	folders = projectJson['Folders']

	path = 'folders/' + type.capitalize() + '/' + assetName
	
	for folder in folders:
		if path in folder['folderPath']:
			projectJson['Folders'].remove(folder)

def resourceFileExists(resourcesDir, project, resource):
	resPath = resource['id']['path']
	path = dirname(resourcesDir) + resPath

	return exists(path)

def excludeResourceTypeFromProject(resourcesType, resourcesDir, project):
	projectJson = utils.readJson(project.file)
	resources = projectJson['resources']

	for res in resources:
		if not resourceFileExists(resourcesDir, project, res):
			projectJson['resources'].remove(res)

	excludeResourceFoldersFromProject(resourcesType, projectJson)
	utils.writeJson(project.file, projectJson)

def excludeAssetResourcesFromProject(project):
	excludeResourceTypeFromProject('scripts', project.scriptsDir, project)
	excludeResourceTypeFromProject('objects', project.objectsDir, project)
	excludeResourceTypeFromProject('extensions', project.extensionsDir, project)