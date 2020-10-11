import utilities as utils
from models import folderJson, resourceJson, resourceRelativePath
from os.path import join, basename, dirname, normpath, split, exists
from paths import workPaths


# def yypHasFolder(foldersJson, folderPath):
# 	folder = [f for f in foldersJson if f['folderPath'] == folderPath ]
# 	return folder

# def excludeFolderFromProject(folderPath, projectFolders):
# 	folderName = utils.getFileName(folderPath, True)
# 	folder = folderJson(folderPath, folderName)
# 	projectFolders.append(folder)

# def excludeResourceFoldersFromProject(parentPath, resourceName, projectJson):
# 	folders = projectJson['Folders']
# 	pathLen = len(utils.splitPath(parentPath))

# 	for _ in range(pathLen - 1):
# 		if not yypHasFolder(folders, parentPath):
# 			excludeFolderFromProject(parentPath, folders)
		
# 		parentPath = split(parentPath)[0] + '.yy'

# def appendResourceToResources(projectJson, path):
# 	json = resourceJson(path)
# 	projectJson['resources'].append(json)


# def excludeResourceFromProject(type, resource, projectJson):

	# name = resource.name
	# file = resource.file
	# yyJson = utils.readJson(file)
	# parentPath = yyJson['parent']['path']

	# path = resourceRelativePath(type, name) #e.g. scripts/doThing/doThing.yy
	
	# if not resourceInProject(projectJson, path):
	# 	appendResourceToResources(projectJson, path)
	# 	excludeResourceFoldersFromProject(parentPath, name, projectJson)

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