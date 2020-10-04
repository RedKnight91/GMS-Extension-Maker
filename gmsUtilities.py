import utilities as utils
from models import folderJson, resourceJson, resourceRelativePath
from os.path import join, basename, normpath, split

class File:
	def __init__(self, name, dir, extension):
		self.name	= name
		self.dir	= dir
		self.file	= join(dir, name) + '.' + extension

	def __str__(self):
		return 'name: {},\ndir : {},\nfile: {}\n'.format(self.name, self.dir, self.file)

class Project(File):
	def __init__(self, name, dir):
		dir = normpath(dir)

		File.__init__(self, name, dir, 'yyp')
		self.scriptsDir		= join(dir, 'scripts')
		self.objectsDir		= join(dir, 'objects')
		self.extensionsDir	= join(dir, 'extensions')

	def __str__(self):
		output = File.__str__(self)
		return output + 'scriptsDir: {},\nobjectsDir: {},\nextensionsDir: {}'.format(self.scriptsDir, self.objectsDir, self.extensionsDir)

class ProductionPaths():
	def __init__(self, projectsDir, assetProjectDir, combinedDir, assetScriptsGroup, assetObjectsGroup):
		self.projectsDir		= normpath(projectsDir)

		assetProjectName		= basename(assetProjectDir)
		self.assetProject		= Project(assetProjectName, assetProjectDir)

		self.combinedDir		= join(normpath(combinedDir), assetProjectName)
		combinedFileName		= assetProjectName + 'ScriptsCombined'

		self.combinedScripts	= File(combinedFileName, combinedDir, 'gml')

		self.assetScriptsGroup	= assetScriptsGroup
		self.assetObjectsGroup	= assetObjectsGroup

def splitPathIntoParts(path):
	allparts = []
	while True:
		parts = os.path.split(path)
		if parts[0] == path:
			allparts.insert(0, parts[0])
			break
		elif parts[1] == path:
			allparts.insert(0, parts[1])
			break
		else:
			path = parts[0]
			allparts.insert(0, parts[1])

	return allparts

def makeResourcePath(projectDir, partialResourcePath):
	path = join(projectDir, partialResourcePath)
	return path

def makeResourceDirPath(projectDir, partialResourcePath):
	fullPath = makeResourcePath(projectDir, partialResourcePath)
	dirPath = utils.getDir(fullPath)
	return dirPath

def yypHasFolder(foldersJson, folderPath):
	folder = [f for f in foldersJson if f['folderPath'] == folderPath ]
	return folder

def includeFolderToYyp(folderPath, projectFolders):
	folderName = split(folderPath)[1]
	folder = folderJson(folderPath, folderName)
	projectFolders.append(folder)

def includeResourceFoldersToYyp(resourcesName, resourceName, projectJson):
	folders = projectJson['Folders']

	#TODO
	path = 'folders/' + resourcesName + '/' + assetName + '/' + relPath + '.yy'
	pathLen = splitPathIntoParts(path)

	for _ in (pathLen - 1):
		exists = yypHasFolder(folders, path)

		if not exists:
			includeFolderToYyp(path, folders)
		
		path = split(path)[0] + '.yy'

	return

def includeResourceToYyp(resourcesName, resourceName, projectJson):
	path = resourceRelativePath(resourcesName, resourceName)
	json = resourceJson(path)
	projectJson['resources'].append(json)
	includeResourceFoldersToYyp(resourcesName, resourceName, projectJson)

	#TODO is the above enough to actually get it written to json?

def includeResourcesToYyp(resourcesTypeName, resourceNames, projectFile):
	projectJson = utils.readJson(projectFile)

	for name in resourceNames:
		includeResourceToYyp(resourcesTypeName, name, projectJson)
			
	utils.writeJson(projectFile, projectJson)