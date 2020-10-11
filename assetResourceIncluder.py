import utilities as utils
from models import folderJson, resourceJson, resourceRelativePath
from os.path import join, basename, normpath, split
from paths import workPaths


def yypHasFolder(foldersJson, folderPath):
	folder = [f for f in foldersJson if f['folderPath'] == folderPath ]
	return folder

def includeFolderToProject(folderPath, projectFolders):
	folderName = utils.getFileName(folderPath, True)
	folder = folderJson(folderPath, folderName)
	projectFolders.append(folder)

def includeResourceFoldersToProject(parentPath, resourceName, projectJson):
	folders = projectJson['Folders']
	pathLen = len(utils.splitPath(parentPath))

	for _ in range(pathLen - 1):
		if not yypHasFolder(folders, parentPath):
			includeFolderToProject(parentPath, folders)
		
		parentPath = split(parentPath)[0] + '.yy'

def resourceInProject(projectJson, resPath):
	matches = [res for res in projectJson['resources'] if res['id']['path'] == resPath]
	isInProject = len(matches) > 0

	return isInProject

def appendResourceToResources(projectJson, path):
	json = resourceJson(path)
	projectJson['resources'].append(json)

def includeResourceToProject(type, resource, projectJson):
	name = resource.name
	file = resource.file
	yyJson = utils.readJson(file)
	parentPath = yyJson['parent']['path']

	path = resourceRelativePath(type, name) #e.g. scripts/doThing/doThing.yy
	
	if not resourceInProject(projectJson, path):
		appendResourceToResources(projectJson, path)
		includeResourceFoldersToProject(parentPath, name, projectJson)

def includeResourceTypeToProject(resourcesType, resources, project):
	projectJson = utils.readJson(project.file)

	for resource in resources:
		includeResourceToProject(resourcesType, resource, projectJson)
			
	utils.writeJson(project.file, projectJson)

def includeAssetResourcesToProject(project):
	asset = workPaths.assetProject
	includeResourceTypeToProject('scripts', asset.scripts, project)
	includeResourceTypeToProject('objects', asset.objects, project)
	includeResourceTypeToProject('extensions', asset.extensions, project)